'''
def items_in_inventory(inventory):
    for i in inventory:
        if i[1] == 1:
            return True
        else:
            return False


len(list(filter(items_in_inventory,list(inventory.items()))))

'''
from random import *
def lost():
    lost_lines = ["This doesn't seem right, it feels like you've been here before...", "The numbers on these doors seem to be repeating...", "You don't remember these paths, what is going on?", "How does the hotel seem more bigger than it is?","There is something off... you feel you are lost"]
    def gorightleft():
        x = [None, None]
        count_error = 0
        while True:
            while(x[0] != "go"):
                if count_error > 2:
                    print("Having trouble? \nEnter 'go right' to go right or 'go left' to go left")
                    count_error = 0
                else:
                    x = (input("A junction, do you turn left or right? : ").lower()).split()
                    if x == []:
                        x = [None,None]
                    count_error += 1
            if x[1] == "right" or x[1] == "left":
                print(f'You turn {x[1]}')
                return
            else:
                x = [None, None]
    
    i = randint(4,8)
    for i in range(0,i):
        gorightleft()
        line = randint(0,4)
        print(lost_lines[line])
    return

def helping():
	print("Having a tough time? Below are the commands and instructions needed to play the game\n")
	print("To go to an object within the room - goto 'object / place name'")
	print("To pick up an item - take 'item name'")
	print("To drop an item - drop 'item name'")
	print("To look what is around in the room - look around")
	print("To look what you are carrying - open inventory")
	print("To move to a different room - moveto 'room name'\n")

class Character:
    def __init__(self):
        self.inventory = []
        self.room404_count = 0
        self.hall_count = 0
        self.room408_count = 0
        self.basement_count = 0
        self.corridor_count = 0
        self.room516_count = 0


liz = Character()



def input_command(commands):
    x = [None,None]
    count_error = 0
    
    while True :
        while x[0] not in commands.keys() :
            if count_error > 2:
                helping()
                count_error = 0
            else:
                x = (input("Enter here: ").lower()).split()
                if x == []:
                    x = [None,None]
                count_error += 1
        
        if len(x) == 2:
            if x[1] in list(commands[x[0]].keys()):
                return x
            else:
                x = [None,None]
        else:
                x = [None,None]

a = False

def execute(input,commands, character, mapping,room):                        #execute(input_command(commands), commands, table)
    if input[0]    == "goto":
        for i in commands["goto"].keys():
            if commands["goto"][i] == 1:
                commands["goto"][i] = 0
        commands["goto"][input[1]] = 1
        
        if len(mapping[input[1]][1]) != 0:
            print('\n'+mapping[input[1]][1][0]+'\n')
        return input[1]
        
    

    elif input[0] == "take":
        
        for i in commands["goto"].keys():
            if commands["goto"][i] == 1:
                current_place = i
                print(f'current place: {current_place}')
        
        if len(character.inventory) >=3:
            print('Inventory full, drop items to pick up new items.')

        elif input[1] in mapping[current_place][0]:
            character.inventory.append(input[1])
            print(f'{input[1]} added to inventory')
            mapping[current_place][0].remove(input[1])
            
        elif input[1] in character.inventory:
                print("You already have", input[1])
        else:
            print(input[1], "is not here.")
        return input[1]
    
    #new
    elif input[0] == 'drop':
        for i in commands["goto"].keys():
            if commands["goto"][i] == 1:
                current_place = i
                print(f'current place: {current_place}')
        
        if input[1] in character.inventory:
            mapping[current_place][0].append(input[1])
            print(f'{input[1]} dropped')
            character.inventory.remove(input[1])
        else:
            print(f'{input[1]} not present in inventory')
        return input[1]
    
    elif input[0] == 'look' and input[1]== 'around':
        for i in commands["goto"].keys():
            if commands["goto"][i] == 1:
                current_place = i
                print(f'current place: {current_place}')
                
        if len(mapping[current_place][0]) != 0:
            print('You find:')
            for pos,i in enumerate(mapping[current_place][0],1):
                print(f'{pos}) {i}')
            
        else:
            print('Nothing here.\n')
        return input[1]
            
    
    elif input[0] == 'open' and input[1] == 'inventory':
        if len(character.inventory)!=0:
            print('Inventory:')
            for pos,item in enumerate(character.inventory,1):
                print(f'{pos}) {item}')
        else:
            print('Inventory empty')
        return input[1]

    elif input[0] == 'read' and input[1] == 'letter':
        if 'letter' in character.inventory:
            print('''
            ===============================================================================================================================
            COMPLAINT
            _________
            
            DEAR hotel authority,
                We have several complaints about this hotel, they need to be looked into.
                Every time we come back to the room, there are things missing, if it was small objects we would have ignored it,
                but it has gone on too many times to ignore.
                The mirrors... there's something wrong with them... please get them exchanged. 
                We cannot count the number of times things we have seen things on it that cannot be possible. Her face is still haunting us. 
                If you do not know what I am talking about, please observe this room for a day.
                There's definitely something wrong with it.
                Can't overlook the writings on the wall that vanish infront of our eyes and the singing we hear at night...
                Please provide us with a new room meanwhile.
                We just can't stay here any longer.
                
                                                                            Yours truly,
                                                                            jonathan and beth-room408
            ===============================================================================================================================''')
            
        else:
            print('You do not have that.')

    elif input[0]=='read' and input[1]=='map':
        if liz.basement_count > 0:
            print('Places nearby:')
            for x,y in enumerate(mapping[room].keys(),1):
                print(x,')',y)
        else:
            print('Not enough locations discovered.')

    elif input[0] == 'moveto':
        mapping[room][input[1]](liz,input[1])
        return 0

        

class Game:
    
        
    #method for each area
    def choices(self,*args): 
        print('choices: ')
        for pos,choice in enumerate(args):
            print(f'{pos+1}):{choice}')         #hey
        reply = -1
        while reply not in list(map(str,list(range(1,len(args)+1)))):
            reply = input('enter choice: ')
        return int(reply),args[int(reply)-1]
    
    #to await an enter after each statement
    def eol(self):
        input('\n')
        # print("\033[A                             \033[A")#ansi escape arrow up then overwrite the line. might not work for some windows as it doesn't have ansi support
        
    def beginning(self):
        print('\nYou awake to the quiet rumbling of your car.\n')
        self.eol()
        print(
            'You can hear the constant chattering of your parents in the background, as your car travels down a long road, surrounded by endless fields of nothing.')
        self.eol()
        print('''
        Dad : It's quite late already isn't it? We were trying to reach the camping grounds by evening but the sun has already set!
        How about we spend the night at the nearest hotel?

        Mom : I think that's a good idea, I'll start looking for hotels nearby.
        Aren't you excited honey?! We'll get to spend the night at a lovely hotel and then tomorrow we can have a wonderful day camping and fishing!
        ''')
        self.eol()

        x, y = self.choices(
            "Hmph I wouldn't even have to be here if not for you guys, why can't you just leave me alone ugh!",
            "Tch excited?!? I would've preferred to be watching movies with my friends.",
            "Is it too late to go home now? I hate this trip ugh!")
        print(f'\n        You : {y}')
        print('''
        Dad : Don't say that to your mom! Try and have fun for once, we finally get to go on a vacation as a family.

        Mom : Never mind that silly stuff... Sweetie are you getting any network? It seems to have suddenly gone out of coverage for me.
        Last I saw, hotel Serenity was the closest, and it should be a few miles ahead.''')
        self.eol()

        print('\nYou check your phone and see it display no bars.')
        print('''
        You: Ugh this trip just got worse.''')
        self.eol()
        print(
            '\nA sudden mist sets in... the fields vanish into a void of grey.\nThe last bits of moonlight filter through the gaps eerily, as the car drifts along the rapidly vanishing road')
        self.eol()
        print('''
        Dad : My god, where did all this mist come from, I can't see a thing! How far did you say that hotel Serenity was again, because I don't know if we can make it there safely now.''')
        self.eol()
        print(
            '\nAs you bide your time waiting to reach, you glance out of the windows hoping to catch sight of anything man made.\nThe flowing mist seems to take the shape of shadows of men and other creatures of imagination, it unnerves you and sends a little chill down your back.')
        self.eol()



        print("\nAs you drive through the fog, you see a faint light in the distance. You realize it's a sign for a hotel as you approach it. ")
        self.eol()
        print("\nYou park your car under the flickering lights of the signboard")

        print('''
        DAD : Ahh what a relief, we found a hotel. I guess we should stay here for the rest of the night and go camping in the morning
        ''')
        self.eol()

        print("\nAs you get out of your car, you feel a gust of cold breeze wind past you. "
              "You see a huge, rusty gate hanging under the dull street light.")
        self.eol()
        print("\nThe gate makes a creaking sound as you enter the hotel")
        print("You feel a chill down your spine as you look at the hotel.")

        print( "You see broken windows, a dusty frontyard, you hear the windows creaking due to the strong winds and ripped curtains in the windows\n")
        self.eol()
        x,y = self.choices(
            "This place is giving me creeps!! Why do we have to stay in such a stupid place?!",
            "When was the last time they even cleaned and maintained this place?! Why are we staying in such a place??!",
            "AHHH what the hell?! Why did I even come on such a stupid trip?!"
            )
        print(f'\n        YOU: {y}')
        print('''
        DAD : Come on! How bad could it be? We are just staying here for one night anyway
        '''
              )
        self.eol()
        print("As you enter the hotel, you see the walls are covered with dust and cobwebs, sheets on the furniture and broken tables ")
        print("There are holes in the walls, chandelier with broken strings of crystal and a flickering bulb under which was the reception")
        self.eol()
        print("A tall figure is at the reception with pale skin, greased back hair, hunched back, piercing black eyes, false smile,he watches you like a wolf might observe it's prey. He slightly smiles at you parents.")
        print("\nYou feel uneasy and uncomfortable under his cold stare. As you look around the hotel, you hear a coarse voice. ")
        self.eol()
        print('''
        RECEPTIONIST: WELCOME TO HOTEL SERENITY! How can I help you today?'''
        )
        print('''
        DAD: A room for three please''')
        self.eol()
        print('''
        RECEPTIONIST: Here are your keys. Room 404 on the first floor.''')
        self.eol()
        print("\nThere was a rickety old staircase that went up, the ground seemed to go far away as you climbed the creaky stairs ")
        print("You could smell the rotten wood which composed the walls.As you reached the top there was a big old wooden door on the right which said 404")
        print("\nAs you approached the door, you could sense someone looking at you through the peephole. ")
        self.eol()
        print("You shiver, as though, ice had replaced your spine. The cold air envelops your entire body")
        print("\nThe door begrudgingly creaks open. A musty, dank order creeps into your nose. The room was dead silence except for the intermittent creaks and moans.")
        print ("Black and brown mold dotted the ceiling in clusters, evident of rain seeping through the roof. ")
        self.eol()
        print("\nYou quietly enter the dark living room. Windows covered with grime and dirt, the calm moonlight struggled to penetrate the darkness in thin thread rays.")
        print ("Sharp shadows roamed around the room. ")

    def room_404(self, character,room):
        commands = {'read':{'map':0},'moveto':{'hall':0,'room404':0},'stop':{'null':0},"goto":{"table":0,"cupboard":0,"bookshelf":0,"bed":0,"tv":0,"mirror":0,'base':1},"take":{"flashlight":0,"rope":0, "pen":0,"keychain":0,"knife":0,"axe":0,"ring":0, "letter":0,'screwdriver':0,"key":0,"matchox": 0,"bandages":0,"locket": 0, "bottle": 0},"drop":{"flashlight":0,"rope":0, "pen":0,"keychain":0,"knife":0,"axe":0,"ring":0, "letter":0,'screwdriver':0,"key":0,"matchbox": 0,"bandages":0,"locket": 0, "bottle":0},'look':{'around':0},'open':{'inventory':0}}
        dict1 = {'room404':{'hall':g.hall},'table':[['pen'],['A rather old table, cracked around the edges.']],'cupboard':[['flashlight','keychain'],['The cupboard seems to have been untouched for many years.']],'bed':[['knife'],["There's probably more dust in the sheets than on the ground"]],'base':[[],['There is a cupboard nearby, a table next to it. To your side lies a bed, there is a dusty bookshelf next to the bed. There is an old TV set infront of you, a large mirror on the wall next to it. ']],'mirror':[[],['You see your reflection looking back at you, but the image seems hazy. Rather unsettling.']],'tv':[[],['An old fashioned box TV set, has a few cracks, it might not even be functional.']],'bookshelf':[['locket'],['A lot of old books seem to have been stuffed in the bookshelf. The pages seem wrinkly and delicate.']]}
        
        exit_criteria = 1
        character.room404_count += 1
        if (character.room404_count > 1):
             print("It's a dark shabby room with just enough space for the three of you.There is a cupboard nearby, a table next to it. To your side lies a bed, there is a dusty bookshelf next to the bed. There is an old TV set infront of you, a large mirror on the wall next to it.")
        if (character.room404_count == 1):
            print("You walk into the room 404 with your parents. It's a dark shabby room with just enough space for the three of you.There is a cupboard nearby, a table next to it. To your side lies a bed, there is a dusty bookshelf next to the bed. There is an old TV set infront of you, a large mirror on the wall next to it. ")

            print(''' DAD: We are going to the reception now for the formalities, just wait here for 10 minutes, we'll be back soon. Don't leave the room until we are back''')
            self.eol()

            print("Your parents move out\n")
            print("You get time to look around the room.\n")
            while len(character.inventory) < 3:

                execute(input_command(commands), commands, liz, dict1, room)
                if 'flashlight' not in character.inventory:
                    print('The lights seem to be flickering, you might need to find some source of light.')
                elif len(character.inventory) < 3:
                    print('Maybe you need more items.')
            print('\n You suddenly hear a loud thud. You see a huge book lying at the feet of the bookshelf')
            self.eol()
            while exit_criteria != 'bookshelf':
                exit_criteria = execute(input_command(commands), commands, liz, dict1, room)
            print("You pick up a black,leather-bound book with a degrading cover. You get the soothing scent of the old leather. ")
            print("As you flip through the dry pages of the book, you realize it's an old diary.")
            print("The diary dates back to 1912. It seems to be a diary of a woman named Agatha. ")
            self.eol()
            print('''
            May 9, 1912.
                Mark is still looking for a job. We had to move out of our apartment as we couldn't afford rent.
                Luckily we found an old hotel which was cheap enough.
                Sheldon had to drop out of school as we couldn't afford the fees. 
                Mark's health has gone for a toss and his alcohol addiction is at peak due to the hard times.
                Mark works part-time as a milkman and a delivery guy to provide us with basic amenities.
                Most of our income is siphoned off on his drinking problem. I hope Mark finds a steady job soon.
                Sheldon wishes for our family to be happy. He gifted me a locket with a picture of our family.
                It was such a cute gesture during these hard times. 
                It seemed like I was the happiest person in this world!
                .''')
            self.eol()
            print('You continue to flip through the pages')
            print('''
            May 12,1912.
            I can't sleep. The night is dark and I'm filled with terror. 
            Sometimes, when I write this diary, I think maybe there's more to life than sadness and fights.
            Mark came home drunk again. His drinking provokes his aggression.
            He started taking his anger out on Sheldon. I just couldn't bear to see my son get hurt.
            I just couldn't take it anymore. I barged in to stop Mark. This just made him more aggressive. A few blows were exchanged.
            I dragged Sheldon out of the hotel room and left Mark locked in. None of the hotel members even bothered to help us.
            Me and Sheldon just spent most of our night in the hallway crying. I just cant take it anymore.
            I pray that this all ends fast.''')
            self.eol()
            print('You turn the page.\n')
            print('''
            May 21, 1912.
            There used to be days that I thought we were okay, or at least that we were going to be okay.
            We'd be living somewhere and everything would just fit right and I would think "it will be okay if it can just be like this forever".
             But of course nothing ever goes the way you want it to go.
             I LOST EVERYTHING! That devil ended up taking the most dearest thing away from me!
             I lost sheldon. I can't take it anymore. He ended up taking his own life also in grief over his actions.
             He left me all alone in this dreadful world. None of the hotel members believe me. 
             They accused me for the death of my OWN FAMILY. They never helped us.
             They didn't believe me. Nobody did. I was always the one suffering.
             It's my turn to spread the same fear instilled upon me day by day.
             IT'S MY TURN!
             I'm going to put myself to sleep now in this dreaded hotel. For a bit longer than usual.
             Call it eternity. 
             ''')
            self.eol()
            print("You find your arms trembling with fear as you finish reading. Your vision gets blurry.  ")
            print("You can feel your heart pounding fast and you feel frozen with fear.")
            
            self.eol()
            # the stuff
            print("There's a sudden flash as the tv turns on and the sound of dead static envelops the room.\n")
            print("It seems to be unplugged.")
            self.eol()
            print("As you head to investigate, the flickering lights cut and burst and the buzzing sounds vanish as the room fades into an eerie darkness. You can't see anything.")
            if 'flashlight' not in character.inventory:
                print('You fumble around the darkness. A feeble light pours in through a window nearby and you go near it.')
                self.eol()
                print("Your hands reach out and feel the cold smoothness of glass. With a sigh of relief you open the window.")
                self.eol()
                print("The cold mist pours in from the outside as you try to discertain the sight. As you squint your eyes through the window, you feel a hot breath on your neck...")
                self.eol()
                print('Before you get a chance to scream or even turn around, you feel a hard shove on your back and you feel yourself falling out.')
                print('The winds gush past you as you desperately scramble for any hold as you fall')
                self.eol()
                print('BUT DARKNESS IS ALL THAT AWAITS')
                print('You die.')
                return
                #escape sequence
            else:
                print('You turn on the flashlight you picked up.')
                self.eol()
                print("On glancing at the mirror above the dead tv, you see a sight that leaves you petrified...")
                self.eol()
                print("Written in what looks like blood... the words 'DO YOU BELIEVE ME?' lie scribbled across it's smooth surface.")
                self.eol()
                print("Sheer terror erupts within you and you scramble backwards for the door. You haven't the slightest clue about what just occurred, but you know one thing. Just one thing had etched itself into your being. You can't stay here, not anymore, not ever again. You HAVE to escape.")
                self.eol()
                print('Escape to the hall')
        while exit_criteria != 0:
            exit_criteria = execute(input_command(commands), commands, liz, dict1,room)
        return
        
      

    def corridor(self, character, room):
        character.corridor_count +=1
        exit_criteria = 1
        commands = {'moveto':{'basement':0,'hall':0},'goto':{'right':0},'open':{'inventory':0},"read":{"letter":0,'map':0}}
        dict1 = {'corridor':{'basement':g.basement,'hall':g.hall},'right':[[],[]],'door':[[],[]],'table':[['letter'],['Papers are skewed across the table, there seems to be a letter with a big red heading.']],'cupboard':[['screwdriver'],['It seems to be mainly empty.']],'bed':[[],["The sheets seem to have red stains on them."]],'base':[[],['There is a cupboard nearby, a table next to it. To your side lies a bed, there is a dusty bookshelf next to the bed. There is an old TV set infront of you, a large mirror on the wall next to it. ']],'board':[[],['Many newspaper clippings about an incident that occured in 1912 are pinned across the board']],'curtains':[['axe'],['An object seems to peek out from behind a tattered mess of curtains, it has a mean glint to it.']]}
        
        if character.corridor_count == 1:
            print("You suddenly hear a voice calling your name in the distance")
            self.eol()
            print("You realize it's the voice of your mother!")
            self.eol()
            print("You run towards the voice, it gets louder and louder as you approach it")
            self.eol()
            print("As you take a right in the hallway, you see two figures at the end of the hallway running frantically.")
            self.eol()
            print("You yell MOM DAD and run towards them! Your eyes are filled with happiness and relief when you see them.")
            self.eol()
            print('''
            DAD: Ahhh Liz! Are you okay?! Lets get out of this wretched place!!''')
            self.eol()
            print("As your parents are about to embace you, you see a dark humanoid figure behind them")
            self.eol()
            print("It grabs your mother by her neck and drags her around the corner")
            self.eol()
            print("You just stand there frozen, your legs go weak and you drop down on your knees")
            self.eol()
            print("You don't know whats happening anymore, everything seems to go dark, you suddenly feel your dad grab your shoulder.")
            self.eol()
            print('''
            DAD: LIZ LIZ! RUN! JUST GET OUT OF THIS PLACE! I'LL GO LOOK FOR MOM! YOU JUST LEAVE THIS PLACE! DON' FOLLOW ME! I'LL GET MOM BACK SAFELY''')
            self.eol()
            print('''
            YOU: BUT DAD! WHAT ABOUT MOM?! I CAN HELP''')
            self.eol()
            print('''
            DAD: DON'T WORRY ABOUT HER! I'LL FIND HER! JUST GO! PLEASE! I PROMISE THAT I'LL FIND HER! WE LOVE YOU LIZ''')
            self.eol()
            print("You see your dad go around the corner yelling the words RUN RUN")
            self.eol()
            x, y = self.choices(
                "Run away and look for a way to escape",
                "Go after dad and help him"
            )
            if x == 1:
                print("You decided to runaway! Find an escape route fast!")
                #lost()
                self.basement(liz, 'basement')
            else:
                print("You go after dad to help him find mom! ")
                self.eol()
                print("As you take a turn around a corner, you see an empty hallway.")
                self.eol()
                print("It's as if your dad disappeared into thin air. You feel your body brimming with fear and loneliness.")
                self.eol()
                print("You run around frantically looking for them!")
                
                self.basement(liz, 'basement')
        print('You are in corridor now')
        while exit_criteria != 0:
            exit_criteria = execute(input_command(commands), commands, liz, dict1,room)


    def hall(self, character, room):

        commands = {'moveto':{'room404':0,'room408':0},'goto':{'right':0},'open':{'inventory':0},"read":{"letter":0,'map':0}}
        dict1 = {'hall':{'room404':g.room_404,'room408':g.room_408,'corridor':g.corridor},'right':[[],[]],'door':[[],[]],'table':[['letter'],['Papers are skewed across the table, there seems to be a letter with a big red heading.']],'cupboard':[['screwdriver'],['It seems to be mainly empty.']],'bed':[[],["The sheets seem to have red stains on them."]],'base':[[],['There is a cupboard nearby, a table next to it. To your side lies a bed, there is a dusty bookshelf next to the bed. There is an old TV set infront of you, a large mirror on the wall next to it. ']],'board':[[],['Many newspaper clippings about an incident that occured in 1912 are pinned across the board']],'curtains':[['axe'],['An object seems to peek out from behind a tattered mess of curtains, it has a mean glint to it.']]}
        exit_criteria = 1
        
        if character.hall_count == 0:
            character.hall_count += 1
            print('As you take a step out of the room, a sudden chill sweeps through your bones.')
            print('The path seems soft, intangible even. Darkness sticks to your face as you walk down the empty hallway.')
            self.eol()
            print('The hallway seems endless, corrosive, barren and dead. Your legs are frozen with fear which slows you down,impeding your moves')
            print('You stumble on this road down the abyss of darkness. As you yearn for the sun, you see a small figure at the end of the hallway')
            self.eol()
            print('You see a door wih rotting wood on your right. Room408')
            self.eol()
            print('On the other side you see a woman who is stripped of her humanity. Her sick pale skin decorates her rotting flesh.')
            print('You hear her humming an unearthly tune. As you take a step forward, she notices you and gives a death glare.')
            x, y = self.choices(
                "Go to the woman.",
                "Run towards the room."
            )
            if x == 1:
                print('Her stiff eyes, devoid of emotion stares right into your soul.')
                print('You see her talking slow steps towards you. She points her dead arms and starts progressing towards you.')
                self.eol()
                print('You try running but your body is cold as ice and you find yourself frozen with fear.')
                print('You force your legs to move as the corpse of the woman advances at inhumane speed.')
            self.eol()
            print('You approach the huge door which says 408.')
            self.eol()

            print('Each little grain that makes up the door is staring at you, inducing fear.')
            self.eol()
            print('The darkness that seeps through the gas is reaching out to you.')
            self.eol()
            if 'keychain' not in character.inventory:
                print("You try opening the door but the door doesn't budge. The door seems to be locked")
                print("You push the door with all your might and the door doesn't flinch.")
                print('You have no keys for the room.')
                self.eol()
                print("You suddenly hear a loud screetching noise behind you.")
                self.eol()
                print("You corner yourself to the door, looking around in fear. You try screaming but no voice comes out.")
                print("You suddenly see the girl with spindly arms hanging from her torso, scarcely able to hold carry the weight of her skeletal arms ")
                self.eol()
                print("You suddenly feel a massive force hit your head as it hits the big old door. You hear your skull cracking and darkness envelops you")
                print("You feel her fingers on your neck with trembling claws with nails filed into sharp points.")
                self.eol()
                print("As you lay down on the floor with blood seeping through your head, you see her sunken, black eyes.")
                print("She stares into your soul with a dead gaze and squeezes your neck ")
                self.eol()
                print("Slowly, her lips parted, and a vile grin crept across her decayed face, revealing a set of rotten fangs and black gums")
                print("Now all you see is darkness, as your soul is squeezed out of your body.")
                print("You Died. Game Over.")
                return
            print("You frantically try each key within the keychain you took. Then suddenly you hear a click on your third try. You push open the door and enter")
            self.room_408(liz, 'room408')
        elif character.hall_count == 1:
            print("You're back to the hall, room404 and room408 are nearby, and there's a right turn ahead.")
            
            while exit_criteria != 'right':
                exit_criteria = execute(input_command(commands), commands, liz, dict1,room)
            character.hall_count += 1    
            print('You turn right.')
            lost()
            self.corridor(liz,'corridor')
            return
        else:
            #here we have to change the exit criteria because new places are known
            commands['moveto']['corridor'] = 0
            print("You're back to the hall, room404 and room408 are nearby, and there's a right turn ahead.")
            
            while exit_criteria != 'right':
                exit_criteria = execute(input_command(commands), commands, liz, dict1,room)

    
    def room_408(self, character, room):
        exit_criteria = 1
        character.room408_count +=1
        commands = {'moveto':{'null':0},'stop':{'null':0},"goto":{'door':0,"table":0,"cupboard":0,'curtains':0,'board':0,"bed":0,'base':1},"take":{"flashlight":0,"rope":0, "pen":0,"keychain":0,"knife":0,"axe":0,"ring":0, "letter":0,'screwdriver':0,"key":0,"matchox": 0,"bandages":0,"locket": 0, "bottle": 0},"drop":{"flashlight":0,"rope":0, "pen":0,"keychain":0,"knife":0,"axe":0,"ring":0, "letter":0,'screwdriver':0,"key":0,"matchbox": 0,"bandages":0,"locket": 0, "bottle":0},'look':{'around':0},'open':{'inventory':0},"read":{"letter":0,'map':0}}
        dict1 = {'room408':{'hall':g.hall},'door':[[],[]],'table':[['letter'],['Papers are skewed across the table, there seems to be a letter with a big red heading.']],'cupboard':[['screwdriver'],['It seems to be mainly empty.']],'bed':[[],["The sheets seem to have red stains on them."]],'base':[[],['There is a cupboard nearby, a table next to it. To your side lies a bed, there is a dusty bookshelf next to the bed. There is an old TV set infront of you, a large mirror on the wall next to it. ']],'board':[[],['Many newspaper clippings about an incident that occured in 1912 are pinned across the board']],'curtains':[['axe'],['An object seems to peek out from behind a tattered mess of curtains, it has a mean glint to it.']]}
        if character.room408_count == 1:
            
            
            print("As you enter the room, you close and lock the door behind you.")
            self.eol()
            print("The only source of light is your flashlight, as it illuminates different parts of the room, you realise that it seems just as unoccupied as the previous room. ")
            self.eol()
            print("There's a table placed at the center of the room. Tattered curtains lie to the side covering a section of the wall.\nA large board lies to the edge of the room and there's a cupboard next to it. The door is closed behind you.")      
            exit_criteria = 0
            self.eol()
            while exit_criteria != 'door':
                exit_criteria = execute(input_command(commands), commands, liz, dict1,room)
            
            print('As you turn around to go to the door, your vision falters and everything seems hazy.')
            self.eol()
            print("You rub your eyes to try and recover. When you open them there lies a a woman's body, hanging in the air from something unseen, her head at an unnatural angle.")
            self.eol()
            print("You are paralyzed to the spot, the menacing aura is holding you in it's tightening grip ")
            self.eol()
            print("As you blink, the body disappears into thin air!")
            self.eol()
            print("You flee towards the door! The door doesn't budge open!")
            self.eol()
            if 'axe' not in character.inventory:
                print("You can't open the door, you have to break it.")
                while exit_criteria != 'axe':
                    exit_criteria = execute(input_command(commands), commands, liz, dict1,room)
            print("You get a firm grip on the axe, with all your might you take a wide swing at the door")
            self.eol()
            print("The door cracks upon! You kick the crack hard which makes a small opening. You squueze through the small opening to enter the hall")
            self.hall(liz, 'hall') 
        commands['moveto']['hall'] = 0
        print('You are back in room408')
        print("There's a table placed at the center of the room. Tattered curtains lie to the side covering a section of the wall.\nA large board lies to the edge of the room and there's a cupboard next to it.")      
        while exit_criteria != 0:
            exit_criteria = execute(input_command(commands), commands, liz, dict1,room)
        return

    def basement(self, character, room):
        print("You are in basement now.")
        character.basement_count += 1
        exit_criteria = 1
        commands = {'moveto':{'corridor':0, 'room516': 0},'stop':{'null':0},"goto":{'locker':0,"dustbin":0,"table":0,'boiler':0,'sofa':0,"aquarium":0,'base':1},"take":{"flashlight":0,"rope":0, "pen":0,"keychain":0,"knife":0,"axe":0,"ring":0, "letter":0,'screwdriver':0,"key":0,"matchox": 0,"bandages":0,"locket": 0, "bottle": 0},"drop":{"flashlight":0,"rope":0, "pen":0,"keychain":0,"knife":0,"axe":0,"ring":0, "letter":0,'screwdriver':0,"key":0,"matchbox": 0,"bandages":0,"locket": 0, "bottle":0},'look':{'around':0},'open':{'inventory':0},"read":{"letter":0,'map':0}}
        
        
        dict1 = {'basement':{'corridor':g.corridor, 'room516': g.room_516},'locker':[["bandages"],["Amongst the dirty old furnitures lies a giant locker, eaten away by years of rust."]],'table':[['bottle'],['An old table with the things on it scattered around everywhere']],'dustbin':[[],['Inside the dustbin you find a severed finger. With a gasp you realise that it has the same ring which you found in room 408']],'boiler':[[],["You feel the boiler's scorching heat burning up the last remnants of your energy and will to keep going forward."]],"sofa":[[],["You see a torn and filthy sofa which has rotting food all over it"]],"aquarium":[[],["A broken aquarium having the shattered glass pieces lying around."]],'base':[[],['Boiler \nYou walk into the basement giving out strong heat because of a boiler. There stands a humongous locker beside you, a dusty sofa, a broken aquarium and a dustbin. A messy table with a lot of papers and a bottle. Something about this room runs a shiver down your spine inspite of the heat.']]}
        if character.basement_count == 1:
            print("The basement was like a place out of time. Shadows scraped all over the walls. You hear a consitent dripping noise. A rancid smell makes you want to leave the room as soon as possible.")
            self.eol()
            print("You follow the dripping sound which takes you to the back of the locker.")
            self.eol()
            print("You see two bodies at a distance hanging down the ceiling by a net made of rope. The bodies were motionless and their skin seemed pale.")
            self.eol()
            print("A trail of blood that dripped from one of their hands trickled down to your feet.")
            self.eol()
            print("As you approach the corpses, you notice the bleeding hand holds the bracelet that you gifted your mom on her last birthday.")
            self.eol()
            print("Your knees buckle as memories race through your head and your hands get numb as you recognise that the bodies are none other than those of your parents.")
            self.eol()
            print("You drop down on your knees in a disheveled heap as your grief poured down as a flood of uncontrollable tears.")
            self.eol()
            print("All you can think about is the horrible words you told your parents when all they wanted you was for you to survive and have a good life.")
            self.eol()

            print("After putting yourself together, you notice a key dangling from your dad's pant pocket.")
            print("Their bodies dangle at a considerable height from where you cannot reach for the pocket.")
            self.eol()
            if "knife" not in character.inventory:
                print("Only if you had something to cut the rope...")
                while(exit_criteria != 0):
                    
                    
                    exit_criteria = execute(input_command(commands), commands, liz, dict1,room)
                return
            else:
                print("You use your knife to cut the rope. The bodies fall down with a big thud.")
                self.eol()
                print("As you see the bloodied bodies of your parents, you find the key in your dad's pocket")
                while(exit_criteria != "key"):
                    exit_criteria = execute(input_command(commands), commands, liz, dict1,room)
                print("On the keychain you read the numbers room516.")
                print("This is the last object your dad saved for you. Maybe it wasn't all in vain.")
                self.room_516(liz, "room516")
                return
        if character.room516_count == 0:        
            if "knife" not in character.inventory:
                print("Only if you had something to cut the rope...")
                while(exit_criteria != 0):
                        
                        
                    exit_criteria = execute(input_command(commands), commands, liz, dict1,room)
                return
            else:
                print("You use your knife to cut the rope. The bodies fall down with a big thud.")
                self.eol()
                print("As you see the bloodied bodies of your parents, you find the key in your dad's pocket")
                while(exit_criteria != "key"):
                    exit_criteria = execute(input_command(commands), commands, liz, dict1,room)
                print("On the keychain you read the numbers room516.")
                print("This is the last object your dad saved for you. Maybe it wasn't all in vain.")
                self.room_516(liz, "room516")
                return

        while(exit_criteria != 0):
            exit_criteria = execute(input_command(commands), commands, liz, dict1,room)
        return
    

      

    def room_516(self, character, room):
        global a 
        
        character.room516_count +=1
        print("You are in room 516")
        exit_criteria = 1
        dict1 = {'room516':{'basement':g.basement,"shrine":g.shrine},'briefcase':[["vial"],["You see an open old and ragged briefcase having bloodstains on them, inside which there is a vile of holy water."]],'mirror':[[],['You see a large mirror which has the words "NONE OF YOU BELIEVED ME" written with blood.']],'wall':[[],["You see a wall where there are more words written in smeared blood, 'I KILLED EVERYONE, EVERYONE WHO TRIED TO STAY IN THIS DAMNED HOTEL WHERE NO ONE BELIEVED ME.'"]],'dresser':[["comb"],["An old dresser, whose mirror is shattered."]],"skeleton":[[],["The skeleton looks like it is clenching on to something"]],'base':[[],['Room516 \nA room enveloped with an eerie darkness with heaps of skeletons piled up next to the dresser with shattered glass. There is another mirror on the other end of the room whith smeared blood stains and also a wall with similar stains and both of them seem to be having a message etched upon with the same blood. One of skeleton seems to be clenching something in its hand, and on the opposite side of the room you find a briefcase which is too large to carry around. ']]}
        commands = {'moveto':{"shrine":0,'basement':0},'stop':{'null':0},"goto":{'briefcase':0,"mirror":0,"wall":0,'dresser':0,"skeleton":0,'base':1},"take":{"flashlight":0,"rope":0, "pen":0,"keychain":0,"knife":0,"axe":0,"ring":0, "letter":0,'screwdriver':0,"key":0,"matchox": 0,"bandages":0,"locket": 0, "bottle": 0, "vial": 0},"drop":{"flashlight":0,"rope":0, "pen":0,"keychain":0,"knife":0,"axe":0,"ring":0, "letter":0,'screwdriver':0,"key":0,"matchbox": 0,"bandages":0,"locket": 0, "bottle":0, "vial":0},'look':{'around':0},'open':{'inventory':0},"read":{"letter":0,'map':0}}
        

        if character.room516_count == 1:

            
            while exit_criteria != "skeleton":
                exit_criteria = execute(input_command(commands), commands, liz, dict1,room)
                
            commands["moveto"]["shrine"] = 0
            commands["moveto"]["basement"] = 0
            a = True
            print("The skeleton is clenching on a note. You slowly take it out of its hand and start reading")
            self.eol()
            print("It's November 3, 1978. I was called to check over a hotel where strange unexplainable things were happening. \
                   \nI came to the shrine, it was where I was told that nobody returns from. This had to have been where everything occured.\
                   But little did I know that it would be one of the most terrifying experience that I have ever had.\
                   \nAs I sit in this small confinments I've made for myself,  I have momentarily avoided certain death, the holy water seems to be keeping her at bay.\
                   \nAt this moment there's nothing I can think about other than my family, I cant do anything except stare at their last picture.\
                   \nDo demons have feeling?\
                   \nDo demons have any earthly connection?\
                   \nIf so as a father, I really wish i could show this demon anything that reminds her of her family.\
                   \nMaybe that would finally let her rest.\
                   \nIf only I had something")
            self.eol()
            print("You look around the room and notice a small door hidden behind the dresser with a cross on top of it. It only takes you a moment to realise that this is the entrace to the shrine the shaman was talking about.")
            self.eol()
            print("This is the path of no return treading upon which will determine whether you live your die.")
            self.eol()
            print("The only thought on your mind is that if you don't tread on this path, your parents would have died in vain.")
            self.eol()
            print("This is the final battle...")
        if a == True:
            commands["moveto"]["shrine"] = 0
            commands["moveto"]["basement"] = 0
        while(exit_criteria != 0):
            exit_criteria = execute(input_command(commands), commands, liz, dict1,room)     
        return 

    def shrine(self,character,room):
        if 'locket' in character.inventory and 'vial' in character.inventory:
            print("As you enter the shrine, you feel the air turn cold.")
            self.eol()
            print("With a shriek of terror you see a woman zipping through the air towards you")
            self.eol()
            print("Without a second thought, you throw the vial down to the floor infront of you. It shatters and creates a puddle of holy water on the floor and you hurriedly step into it.")
            self.eol()
            print("The woman suddenly slows down and comes to a standstill. You realise you've succesfully saved yourself just like the shaman did.")
            self.eol()
            print("You take the locket out of your pocket and proceed to decide.")
            x,y = self.choices('Break the locket','Show her the locket')
            if x == 1:
                print("You throw the locket to the ground as hard as you can. The fragile locket breaks and a picture of a family smiling falls out of it into the holy water.")
                self.eol()
                print("The woman starts screeching, the bloodcurdling screams are hard to bear as you watch her in agony.")
                self.eol()
                print("Little by little, her body starts to go up in flames. In less than a minute, there is no trace left but the ashes.")
                return
            else:
                print("You open the locket and see a picture of a family with smiles drawn on their faces.")    
                self.eol()
                print("You realise the woman in the picture bears striking resemblance to the woman infront of you. Just as the shaman had said, you decide to show her her family again.")
                self.eol()
                print("As you turn the locket over to her, she lets out a short gasp. She looks at the locket with utter shock.")
                print("Tears start streaming down her face, one by one and her lips start whimpering.")
                self.eol()
                print("'My boy. My sheldon. He just wanted us to be happy together. Yet here I am, after having left him all alone somewhere out of this world. I've been living this life seeing all the wrong things. I missed what the most important thing was' ")
                self.eol()
                print("Her body begins to slowly fade away from your sight as she finally returns back to her child she left behind.")
                print("Soon there is nothing left, she is long gone, far, far away from you")
            print("The sunlight slowly starts seeping through the windows as the mist lifts.")
            self.eol()
            print("You've made it through the day. You've lost so much that you cannot even imagine how life would be from now onwards.")
            print("Yet the fact remains that you survived. Your parents live on through your memories and you have a whole life ahead of you.")
            self.eol()
            print("As you finally take your first steps out of the wretched hotel, you can't help but wish this is all a dream. Wish you wake up at your friend's house or in your parents car as you travel to find a hotel.")
            self.eol()
            print("But you know in your heart that this is no dream. This really was...")
            print("Agatha's revenge.")
            return
        elif 'locket' in character.inventory:
            print('The shrine sends chills down your spine as you enter it.')
            self.eol()
            print("You get ready to destroy the locket. But suddenly you hear someone breathing over your shoulder. ")
            self.eol()
            print("You try turning around but you feel a cold grip on your neck. You try shouting and nothing comes out")
            self.eol()
            print("As you struggle to breathe, you feel your conciousness fade away and you see a crooked dark figure glaring at you as you sink into the abyss of darkness")
            self.eol()
            print("As you lose conciousness and you're wiped out of existence, you realize that you would've won if you had a means to slow her down from attacking you.")
            self.eol()
            print("If only you could do it the right way again...")
        elif 'vial' in character.inventory:
            print('As you enter the door, you feel a sudden chill and hear howling winds')
            self.eol()
            print("You realise the winds are nothing but the shrieks of a woman as she zips towards you.")
            self.eol()
            print("You scream and drop the vial of holy water. It shatters on the floor and creates a puddle under you.")
            print("The woman suddenly stops as she was just about to reach you.")
            self.eol()
            print("You realise this was how the shaman survived. Back then it was him. Now it's you. You both doomed yourself to suffer within these small confines for an eternity until you perish.")
            self.eol()
            print("If only you had listened to the shaman's last wishes. If only you found something the woman had a connection to. You vaguely remember something about a locket, but you jsut can't place it.")
            print("You realise this is how you die. Starvation and thirst. With this realisation, you wish you could see your family one last time as you set in for the long trip")
            self.eol()
            print("You die of thirst. Game over.")
            return
        else:
            print('As you enter the shrine room, you feel the temperature drop greatly. Your ears pop as the pressure decreases. ')
            self.eol()
            print('Not a moment passes before you feel all the air sucked from your lungs.')
            print('You drop to the floor choking for a breath. No matter how much your chest expands, not a bit of air enters.')
            self.eol()
            print('As you feel your consciousness fade away, you see a womans face lower to your ears.')
            self.eol()
            print("'My name is Agatha, and this is my revenge.'")
            self.eol()
            print('The darkness creeps in as you realise you had nothing you could stop her with. The shaman had given you the hints, but you did nothing with it. If only you could do it all again the right way....')
            self.eol()
            print("You die. Game over.")
            return
                
g = Game()
'''

execute(input_command(commands), commands, liz, dict1)
print(commands)
print(dict1)
print(liz.inventory)

'''
'''

g = Game()
g.beginning()
g.room_404(liz)
'''

g.beginning()



g.room_404(liz,'room404')
