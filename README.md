# sms
## Skills management system


Tool di gestione competenze interno ad un azienda di sviluppo software.

Potranno essere realizzate versioni più generiche, ma al momento questo è ciò che mi interessa. : )

Il software verrà realizzato principalmente in python, semplicemente perchè è il linguaggio con cui mi trovo più comodo per fare questo genere di cose. ; )

Viene rilasciato sotto licenza GNU AGPLv3.

Il codice sarà in inglese ma probabilmente le parti più descrittive (tipo questa) rimarranno in italiano finchè non mi verrà voglia di tradurle. XD


Di seguito provo a definire le fasi di sviluppo. Non è detto che riuscirò a mantenere esattamente questo flusso. In particolare, cercerò di eseguire gli sviluppi di ogni fase tenendo a mente che l'obiettivo è di arrivare a realizzare anche le fasi successive. Quindi se ad esempio dovesse emergere che nel fare uno sviluppo per la fase 2 viene comodo implementare subito uno sviluppo della fase 3 probabilimente lo farò.


### Fase 1 MVP
Per ogni account consentire di:
 - indicare i linguaggi di programmazione che si conoscono a partire da un set predefinito, ma con possibilità di aggiungere nuovi linguaggi;
 - per ogni linguaggio indicare il livello di familiarità da 0 a 5, dove 0 = mancaanza di conoscenza del linguaggio e 5 = ottima padronanza del linguaggio;

#### Legenda livelli di conoscenza:
- 0 magari l'ho sentito nominare ma di fatto non lo conosco;
- 1 penso di saperlo leggere;
- 2 so farci qualcosa, ma sto imparando;
- 3 posso lavorarci, ma meglio se insieme a qualcuno che ne sa di più;
- 4 posso lavorarci autonomamente;
- 5 posso usarlo anche per farti il caffè;

### Fase 2
 - Verificare i linguaggi: per ogni linguaggio consentire di aggiungere link a progetti a cui si ha contribuito o pagine di certificazione;
 - All'inserimento di un linguaggio non ancora gestito inviare notifica ad un gruppo di utenti supervisori.

Dashboard con riassunto di percentuali di diffusione delle varie competenze senza differenziazione per livello di conoscenza


### Fase 3
Consentire l'inserimento di altre competenze oltre ai linguaggi di programmazione:
 - Elenco di argomenti definito da un gruppo di utenti;
 - Linguaggi di markup;
 - Framework (angular, ecc)
 - ? Formati dati (csv, json...);
 - ? Protocolli di comunicazione;
 - ? Modalità di lavoro: waterfall, AGILE (quale AGILE);
 - ? Architetture: monolite, microservizi (tipologia REST, SOAP);
 - ? Paradigmi di programmazione;
 - ? Lingua parlata, scritta, compresa?;
 - Altro.


Dashboard con riassunto di percentuali di diffusione delle varie competenze con differenziazione per livello di conoscenza


### Fase 4
Consentire la generazione di account per team/gruppi/macrogruppi
- ogni team potrà indicare gli utenti membri e i progetti di competenza, per ogni progetto inserire una descrizione e le competenze utilizzate (non solo linguaggi)
- ogni gruppo potrà definire i team da cui è composto
- ogni macrogruppo potrà definire i gruppi da cui è composto


Dashboard suddivise per team, gruppi, macrogruppi che riportano la percentuale di competenze divise per tipologia, senza differenziazione per livelli di conoscenza.
Ad esempio: 
- la dashboard del team T dirà che è composto da N persone e per quanto rugarda la competenza C (esempio i linguaggi di programmazione) n% ha almeno livello 1 in c_{1} (elemento di C ad esempio Java) m% ha almeno livello 1 in c_{2} (elemento di C ad esempio Python), ecc;
- la dashboard del gruppo G dirà che è composto da Y team e per quanto riguarda la competenza C (esempio i linguaggi di programmazione) y% dei team ha almeno livello 1 in c_{1} (elemento di C ad esempio Java) z% ha almeno livello 1 in c_{2} (elemento di C ad esempio Python), ecc +  n% delle persone del gruppo ha almeno livello 1 in c_{1} (elemento di C ad esempio Java) m% ha almeno livello 1 in c_{2} (elemento di C ad esempio Python), ecc;  


Dashboard delle singole competenze che riportano la percentuale di gruppi. Cioè la visione opposta rispetto alla dashboard precedentemente descritta, ad esempio:
- la dashboard della competenza C (esempio i linguaggi di programmazione) dirà che la competenza c1 (elemento di C ad esempio Java) è conosciuto almeno a livello 1 da n% degli utenti, y% dei team, g% dei gruppi, m% dei macrogruppi, ecc


### Fase 5
Tutte le dashboard filtrabili per livelli di conoscenza.

Interfaccia per eseguire ricerca di utenti/team/gruppi/macrogruppi per competenza e livello di competenza.


### Fase 6
Consentire a team, gruppi, macrogruppi di pubblicare annunci di posizioni aperte.


Consentire agli utenti di rispondere alle posizioni aperte ed effettuare candidature spontanee

### Fase 7
Validazione delle conoscenze.
Esempio sui linguaggi di programmazione:

Per ogni linguaggio conosciuto, ogni 3 mesi si chiede di scrivere un breve pezzo di codice con un output ben definito e questo viene inviato random alle altre persone che dichiarano di conoscere il linguaggio alle quali si richiede di indicare qual'é l'output. Ad ogni persona deve arrivare un massimo di boh, 2 o 3 test per linguaggio e sarebbe bene valutare in modo differente un test non fatto da un test fallito. 





