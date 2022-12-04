import unicodedata
from bs4 import BeautifulSoup
import os
import json 
import re


class Section:
    
    def __init__(self,stype,text):
        self.text=text
        self.stype=stype
        self.rows=[]
    
    def append(self,stype,text):
        section=Section(stype,text)
        self.rows.append(section)
        return section
        
    def haveRows(self):
        return len(self.rows)!=0
    
    def display(self,parent=""):
        parent= self.stype if parent=="" else parent + ">" + self.stype
        print(parent,self.text)
        for r in self.rows:
            r.display(parent)
    
    def innerText(self,indent="",indentChar="\t"):
        text=""
        for r in self.rows:
            text+=indent+r.text+"\n"
            if r.haveRows():
                text+=r.innerText(indent+indentChar,indentChar)
        return text
        
class DictEntry:


    def __init__(self,entry):
        self.html=entry["html"]
        self.ref=entry["ref"]
        self.title=entry["title"]
        b=BeautifulSoup("<html>"+self.html+"</html>","xml")
        #self.title=b.find("h1").text
        sections={}
        section=[]
        for h3 in b.find_all(["h3"]):
            section=Section("section",h3.text)
            sections[h3.text]=section
            for tag in h3.find_next_siblings():#(["p","ol","ul"]):
                if tag.name=="h3":
                    break
                elif tag.name=="p":
                    section.append("paragraph",tag.text)
                elif str(tag.name) in ["ol","ul"]:
                    self.getList(tag,section.append(tag.name,""))
        self.sections=sections
        
    def getList(self,tag,section):
        for child in tag.children:#(["li","ol","ul"]):
            if child.name=="li":
                section.append("item",child.text)
            elif str(child.name) in ["ol","ul"]:
                self.getList(child,section.append(child.name,""))
        return section

    def display(self):
        print(self.title)
        for name in self.sections.keys():
            self.sections[name].display()
    
    def innerText(self,indentChar="\t"):
        text=self.title.title()+"\n"
        for name in self.sections.keys():
            text+="\n"+name.title()+"\n"
            text+=self.sections[name].innerText(indentChar,indentChar)
        return text
        

class WikiDict:

    def __init__(self,filename):
        file=open(filename,"r",encoding="utf-8")
        self.dictionary=json.loads(file.read())
        file.close()
        
    def search(self,word):
        word=unicodedata.normalize("NFKD", word.casefold())#text.casefold()
        entry=self.dictionary.get(word,False)
        if entry:
            entry=DictEntry(entry)
        return entry
        
          