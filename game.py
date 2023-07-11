import textwrap
import os
import random

# initializing player status, stats, and inventory along with yesno as a conditional checked pretty frequently

yesno = ["y", "n"]

status = {"wet": False, "mark": False, "stalker": False, "champion": 0, "help": []}

inventory = {"armour": ("rags", 5, 5), "weapon": ("fists", 5)}
stats = {"NAME": "You", "AGI": 10, "ATK": inventory["weapon"][1], "DEF": inventory["armour"][1], "HP": 15, "TOTAL": 15, "CHOICE": True}

# function used to check if a player's response matches any of the options listed, then returns response

def answer(text, choices):
    text += "\n\n"
    choice = input(text).lower()
    while choice not in choices:
        choice = input("Please re-input your command.\n").lower()
    print('\n')
    return choice

# function to check if value is true to then return text parameter

def check(thing, text):
  if thing:
    return text
  else:
    return ""

# function used to display long text (most of the project) by limiting characters of text per line then splitting with \n so it formats better on screen

def wrap_text(text):
  paragraphs = text.split('\n')

  wrapped_paragraphs = [textwrap.fill(p, 120) for p in paragraphs]

  print('\n'.join(wrapped_paragraphs))

# function used to fight characters, has random assignment of first to act based off algorithm of agility stat, also couple algorithms for calculating damage/dodge

def fight(fighter):
  playerSpeed = random.randint(1, stats["AGI"])
  fighterSpeed = random.randint(1, fighter["AGI"])

  if playerSpeed > fighterSpeed:
      attacker1 = stats
      attacker2 = fighter
  else:
      attacker1 = fighter
      attacker2 = stats


  while stats["HP"] > 0 and fighter["HP"] > 0:
    print(f"HP: {stats['HP']}")
    print(f"ENEMY HP: {fighter['HP']}")
    stats["CHOICE"] = answer("What will You do? (Attack, Dodge)", ["attack", "dodge"])
    fighter["CHOICE"] = random.choice(["attack", "dodge"])

    if attacker1["CHOICE"] == "attack":
      damage = random.randint(0, attacker1["ATK"])
      damage = damage * (1 - attacker2["DEF"] / 100.0)
      if attacker2["CHOICE"] == "dodge":
        damage *= random.choice([1, 1, 1, 1, 1, 1, 1, 1, 1, 0])
      attacker2["HP"] -= damage
      attacker2["HP"] = round(attacker2["HP"], 2)
      
      if damage > 0:
        print(f"{attacker1['NAME']} hit for {round(damage, 2)} damage!")
      else:
        print(f"{attacker1['NAME']} miss!")

    if attacker2["CHOICE"] == "attack":
      damage = random.randint(0, attacker2["ATK"])
      damage = damage * (1 - attacker1["DEF"] / 100.0)
      if attacker1["CHOICE"] == "dodge":
        damage *= random.choice([1, 1, 1, 1, 1, 1, 1, 1, 1, 0])
      attacker1["HP"] -= damage
      attacker1["HP"] = round(attacker1["HP"], 2)

      if damage > 0:
        print(f"{attacker2['NAME']} hit for {round(damage, 2)} damage!")
      else:
        print(f"{attacker2['NAME']} miss!")

    if attacker1["CHOICE"] == "dodge" and attacker2["CHOICE"] == "dodge":
      print("Both of You dodged!")
  
  if stats["HP"] > 0:
    return True
  else:
    return False

# function used to update a player's inventory and update their corresponding stat

def updateGear(type, value):
  inventory[type] = value
  stats["ATK"] = inventory["weapon"][1]
  stats["DEF"] = inventory["armour"][1]

  if type == "armour":
    stats["HP"] = stats["TOTAL"] + inventory["armour"][2]
    stats["TOTAL"] = stats["HP"]


print("Welcome, to the game.\n")
input()
print("By playing this game you agree to the Introductory Clause.\n")
input()
name = input("Please sign your real-life first name here if you understand all the rules: ")
print('\n\n')

wrap_text("Sparks fly across your mind. Visions of a dimly lit room and scattered junk temporarily fade in and out before disappearing. A few moments of eternal darkness blink away.")
input()
wrap_text("*Click* You open your eyes and find yourself in a beautifully vibrant green field. The world You find yourself in is reminiscent of something You'd find in a fairy tale. With trees dotted around, You find yourself in an opening of an otherwise dense forest. You don't have much, it seems You have no more than some rags on your back and a determination to find out where You are and just exactly why you're here. You might as well explore your surroundings in this field.\n")

done = False

print('\n')

# basically just a loop for an area with a hub

while done == False:
  c = answer("Where will You go? (North/East/South/West)", ["north", "east", "south", "west"])
  if c == "south":
    wrap_text("You find yourself at the edge of the field and notice a marker in the ground. It reads “for those who hath arrived, hath good luck in exit.” You read this and feel a bit disturbed. What could it mean? You go back to the center of the field.")
  elif c == "east":
    c2 = answer("You find a small pond. A quick examination through its surprisingly clear water reveals that there is not much going on inside of it. Will You jump in? (y/n)", yesno)
    if c2 == "y":
      wrap_text("You dive into the pond. You try looking for something but find nothing. You are now wet. Congratulations. You sloppily make your way back to the center of the field.")
      status["wet"] = True
      status["mark"] = True
    else:
      wrap_text("You decide that jumping in and getting wet outweighs the benefit of potential treasure and head back to the center of the field.")
  elif c == "west":
    c2 = answer("You find, unsurprisingly, more grass and are presented in front of the looming dense forest. your curiosity invites You to poke the tree. Will You do it? (y/n)", yesno)
    if c2 == "y":
      wrap_text("You poke the tree, and... nothing happens. You notice the howling of the wind and make your way back to the center of the field.")
    else:
      wrap_text("You realize that it's probably not best to touch plants that You are unfamiliar with. You head back to the center of the field.")
  elif c == "north":
    wrap_text("You find yourself in front of the dense forest. A dense fog sets in from something deeper within. The entrance seems neither inviting nor frightful, rather an invitation for exploration.")
    c2 = answer("Will You go in? [y/n] (You may not return to the field after going into the forest.)", yesno)
    if c2 == "y":
      done = True
    else:
      wrap_text("You decide to wait until You enter this looming forest. You turn from the entrance and head back to the center of the field.")

wrap_text("Upon entering the forest You don't notice anything too out of the ordinary. You continue on a path noting that the bright sunlight from before has dissipated; being blocked from the impenetrable leaves casted above You. You continue for what feels like a while finally arriving at a log cabin. You see smoke coming out from the chimney. You further notice a stone campfire outside its domain.")

c = answer("Do You make You way inside? (y/n)", yesno)

# basically just a loop for dialogue with the old man npc

if c == "y":
  status["stalker"] = True
  done = False
  wrap_text("You open the log cabin's door and see an old man on a rocking chair balancing a dagger. He wears an eyepatch and rugged look. He's bald and has a sharp silver beard. He glances at You.\n\n*Hmph*.")
  while done == False:
    print(r"""
                                                                                                        
                                                                                                    
                                         .:^~7?JYJJJJJJJJJJJJ?!:                                    
                                  .^!?5GBB&@#P55JJJJJJJJJJJJYPB#BP?~.                               
                          .^!JPGBB##G5Y7~:!&&7                 :!JG##BPY7^.                         
                      :7PBB#GPJ!^~:.       ^G@B!.       ..::::::::. :~?5GB#G!                       
                     5@#Y!^.       ~J:       ~Y#&P?~^..P#&&@@@@@@@&~    .~5@#.                      
                   .P@5           :@@:         .~YPB#B#@@@@@@@@@@@@BPPGB##B@#.                      
                  .B@J            ?@P               ~#@@@@@@@@@@@@@G~!~^: :@#.                      
                  ~GP.            7@B.              !B#&&@@@@@@@@@#~   .7!7B#.                      
                  !JJ7            .#&:                ..:::^~~~~~^.    .JJJGG                       
                  7YJJ.            ::                                  !JJJP~                       
                  7JJ7 .!~.            .~!~:^!~!!~^. ..          ..^~:~JYJJ^                        
                  7PJ?^7JJ?~:        :!J?~!777?!^!??7?J~      ^!7?JJJJJ?7^.                         
                  .!JJ5B5JJJJ?~:..  ~JJ~           ^?JJJ^..:!?JYY5YJJ7~.                            
                    ^77JYJJJJYYJJJ!7JYJ!~!!^^?YYY55J?JJJJ5JJJ??JJ?^..                               
                       .^~~~^:^!?JJJJJY5YPPJYPYJYYJYY#YJJ7:^:                                       
                                 ~JJYY:?JJJJJ~^!JJJJG@!^?!                                          
                                 ~J5JJJ?7?~!777~:~7~5@J                                             
                                  ~@G::             ^&&!.........                                   
                   .:^!?YYYB#GGGPYB@J                7@@&BBBBBBBBGGGGBGP5J7^.                       
           .:^7Y5GB#BBGPYJJJ?!7@@&J^               ^G&B57.......:^^^^^!7J5G##B57:                   
        !5GB#BG5?!~^.          ?B@@?.             ?@&!                     .^7Y#@G!                 
       Y@B!^.                    ~Y#&5^         ^P@G:                           !P@B~               
      ?@B.                         .?B&B57~.  ~P@B7                               !@@7              
     7@B:                             :!YG##GB&B7                                  ^G@5             
    :&@^                                  .:^^:                                     .B@7            
    7@P                                                                              Y@?            
    G@7                                                                              P@7            
   ^@#.                                                                             7@B.            
   ^@B                                                                              P@7             
   ^@#.                                                                            :&@^             
   .B&:                                                                            ~#Y              
    ::                                                                                              
    """)
    c2 = answer("1. Who are You?\n2. Where am I?\n3. Can I sit by your fire?\n4. Okay... this is weird, I'm leaving.", ["1", "2", "3", "4"])
    if c2 == "1":
      wrap_text("\"Me? Well I'm just an old geezer who shouldn't be alive. I haven't seen You around here before. Let an old man give You some passing advice. It's dangerous to go alone, take this.\" *He tosses You the dagger * \"You'll need this if You wanna survive in these woods.\"(You have now obtained a sharp dagger!)")
      updateGear("weapon", ("dagger", 10))
    elif c2 == "2":
      wrap_text("\"You are in Resken. \'The greatest country of the midwest\', at least thats what *they* want You to think. You want my opinion? your in a dumpster of a country somewhere on its last legs, at least if no one does anything about it. Right now though, You are in champion woods, *MY neck of the woods* if You know what I mean. Only good place *they* haven't infected.\"")
    elif c2 == "3":
      wrap_text("\"Go right ahead" + check(status["wet"], ", its not good to stay wet for so long") + ". Just dont get burnt.\" *You peer into the fire and notice a fine white ash in a tray next to the mantle*")
    elif c2 == "4":
      print("\"...\"")
      done = True
      wrap_text("You decide to leave that old man's weird house and continue down the path for a while.")
else:
  wrap_text("You decide against entering a stranger's home and continue on the path through the dense forest.")
  if status["wet"]:
    status["stalker"] = True

wrap_text("The woods are very serene and even feel peaceful, You almost feel like You understand yourself a bit better.")

input()

# stalked by an old man who fights you

if status["stalker"]:
  wrap_text("Suddenly, You notice a bush rustling and out pops an old man! He nearly cuts one of your fingers off. (Begin fight)")
  garth = {"NAME": "The old man", "AGI": 5, "ATK": 8, "DEF": 5, "HP": 10, "CHOICE": True}
  outcome = fight(garth)
  if outcome == False:
    wrap_text("\"Ahh the thrill of the hunt, gotta love it! Enjoy being worm food pal.\"\n")
    print(r"""
              
   _____          __  __ ______       ______      ________ _____    
  / ____|   /\   |  \/  |  ____|     / __ \ \    / /  ____|  __ \   
 | |  __   /  \  | \  / | |__       | |  | \ \  / /| |__  | |__) |  
 | | |_ | / /\ \ | |\/| |  __|      | |  | |\ \/ / |  __| |  _  /   
 | |__| |/ ____ \| |  | | |____     | |__| | \  /  | |____| | \ \ _ 
  \_____/_/    \_\_|  |_|______|     \____/   \/   |______|_|  \_(_)
                                                                                                                                   
              """)
    input()
    quit()
  else:
    wrap_text("\"Heh... I used to be the champion of these woods. *cough* I guess you've usurped that title, hah! Well, you've earned this sword and this armor. It's been passed through every champion since the start of these wicked trials. I know we don't know each other, but please, for the sake of the future of this country, do something about that government, would ya?\"")
    input()
    wrap_text("\n\n(You have acquired the champion's blade and champions armor set! The sword is a sleek and ornate sword carved out of what seems to be pure tungsten. It sure is heavy. The complementing armor set is made out of pure brass and covers You from head to toe.)")
    input()
    status["champion"] = 1
    updateGear("weapon", ("champion1", 20))
    updateGear("armour", ("champion1", 20, 20))
    garth = False

print(r"""
                           .^^::.                           
                         ^JY5555YJ!                         
                         JP555555PJ                         
                         .?YJJJJY7:                         
                          ^J????J:                          
                          ^J????J^                          
                          ^J??JJJ~                          
                          ^J????J~                          
                          ^J????J~                          
                          ^J????J~                          
                        .:~JJJJJYJ7!^:.                     
                 :^^^!?Y55PPPPPPPPPP555J!^:.                
                ^5PPPPPPPPPPPPPPPPPPPPPPPPP57               
                :5PPPPPPPPPP5PPPPPPPPPPPPPYY~               
                 .~!?Y5PPPPPPPPPPPPPP5Y?!^.                 
                      .:YPPPPPPPP5J^:.                      
                        ?PPPPPPPP57                         
                        ?PPPPPPPP55:                        
                        ?PPPPPPPP5!                         
                        75PPPPPP5J                          
                        .~J5PPPP55^                         
                         :Y5PPPPP?                          
                         ^YPPPPPP~                          
                          ?PPPPP5:                          
                         !55PPPP5^                          
                         :J5PPP55^                          
                         ^5PPP555?                          
                        ^55PPPPP55!                         
                        J5PPPPPPPP^                         
                        J5PPPPPPPP:                         
            .^~!777777: J5PPPPPPP5~!?J?????JJ?~.            
         .?JJ?!~^^^^^!J?5PGGGBG5Y?7!^.      .^?Y?~          
        7P7.           .:^!!!!:                .^JP^        
       ~@^                                        ~55       
       JG                                           PY      
       5J                                            55.    
       YP                                             P5    
       :~                                              ~    
""")

c = answer("You continue on the path when You notice a rusty sword held in a rock. Do You try pulling it out? (y/n)", yesno)

swordIn = True

# getting optional sword

if c == "y":
  c = answer("You try pulling the sword out but to no avail. Do You try again? (y/n)", yesno)
  if c == "y":
    wrap_text("This time You really use all your strength to pull out the sword and are about to feel something pop when You still fall short.")
    c = answer("Do You try again? (y/n)", yesno)
    if c == "y":
      wrap_text("You yank, pull, tug - You put every last fiber of your being into this sword when suddenly, You pull your back. Ouch! That's gotta hurt...")
      stats["AGI"] -= 5
    elif c == "n":
      wrap_text("After walking away You suddenly hear a clink. The sword has fallen out of its socket. You carefully walk over and pick it up. (You have now acquired a rusty longsword!)")

      if inventory["weapon"][0] == "champion1":
        wrap_text("You realize that the longsword looks worse than the champion blade You already possess, so You decide to toss it.")
      else:
        updateGear("weapon", ("longsword", 15))
      swordIn = False

wrap_text("You decide to walk away from the sword pedestal" + check(swordIn, ", (no matter how tempting it might be)") + ".")
input()

print(r"""
                                                                                                                        
                                                            ...:::^^^^^^^^^^~!!!~~^^^:...                               
                                       ..::::....::^^^~~~!!!!!!!!!!~~~~~7YPPB######BBBBGGPPY7!~^..                      
                                 .:^!!!7?????7!!!!!!!~~~~~~~~~~~~~~~~~~JB###BBBBBBBBBBBBB#BYYYYYYJJ???77~               
                             :^~!!!~~~~~~~~^^~~~~~~~~~~~~~~~~~~~~~~~~~5#BBBBBBBBBBBBBBBBBPJJJJJJJJJJJYYYY.              
                         .^~!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~P#BBBBBBBBBBBBBB#BG5JJYYY555555YYJJY?              
                      :~!!!~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!~!~~~~~~~~^Y#BBBBBBBBBB#BBGG5YJJJ5BBBBGGGGGBBPJJ5              
                   .~!!!~~~~~~~~~~~~~!~~~~~~~~~~~~~~~!~~~~~!~~~~~~^?BBBBBBBBBGGP5Y5GGGGGBBBBY!~~~~^?B#PJ5!              
                .:^~~~~~~~~~~!~~!!~~!!~~~~~~!~~~~~~~!~~~~~~~~~~~^~YBBBBBB#GYYJJJJJP#BYYJJ?7~^^^^^~JB#GYY!               
             .^!!~~~~~~~~~~~~!~~~!~~!~~~~~~~~~~~~~~~~~~~~~~~~~^~7P#BBBBB#PJJJJJJY5B#5^^^^^^7?JY5PGBB5YJ:                
           :!7!~~~~~~~~~~~~~!~~~~~~~!~~~~~~~~~~~~~~~~~~~~~~^^~?PB#BBBBBB5JJJJJYGBBP?~^~~~^J##GGPP5YJYY.                 
         ^!!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~!7?YG##BBBBBBB5JJJY5GBBY!^^^~~~~^J#B5JJJJJJ5^                  
       ^7!~~~~~!!~!!~~~~~~~~~~~~~~~~~~~~!!!~~~~~~~~~~~~YGBB##BBBBBBBBB5JJJJP##5!^^^~~~~~~^^Y#BYJJJJYY                   
     .77~~~~~~~!~~!!~~~!!!!!~!~!!~~~~~~!~~~!~~~~~~~~~~P##BBBBBBBBBBBB5JJJJJP#B!^^^^^^^^^^^^J#BYJJJJYJ                   
    ^?~~~~~~~~!~~~~~~~~!!~~~~~~~!~~~~!!~~~!!~~~~~~~~^?#BBBBBBBBBBBBBPJJJJJJ5BBY?7!~~~~~~!7YG#GYJJJJYJ                   
   ~7~~~~~~~~~~~~~~~~~~!!~~~~~~~~~~~~~~~~~~~~~~~~~~~^P#BBBBBBBBB#BPYJJJJJJJJ5GBBBBBGGGGGBBBG5YJJJJJYY                   
  ~?~~~~~~~~~~~~!!~!~~~!~~~~~~~~~~~~~~~~~~~~~~~~~~~^Y#BBBBBBBB#B5YJJJJJJJJJJJJJYYYY55555YYJJJJJJJJJJ5^                  
 .J~~~~~!~~!~~~~!~~~~~~!!~~~~~~~~~~~~~~~~~~~^^^^~~!Y#BBBBB###BPYJJJJJJJJJJJJJJJY555PPPPPPPPP55YJJJJJYJ                  
 ~7~~~~~!~~~~~~~!~~~~~~~!~~~~~~~~~~~~~~~^^~!7JY5PGB#BBBBBBP55YJJJJJJJJJJJJJJJYGGGGPPPPPPPPPPPGGPYJJJJ5!                 
 ?~~~~~~!~~~~~~~~~~~~~~~~~~~~~~~~~~~^^~!7YGBB####BBBBBB#B5JJJJJJ MIDFIELD JJJJJPGPPPPPPPPPPPPPPPPPPPYJJYY                 
 ?~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^~!7YPBB#BBB########BGPJJJJJJJJJJJJJJJJJJJJJ5GPPPPPPPPPPPPPPPPPPPP5YJY                 
.J~~~~~~~~~~~~~~~~~~~~~~~^^^^~~!J5GBB##BBB##BG5Y?7!!7~^::^7JJJJJJJJJJJJJJJJJJPGPPPPPPPPPPPPPPPPPPPPGPYY                 
 ?~~~~~~~~~~~~~~~^^^~~~!!?JY5PGB###BBB##BG5?~::...:..::::::?YJJJJJJJJJJYYYYY5GPPPPPPPPPPPPPPPPPPPPPPPGJ                 
 ^J^~~~~~~~^^~!!7JY5PPGBB########BBBBG5?~^:.::::::::::::::.~JJJYJJJJ5PPGGGPGGPPPPPPPPPPPPPPPPPPPPPPPPPG:                
  !7~~^^~~7JYPBBB########BBGP5Y?7!~~^::.:::::^~~!!~~~!!~~~^^^^~!?J5PGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPG5.               
   ~7!?Y5GB###BBB####GY?7~^:::...::::::::^~!!!^^::::::::^^~!^::::!GPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPBY               
    ^P###BBB##BBGP5J7^...:::::::::::::^!~~~^::::::::::::::::::::::PPPPPPPPPPPGPP5YYY5PPPPPPPPPPPPPPPPPPPB~              
     :G####GJ7~^^::..::::::::::::::::::::::::::::::::::::::::::::.JGPPPPPPPP5?7!~~~~~!!!!?YPPPPPPPPPPPPPGY              
      ~BY?!^..::::::::::::^^^^^:::::::::::::~~~^^^~~~~~~^:::::::::~GPPPPPPP?~~~~~~~~~~~~~~~?PPPPPPPPPPPPPP.             
       7~.:::::::::^~~~!!!~~^~~!!^:::::::::::^^^^^^^^^^^7:::::::::.5GPPPPP5~~~~~~~~~~~~~~~~~5PPPPPPPPPPPPG^             
       .?::::::::::^^^^:::.::::::::::::::^^~~^^^^:::::::::::::::::.7GPPPPP5!~~~~~~~~~~~~~~~7PPPPPPPPPPPPPGJ             
        ~!.:::::::::::::::^^^^^^^^^^^^~!!~~^^^^~~!!!^::::::::::::::!GPPPPPP5?!~~~~~~~~~~~!JPPPPPPPPPPPPPPPP.            
         7~:::::::::::::::^^^^~~~~~~~~^::::::::::::^^:::::::::::::^GPPPPPPPPPP5YJ?7?JY555PPPPPPPPPPPPPPPPPG~            
          !!:::::::::::::::::::::::::::::^^^^^^^^^:::::::::::::::.?GPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPGJ            
           ^7~::::::::::::::::::::::::^!~~~~~~~~~~:::::::::::::::.?GPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP            
            .^!~^:::::::::::::::::::::::::::::::::^^^~~~~~~~~~~^:.7GPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPG?           
               :^~~~^:::::::::::::^^^~~~~~~~~~~^^^:::....   ..:^~~!GPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPG7          
                  .:^~~~~~~~~~~~~^^::......                      .:YY5GGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPG!         
                        ......                                       .^7J5GGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPG^        
                                                                         .^!J5PGGPPPPPPPPPPPPPPPPPPPPPPPPPPPPPGP.       
                                                                              :~7J5PGGGPPPPPPPPPPPPPPPPPGGGPP5JJ7       
                                                                                   :^~7JYY5PPPPPPPP55YJ?7!^:.   ^       
                                                                                          ..........                    
""")

wrap_text("Eventually, You make it out of the woods and are placed in front of a set of long rolling plains, noting a convenient sign to the right that reads \"Midfield\". To the west, appears of set of never-ending dunes. To the east, a huge lake. Yet, to the north there is a cavern; a seemingly impassable ravine.\n")

done = False

options = ["north", "east", "west"]

# basically just a loop for a hub but the hub splits into east and west, with the main program continuing once the player heads north

while done == False:
  c = answer(f"Where will You go? ({options[0]}, {options[1]}, {options[2]})", options)

  # progress the story and head into the cavern

  if c == "north":
    wrap_text("You head North and see the ravine You spotted from a distance away. Upon gazing in, You see a bright set of dancing lights in the depths below. You examine the cavern itself and there seems like no other way of getting down there except for jumping in.")
    c2 = answer("Do You jump in? (You will not be able to explore any of the other locations after jumping in.) (y/n)", yesno)
    if c2 == "y":
      done = True
  
  # head west to learn more about the dunes there

  elif c == "west":
    wrap_text("You head West and You gaze upon a sea of dunes. You notice a sandstorm picking up along with a sled resting at the top of one of the hills.")
    c2 = answer("Will You explore these dunes? (y/n)", yesno)
    if c2 == "y":
      colosseum = False

      wrap_text("You pick up the sled and start carving along the dunes. The sandstorm starts picking up and sweeps You into the air. You lose consciousness...")
      input()
      wrap_text("You wake up inside a chiseled brick dungeon. You gather your surroundings and realize You are deep underground. Upon waking up, your cell door opens and a guard escorts You out. He leads You through a labyrinth of other cells until You finally reach an opening that reveals a thriving town at the center of a subterranean oasis. A woman with red hair wearing a regal outfit along with a crown greets You.\n")

      print(r"""
                                                                                                              
                            .::::::.    .:::::..           ..                                       
                            :~^~~~~~^..:^~~~~~~~:.     .:^^^^^^.    ::^^^^^.                        
                            ^~^~~~~^~~~~^~~~~~~^~~^::^~~~~~~~^~~^ .~~~~~~~~.                        
                            :~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~^~~^~~~^~^                         
                          :!Y!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^~~~~^~:                         
                      :J5PBBBP!~~~~~^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~^                          
                    :!!5BBBBB#G5^..     .. ......:::^^~~~~~~~~~~~~~~~~~^!!:                         
                   :G#BBBBB&#J~:  :!!7:               ....::^^^~~~~~~~~?GBB^                        
                   7BBBBBB&Y:     !PB@G                 .!Y^   ...:7GBGBBBBP:                       
                   7BBBBBB!         5@?                 P@@&Y       ^Y#BBBBBG!                      
                   ~BBB##?          G@!                !@#:^^         5#BGBBBB~                     
                   ^BB&P~.          !Y:                5@J            G&BBBBBB5                     
                   5BB&^                               JB^           ~&#BBBBBBB7                    
                  !BBB&:                 ?55555Y.                   7@&BBBBBBBBP                    
                  YBBB&G~.               !?????7.                 :Y@&BBBBBBBBBG.                   
                 :GBBBB##BGP5J7!^.                        .:..:^75###BBBBBBBBBBB:                   
                 7BBBBBBB75#GG&##BBP5JJ?!^::::::^~!7?JY55PGBB##&&GGBBBBBBBBBBBBB7                   
                .GBBBBBBBGBBGPBBGG#575@&GBBBBBBBBGGP@@G#BBBBBBBBBBBBBBBBBBBBBBBBY                   
                YBBBBBBBBBBBBBBBBBB5!J#P           .&#BBBBBBBBBBBBBBBBBBBBBBBBBBG.                  
               ?BBBBBBBBBBBBBBBBBBBBBBBP           7@#BBBBBBBBBBBBBBBBBBBBBBBBBBB?                  
              !BBBBBBBBBBBBBBBBBBGBBBB#G           5@BBBBBBBBBBBBBBBGGBBPBBBBBBBBY                  
             .GBBBBBBBBBBB5J7?P#5Y##BB#B.         :&@#####BBB#######GG#BP#BB??BBBY                  
            ^YB#####BB#BBBGGGGB#GGP5PB@@7         .7J&@P^:..:^~~^^!&@G?YG#&&GYJGBG!                 
          :G&BPPY?7~7P#!^::::::.   7#BB5.            :#@^         :@&.   .^~7#@BGGBP!.              
         ?&@?.      ?@#:           G@5~~~7J~   7P?....B@~         .G@P!:.     7B@G?Y5^              
       .P@P.      !P@B:            ~YPPPG@@!   5@@BBB##P:           75B##GJ77!^~G@P                 
     .JG@&?7??JYPB@P!                    G@GPPB&B!::::.                .~?5PPGGGP@@^                
      5@BY5555YJ?!:                      .^~~~~:                                 J@G                
     .#@~                                                                         G@?               
    .5@5                                                                          :&@!              
   ^&@@^                                                                           J@&^             
   .#@Y                                                                            ^&@!             
   .#@^                                                                             J@5             
          """)

      wrap_text("\"I've brought You here to be entertainment for my people.\"\n")
      if status["champion"] > 0:
        input()
        wrap_text("\"I'm sorry, is that a set of champions gear? I apologize immediately, I didn't recognize You. Well I apologize for the confusion. My name is Sierra and I, too, am a champion. Allow me to re-accommodate You immediately.\"\n\nYou follow Sierra as she takes You to a regal looking centerpiece afloat the oasis You previously spotted. You enter the palace and immediately notice the gold trimmings and ornate architecture glittered throughout the building. The guards look intimidating and for better or for worse, would likely end You in one fell swoop. Finally, You arrive at the throne room and Sierra seats You.\"Now, what can I help You with, Champion?\"")

        done2 = False
        help = False

        while done2 == False:
          print(r"""
                                                                                                              
                            .::::::.    .:::::..           ..                                       
                            :~^~~~~~^..:^~~~~~~~:.     .:^^^^^^.    ::^^^^^.                        
                            ^~^~~~~^~~~~^~~~~~~^~~^::^~~~~~~~^~~^ .~~~~~~~~.                        
                            :~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~^~~^~~~^~^                         
                          :!Y!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^~~~~^~:                         
                      :J5PBBBP!~~~~~^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~^                          
                    :!!5BBBBB#G5^..     .. ......:::^^~~~~~~~~~~~~~~~~~^!!:                         
                   :G#BBBBB&#J~:  :!!7:               ....::^^^~~~~~~~~?GBB^                        
                   7BBBBBB&Y:     !PB@G                 .!Y^   ...:7GBGBBBBP:                       
                   7BBBBBB!         5@?                 P@@&Y       ^Y#BBBBBG!                      
                   ~BBB##?          G@!                !@#:^^         5#BGBBBB~                     
                   ^BB&P~.          !Y:                5@J            G&BBBBBB5                     
                   5BB&^                               JB^           ~&#BBBBBBB7                    
                  !BBB&:                 ?55555Y.                   7@&BBBBBBBBP                    
                  YBBB&G~.               !?????7.                 :Y@&BBBBBBBBBG.                   
                 :GBBBB##BGP5J7!^.                        .:..:^75###BBBBBBBBBBB:                   
                 7BBBBBBB75#GG&##BBP5JJ?!^::::::^~!7?JY55PGBB##&&GGBBBBBBBBBBBBB7                   
                .GBBBBBBBGBBGPBBGG#575@&GBBBBBBBBGGP@@G#BBBBBBBBBBBBBBBBBBBBBBBBY                   
                YBBBBBBBBBBBBBBBBBB5!J#P           .&#BBBBBBBBBBBBBBBBBBBBBBBBBBG.                  
               ?BBBBBBBBBBBBBBBBBBBBBBBP           7@#BBBBBBBBBBBBBBBBBBBBBBBBBBB?                  
              !BBBBBBBBBBBBBBBBBBGBBBB#G           5@BBBBBBBBBBBBBBBGGBBPBBBBBBBBY                  
             .GBBBBBBBBBBB5J7?P#5Y##BB#B.         :&@#####BBB#######GG#BP#BB??BBBY                  
            ^YB#####BB#BBBGGGGB#GGP5PB@@7         .7J&@P^:..:^~~^^!&@G?YG#&&GYJGBG!                 
          :G&BPPY?7~7P#!^::::::.   7#BB5.            :#@^         :@&.   .^~7#@BGGBP!.              
         ?&@?.      ?@#:           G@5~~~7J~   7P?....B@~         .G@P!:.     7B@G?Y5^              
       .P@P.      !P@B:            ~YPPPG@@!   5@@BBB##P:           75B##GJ77!^~G@P                 
     .JG@&?7??JYPB@P!                    G@GPPB&B!::::.                .~?5PPGGGP@@^                
      5@BY5555YJ?!:                      .^~~~~:                                 J@G                
     .#@~                                                                         G@?               
    .5@5                                                                          :&@!              
   ^&@@^                                                                           J@&^             
   .#@Y                                                                            ^&@!             
   .#@^                                                                             J@5             
          """)
          c2 = answer("1. I need your help to deal with the government of this country.\n2. How many champions are there?\n3. How did you become a champion?\n4. I'll be going now.", ["1", "2", "3", "4"])
          if c2 == "1":
            wrap_text("\"Hmm... very well. I will join You in your time of need. The government has as of late, made my colosseum business quite difficult to keep intact.\"")
            if help == False:
              help = True
              status["help"].append("Sierra")
          elif c2 == "2":
            wrap_text("\"Including us, there are 4 total. Each are at different corners of this country. Here is a map representation:\"")
          elif c2 == "3":
            wrap_text("\"Well, I become a champion through besting any who dared fight me in the colosseum. That is, in my culture, you become Champion after completing the colosseum, until no one dares fight You.\"")
            c3 = answer("1. I'd like to participate in the colosseum.\n2. Wow... sounds interesting.", ["1", "2"])
            if c3 == "1":
              wrap_text("\"You... WANT to fight in the colosseum? Normally its custom to have, well, no choice in fighting. If You really are interested, I will escort You there immediately.\"")
              input()
              if help:
                status["help"].pop()
              wrap_text("Champion Sierra reluctantly gets up from her throne and begins walking back to where You originally were. You follow in haste. Maybe You just felt nervous but the vibrant colours of the ornate throne-room suddenly disappeared as You entered the central bustling city. However, this is not your destination. Travelling for only fleeting moments but feeling like an eternal decade You arrive at the colosseum. You feel a burning sensation in your chest.\n\"Good... luck.\" She says.\"\n\nThe door to the colosseum is locked and You can hear the intricate mechanism of the door clicking as You finally realize your fate.")
              done2 = True
              colosseum = True
          elif c2 == "4":
            wrap_text("\"Farewell, Champion.\"")
            done2 = True
      else:
        colosseum = True

        wrap_text("your stomach drops. Entertainment? What could that possibly mean?! With your mind lost in your thoughts You follow her as she takes You to an arena. Upon peering in You see savages, along with creatures battling to their deaths.\n\n\"Welcome to the colosseum. Here is where You will be fighting... for your death.\"\n\nyour stomach would drop for the second time but you've kind of expected that to be her response. She takes You to the armory before the arena and locks the door behind You. It seems like your only option is to fight.")
      
      if colosseum == True:
        c2 = answer("You have three weapons in front of You, what will You take?\n\n(Mace, Spear, Shortsword, Nothing)", ["mace", "spear", "shortsword", "nothing"])

        if inventory["weapon"][0] == "champion1" or inventory["weapon"][0] == "longsword":
          wrap_text("You realize that none of the available weapons look better than what You have now, and continue with what You have currently equipped.")
        elif c2 == "mace":
          wrap_text("You have chosen the mace.")
          updateGear("weapon", ("mace", 10))
        elif c2 == "spear":
          wrap_text("You have chosen the spear.")
          updateGear("weapon", ("spear", 10))
        elif c2 == "shortsword":
          wrap_text("You have chosen the shortsword.")
          updateGear("weapon", ("shortsword", 10))

        input()

        enemy1 = {"NAME": "Wolf", "AGI": 20, "ATK": 5, "DEF": 5, "HP": 10, "CHOICE": True}
        enemy2 = {"NAME": "Savage", "AGI": 10, "ATK": 10, "DEF": 10, "HP": 15, "CHOICE": True}
        enemy3 = {"NAME": "Goliath", "AGI": 5, "ATK": 13, "DEF": 15, "HP": 25, "CHOICE": True}

        outcome = fight(enemy1)

        if outcome:
          wrap_text(f"You have beat {enemy1['NAME']}, now on to the next.\n")
          outcome = fight(enemy2)
          if outcome:
            wrap_text(f"You have beat {enemy2['NAME']}, now on to the next.\n")
            outcome = fight(enemy3)
            if outcome:
              wrap_text("The spectator's cheers suddenly intensify. You catch your breath for a minute and suddenly realize no one else is challenging You. You've done it! You have bested the colosseum.")
              input()
              wrap_text("Out of a podium from the ceiling, somebody descends" + check(status["champion"] > 0, " it's Sierra" + ".") +  "\n\n\"You deserve this\". She hands You her golden ornate crown and armor, along with a shiny scimitar. (Unfortunately these items are too small for You to equip).\"You are now the Champion of the dunes of Kamus. I have other business to attend to.\"She rises back through the podium she descended with and You have the suspicion that You'll probably never see her again. You make your way out of there are arrive back on the surface where it all started. You decide to pick back up that sled and carve your way back to the center plains area.")
              status["champion"] += 1
            else:
              wrap_text("your fate has been sealed. You feel the enemy gladiator's attack before feeling your vision fade away into darkness.\n\n")
              print(r"""
              
   _____          __  __ ______       ______      ________ _____    
  / ____|   /\   |  \/  |  ____|     / __ \ \    / /  ____|  __ \   
 | |  __   /  \  | \  / | |__       | |  | \ \  / /| |__  | |__) |  
 | | |_ | / /\ \ | |\/| |  __|      | |  | |\ \/ / |  __| |  _  /   
 | |__| |/ ____ \| |  | | |____     | |__| | \  /  | |____| | \ \ _ 
  \_____/_/    \_\_|  |_|______|     \____/   \/   |______|_|  \_(_)
                                                                                                                                   
              """)
              input()
              quit()
          else:
            wrap_text("your fate has been sealed. You feel the enemy gladiator's attack before feeling your vision fade away into darkness.\n\n")
            print(r"""
              
   _____          __  __ ______       ______      ________ _____    
  / ____|   /\   |  \/  |  ____|     / __ \ \    / /  ____|  __ \   
 | |  __   /  \  | \  / | |__       | |  | \ \  / /| |__  | |__) |  
 | | |_ | / /\ \ | |\/| |  __|      | |  | |\ \/ / |  __| |  _  /   
 | |__| |/ ____ \| |  | | |____     | |__| | \  /  | |____| | \ \ _ 
  \_____/_/    \_\_|  |_|______|     \____/   \/   |______|_|  \_(_)
                                                                                                                                   
              """)
            input()
            quit()
        else:
          wrap_text("your fate has been sealed. You feel the enemy gladiator's attack before feeling your vision fade away into darkness.\n\n")
          print(r"""
              
   _____          __  __ ______       ______      ________ _____    
  / ____|   /\   |  \/  |  ____|     / __ \ \    / /  ____|  __ \   
 | |  __   /  \  | \  / | |__       | |  | \ \  / /| |__  | |__) |  
 | | |_ | / /\ \ | |\/| |  __|      | |  | |\ \/ / |  __| |  _  /   
 | |__| |/ ____ \| |  | | |____     | |__| | \  /  | |____| | \ \ _ 
  \_____/_/    \_\_|  |_|______|     \____/   \/   |______|_|  \_(_)
                                                                                                                                   
              """)
          input()
          quit()
    options[2] = ""  
  
  # head east to learn more about the giant lake

  elif c == "east":
    wrap_text("You head East and see just how gigantic that lake really was, and at a closer inspection, it seems even larger. You find a rowboat by a dock.")
    c2 = answer("Will You enter the boat? (y/n)", yesno)
    if c2 == "y":
      wrap_text("You enter the boat and row your way to the center, expecting perhaps a buried sunken treasure along the way. To your dismay, You find nothing and arrive at the center with not much accomplished. You take a moment to appreciate the beauty of nature when You notice a fog creep in over the waters. You feel a rumbling deep below You and You find your boat lifted up at a rapid speed. You nearly lose your balance when suddenly a giant slithering tentacle lifts You up and places You infront of its eyes. In front of You, a giant red octopus.\n\n\"Why hast thou awakened me during my century long slumber?\"")
      if status["champion"] > 0:
        input()
        wrap_text("\"Hold on... by the stars it is! It's a truly authentic set of Champion's armor! Well I'll be damned. I, err, am glad to make your acquantaince. I, too, am a Champion. One by the name of Dragus the fifth.  Allow me to lower You so we can speak on more even grounds.\"\n\nDragus carefully lowers its tentacle and releases its grasp from your row boat.\n\n\"Now, what can I help You with?\"")

        done2 = False
        failed = False
        help = False

        while done2 == False:
          print(r"""
                                                                                                              
                                                                                                    
                                                                                                    
                         .::^~77J5YY5PPPPPPPPP5YJJ?777~:..                                          
                      ^?G##BBBG5YJ???7!!!!!!!7?JYY555PBBB#GGP5Y!.                                   
                   :Y#&GJ~.                            .:^~!7?P#&GY!^.                              
                 :J@&J:  ^!!!~::..                              ^?5G##GJ:                           
               ~P&#Y.    JPPGBBBBBB5.                    :^~7?J5J.  .^J@&?.                         
              P@G!.         .. .:^~~                     YBBP55J7      :Y&#?.                       
             J@G           .G&?                                7G7J!     :Y@#?                      
            J@B.           ^@@#J                               B@P@#.      :G@5                     
           ~@#.            ~@@@B                               G@&@#.        5@P                    
           Y@Y             ~@@@J                               P@@@#.         P@P                   
           P@!             ?@@#.                               J@@@#.          #@^                  
           5@?             5@@#.                               Y@@@#.          B@^                  
           !@#.            5G~:                                J@@@#.          B@^                  
            J@B^                                               .^J@G          :#@^                  
             !#@Y:                         .~!777!^:.             :.         7&&7                   
              .?#@5~                     .7B@B555GBB#BY^                   .J@#:                    
                .7G&B5!^               .J&&Y?^:^:  .:J@G                ~YG#&5:                     
                   :75B#B57^          .B@J.  P@@@#?  !@G           :~75#&G7^.                       
                       :!YG#BP7:      .&@?:. :!???!:!B@J       .!5B#BG57:                           
                           :!Y#&B?^    ^5B#BGGGGPPB#B5!   ^!7JG##P7:                                
                               ^JB&B?:    ::::^~~~~:   ^Y#&GPY?~.                                   
                                  ^Y@&^              ^Y@#7:                                         
                                    G@!           :?B&B?.                                           
                                  :P@G:           !#@P                                              
         !JPGG5J?~:...     .:^~?YP&&?              ~@G                                              
       :P@G?!7?YPBBBBBBGGGB#BBBPY?~.               :&@~              .^7JJJJJJ7!:                   
      .B@J        .::^^^^^~^..                      !&@Y!:......^!JPB##GYYYYY5PB#BJ                 
      Y@P                        ..:^~77.            :?PB#BBBBBB#B5J!^.         :B@Y                
    :~@#.       .!?J5PPP5J7^^!?YGBBBBBG&#Y:              ........                .5@P:              
   .B@@B      .?#@PYJ7!7J5GBBB5Y7^..   .?@&?~~~~~~~7?J555YYY5PPPPPPPPPPPPP55J7~:   B@@!             
   .#@@B      7@G^         ..            :5BGGGGGGGGP5J??????7!!!!!!!!!!7??J5B#&B5..P@P             
          """)
          c2 = answer("1. Got any buried treasure?\n2. I'm here to take your name as champion.\n3. I need your help dealing with the government of this country.\n4. I don't need anything else, see ya.", ["1", "2", "3", "4"])
          if c2 == "1":
            wrap_text("\"You may take this dagger that's been sitting at the bottom of this lake. It's probably been here for years, decades maybe.\" (You have now obtained a dagger!)")
            if inventory["weapon"][1] < 13:
              updateGear("weapon", ("dagger", 13))
            else:
              wrap_text("Unfortunately for You, it seems like You already have a better item equipped.")
          elif c2 == "2":
            wrap_text("\"Hah! Unfortunately that isn't exactly how champions work in these parts. If You want to become champion, You must be a direct descendant of Lord Dragus his first.\"")
            c3 = answer("1.  I... am.\n2. Oh well.", ["1", "2"])
            if c3 == "1":
              if status["mark"] or (random.randint(1, 100) == 1) and (failed == False):
                wrap_text("\"By the stars... You... YOU HAVE THE MARK OF DRAGUS! You... really are a descedant. Here, please take my customary armor and trident champion heirloom. I just ask that You take this role seriously. (Unfortunately for You, its armor and weapon are far too big for You to use.)\"\n\nYou see Dragus descend back into the depth with the lingering suspicion that You probably wont see it ever again.")
                if help:
                  status["help"].pop()
                status["champion"] += 1
                done2 = True
              else:
                failed = True
                wrap_text("\"Nice try but You aren't fooling anyone.\"")
          elif c2 == "3":
            wrap_text("\"Hmm... Okay, I will do it. The government has been really running this country down as of late, I cannot lie. There policies reducing lake sizes by over 10 percent has been detrimental to my race and overall sleep quality. I will join You in the final battle against them.\"")
            if help == False:
              help = True
              status["help"].append("Dragus")
          elif c2 == "4":
            wrap_text("\"May the winds be in your sails, Champion.\"")
            done2 = True
      else:

        done2 = False

        while done2 == False:
          print(r"""
                                                                                                              
                                                                                                    
                                                                                                    
                         .::^~77J5YY5PPPPPPPPP5YJJ?777~:..                                          
                      ^?G##BBBG5YJ???7!!!!!!!7?JYY555PBBB#GGP5Y!.                                   
                   :Y#&GJ~.                            .:^~!7?P#&GY!^.                              
                 :J@&J:  ^!!!~::..                              ^?5G##GJ:                           
               ~P&#Y.    JPPGBBBBBB5.                    :^~7?J5J.  .^J@&?.                         
              P@G!.         .. .:^~~                     YBBP55J7      :Y&#?.                       
             J@G           .G&?                                7G7J!     :Y@#?                      
            J@B.           ^@@#J                               B@P@#.      :G@5                     
           ~@#.            ~@@@B                               G@&@#.        5@P                    
           Y@Y             ~@@@J                               P@@@#.         P@P                   
           P@!             ?@@#.                               J@@@#.          #@^                  
           5@?             5@@#.                               Y@@@#.          B@^                  
           !@#.            5G~:                                J@@@#.          B@^                  
            J@B^                                               .^J@G          :#@^                  
             !#@Y:                         .~!777!^:.             :.         7&&7                   
              .?#@5~                     .7B@B555GBB#BY^                   .J@#:                    
                .7G&B5!^               .J&&Y?^:^:  .:J@G                ~YG#&5:                     
                   :75B#B57^          .B@J.  P@@@#?  !@G           :~75#&G7^.                       
                       :!YG#BP7:      .&@?:. :!???!:!B@J       .!5B#BG57:                           
                           :!Y#&B?^    ^5B#BGGGGPPB#B5!   ^!7JG##P7:                                
                               ^JB&B?:    ::::^~~~~:   ^Y#&GPY?~.                                   
                                  ^Y@&^              ^Y@#7:                                         
                                    G@!           :?B&B?.                                           
                                  :P@G:           !#@P                                              
         !JPGG5J?~:...     .:^~?YP&&?              ~@G                                              
       :P@G?!7?YPBBBBBBGGGB#BBBPY?~.               :&@~              .^7JJJJJJ7!:                   
      .B@J        .::^^^^^~^..                      !&@Y!:......^!JPB##GYYYYY5PB#BJ                 
      Y@P                        ..:^~77.            :?PB#BBBBBB#B5J!^.         :B@Y                
    :~@#.       .!?J5PPP5J7^^!?YGBBBBBG&#Y:              ........                .5@P:              
   .B@@B      .?#@PYJ7!7J5GBBB5Y7^..   .?@&?~~~~~~~7?J555YYY5PPPPPPPPPPPPP55J7~:   B@@!             
   .#@@B      7@G^         ..            :5BGGGGGGGGP5J??????7!!!!!!!!!!7??J5B#&B5..P@P             
          """)
          c2 = answer("1. I'm sorry I didn't mean to.\n2. Got any buried treasure?\n3. Who are You and where am I?\n4. Okay I'll be going now.", ["1", "2", "3", "4"])
          if c2 == "1":
            wrap_text("\"Hmph. Very well. Well, regardless of whether You intended to wake me up or not, your business is now mine. What brings You to this area?\"")
            c3 = answer("1. Just... looking around.\n2. I'm looking for a fight.", ["1", "2"])
            if c3 == "1":
              wrap_text("\"Well... I expected a more important or interesting answer.\"")
            else:
              wrap_text("\"Hah! You truly are a funny specimen. Unfortunately, I am not interested in that tomfoolery. Maybe You can find another primordial octopus to bother.\"")
          elif c2 == "2":
            wrap_text("\"Are You seriously asking me if I have buried treasure? Well I do. Obviously. But I'm not just going to give it to some random simpleton who asks.\"")
          elif c2 == "3":
            wrap_text("\"My name is Dragus the fifth, and this is Dragus Lake. The resting place of my ancestors and many more before me. I am a champion, similar to the one found in champion woods. My duty as the champion is to defend this area, from people like You.\"")
          elif c2 == "4":
            wrap_text("\"Hmph. Farewell.\"")
            done2 = True
    options[1] = ""  

# jumping into the cavern

wrap_text("You take a leap of faith, quite literally, and start free-falling into the ravine with your eyes closed. 1 second, two seconds, three seconds, until You suddenly stop. You open your eyes and are face to face with a dwarven creature, one with a big burly ginger beard, and wrinkles that could tell a story.")
input()
wrap_text("\n\n\"Would ya mind falling somewhere else?!?!\" You notice that You are suspended in a bubble. You look up and realize the, now in your head named, \"bubbling machine\" that bubbles any visitors who enter the ravine. After making that astute observation You notice just how massive this city is, with little homes scattering all through the cavern You are located in. A quick glance to your left lets You realize You are in the aptly named, \"Cavern City\"... maybe that bubble machine really is called the \"bubbling machine\".\n\nYou realize You still haven't replied to that dwarf.")
input()
wrap_text("\n\n\"Oh yeah, sorry\". You pop your own bubble and start walking around. You bump into more angry dwarfs until You spot a massive glowing forge and decide to head over there. You, unsurprisingly, meet a dwarf who announces:\n\n\"Well hellow there, how can I help ye?\"")

done = False

dialogue = ["1. What can you do for me?", "2. How do I get to the government from here? (Leave)"]
options = ["1", "2"]

# talking with the reforge dwarf npc

while done == False:
  c = answer(f"{dialogue[0]}\n{dialogue[1]}", options)
  if c == "1":
    stats["HP"] = stats["TOTAL"]
    if status["champion"] == 3:
      wrap_text("\"Well, by the looks of your armor... no... it can't be... YOU HAVE 3 SETS OF CHAMPION'S GEAR?!!?! Please don't hurt me! Oh all mighty, the prophecy is coming true. Allow me to forge You the ultimate champions gear, just... remember *me* when You make it, and spare our little civilization.\"\n\n(You've obtained something truly special: the ultimate champions armor and weapon - a spectacle of mass destruction)")
      updateGear("weapon", ("ultimate", 70))
      updateGear("armour", ("ultimate", 50, 50))
    elif status["champion"] > 0:
      wrap_text("\"Well, by the looks of your armor... by the by! You have a set of champions armor! It is an honor to meet You, truly. Allow me to polish your gear up and reforge it a tad bit.\"")
      stats["ATK"] += 5
      stats["DEF"] += 5
      stats["HP"] += 5
      stats["AGI"] += 5
    else:
      wrap_text("\"Well, by the looks of your armor and weapons... not much. If ye'd like, however; I can melt down whatcha got and make some finer armor. Free of cost of course, thats how we operate around here.\"")
      stats["ATK"] += 2
      stats["DEF"] += 2
      stats["HP"] += 2
    options[0] = ""
    dialogue[0] = ""
  if c == "2":
    done = True

# series of tests of the player's will

wrap_text("\"Well, ye'll want to take those stairs over there.\"\n\nHe points to a set of steep stairs heading through the caverns.\n\n\"If You keep going You'll reach Rockine Plains, truly a desolate place. But if You persist through that, You'll reach the capital, Draconius. Best of luck, stranger.\"")
input()

wrap_text("You make your way up those cascading stairs. After about 30 steps You glance up and realize that You still have probably 1000 more to go. After losing track of time You manage to climb those steps. You pass out at the very top.\n\nYou have a vivid dream of living another life, one with friends, relationships, schooling, and most importantly a sense of safety.")
input()
wrap_text("\n\nSuddenly your heart races and You wake up. your back on top of the stairs. It is now nighttime, You continue through the Rockine plains. You walk through the rocky desert. The ground is cracked and the visible flora and fauna is nonexistent. The landscape is grey and absolutely horrid. Some more time passes, and that dwarf from earlier wasn't lying, it truly is desolate and empty here.")
input()
wrap_text("After walking some more You fall over from fatigue.")

c = answer("Do You get back up? (y/n)", yesno)

if c == "n":
  wrap_text("You succumb to the tides of causality and do not get back up.\n\n")
  print(r"""
              
   _____          __  __ ______       ______      ________ _____    
  / ____|   /\   |  \/  |  ____|     / __ \ \    / /  ____|  __ \   
 | |  __   /  \  | \  / | |__       | |  | \ \  / /| |__  | |__) |  
 | | |_ | / /\ \ | |\/| |  __|      | |  | |\ \/ / |  __| |  _  /   
 | |__| |/ ____ \| |  | | |____     | |__| | \  /  | |____| | \ \ _ 
  \_____/_/    \_\_|  |_|______|     \____/   \/   |______|_|  \_(_)
                                                                                                                                   
              """)
  input()
  quit()

wrap_text("You get back up and continue. You feel lightheaded and tired, your vision blurs and You get nauseous and dizzy. You fall over, once more.")
c = answer("Do You get back up? (y/n)", yesno)

if c == "n":
  wrap_text("You succumb to the tides of causality and do not get back up.\n\n")
  print(r"""
              
   _____          __  __ ______       ______      ________ _____    
  / ____|   /\   |  \/  |  ____|     / __ \ \    / /  ____|  __ \   
 | |  __   /  \  | \  / | |__       | |  | \ \  / /| |__  | |__) |  
 | | |_ | / /\ \ | |\/| |  __|      | |  | |\ \/ / |  __| |  _  /   
 | |__| |/ ____ \| |  | | |____     | |__| | \  /  | |____| | \ \ _ 
  \_____/_/    \_\_|  |_|______|     \____/   \/   |______|_|  \_(_)
                                                                                                                                   
              """)
  input()
  quit()

if inventory["armour"][0] == "ultimate":
  wrap_text("You attempt to get back up. You can't...\n\nYou suddenly feel a surge of power. The ultimate armor sends pulses of energy through your body. How can You get more of this? It... feels invigorating. You remember what the dwarf said, who cares about persisting when You could get more power like this.")
else:
  wrap_text("You attempt to get back up. You can't...\n\nYou remember what the dwarf told You, to persist. You ponder that thought. What options do You have as a stranger in this world if not to persist, to struggle, for if You give up, You are no better than those you've slain or injured along the way.")

input()

wrap_text("You get back up, and continue until You reach the capital.")

input()

# the player's final destination and final encounter

wrap_text("The capital, in all it's glory; seemingly the final destination of your efforts. You see it's ivory towers, its marble pillars, it's studded doors, every piece of this city is exaggerated. Maybe this is where You can learn just exactly why you're here. You take one step, and hear a rumble in the air. You look around, nothing. You hear a sonic boom, You look again - nothing.")
input()

print(r"""
            _.===._      ,"^^^^",
           /_\^^^/_\    /  ^ ,^  \     ,
           (0\ ^ /0)\  / ^  /  ^  \    /\
            \     /  ^^   ^ \ ^ \  ",." /
             )   (  ^  ^   ^ \   \    ,'
             (o_o)^    \ ^   ,)  /`^^`
              ^V^\ ^ \  \_,-"((((
              /  /`""/  /
             (((`   '(((
""")

wrap_text(f"Until it appears in front of You and cracks the ground underneath it, a real-life dragon.\n\"I know why you're here. Let me guess, to defeat me?\"\n\nYou hesistate for a moment: \"I want to know why I'm here; how I got here. I don't belong here.\"\n\nThe dragon replies \"Best me in this encounter, and I might just tell You. But.. let me say this. It all has to do with the Introductory Clause, {name}.\"\n\nYou start sweating.")

input()

drane = {"NAME": "The Dragon", "AGI": 20, "ATK": 20, "DEF": 20, "HP": 100, "CHOICE": True}

if len(status["help"]) > 0:
  wrap_text("Hey, Champion!\n\nYou turn around and see:\n")
  for i in status["help"]:
    wrap_text(i)
    stats["ATK"] += 10
  wrap_text("You realize that this fight will be much easier with that added help.")
  wrap_text("The dragon shouts \"Now! Let's get started!\"\n\n(Fight Begin)")

if inventory["armour"][0] == "ultimate":
  wrap_text(f"It pauses.\n\"Me and You, y'know, we're more alike than what might first meet the eye. What you're wearing, what You have - it's ultimate champion armour right? Doesn't that power feel - refreshing? Believe me I know... I once had a set too. Listen we can do so *much* with this country; with this playground. Just think about it, all the power You'll have if we combine forces.\"")
  c = answer(f"\"Now, what will You say... {name}?\" (y/n)", yesno)
  if c == "y":
    wrap_text(f"\"Oh how wonderful!\"\n\nThe dragon grabs You and strikes off the ground, travelling at the speed of sound. Due to the extreme pressure and g-forces You experience, You pass out. You wake up - infront of You is the dragon, albeit humanoid, smaller, and inside a library. It turns around.\n\n\"Ah, you've awoke. My name is Drane. I've brought You here to show You something.\"\n\nIt hands You a book, labelled Loculus Manuscript.\n\n\"Flip to page 13.")
    input()
    wrap_text(f"\"\n\nYou flip to page 13, and it reads:\n\n---\nIntroductory Clause:\nUpon reading this, You agree to Loculus' collection of sensitive user data, as well as the temporary erasure of user memory in specific games or adventures.\n---\n\nYou look up at Drane and ask \"What does any of this mean?\"\n\n\"It means we're GODS living inside of a game, {name}. We can do anything we damn please to. Those other champions? They are other players too. And You have their equipment, they are powerless in face of our tyranny.\n\nFor a moment, You feel disconnected from reality... until You aren't. {name}... starts controlling You. And all You can do is watch it happen.\n\n//\n\nWithout much delay, {name} and Drane manage to create a dystopia for those living in Resken, all while You are incapable of doing anything, an ethereal life form floating in a blank realm with nothing to do. You have failed.\n\n")
    print(r"""
              
   _____          __  __ ______       ______      ________ _____    
  / ____|   /\   |  \/  |  ____|     / __ \ \    / /  ____|  __ \   
 | |  __   /  \  | \  / | |__       | |  | \ \  / /| |__  | |__) |  
 | | |_ | / /\ \ | |\/| |  __|      | |  | |\ \/ / |  __| |  _  /   
 | |__| |/ ____ \| |  | | |____     | |__| | \  /  | |____| | \ \ _ 
  \_____/_/    \_\_|  |_|______|     \____/   \/   |______|_|  \_(_)
                                                                                                                                   
              """)
    print("\n\nYou, have lost.")
    input()
    quit()
  else:
    wrap_text("\"How disappointing. Part of me kind of expected this to happen. Oh well.\"\n\n(Fight Begin)")


outcome = fight(drane)

if outcome:
  wrap_text(f"*Cough*\n\n\"You... simpleton. If only You knew what power You could have had. You wanna know why you're here? I'll tell You why. It's because none of it is real, You are here because of {name}, someone You are very, very close with.\"\n\nYou feel disconnected.")
  input()
  print(r"""
  
 __     ______  _    _     __          _______ _   _ _ 
 \ \   / / __ \| |  | |    \ \        / /_   _| \ | | |
  \ \_/ / |  | | |  | |     \ \  /\  / /  | | |  \| | |
   \   /| |  | | |  | |      \ \/  \/ /   | | | . ` | |
    | | | |__| | |__| |       \  /\  /   _| |_| |\  |_|
    |_|  \____/ \____/         \/  \/   |_____|_| \_(_)
                                                       
                                                       

  """)
  input()
  wrap_text(f"\n\nThanks for playing!\n\n{name} takes off their headset: \"What a neat game!\". {name} puts their phone down, reading a question: \"Why'd Drane leave the chat?\"\n\nOn a table next to their headset reads:\n\n---\nIntroductory Clause:\nUpon reading this, You agree to Loculus' collection of sensitive user data, as well as the temporary erasure of user memory in specific games or adventures.\nNote: dying in game results in real death in some games, be careful.\n---\n\nMaybe You should have read that before playing...\n\n")
  print(r"""
  
  _______ _    _ ______       ______ _   _ _____  
 |__   __| |  | |  ____|     |  ____| \ | |  __ \ 
    | |  | |__| | |__        | |__  |  \| | |  | |
    | |  |  __  |  __|       |  __| | . ` | |  | |
    | |  | |  | | |____      | |____| |\  | |__| |
    |_|  |_|  |_|______|     |______|_| \_|_____/ 
                                                  
                                                  

  """)
  input()
  quit()
else:
  wrap_text("What a pitiful creature! You couldn't get back up even if You tried.\n\n")
  print(r"""
              
   _____          __  __ ______       ______      ________ _____    
  / ____|   /\   |  \/  |  ____|     / __ \ \    / /  ____|  __ \   
 | |  __   /  \  | \  / | |__       | |  | \ \  / /| |__  | |__) |  
 | | |_ | / /\ \ | |\/| |  __|      | |  | |\ \/ / |  __| |  _  /   
 | |__| |/ ____ \| |  | | |____     | |__| | \  /  | |____| | \ \ _ 
  \_____/_/    \_\_|  |_|______|     \____/   \/   |______|_|  \_(_)
                                                                                                                                   
              """)
  input()
  quit()