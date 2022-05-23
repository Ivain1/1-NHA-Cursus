F = open("testbestand.txt","w+")
lowerBound = 0
upperBound = 999999
trueNum = 50
userNum = input('Vul hier een getal naar uw keuze in\n')

if not userNum.isdigit():
    raise ValueError('Incorrect input - Uw input was niet een getal. Vult u alstublieft een getal in')
elif int(userNum) < lowerBound or int(userNum) > upperBound:
    raise ValueError('Out of bounds - Houdt uw getal alstublieft tussen de {0} en de {1}'.format(lowerBound,upperBound))
elif int(userNum) > trueNum:
    wData = 'De input van de gebruiker was {0}'.format(userNum)
    #print(wData)
    F.write(wData)
F.close()

