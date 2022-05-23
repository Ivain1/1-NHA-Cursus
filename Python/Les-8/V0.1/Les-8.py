from Register import CursistenRegister

#R = CursistenRegister(None,None,None,None)
vNaamData = str(input('Uw voornaam hier: '))
#R.voorNaam(vNaamData)
aNaamData = str(input('Uw achternaam hier:'))
#R.achterNaam(aNaamData)
cAdresData = str(input('Uw Adres hier:'))
#R.cursistAdres(cAdresData)
cEmailData = str(input('Uw Email-adres hier:'))
#R.cursistEmail(cEmailData)
R = CursistenRegister(vNaamData,aNaamData,cAdresData,cEmailData)
R.welkomstBericht()


