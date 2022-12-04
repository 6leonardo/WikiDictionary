import re
import pathlib
import unicodedata
import pandas as pd
from urllib.request import Request, urlopen, HTTPError
import numpy as np
from bs4 import BeautifulSoup
import os
import json 
import re
import xml.etree.ElementTree as ET
from tqdm import tqdm
import argparse

from symbols.lang import lang
from symbols.abbr import abbr
from symbols.skip_sections import skip_sections
        
#import markdown as md
from IPython.display import HTML,display



def normalize_caseless(text):
    return unicodedata.normalize("NFKD", text.casefold())#text.casefold()


class DummyFile:

    def write(self,text):
        pass
    
    def close(self):
        pass
        
        
class App:

    def __init__(self):    
        parser=argparse.ArgumentParser(description="Wiki Dictionary articles parser")
        parser.add_argument("articles", default="itwiktionary-latest-pages-articles.xml", type=str, help="it articles filename to parse")
        parser.add_argument("dictionary", default="itdictionary.json", type=str, help="dictionary json output filename")
        parser.add_argument("-page", default=None, nargs=1, help="page list txt filename")
        parser.add_argument("-pagesdir", default=None, nargs=1, help="articles page output dir")
        args=parser.parse_args()
        self.args=args

    def parsexml(self,callbacks):
        
        def tag(name):
            return "{http://www.mediawiki.org/xml/export-0.10/}"+name
        
        node = 'page'
        tree = ET.parse(self.args.articles)
        root=tree.getroot()
        pages=0
        a=root.iter()
        langs=lang.keys()
        langs="(?:"+")|(?:".join(langs)+")"
        rxlangs=re.compile(r"== ?{{- *("+langs+") *-}} ?==")
        pagefile=open(self.args.page,"w",encoding="utf-8") if self.args.page!=None else DummyFile()
        
        for b in tqdm(root.iter()):
            if b.tag==tag("page"):
                title=b.find(tag("title")).text
                if not re.search(r"^(MediaWiki)|(Template)|(Wikizionario)|(\w+:)",title):
                    pagefile.write(title+"\t")
                    title=title.replace("/","-")
                    title=title.replace("\\","-")
                    text=b.find(tag("revision")).find(tag("text"))
                    if text!=None:   
                        langs=rxlangs.findall(text.text)
                        pagefile.write("|".join(langs)+"\n")
                        if "it" in langs:
                            pages+=1
                            for callback in callbacks:
                                callback(title,text.text)
                    else:
                        pagefile.write("no revision\n")
        
        pagefile.close()
        
    
    def extract(self):
        def savepage(title,text):
            file= open(os.path.join(basepagedir,title+".wiki","w",encoding="utf-8"))
            file.write(text.text)
            file.close()
            
        def translate(title,text):
            html,referer=parser.parse(title,text)
            dictionary[normalize_caseless(title)]={"title":title,"html":html,"ref":referer}
            
        basepagedir=self.args.pagesdir
        dictionary={}
        print(self.args.articles)
        parser=WikiTextParser()
        
        callbacks=[]
        if basepagedir!=None:
            callbacks.append(savepage)

        callbacks.append(translate)

        self.parsexml(callbacks)
        
        file= open(self.args.dictionary,"w",encoding="utf-8")
        file.write(json.dumps(dictionary))
        file.close()
        
        
        
        
class WikiTextParser:

    def __init__(self):
        langs=lang.keys()
        langs="(?:"+")|(?:".join(langs)+")"
        self.rxlangs=re.compile(r"== ?{{- *("+langs+") *-}} ?==")        
        
    def titolo1(self,caption):
        return "<h1>"+caption+"</h1>"

    def titolo2(self,caption):
        return "<h3>"+caption+"</h3>"

    def sigla(self,testo):
        return "<span class='sigla'>"+testo+"</span>"

    def cutSection(self,text,section):
        start=re.search(section,text)
        if start:
            end=re.search("\n\n",text[start.end():])
            if end:
                text=text[:start.start()]+text[start.end()+end.end():]
            else:
                text=text[:start.start()]
        return text
                
    def replaceLang(self,m):
        l= lang.get(m.group(1),"")
        return l if l!="" else m.group(0)

    def newLines(self,g1,g2,g3,text):
        if g1=="\n":
            text="\n"+text
        if g3!=None:
            text+=g3
        if g2=="\n":
            text+="\n"
        return text


    def replaceAbbr(self,m):
        g1=m.group(1)
        g2=m.group(6)
        g3=m.group(5)
        title=(g1=="\n" and g2=="\n")
        ab=m.group(3)=="-"
        easy=m.group(4)=="|it"
        w=m.group(2)
        #print(w,title,g1==None,g2==None,"e"+g1+"e","$"+g2+"$",repr(g1),repr(g2))
        l= abbr.get(w,"")
        if l!="":
            if title:
                return self.newLines(g1,g2,g3,self.titolo2(l))
            elif not ab:
                return self.newLines(g1,g2,g3,self.sigla(l))
            return self.newLines(g1,g2,g3,l)
        return m.group(0)

       
    def clean(self,html):
        return re.sub(r"(?m)\n==[^=]+==\n.+$","",html)

    def getword(self,path,word,clean=True):        
        try:
            file=open(os.path.join(path,word+".wiki","r",encoding="utf-8"))
            text=file.read()
            file.close()
        except:
            text=""
        return self.parse(word,text,clean)
            
    def parse(self,word,text,translate=True):
        if text=="":
            return "",""
        it=re.search(r"== *{{- *it *-}} *==",text)
        ot=self.rxlangs.search(text[it.end():])
        if ot:
            text=text[it.end():it.end()+ot.start()]
        else:
            text=text[it.end():]
        
        referer=re.search(r"{{Vd\|(\w+)}}", text)
        if referer:
            referer=referer.group(1)
        else:
            referer=""
        
        if translate:
            for skip_section in skip_sections:
                text=self.cutSection(text,skip_section)
            
            for skip_section in [r"{{Trad1.*}}"]:
                skip=self.cutSection(text,skip_section)
                while skip!=text:
                    text=skip
                    skip=self.cutSection(text,skip_section)


            for cerca,sost in [ (r"(?m)(\n?){{((-?)[\w ]+-?)(\|it)?}}( *)(\n?)",self.replaceAbbr),
                                #(r"({{[A-Za-z]+}})",replaceAbbr),
                                (r"{{((\w|-)+)}}",self.replaceLang),
                                (r'\[\[File(.)*\]\]', ""),
                                #(r'^\n+', "\n"),
                                (r'{{[Pp]n ?(\| ?((.*)))*}}',"<b>"+word+"</b>"),
                                (r"{{Linkp\|(\w+)}}",r"Plurale \1"),
                                (r"{{Glossa\|([^}]+)}}",r"\1"),
                                (r"{{Fig}}","Figurativo:"),
                                (r"(?m)^#\*\* ?(.+)$",r"<ol><ul><ul><li>\1</li></ul></ul></ol>"),   # #* apertura
                                (r"(?m)^#\* ?(.+)$",r"<ol><ul><li>\1</li></ul></ol>"),              # #** apertura
                                (r"(?m)^#\# ?(.+)$",r"<ol><ol><li>\1</li></ol></ol>"),              # ## apertura
                                (r"(?m)^# ?(.+)$",r"<ol><li>\1</li></ol>"),                         # # apertura
                                (r"(?m)^\*\* ?(.+)$",r"<ul><ul><li>\1</li></ul></ul>"),             # #* apertura
                                (r"(?m)^\* ?(.+)$",r"<ul><li>\1</li></ul>"),                        # #* apertura
                                (r"</(?P<list>[ou]l)>\n<(?P=list)>",r"\n"),                         #  chiusura 1
                                (r"</(?P<list>[ou]l)>\n<(?P=list)>",r"\n"),                         #  chiusura 2
                                (r"'''([^']+)'''", r'<i>\1</i>'),
                                (r"''(.+)''", r'"\1"'),
                                (r"(''|\")\((.+)\)(''|\")",r'"\2"'),
                                (r"{{Vd\|(\w+)}}",r"Vedi \1"),
                                (r"{{Tabs\|\s*((\w|\|)+)}}",r"Forme Flesse \[\1\]"),
                                (r"{{Term\|(\w+)\|\w\w}}",r"(term. \1)"),
                                (r"{{(\w+)\|it}}",r"\1"),
                                (r"\[\[Categoria[^]]+\]\]",""),
                                (r"\[\[(\w:)?[^]|]+\|([^]]+)\]\]",r"<b>\2</b>"),
                                (r"\[\[([^]]+)?#[^]|]+\|([^]]+)\]\]",r"<i>\2</i>"),
                                (r"\[\[([^]]+)\]\]",r"\1"),
                                #(r"\n","<br>")
                            ]:

                text=re.sub(cerca, sost, text)
            
            for skip_section in [r"{{Quote",r"{{-(\w+)-}}"]:
                skip=self.cutSection(text,skip_section)
                while skip!=text:
                    text=skip
                    skip=self.cutSection(text,skip_section)

            text=self.titolo1(word)+"\n\n"+re.sub(r"(?m)^(((<b)|(<span)|[^<\n][\w\s'\"]+)(.+))$",r"<p>\1</p>",text)
            
        return self.clean(text),referer
        #display(HTML(md.markdown(text)))

        
    
   
if __name__ == "__main__":
    app=App()
    app.extract()

