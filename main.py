# GALGJE SPEL
# GESCHREVEN DOOR Guus Vlaskamp en Ischa van Weeren
# DOEL VAN PROGRAMMA Het maken van een Galgje
###################
#IMPORTS
###################
import random
###################
#GLOBALE VARIABELEN
####################
geheim_woord = []  #dit is wat de gebruiker moet gaan raden
tot_nu_toe_geraden_woord = [
]  #dit is wat de gebruiker tot nu toe goed heeft geraden
foute_gokken = []
spel_afgelopen = False
levens = 10


##############
# FUNCTIE DEFINITIES
##############
def welkomstWoord():
    print("Welkom bij Galgje!")
    print(
        "Dit zijn de spelregels 1.Je hebt maximaal 10x fout raden. 2.De spelers raden om de beurt een letter {Deze regel is alleen van toepassing als er meer dan 1 speler is} 3.De speler die het woord als eerste raad wint het spel."
    )


def raadLetter(): #Dit zorgt ervoor dat de gebruiker een woord kan gaan raden
    print("Wil je een letter raden?")
    invoer = input()
    return invoer


def maakWoordMetStreepjes():
    streepjes_woord = []
    for i in range(len(geheim_woord)):  #voor elk letter in geheim woord
        streepjes_woord.append(
            "_")  #per letter in het te raden woord aanvullen met streepjes
    print("Tot nu toe geraden woord",
          streepjes_woord)  #even printen om te testen
    return streepjes_woord


def verwerkGoedeGok(tot_nu_toe_geraden_woord, gok, geheim_woord,
                    spel_afgelopen): #als de letter in het woord zit zorgt dit er voor dat dat verwerkt wordt
    print("Hoera!")
    index_teller = 0
    for letter in geheim_woord:
        if gok == letter:
            tot_nu_toe_geraden_woord[index_teller] = gok
        index_teller += 1
    if '_' not in tot_nu_toe_geraden_woord:
        print("Gefeliciteerd! Je hebt het woord geraden, speel gerust opnieuw!")
        spel_afgelopen = True
    return tot_nu_toe_geraden_woord, spel_afgelopen

    #Zet letter op goede plek
    #Check spel afgelopen


def verwerkFouteGok(levens, spel_afgelopen, gok):
    print("Fout")
    levens -= 1
    foute_gokken.append(gok)
    print("tot nu toe fout gegokte letters", foute_gokken)
    if levens == 0:
        print("Helaas, het is je niet gelukt om het woord te raden, het woord was,", geheim_woord, "probeer het gewoon opnieuw!")
        spel_afgelopen = True
    return levens, spel_afgelopen, foute_gokken


def toonSpelstatus():
    print("spel status", tot_nu_toe_geraden_woord)
    print("Hoeveelheid levens:", levens)



def kieswoord():
  woorden = ["autobandventieldopje", "liquidatie", "dextrose", "anticipatie", "portefeuille", "confisqueren", "bestuurdersaansprakelijksheidverzekering"]
  gekozen_woord = random.choice(woorden)
  for letter in gekozen_woord:
    geheim_woord.append(letter)


################
#HOOFDPROGRAMMA
################
welkomstWoord()
kieswoord()
tot_nu_toe_geraden_woord = maakWoordMetStreepjes()
while not spel_afgelopen:
    toonSpelstatus()
    gok = raadLetter()
    print("gegokt, tot nu toe:", tot_nu_toe_geraden_woord)
    if gok in geheim_woord:
        tot_nu_toe_geraden_woord, spel_afgelopen = verwerkGoedeGok(
            tot_nu_toe_geraden_woord, gok, geheim_woord, spel_afgelopen)

    else:
        levens, spel_afgelopen, foute_gokken = verwerkFouteGok(levens, spel_afgelopen, gok)
