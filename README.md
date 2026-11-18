
# Auto Fix 5Ghz Modem

## Descrizione

Uno script ancora incompleto.

Tempo fa notavo che la rete tramite WiFi del Router non performava abbastanza fino a staccarsi quasi del tutto.  
Ho indagato e tra le varie motivazioni ho scoperto anche che la frequenza 5GHz può generare interferenze o problematiche varie alla 2.4Ghz, soprattutto a una certa distanza e a quei dispositivi che necessitano obbligatoriamente della 2.4Ghz.

Da quel momento l'ho spenta ma per motivi esterni torna ogni tot a riaccendersi, cominciando così ad attendere che si riaccendesse per andare a disabilitarla maunualmente subito dopo.

Dopo tutta questa manualità, nasce l'esigenza di dover automatizzare il tutto, grazie all'utilizzo della Libreria "selenium".

Lo Script si occupa di entrare effettuando il login, andare a spegnere la 5GHz e riavviare il Router.
