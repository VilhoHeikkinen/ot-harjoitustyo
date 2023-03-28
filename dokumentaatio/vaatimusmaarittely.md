# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen on tarkoitus olla klassinen miinaharava, johon sisältyy kolme vaikeusastetta. Eri vaikeusasteiden suoritusnopeuksista pidetään tulostaulukkoa, johon tulos tallennetaan käyttäjänimen mukaan

## Käyttöliittymäluonnos

Sovellus aukeaa suoraan pelin käyttöliittymään, johon sisältyy kello, jäljellä olevien pommien määrä sekä nappi, jolla voi aloittaa pelin uudestaan. Toinen käyttöliittymä sisältää tulostaulukon.

## Perusversion tarjoama toiminnallisuus

### Pelissä

- Peli alkaa täysin peitossa olevasta ruudukosta, josta pitää etsiä kaikki ruudut, joissa ei ole pommia.
- Käyttäjä voi valita pelin vaikeusasteen kolmesta eri vaihtoehdosta
- Pelin voi nollata ja aloittaa uudestaan
- Pelatessa lasketaan jäljellä olevat pommit sekä aika sekunteina
  - Pommien jäljellä oleva määrä perustuu pelaajan merkkaamiin kohtiin, joissa voisi olla pommi
- Pommit asetetaan pelikentälle jonkin logiikan mukaan (esim. ensimmäisellä siirrolla ei voi osua pommiin)
- Pelikentältä aukeaa tyhjää klikkauksen jälkeen sopivasti
- Peitossa olevien ruutujen viereen kohtiin, joissa ei ole pommeja, piirretään numeroita, joiden avulla voi päätellä lähellä olevien pommien määrän

### Pelin jälkeen

- Kun peli loppuu tilanteeseen, että kaikki pommit on löydetty, niin käyttäjä antaa nimimerkkinsä
  - Tälle nimimerkille tallennetaan suoritusaika tilastoihin
- Jos pelin häviää, käyttäjälle ilmoitetaan, että hän hävisi, jonka jälkeen pelin voi aloittaa alusta

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää voitaisiin kehittää esim. seuraavilla ominaisuuksilla:

- Ruudukon koon sekä pommien määrän voi päättää itse
- Tilastoja voi tarkastella nimimerkin perusteella
- Peli antaa vinkkejä pelaajalle (miinaharavaan liittyy myös paljon muistisääntöjä, joista voisi kertoa)
- Peliä voisi pelata myös muilla muodoilla (esim. kolmioilla), jos logiikka sen sallii
