# WikiDictionary
Parse Italian Wiki Dictionary Articles

wikiparse can parse italian wiki dictionary articles xml file ( https://dumps.wikimedia.org/itwiktionary/latest/itwiktionary-latest-pages-articles.xml.bz2 ) into html, text or structured text

## how to use

download the articles file unzip it and use:

```
wikiparse.py articles.xml dictionary.json
```

the command will create a json file with all italian dictionary entries in json format.

every entry have title, html, ref properties.

## wikidict helper

The helper class WikiDict can read dictionary.json file and search for word entries

usage:

```python
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


## Example of word.display()

```python
word.display()
```

```text
casa
section Sostantivo
section>paragraph casa
section>ol 
section>ol>item (term. architettura) (term. edilizia) (term. tecnologia) (term. ingegneria) edificio costruito per essere 
section>ol>ul 
section>ol>ul>item "un mio amico ha acquistato una bella casa in montagna" 
section>ol>item dimora di una persona;  costruzione o struttura in cui uno vive; in particolare la casa in cui uno vive con la sua famiglia
section>ol>ul 
section>ol>ul>item "ti avviso che stasera torno a casa tardi dal lavoro"
section>ol>ul>item "e, in quel momento solo, si recò in piazza per poi andare a casa e riprendere il lavoro"
section>ol>item edificio che accoglie temporaneamente, per motivi specifici di salute o altro, alcune categorie di persone
section>ol>ul 
section>ol>ul>item "ha dovuto ricoverare sua zia in una casa di riposo"
section>ol>item (senso figurato) (term. industriale) casa costruttrice
section>ol>ul 
section>ol>ul>item "ho portato il mio scooter dal meccanico per una riparazione, ma ho dovuto aspettare qualche giorno perché  il pezzo di ricambio era reperibile solo presso la casa costruttrice"
section>ol>item (term. scacchi) nel gioco degli scacchi, è il nome tecnico della casella sulla scacchiera
section>ol>item (term. astrologia) ognuna di dodici parti in cui è suddiviso il cielo in un dato momento
section>ol>ul 
section>ol>ul>item "alla tua nascita Saturno si trovava nella settima casa"
section>ol>item (term. astrologia) casa lunare: ognuna di ventotto parti in cui è suddiviso il cielo durante il moto di rivoluzione della Luna
section>ol>ul 
section>ol>ul>item "la Luna entrerà nella venticinquesima casa lunare alle 16:31 di giovedì prossimo"
section Etimologia
section>paragraph dal latino "casa", ossia "capanna, casa rustica"
section Sinonimi
section>ul 
section>ul>item "casa in riferimento al materiale di cui è fatta: pietra, mattoni" costruzione
section>ul>item "casa in senso burocratico e legale" stabile 
section>ul>item "genericamente:casa adibita a vari scopi" edificio, (per es. palazzo d'abitazione
section>ul>item "casa in cui si radunano gli studenti per apprendere sotto la direzione degli insegnanti" scuola
section>ul>item "casa pubblica in cui si possono consultare libri o prenderli a prestito" biblioteca
section>ul>item "casa in cui vengono curati i malati d una certa gravità"  ospedale
section>ul>item "casa adibita al culto in cui i cristiani pregano" chiesa
section>ul>item "casa adibita al culto in cui gli ebrei pregano" sinagoga
section>ul>item "casa adibita al culto in cui i musulmani pregano" moschea 
section>ul>item "casa adibita al culto in cui i buddisti pregano" tempio 
section>ul>item "casa  in cui si recitano commedie" teatro
section>ul>item "casa in cui si proiettano film" cinema
section>ul>item "in maniera specifica: tipologia" fabbricato (per es. rurale, civile, industriale)
section>ul>item "casa in cui si abita in senso generico" abitazione
section>ul>item "casa in cui si risiede abitualmente" dimora
section>ul>item "casa in cui si abita in senso amministrativo" residenza
section>ul>item "casa dove si curano i propri interessi o si fanno affari" domicilio
section>ul>item "casa in comproprietà per più famiglie" condominio
section>ul>item "grande casa signorile o per uffici pubblici" palazzo (per es. il palazzo dell'INPS)
section>ul>item "casa signorile per più famiglie" palazzina
section>ul>item "casa per più famiglie abitata da ceti popolari" casamento
section>ul>item "parte di condominio abitata da una famiglia o da persone sole" appartamento
section>ul>item "casa ampia ed elegante con grande giardino, signorile" villa
section>ul>item (term. antico), (term. letterario) "casa signorile" magione
section>ul>item "casa dei re o specialmente con valore iperbolico: casa magnifica" reggia
section>ul>item "piccola casa con giardino" villetta
section>ul>item "casa unifamiliare o bifamiliare con giardino" villino
section>ul>item "in campagna: casa isolata" casale, casolare
section>ul>item "casa di campagna di pregio" cottage
section>ul>item "in alta montagna: casa in legno  utilizzata stagionalmente come ricovero" baita
section>ul>item "in montagna: casa di villeggiatura o per fare sport" chalet
section>ul>item "casa misera, povera" tugurio, stamberga, casupola
section>ul>item "casa misera e decrepita" catapecchia
section>ul>item "di animali selvatici" tana, covo
section>ul>item "di animali: uccelli" nido
section>ul>item (senso figurato)"ambiente domestico" focolare, tetto, mura domestiche, nido
section>ul>item (per estensione) "casa in senso di discendenza" famiglia, casato, stirpe
section>ul>item "casa regnante appartenente alla stessa famiglia" dinastia
section>ul>item "casa in senso commerciale" impresa, ditta, azienda
section>ul>item "diritto: in riferimento ad un impresa commerciale" società
section>ul>item "casa di un'impresa" sede
section>ul>item "casa in cui lavorano gli operai" fabbrica
section>ul>item "casa dove si depositano le merci ed altro materiale" magazzino
section>ul>item "casa dove si vendono le merci al dettaglio" negozio
section>ul>item "giochi: scacchi" casella
section>ul>item "casa nel senso di fortificazione" mura
section>ul>item "insieme di case limitrofe ove risiedono generalmente persone dello stesso  ceto" quartiere: es. quartiere popolare
section>ul>item "casa per militari" quartiere
section>ul>item "casa dei propri padri nel senso di antenati" patria, terra
section>ul>item "casa da cui ripararsi dalle intemperie o dai pericoli" ricovero
section>ul>item "casa dove si sta temporaneamente" alloggio
section>ul>item "casa per persone bisognose o per bambini in età prescolare" asilo
section>ul>item "casa per detenuti" carcere
section>ul>item "finta casa adibita a postazione da sparo per l'artiglieria" casamatta
section>ul>item "casa da gioco" casinò
section Derivate
section>ul 
section>ul>item casabase, casale, casalina, casalinga, casalinghità, casalinghitudine, casalingo, casalino, casamatta, casamento, casamobile, casareccio, casata, casatico, casato, casatorre, caseggiato, casella, casellante, casellario, casellista, casello, casereccio, casiere, casigliano, casinista, casino, casinò,  casolare, casone, casotto, casula, senzacasa 
section Alterati
section>ul 
section>ul>item (accrescitivo)  casone (in particolare in riferimento a impianti come quelli delle funivie)
section>ul>item (diminutivo) casina
section>ul>item (vezzeggiativo) casetta
section Proverbi, Modi di dire
section>ul 
section>ul>item "casa dolce casa"
section>ul>item "casa mia, casa mia, per piccina che tu sia, tu mi sembri una badia": avere una casa propria significa avere più libertà
section>ul>item "essere casa e chiesa": essere una persona retta, a volte anche con accezione negativa
section>ul>item "essere di casa": essere frequentatore abituale di un certo ambiente
section>ul>item "mettere su casa": crearsi una famiglia
section>ul>item "giocare in casa": agire in un ambiente conosciuto
section>ul>item "tornare a casa": usato anche con significato più ampio, come tornare in patria o nella propria città
section>ul>item "donne per casa, una in figura, l'altra in pittura": se si vuole la pace in casa deve esserci una sola donna
section>ul>item "grosso come una casa": qualcosa di notevole, molto evidente
section>ul>ul 
section>ul>ul>item "ha commesso un fallo grosso come una casa"
section>ul>ul>item "gli ha fatto un regalo grosso come una casa"
section>ul>item "Due noci in un sacco e due donne in casa fanno un bel fracasso"
section>ul>item "aiutarli a casa loro": slogan politico che insiste affinché alcuni stranieri non si stabiliscano neanche come cittadini in altri Paesi: senza specificare l'origine della "casa", s'intende quindi che restino al di fuori dei confini senza capire bene quale aiuto verrebbe appunto offerto
```

## Example of word.innerText()

```python
word.innerText()
```

```text
Casa

Sostantivo
casa

(term. architettura) (term. edilizia) (term. tecnologia) (term. ingegneria) edificio costruito per essere 

"un mio amico ha acquistato una bella casa in montagna" 
dimora di una persona;  costruzione o struttura in cui uno vive; in particolare la casa in cui uno vive con la sua famiglia

"ti avviso che stasera torno a casa tardi dal lavoro"
"e, in quel momento solo, si recò in piazza per poi andare a casa e riprendere il lavoro"
edificio che accoglie temporaneamente, per motivi specifici di salute o altro, alcune categorie di persone

"ha dovuto ricoverare sua zia in una casa di riposo"
(senso figurato) (term. industriale) casa costruttrice

"ho portato il mio scooter dal meccanico per una riparazione, ma ho dovuto aspettare qualche giorno perché  il pezzo di ricambio era reperibile solo presso la casa costruttrice"
(term. scacchi) nel gioco degli scacchi, è il nome tecnico della casella sulla scacchiera
(term. astrologia) ognuna di dodici parti in cui è suddiviso il cielo in un dato momento

"alla tua nascita Saturno si trovava nella settima casa"
(term. astrologia) casa lunare: ognuna di ventotto parti in cui è suddiviso il cielo durante il moto di rivoluzione della Luna

"la Luna entrerà nella venticinquesima casa lunare alle 16:31 di giovedì prossimo"

Etimologia
dal latino "casa", ossia "capanna, casa rustica"

Sinonimi

"casa in riferimento al materiale di cui è fatta: pietra, mattoni" costruzione
"casa in senso burocratico e legale" stabile 
"genericamente:casa adibita a vari scopi" edificio, (per es. palazzo d'abitazione
"casa in cui si radunano gli studenti per apprendere sotto la direzione degli insegnanti" scuola
"casa pubblica in cui si possono consultare libri o prenderli a prestito" biblioteca
"casa in cui vengono curati i malati d una certa gravità"  ospedale
"casa adibita al culto in cui i cristiani pregano" chiesa
"casa adibita al culto in cui gli ebrei pregano" sinagoga
"casa adibita al culto in cui i musulmani pregano" moschea 
"casa adibita al culto in cui i buddisti pregano" tempio 
"casa  in cui si recitano commedie" teatro
"casa in cui si proiettano film" cinema
"in maniera specifica: tipologia" fabbricato (per es. rurale, civile, industriale)
"casa in cui si abita in senso generico" abitazione
"casa in cui si risiede abitualmente" dimora
"casa in cui si abita in senso amministrativo" residenza
"casa dove si curano i propri interessi o si fanno affari" domicilio
"casa in comproprietà per più famiglie" condominio
"grande casa signorile o per uffici pubblici" palazzo (per es. il palazzo dell'INPS)
"casa signorile per più famiglie" palazzina
"casa per più famiglie abitata da ceti popolari" casamento
"parte di condominio abitata da una famiglia o da persone sole" appartamento
"casa ampia ed elegante con grande giardino, signorile" villa
(term. antico), (term. letterario) "casa signorile" magione
"casa dei re o specialmente con valore iperbolico: casa magnifica" reggia
"piccola casa con giardino" villetta
"casa unifamiliare o bifamiliare con giardino" villino
"in campagna: casa isolata" casale, casolare
"casa di campagna di pregio" cottage
"in alta montagna: casa in legno  utilizzata stagionalmente come ricovero" baita
"in montagna: casa di villeggiatura o per fare sport" chalet
"casa misera, povera" tugurio, stamberga, casupola
"casa misera e decrepita" catapecchia
"di animali selvatici" tana, covo
"di animali: uccelli" nido
(senso figurato)"ambiente domestico" focolare, tetto, mura domestiche, nido
(per estensione) "casa in senso di discendenza" famiglia, casato, stirpe
"casa regnante appartenente alla stessa famiglia" dinastia
"casa in senso commerciale" impresa, ditta, azienda
"diritto: in riferimento ad un impresa commerciale" società
"casa di un'impresa" sede
"casa in cui lavorano gli operai" fabbrica
"casa dove si depositano le merci ed altro materiale" magazzino
"casa dove si vendono le merci al dettaglio" negozio
"giochi: scacchi" casella
"casa nel senso di fortificazione" mura
"insieme di case limitrofe ove risiedono generalmente persone dello stesso  ceto" quartiere: es. quartiere popolare
"casa per militari" quartiere
"casa dei propri padri nel senso di antenati" patria, terra
"casa da cui ripararsi dalle intemperie o dai pericoli" ricovero
"casa dove si sta temporaneamente" alloggio
"casa per persone bisognose o per bambini in età prescolare" asilo
"casa per detenuti" carcere
"finta casa adibita a postazione da sparo per l'artiglieria" casamatta
"casa da gioco" casinò

Derivate

casabase, casale, casalina, casalinga, casalinghità, casalinghitudine, casalingo, casalino, casamatta, casamento, casamobile, casareccio, casata, casatico, casato, casatorre, caseggiato, casella, casellante, casellario, casellista, casello, casereccio, casiere, casigliano, casinista, casino, casinò,  casolare, casone, casotto, casula, senzacasa 

Alterati

(accrescitivo)  casone (in particolare in riferimento a impianti come quelli delle funivie)
(diminutivo) casina
(vezzeggiativo) casetta

Proverbi, Modi Di Dire

"casa dolce casa"
"casa mia, casa mia, per piccina che tu sia, tu mi sembri una badia": avere una casa propria significa avere più libertà
"essere casa e chiesa": essere una persona retta, a volte anche con accezione negativa
"essere di casa": essere frequentatore abituale di un certo ambiente
"mettere su casa": crearsi una famiglia
"giocare in casa": agire in un ambiente conosciuto
"tornare a casa": usato anche con significato più ampio, come tornare in patria o nella propria città
"donne per casa, una in figura, l'altra in pittura": se si vuole la pace in casa deve esserci una sola donna
"grosso come una casa": qualcosa di notevole, molto evidente

"ha commesso un fallo grosso come una casa"
"gli ha fatto un regalo grosso come una casa"
"Due noci in un sacco e due donne in casa fanno un bel fracasso"
"aiutarli a casa loro": slogan politico che insiste affinché alcuni stranieri non si stabiliscano neanche come cittadini in altri Paesi: senza specificare l'origine della "casa", s'intende quindi che restino al di fuori dei confini senza capire bene quale aiuto verrebbe appunto offerto
```

## Example of word.html

```python
word.html
```

```html
<h1>casa</h1>




<h3>Sostantivo</h3>
<p><b>casa</b></p>
<ol><li>(term. architettura) (term. edilizia) (term. tecnologia) (term. ingegneria) edificio costruito per essere </li>
<ul><li>"un mio amico ha acquistato una bella casa in montagna" </li></ul>
<li>dimora di una persona;  costruzione o struttura in cui uno vive; in particolare la casa in cui uno vive con la sua famiglia</li>
<ul><li>"ti avviso che stasera torno a casa tardi dal lavoro"</li>
<li>"e, in quel momento solo, si recò in piazza per poi andare a casa e riprendere il lavoro"</li></ul>
<li>edificio che accoglie temporaneamente, per motivi specifici di salute o altro, alcune categorie di persone</li>
<ul><li>"ha dovuto ricoverare sua zia in una casa di riposo"</li></ul>
<li><span class=\'sigla\'>(senso figurato)</span> (term. industriale) casa costruttrice</li>
<ul><li>"ho portato il mio scooter dal meccanico per una riparazione, ma ho dovuto aspettare qualche giorno perché  il pezzo di ricambio era reperibile solo presso la casa costruttrice"</li></ul>
<li>(term. scacchi) nel gioco degli scacchi, è il nome tecnico della casella sulla scacchiera</li>
<li>(term. astrologia) ognuna di dodici parti in cui è suddiviso il cielo in un dato momento</li>
<ul><li>"alla tua nascita Saturno si trovava nella settima <b>casa</b>"</li></ul>
<li>(term. astrologia) casa lunare: ognuna di ventotto parti in cui è suddiviso il cielo durante il moto di rivoluzione della Luna</li>
<ul><li>"la Luna entrerà nella venticinquesima <b>casa</b> lunare alle 16:31 di giovedì prossimo"</li></ul></ol>

<h3>Etimologia</h3>
<p>dal latino "<b>casa</b>", ossia "capanna, casa rustica"</p>

<h3>Sinonimi</h3>
<ul><li>"casa in riferimento al materiale di cui è fatta: pietra, mattoni" costruzione</li>
<li>"casa in senso burocratico e legale" stabile </li>
<li>"genericamente:casa adibita a vari scopi" edificio, (per es. palazzo d\'abitazione</li>
<li>"casa in cui si radunano gli studenti per apprendere sotto la direzione degli insegnanti" scuola</li>
<li>"casa pubblica in cui si possono consultare libri o prenderli a prestito" biblioteca</li>
<li>"casa in cui vengono curati i malati d una certa gravità"  ospedale</li>
<li>"casa adibita al culto in cui i cristiani pregano" chiesa</li>
<li>"casa adibita al culto in cui gli ebrei pregano" sinagoga</li>
<li>"casa adibita al culto in cui i musulmani pregano" moschea </li>
<li>"casa adibita al culto in cui i buddisti pregano" tempio </li>
<li>"casa  in cui si recitano commedie" teatro</li>
<li>"casa in cui si proiettano film" cinema</li>
<li>"in maniera specifica: tipologia" fabbricato (per es. rurale, civile, industriale)</li>
<li>"casa in cui si abita in senso generico" abitazione</li>
<li>"casa in cui si risiede abitualmente" dimora</li>
<li>"casa in cui si abita in senso amministrativo" residenza</li>
<li>"casa dove si curano i propri interessi o si fanno affari" domicilio</li>
<li>"casa in comproprietà per più famiglie" condominio</li>
<li>"grande casa signorile o per uffici pubblici" palazzo (per es. il palazzo dell\'INPS)</li>
<li>"casa signorile per più famiglie" palazzina</li>
<li>"casa per più famiglie abitata da ceti popolari" casamento</li>
<li>"parte di condominio abitata da una famiglia o da persone sole" appartamento</li>
<li>"casa ampia ed elegante con grande giardino, signorile" villa</li>
<li>(term. antico), (term. letterario) "casa signorile" magione</li>
<li>"casa dei re o specialmente con valore iperbolico: casa magnifica" reggia</li>
<li>"piccola casa con giardino" villetta</li>
<li>"casa unifamiliare o bifamiliare con giardino" villino</li>
<li>"in campagna: casa isolata" casale, casolare</li>
<li>"casa di campagna di pregio" cottage</li>
<li>"in alta montagna: casa in legno  utilizzata stagionalmente come ricovero" baita</li>
<li>"in montagna: casa di villeggiatura o per fare sport" chalet</li>
<li>"casa misera, povera" tugurio, stamberga, casupola</li>
<li>"casa misera e decrepita" catapecchia</li>
<li>"di animali selvatici" tana, covo</li>
<li>"di animali: uccelli" nido</li>
<li><span class=\'sigla\'>(senso figurato)</span>"ambiente domestico" focolare, tetto, mura domestiche, nido</li>
<li><span class=\'sigla\'>(per estensione)</span> "casa in senso di discendenza" famiglia, casato, stirpe</li>
<li>"casa regnante appartenente alla stessa famiglia" dinastia</li>
<li>"casa in senso commerciale" impresa, ditta, azienda</li>
<li>"diritto: in riferimento ad un impresa commerciale" società</li>
<li>"casa di un\'impresa" sede</li>
<li>"casa in cui lavorano gli operai" fabbrica</li>
<li>"casa dove si depositano le merci ed altro materiale" magazzino</li>
<li>"casa dove si vendono le merci al dettaglio" negozio</li>
<li>"giochi: scacchi" casella</li>
<li>"casa nel senso di fortificazione" mura</li>
<li>"insieme di case limitrofe ove risiedono generalmente persone dello stesso  ceto" quartiere: es. quartiere popolare</li>
<li>"casa per militari" quartiere</li>
<li>"casa dei propri padri nel senso di antenati" patria, terra</li>
<li>"casa da cui ripararsi dalle intemperie o dai pericoli" ricovero</li>
<li>"casa dove si sta temporaneamente" alloggio</li>
<li>"casa per persone bisognose o per bambini in età prescolare" asilo</li>
<li>"casa per detenuti" carcere</li>
<li>"finta casa adibita a postazione da sparo per l\'artiglieria" casamatta</li>
<li>"casa da gioco" casinò</li></ul>

<h3>Derivate</h3>
<ul><li>casabase, casale, casalina, casalinga, casalinghità, casalinghitudine, casalingo, casalino, casamatta, casamento, casamobile, casareccio, casata, casatico, casato, casatorre, caseggiato, casella, casellante, casellario, casellista, casello, casereccio, casiere, casigliano, casinista, casino, casinò,  casolare, casone, casotto, casula, senzacasa </li></ul>

<h3>Alterati</h3>
<ul><li><span class=\'sigla\'>(accrescitivo)</span>  casone (in particolare in riferimento a impianti come quelli delle funivie)</li>
<li><span class=\'sigla\'>(diminutivo)</span> casina</li>
<li><span class=\'sigla\'>(vezzeggiativo)</span> casetta</li></ul>

<h3>Proverbi, Modi di dire</h3>
<ul><li>"<i>casa</i> dolce <i>casa</i>"</li>
<li>"<i>casa</i> mia, <i>casa</i> mia, per piccina che tu sia, tu mi sembri una badia": avere una casa propria significa avere più libertà</li>
<li>"essere <i>casa</i> e chiesa": essere una persona retta, a volte anche con accezione negativa</li>
<li>"essere di <i>casa</i>": essere frequentatore abituale di un certo ambiente</li>
<li>"mettere su <i>casa</i>": crearsi una famiglia</li>
<li>"giocare in <i>casa</i>": agire in un ambiente conosciuto</li>
<li>"tornare a <i>casa</i>": usato anche con significato più ampio, come tornare in patria o nella propria città</li>
<li>"donne per <i>casa</i>, una in figura, l\'altra in pittura": se si vuole la pace in casa deve esserci una sola donna</li>
<li>"grosso come una <i>casa</i>": qualcosa di notevole, molto evidente</li>
<ul><li>"ha commesso un fallo grosso come una casa"</li>
<li>"gli ha fatto un regalo grosso come una casa"</li></ul>
<li>"Due noci in un sacco e due donne in <b>casa</b> fanno un bel fracasso"</li>
<li>"aiutarli a <i>casa</i> loro": slogan politico che insiste affinché alcuni stranieri non si stabiliscano neanche come cittadini in altri Paesi: senza specificare l\'origine della "casa", s\'intende quindi che restino al di fuori dei confini senza capire bene quale aiuto verrebbe appunto offerto</li></ul>
```
