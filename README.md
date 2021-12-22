# Blackjack challenge

Blackjack is een eenvoudig kaartspel waar je tegen een dealer (bank) speelt. Ken je het spel niet? Hier kan je een korte uitleg vinden: [https://nl.wikipedia.org/wiki/Blackjack](https://nl.wikipedia.org/wiki/Blackjack)

De variant die we hier spelen is een wat vereenvoudigd:

-   Alleen de basisregels gelden, dus *niet* verdubbelen, verzekeren, splitsen of overgeven.
-   Er blijven op deze manier *twee* opties over voor een speler: een kaart vragen (hit) of passen.
-   Heb je als speler meer dan 21 punten, dan wint de bank.
-   De bank neemt altijd een nieuwe kaart als de totale waarde minder dan 17 is. De bank stopt altijd als hij de waarde tussen 17 en 21 heeft. Heeft de bank meer dan 22, dan wint de speler.
-   De kaarten worden elke keer willekeurig uit de volledige set van kaarten getrokken, dus kaarten tellen heeft geen zin.
-   De kleuren van de kaarten worden niet weergegeven. Elke kaart wordt door een nummer (2-9) of een karakter ('A': aas, 'K': heer, 'Q': vrouw, 'J': boer) weergegeven, waar de aas telt voor 11 of 1, en de anderen voor 10.

Voor deze challenge is het de bedoeling om een programma te schrijven dat bepaalt wat je als speler moet doen: een kaart krijgen (hit) of passen. Pas hiervoor de functie `should_hit` aan.

Als de timer is afgelopen zullen we kijken wie het vaakst van de bank kan winnen. Succes!