Slutuppgift: Bankkonto

Kurs: Programmering i Python, 25 yhp

Student: Mira Lee


# Instruktioner:
I mappen server_klient_mapp ligger det 3 filer, för köra programmet starta bank_server.py och därefter starta bank_klient.py

På klientterminalen börjar menyn köras.
## Alternativ 1'Add an account to register'
För att kunna lägga en bankkonto i register tryck 1. Det leder till en ytterligare input, där man ska mata in (owner, account name, account type. account number). Separera endast med mellanslag och lägg endast 4 ovanstående värden i den ordning som anges. Du får du bekräftelse om det har genomförts eller inte.

```
Write owner, account name, account type, account number: Mira lönekonto privatkonto 123456789

Account added in register
```
## Alternativ 2 'List all accounts'
För att se register med alla bankkonto tryck 2. Om listan är tom erhåller du endast tom lista, annars ser du de kunder som har lagts tidigare vid första alternativet.

## Alternativ 3 'Choose one account for more information'
För att kunna se detaljer för en specifik kund tryck 3. Ange sedan bankkontonummer, direkt efter får du bekräftelse ett bankonto med den angivna nummer eller inte.
```
Account number: 123456789
Requested account: Owner: Mira, account name: lönekonto, account type: privatkonto, account number: 123456789
```

## Testerna för koden
För att kunna köra testerna Aktivera venv och installera requirements.txt. Filen för tester (test_bank_server.py) ligger i katalogen tests. 
Från rootdir: devops22-python-final-miralee94\server_klient_mapp kan man köra kommando tox.

## Virtual Environments

Se requirements.txt för alla paket

```
pip install -r requirements.txt
```

python 3.10



## Betygskriterier
I denna uppgift ska du bygga ett banksystem.

# Krav G

Du kan lägga till en kund i registret

Du kan fråga servern om vilka kunder som finns

Du kan fråga om detaljer för en specifik kund

Du skriver något enhetstest

## Begränsningar
En kund = ett konto
