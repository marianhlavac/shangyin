# Semestrální práce MI-IOT

## Zadání

Vytvořit přístroj, který bude zaznamenávat spotřebu kávy pomocí RFID karet.
Přístroj bude položen vedle kávovaru a přiblížením kartičky zapíše jedno uvaření kávy.
Kartičky budou spárovány s uživateli a jejich příslušností k oddělení a aplikace
pak vypočítá podíl spotřeby kávy mezi dvěmi (či více) oddělení.

## Hardware

 - Platforma Raspberry Pi
 - Čtečka RFID karet RFID-RC522
 - LCD displej LCD1602
 - tlačítko, piezo speaker
 
## Software

 - Python
 - SQLite
 
## Implementace

Implementováno bylo v Pythonu za použití knihoven pro komunikaci s RFID čtečkou
a dalšími komponentami - *CharLCD* a *pirc522*. Knihovna *Flask* pro běh webového
serveru se statistikami.

## Problémy při implementaci

Bylo nutné psát testy, 
