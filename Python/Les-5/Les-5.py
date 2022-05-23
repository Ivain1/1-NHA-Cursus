#!/usr/bin/env python3
'''
-Maak een weekmenu-dictionary met zeven keys
-voeg per key een gerecht toe als waarde
-maak een vraag aan die de gebruiker een dag laat selecteren
-Scrhijf een code die het correcte gerecht aan de gebruiker wordt getoond

'''
#WeekMenu = dict{}
#!/usr/bin/env python3
from pprint import pprint as pp

weekMenu = {
    'Maandag':'Boerenkool stamppot met worst',
    'Dinsdag':'Omelet met prei, ham en kaas',
    'Woensdag':'Thaise groene curry',
    'Donderdag':'Spaghetti Bolognese',
    'Vrijdag':'Pannenkoeken met Ahoornsiroop',
    'Zaterdag':'Runder-Spareribs',
    'Zondag':'Steak met groente',
}
kijkMenu = True
print('Welkom bij het Wekelijkse Restaurant!')
def menuKeuze(Dag):
    if str(Dag) == 'Exit':
        print('U verlaat het restaurant')
        kijkMenu = False
        exit()
    else:
        #menuKaart = weekMenu.copy()
        DagGerecht = weekMenu.get(Dag)
        print("Het is vandaag {0}, het gerecht van de dag is {1}".format(Dag,DagGerecht))
        print('')
        print("Wilt u nog een andere dag inzien? Zo ja vul deze dan in. Zo nee, typ 'Exit'. Om het gehele menu te zien, typ 'Menu'")

while kijkMenu == True:
    print('')
    weekDag = str(input('Welke dag van de week is het? '))
    if weekDag == 'Menu':
        pp(weekMenu)

    else:
        menuKeuze(weekDag)


