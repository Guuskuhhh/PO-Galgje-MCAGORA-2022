# GALGJE SPEL
# GESCHREVEN DOOR Guus Vlaskamp en Ischa van Weeren
# DOEL VAN PROGRAMMA Het maken van een Galgje


###################
#GLOBALE VARIABELEN
####################
geheim_woord = ['h','a','l','l','o']	#dit is wat de gebruiker moet gaan raden
tot_nu_toe_geraden_woord = []					#dit is wat de gebruiker tot nu toe goed heeft geraden
spel_afgelopen = False


##############
# FUNCTIE DEFINITIES 
##############
def welkomstWoord():
	print("Welkom bij Galgje!")
	print("Dit zijn de spelregels 1.Je hebt maximaal 10x fout raden. 2.De spelers raden om de beurt een letter {Deze regel is alleen van toepassing als er meer dan 1 speler is} 3.De speler die het woord als eerste raad wint het spel.")

def raad_letter ():
  print("Wil je een letter raden?")
  invoer = input()
  if invoer != ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
    print("Foute invoer")
  else:
    if invoer in geheim_woord:
      pass
  


def maakWoordMetStreepjes():
  streepjes_woord = []
  for i in range(len(geheim_woord)):        #voor elk letter in geheim woord
    streepjes_woord.append("_")   #per letter in het te raden woord aanvullen met streepjes
  print("Tot nu toe geraden woord", streepjes_woord)  #even printen om te testen
  return streepjes_woord



################
# HOOFDPROGRAMMA
################
welkomstWoord()
maakWoordMetStreepjes()