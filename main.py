# GALGJE SPEL
# GESCHREVEN DOOR Guus Vlaskamp en Ischa van Weeren
# DOEL VAN PROGRAMMA Het maken van een Galgje


###################
#GLOBALE VARIABELEN
####################
geheim_woord = ['h','a','l','l','o']	#dit is wat de gebruiker moet gaan raden
tot_nu_toe_geraden_woord = []					#dit is wat de gebruiker tot nu toe goed heeft geraden
spel_afgelopen = False
levens = 10


##############
# FUNCTIE DEFINITIES 
##############
def welkomstWoord():
	print("Welkom bij Galgje!")
	print("Dit zijn de spelregels 1.Je hebt maximaal 10x fout raden. 2.De spelers raden om de beurt een letter {Deze regel is alleen van toepassing als er meer dan 1 speler is} 3.De speler die het woord als eerste raad wint het spel.")

def raadLetter ():
  print("Wil je een letter raden?")
  invoer = input()
  if invoer not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
    print("Foute invoer")
  else:
    return invoer
  


def maakWoordMetStreepjes():
  streepjes_woord = []
  for i in range(len(geheim_woord)):        #voor elk letter in geheim woord
    streepjes_woord.append("_")   #per letter in het te raden woord aanvullen met streepjes
  print("Tot nu toe geraden woord", streepjes_woord)  #even printen om te testen
  return streepjes_woord

def verwerkGoedeGok( tot_nu_toe_geraden_woord, gok, geheim_woord ):
  print("Hoera!")
  index_teller = 0
  for letter in geheim_woord:
    if gok == letter: 
      tot_nu_toe_geraden_woord [index_teller] = gok
    index_teller += 1
  return tot_nu_toe_geraden_woord
      
  #Zet letter op goede plek
  #Check spel afgelopen

def verwerkFouteGok(levens):
  print("Fout")
  levens -= 1
  if levens == 0:
    spel_afgelopen = True
  return levens, spel_afgelopen

def toonSpelstatus():
  print(tot_nu_toe_geraden_woord)
################
# HOOFDPROGRAMMA
################
welkomstWoord()
tot_nu_toe_geraden_woord = maakWoordMetStreepjes()
while not spel_afgelopen:
  gok = raadLetter()

  if gok in geheim_woord:
   tot_nu_toe_geraden_woord = verwerkGoedeGok(tot_nu_toe_geraden_woord, gok, geheim_woord)
    
  else: 
    levens, spel_afgelopen = verwerkFouteGok(levens)
