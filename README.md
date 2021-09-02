# csv2qif
### Ita
Programma scritto in python per convertire un file in formato CSV in formato QIF per essere
importato direttamente in GNUCASH.
E' presente un file di configurazione *csv2qif.config* che contiene le informazioni necessarie
a mappare correttamente i dati da convertire. La prima colonna del file CSV occupa la posizione 0.

In questa versione del programma non viene valorizzato il campo con la categoria da importare in GNUCASH;
per questo motivo l'indice della colonna corrispondente è valorizzata con la posizione -1.
La categoria di GNUCASH deve avere il formato CATEGORY:SUBCATEGORY:ITEM (ad esempio EXPENSE:CAR:FUEL).

Anche la colonna con il codice della transazione è opzionale e può essere inibito utilizzando l'indice -1.
### Eng
Program written in python to convert a CSV format file to QIF format to be
imported directly into GNUCASH.
There is a configuration file *csv2qif.config* which contains the necessary information
to correctly map the data to be converted. The first column of the CSV file occupies position 0.

In this version of the program the field with the category to be imported into GNUCASH is not filled in;
for this reason the index of the corresponding column is valued with the position -1.
The GNUCASH category must have the format CATEGORY: SUBCATEGORY: ITEM (for example EXPENSE: CAR: FUEL).

The column with the transaction code is also optional and can be inhibited using the index -1.
