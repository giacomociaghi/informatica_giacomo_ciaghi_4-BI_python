# Varianti

| Stato | Servizio / Piattaforma | Indirizzo di Riferimento | Tipologia di Utilizzo |
| :---: | :--- | :--- | :--- |
| ☑  | GitHub Enterprise | [https://github.com](https://github.com) | Condivisione dei repository e consegna progetti |
| ☑  | Jupyter Server | [https://istituto.it](https://istituto.it) | Esecuzione dei notebook e analisi dati |
| ☐ | Server Git Locale | [https://git.local](https://git.local) | ~~Backup obsoleto dei file temporanei~~ |
| ☐ | Database Didattico | [https://istituto.it](https://istituto.it) | Consultazione schemi e query di test |
| ☐ | Registro Elettronico | [https://istituto.it](https://istituto.it) | Verifica delle presenze e dei voti finali |
| ☐ | Cloud Storage | [https://istituto.it](https://istituto.it) | Archivio della documentazione teorica |
## Differenze di rendering tra GitHub e Visual Studio Code

Nell'anteprima integrata di **Visual Studio Code** e sulla piattaforma **GitHub** si osservano comportamenti **parzialmente disallineati** nell'estensione Markdown. **Nell'anteprima standard** di Visual Studio Code, il motore di rendering interno **converte correttamente** le caselle di controllo (`[x]` e `[ ]`) in elementi grafici visivi (quadratini spuntati o vuoti) anche se inserite dentro una tabella; **sulla piattaforma GitHub**, invece, la sintassi **GFM**(GitHub Flavored Markdown) **non supporta le checkbox** all'interno delle tabelle, mostrandole semplicemente come testo piatto a schermo. Entrambi gli ambienti interpretano invece in **modo identico e corretto** l'allineamento centrato della prima colonna, la formattazione dei collegamenti ipertestuali cliccabili e la linea orizzontale sul testo barrato.

