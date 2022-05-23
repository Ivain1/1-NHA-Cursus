#!/usr/bin/env python3

'''
- maak een string van 10 fruitsoorten
- gebruik de functie split() om uw string om te zetten naar een lijst
- gebruik iteratie om de eerste vijf fruitsoorten los te vertonen aan de gebruiker
- BONUS: maak een iterator die een reeks getallen retourneert (beginnend met 1) en de getoonde waarde telkens met 1 verhoogd.


'''
fruitBasket = "appel peer banaan mandarijn sinaasappel ananas aardbei framboos mango cranberry".split()
numList = []
#FruitList = FruitBasket.split(',')
for i in range(0,5):
    print(fruitBasket[i])

def numberBuilder(startPoint,endPoint):
    '''
Een functie die een reeks getallen binnen een aangegeven bereik in een lijst opsomt en die lijst retourneert
startpoint: <int> hoger dan 0
    '''
    if startPoint > 0 and startPoint < 99999 and endPoint > 0 and endPoint < 99999:
        try:
            for x in range(startPoint,endPoint+1):
                num1 = int(x)
                numList.append(num1)
            return (numList)
        except ValueError:
            print('invalid input')

    else:
        print('Input out of range; values must stay between 0 and 99999')

print(numberBuilder(1,206))