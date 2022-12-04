# WikiDictionary
Parse Italian Wiki Dictionary Articles

wikiparse can parse italian wiki dictionary articles xml file ( https://dumps.wikimedia.org/itwiktionary/latest/itwiktionary-latest-pages-articles.xml.bz2 ) into html, text or structured text

## how to use

wikiparse.py articles.xml dictionary.json

the command will create a json file with all italian dictionary entries in json format.

every entry have title, html, ref properties.

## wikidict helper

The helper class WikiDict can read dictionary.json file and search for word entries

usage:

```
wd=WikiDict(filename)
word=wd.search("casa")

word.html # contain the html of definition of word
word.display() # print the word structured content 
word.innerText() # get the all text of definition of word
word.sections # is a dict of all sections of definition

for name,section in word.sections.items():
  # section.text section text
  # section.stype section type
  # section.rows inner section rows, every row is a section object
  section.display()
```
