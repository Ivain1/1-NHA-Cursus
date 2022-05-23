#!/usr/bin/env python3


inputName = str(input('Uw naam hier, alstublieft: '))

def userGreet(userName): #Geeft de gebruiker een persoonlijke begroeting gebaseerd op: -Naam

    ''' Dit is een DocString'''
    secretUser = str('Batman')
    if userName == secretUser:
        print('Initializing BatCave Security Protocols...\nSecuring Digital Environment...\nCapturing Rogues...\nSummoning Alfred...\nWelcome Back, Batman!')
    else:
        print('Welkom terug, Gebruiker', userName, '\nHet Systeem is klaar voor gebruik\nGeen veranderingen sinds de vorige keer dat u ingelogd heeft')

userGreet(inputName)
