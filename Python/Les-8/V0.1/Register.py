class CursistenRegister:
    def __init__(self,vNaam,aNaam,adres,email):
        self._voorNaam = vNaam
        self._achterNaam = aNaam
        self._cursistAdres = adres
        self._cursistEmail = email
        dataList = []


    def voorNaam(self):
        return(self.voorNaam)
        #dataList.append(vNaam1)


    def achterNaam(self):
        return(self._achterNaam)
        #return(aNaam1)


    def cursistAdres(self):
        return(self._cursistAdres)
        #return(cAdres)


    def cursistEmail(self):
        return(self._cursistEmail)
        #return(cEmail)


    def welkomstBericht(self):
        berichtOutput = 'Welkom,{0} {1}.\n Uw pakket is verstuurd naar {2}, het geregistreerde adres\n Meer informatie vindt u in het bericht dat verstuurd is naar {3}'.format(self._voorNaam,self._achterNaam,self._cursistAdres,self._cursistEmail)
        print(berichtOutput)



