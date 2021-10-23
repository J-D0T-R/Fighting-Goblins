###   Arrays Program   ###
###   James Rutley   ###
###   Start Date: 10/22/2021   ###
###   End Date: 10/22/2021   ###

#Imports
import random# Allows the enemy actions to be randomised.

import sys #Allows me to end the program


# Arrays
inventory = ["sword", "herbs"]

health = {"you":80}

recoil = {"dmg":3} # Recoil damage from fire

actions = {"stab":5, "slash":3, "fire":7, "heal":10, "run":0} #player options and thier damage values

goblins = {"ronald":10, "cecil":10, "luke":10, "gabby":15} #The enemies

g_actions = {"stab":6, "buff":5, "miss":0} #enemy options and thier damage values. buff raises a goblins health

# functions
def roll(): # lets the goblins act randomly
    return(random.randint(1, 5))

def fight():
    
    if len(goblins) > 0: #Making sure there are enemies left to fight
        print("What do you do?")
        print(actions.keys()) #Prints the actions but not the values
        action = input().lower() # they pick what to do.
        
        if action == "stab": #Does five damage to a single goblin
            target = input("Which goblin do you stab? ").lower()
            
            if target in goblins:
                goblins[target] = goblins[target] - actions["stab"]
                print(f"You stabed {target}.")
                
                if goblins[target] <= 0:
                    print(f"You have slain {target}!")
                    print(f"{target} dropped some assorted nic naks")
                    inventory.append("nic naks")
                    print("You picked up the nic naks!")
                    del goblins[target] #Removes the dead goblin from the list of goblins.
                    g_fight()
                    
                else:
                    g_fight()
            else: # they enter an incorrect target
                print(f"You look around for {target} but can't find them, mayhaps they have already been vanquished.")
                g_fight() 
                
        elif action == "slash": #does 3 damage to all targets
            # I tried to use a for loop for this but turns out that if the length of a list
            # or dictionary changes while it's being looped
            # it causes an error. So I just did worte out each individual goblin for convience sake
            # if I revist this program in the future I hope to find a way to do this with a loop
            
            if "ronald" in goblins:
                print("You slashed ronald!")
                goblins["ronald"] = goblins["ronald"] - actions["slash"]
                
                if goblins["ronald"] <= 0:
                    print("You have slain ronald!")
                    print("ronald dropped some assorted nic naks")
                    inventory.append("nic naks")
                    print("You picked up the nic naks!")
                    del goblins["ronald"]
                    
                else:
                    pass
                
            else:
                pass
                
            if "cecil" in goblins:
                print("You slashed cecil!")
                goblins["cecil"] = goblins["cecil"] - actions["slash"]
                
                if goblins["cecil"] <= 0:
                    print("You have slain cecil!")
                    print("cecil dropped some assorted nic naks")
                    inventory.append("nic naks")
                    print("You picked up the nic naks!")
                    del goblins["cecil"]
                    
                else:
                    pass
                
            else:
                pass
                
            if "luke" in goblins:
                print("You slashed luke!")
                goblins["luke"] = goblins["luke"] - actions["slash"]
                
                if goblins["luke"] <= 0:
                    print("You have slain luke!")
                    print("luke dropped some assorted nic naks")
                    inventory.append("nic naks")
                    print("You picked up the nic naks!")
                    del goblins["luke"]
                    
                else:
                    pass 
                
            else:
                pass
            
            if "gabby" in goblins:
                print("You slashed gabby!")
                goblins["gabby"] = goblins["gabby"] - actions["slash"]
                
                if goblins["gabby"] <= 0:
                    print("You have slain gabby!")
                    print("gabby dropped some assorted nic naks")
                    inventory.append("nic naks")
                    print("You picked up the nic naks!")
                    del goblins["gabby"]
                    
                else:
                    pass
                
            else:
                pass
            
                    
            g_fight()
            
        elif action == "fire": #Does seven damage to a single goblin and 3 to the player
            target = input("Which goblin do you burn? ").lower()
            
            if target in goblins:
                goblins[target] = goblins[target] - actions["fire"]
                print(f"You burned {target}.")
                health["you"] = health["you"] - recoil["dmg"] #Recoil
                if health["you"] <=0:
                    print("The heat was too much for you and you died.")
                    sys.exit()
                
                else:
                    print("You singed yourself a little.")
                    g_fight()
                    
                    if goblins[target] <= 0: # they kill a goblin.
                        print(f"You have slain {target}!")
                        print(f"{target} dropped some burnt nic naks") #Loot drop
                        inventory.append("burnt nic naks")
                        print("You picked up the nic naks!")
                        del goblins[target] # removing the dead goblin from the list of enemies.
                        g_fight() # enemies turn
                    
                    else:
                        g_fight() # enemies turn
                        
        elif action == "heal": #healing
            print("You ate some herbs and healed yourself!")
            health["you"] = health["you"] + actions["heal"]
            g_fight() # enemy turn
            
        elif action == "run": #ends the program early
            print("You escaped the goblins!")
            sys.exit()
            
        else: #if they enter an input that isn't one of the actions
            print("You don't have that luxury in this situation.")
            fight() #recurisively lets them try agian
            
    else: #They win
        print("You have vanquished the goblins!")
        print("You got some loot from the goblins and added it into your inventory!")
        print(inventory)
        sys.exit()
        
def g_fight(): # goblins turn
    for item in goblins:
        attack = roll()
        if attack == 1 or attack == 2: #stabbing has a 2/5 chance
            print(f"{item} stabbed you!")
            health["you"] = health["you"] - g_actions["stab"]
                
            if health["you"] <= 0: #checking if they're dead
                print("The wound was fatal, you died.")
                sys.exit()
                
            else:
                continue
            
        elif attack == 3: # buff has a 1/5 chance
            print(f"{item} became more durable!")
            goblins[item] = goblins[item] + g_actions["buff"]
                       
        else: #miss has a 2/5 chance
            print(f"{item} tried to stab you and missed.")
            
    fight() # your turn again
    
#Main code
print("You are acousted by four goblins: ronald, cecil, luke, and gabby.")
print("All you have on you is your trusty sword and some herbs.")
fight()