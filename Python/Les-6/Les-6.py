#!/usr/bin/env python3
'''
-neem de code uit Les-5 en integreer hierin een van de uitzonderingen van Les 6
- Maak een nieuwe module met een foutieve code. Speel de code af en maak een schermafdruk van de foutmelding die u krijgt.

'''
#!/usr/bin/env python3
'''
-Maak een weekmenu-dictionary met zeven keys
-voeg per key een gerecht toe als waarde
-maak een vraag aan die de gebruiker een dag laat selecteren
-Scrhijf een code die het correcte gerecht aan de gebruiker wordt getoond

'''
#WeekMenu = dict{}

from pprint import pprint as pp
weekMenu = {
    'Maandag':'noerenkool stamppot met worst',
    'Dinsdag':'omelet met prei, ham en kaas',
    'Woensdag':'thaise groene curry',
    'Donderdag':'spaghetti bolognese',
    'Vrijdag':'pannenkoeken met ahoornsiroop',
    'Zaterdag':'runder-spareribs',
    'Zondag':'steak met groente',
}
kijkMenu = True

def menuKeuze(Dag):
    '''Een functie om een gerecht te kiezen '''
    if str(Dag) == 'Exit':
        print('Exiting program')
        kijkMenu = False
        exit()
    else:
        try:
            DagGerecht = weekMenu.pop(Dag)
            try:
                print("Het is vandaag {0}, het gerecht van de dag is {1}".format(Dag,DagGerecht))
            except KeyError:
                print("KeyError. Please check the list below for valid keys")

            print('')
            print("Wilt u nog een andere dag inzien? Zo ja vul deze dan in. Zo nee, typ 'Exit'. Om het gehele menu te zien, typ 'Menu'")
        except ValueError:
            print('Incorrect Value')
        except KeyError:
            print("KeyError. Please check the list below for valid keys")
            print(weekMenu.keys())


while kijkMenu == True:
    print('')
    try:
        weekDag = str(input('Welke dag van de week is het? '))
        if weekDag == 'Menu':
            Dagen = weekMenu.keys()
            print(Dagen)
        else:
            try:
                menuKeuze(weekDag)
            except ValueError:
                print("Invalid Input, please check for casing or spaces. A correct input would be 'Maandag'")

    except ValueError:
        print("Invalid Input, please check ")
    except IndexError:
        print("Index Out of range")
    except KeyError:
        print("Incorrect key input")

