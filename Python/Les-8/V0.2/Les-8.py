from Register import CursistenRegister

Cursist1 = CursistenRegister([])
inputVolledig = False
while inputVolledig == False:
    Cursist1.voorNaam()
    Cursist1.achterNaam()
    Cursist1.cursistAdres()
    Cursist1.cursistEmail()
    inputVolledig = Cursist1.welkomstBericht()


#R = CursistenRegister(None,None,None,None)
#vNaamData = str(input('Uw voornaam hier: '))
#R.voorNaam(vNaamData)
#aNaamData = str(input('Uw achternaam hier:'))
#R.achterNaam(aNaamData)
#cAdresData = str(input('Uw Adres hier:'))
#R.cursistAdres(cAdresData)
#cEmailData = str(input('Uw Email-adres hier:'))
#R.cursistEmail(cEmailData)
#R = CursistenRegister(vNaamData,aNaamData,cAdresData,cEmailData)
#R.welkomstBericht()


