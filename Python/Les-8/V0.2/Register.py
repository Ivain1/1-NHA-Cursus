#!/usr/bin/env python3

class CursistenRegister:
    def __init__(self,dataList):
        self._dataList = list(dataList)


    def voorNaam(self):
        vNaam1 = str(input('Uw voornaam hier: '))
        if vNaam1.isdigit():
            raise ValueError("Een naam bevat geen cijfers. Vul alstublieft uw naam in alphabetische letters in")
        else:
            self._dataList.append(vNaam1)



    def achterNaam(self):
        aNaam1 = str(input('Uw achternaam hier: '))
        if aNaam1.isdigit():
            raise ValueError("Een naam bevat geen cijfers. Vul uw naam in alphabetische letters in")
        else:
            self._dataList.append(aNaam1)



    def cursistAdres(self):
        print('Vul hier uw Adres in')
        straatNaam1 = str(input('Straatnaam: '))
        if not straatNaam1.isalpha():
            raise ValueError("Een straatnaam bevat geen cijfers. Vul uw straatnaam in alphabetische letters in")
            pass
        else:
            pass
        huisNummer1 = str(input('HuisNummer: '))
        plaatsNaam1 = str(input('Woonplaats: '))
        if plaatsNaam1.isdigit():
            raise ValueError("Een plaatsnaam bevat geen cijfers. Vul uw straatnaam in alphabetische letters in")
            pass
        else:
            pass
        cAdres1 = '{0} {1}\n{2}\n'.format(straatNaam1,huisNummer1,plaatsNaam1)
        self._dataList.append(cAdres1)



    def cursistEmail(self):
        print('Email-Adres')
        cEmail = str(input('Vul hier uw Email-adres in: '))
        if cEmail.isalpha():
            raise ValueError("Een email-adres bevat meer dan alleen letters. Het correcte formaat is adresNaam@domeinnaam(.nl) ")
        # Notitie voor docent: Ik heb ervoor gekozen hier niet een uitgebreide functie om te checken of een email-adres geldig is toe te voegen. Dit is niet deel van de opdracht en significant meer werk dan de andere checks
        elif not cEmail.islower():
            raise ValueError("Een email-adres bevat geen hoofdletters. Zorg alstublieft dat uw email alleen in kleine letters ingevuld wordt")
        else:
            self._dataList.append(cEmail)



    def welkomstBericht(self):
        cNaam1 = self._dataList[0] + ' ' + self._dataList[1]
        cAdres2 = self._dataList[2]
        cEmail2 = self._dataList[3]

        berichtOutput = '\nWelkom bij de cursus, {0}\nUw cursusmateriaal wordt verstuurd naar het geregistreerde adres:\n \n{1}\nMeer informatie vindt u in het bericht dat verstuurd is naar {2}'.format(cNaam1,cAdres2,cEmail2)
        print(berichtOutput)
        return(True)


Cursist1 = CursistenRegister([])
inputVolledig = False
while inputVolledig == False:
    print('Welkom bij de inschrijving van onze Cursus. Vul hieronder AUB uw naam, adres en email-adres in: ')
    Cursist1.voorNaam()
    Cursist1.achterNaam()
    Cursist1.cursistAdres()
    Cursist1.cursistEmail()
    inputVolledig = Cursist1.welkomstBericht()




