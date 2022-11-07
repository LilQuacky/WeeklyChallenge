import os,sys,time,random

#stats
run = True
menu = True
play = False
history= False
key = False
standing = True

#player stats
HP = 50
HPMax = HP
ATK = 5
pot = 1
elisir = 1
gold = 10
x = 0
y = 0
buy= False
speak=False
boss=False

#map
map = [
        ['CyberHome','CyberShop','CyberDesert','CyberDuna','CyberSea','CyberTown'],
        ['CyberCenter','CyberCity','CyberForest','CyberDragonCave','CyberMayor','CyberBridge'],
        ['CyberPlains','CyberHospital','CyberSwamp','CyberMountains','CyberVolcano','CyberHills'],
        ['CyberHome','CyberPlains','CyberDesert','CyberDuna','CyberSea','CyberTown'],
        ['CyberCenter','CyberCity','CyberForest','CyberDragonCave','CyberMayor','CyberBridge'],
        ['CyberShop','CyberHospital','CyberSwamp','CyberMountains','CyberVolcano','CyberHills']
        ]

x_len = len(map)-1
y_len = len(map[0])-1

#biom
biom = {
    'CyberHills': {
        't':'CYBERHILLS',
        'e': True,
        'c': 50},
    'CyberVolcano': {
        't':'CYBERVOLCANO',
        'e': True,
        'c': 70},
    'CyberDesert': {
        't':'CYBERDESERT',
        'e': True,
        'c': 70},
    'CyberDuna': {
        't':'CYBERDUNA',
        'e': True,
        'c': 40},
    'CyberShop': {
        't':'CYBERSHOP',
        'e': False,
        'c': 0},
    'CyberTown': {
        't':'CYBERTOWN',
        'e': False,
        'c': 0},
    'CyberMountains': {
        't':'CYBERMOUNTAINS',
        'e': True,
        'c': 55},
    'CyberPlains': {
        't':'CYBERPLAINS',
        'e': True,
        'c': 20},
    'CyberForest': {
        't':'CYBERFOREST',
        'e': True,
        'c': 70},
    'CyberDragonCave': {
        't':'CYBERDRAGONCAVE',
        'e': True,
        'c': 100},
    'CyberMayor': {
        't':'CYBERMAYOR',
        'e': False,
        'c': 0},
    'CyberBridge': {
        't':'CYBERBRIDGE',
        'e': True},
        'c': 35,
    'CyberSea': {
        't':'CYBERSEA',
        'e': True,
        'c': 55},
    'CyberCity': {
        't':'CYBERCITY',
        'e': False,
        'c': 0},
    'CyberSwamp': {
        't':'CYBERSWAMP',
        'e': True,
        'c': 50},
    'CyberHospital': {
        't':'CYBERHOSPITAL',
        'e': False,
        'c': 0},
    'CyberCenter': {
        't':'CYBERCENTER',
        'e': False,
        'c': 0},
    'CyberHome': {
        't':'CYBERHOME',
        'e': False,
        'c': 0},
    }

current_position=map[x][y]
name_of_biom=biom[current_position]['t']
enemy_biom=biom[current_position]['e']
perc_enemy_biom=biom[current_position]['c']

enemiesList = ["CyberGoblin", "CyberOrc", "CyberSlime", "CyberDemon", "CyberOctopus", "CyberRat"]

mobs = {
    "CyberGoblin":{
        "hp":15,
        "atk":3,
        "gold":8
    },
    "CyberOrc":{
        "hp":26,
        "atk":5,
        "gold":15
    },
    "CyberSlime":{
        "hp":30,
        "atk":1,
        "gold":7
    },
    "CyberDragon":{
        "hp":60,
        "atk":8,
        "gold":100
    },
    "CyberDemon":{
        "hp":18,
        "atk":10,
        "gold":30
    },
    "CyberOctopus":{
        "hp":23,
        "atk":8,
        "gold":40
    },
    "CyberRat":{
        "hp":18,
        "atk":5,
        "gold":12
    },
    }

def write(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    time.sleep(0.4)

def greeting():
    write("Hi! This is a basic RPG games about CyberCavias!\n")
    write("You are a CyberCavia and you have to survive and try to kill the CyberDragon\n")
    write("This game is made by Andrea Falbo\n")
    write("Have fun!\n")

def printMenu():
    write("1: NEW GAME\n")
    write("2: LOAD GAME\n")
    write("3: HISTORY\n")
    write("4: QUIT GAME\n")

def clear():
    os.system("cls")

def draw():
    print("<------------------------------------------------>\n")

def printStats():
    write("Name: "+name+"\n")
    write("HP: "+str(HP) + "/" + str(HPMax)+"\n")
    write("ATK: " + str(ATK)+"\n")
    write("elisir: " + str(elisir)+"\n")
    write("gold: " + str(gold)+'\n')
    write("Coordinates: " +str(x)+",") 
    write(str(y)+'\n') 
   
def printMovement():
    write("0: SAVE AND QUIT\n")
    write("1: OVEST\n")
    write("2: SUD\n")
    write("3: EST\n")
    write("4: NORD\n")
    if pot>0:
        write("5: USE POTION(30HP)\n")
    if elisir>0:
        write("6: USE ELISIR(50HP)\n")
    if map[x][y] == 'CyberDragonCave' or map[x][y] == 'CyberShop' or map[x][y] == 'CyberMayor':
        write("7: ENTER\n")

def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(pot),
        str(elisir),
        str(gold),
        str(x),
        str(y),
        str(key)
    ]

    f = open('load.txt','w')

    for item in list:
        f.write(item + '\n')
    f.close()

def printHistory():
    write("Year:2025. The world has fallen to the powers of a dark cyber sect.\n")
    write("Your job is to pretend to be a cavia as you try to defeat your enemies.\n")
    write("Until you manage to kill the cyberdragon, you will not restore peace into the city.\n")
    write("Be brave.\n")   

def heal(amount):
    global HP
    if HP + amount < HPMax:
        HP+= amount
    else:
        HP = HPMax
    write(name + "'s HP refilled to "+str(HP)+"!\n")
    clear()

def battle():
    
    global fight, play, run, HP, pot, elisir, gold, boss
    write("Enemy encountered! "+ '\n')
    if not boss:
        enemy = random.choice(enemiesList)
    else:
        enemy = "CyberDragon"
    hpMob=mobs[enemy]['hp']
    hpmaxMob=hpMob
    atkMob = mobs[enemy]['atk']
    goldMob = mobs[enemy]['gold']

    while fight:
        clear()
        draw()
        write('Defeat the '+ enemy+'!'+ '\n')
        write(enemy + "'s HP: "+str(hpMob)+"/"+str(hpmaxMob)+ '\n')
        write(name + "'s HP: "+str(HP)+"/"+str(HPMax)+ '\n')
        write('Potions: '+str(pot)+ '\n')
        write('Elisir: '+str(elisir)+ '\n')
        draw()
        write('1: ATTACK'+ '\n')
        if pot >0:
            write('2: USE POTION (30 HP)'+ '\n')
        if elisir>0:
            write('3: USE ELISIR (50 HP)'+ '\n')
        draw()

        choice = input("> ")

        if choice == '1':
            if random.randint(0,100) <=30:
                write("You hit a critical damage!")
                hpMob-=2*ATK
                write(name+ ' dealt '+str(2*ATK)+' damage to the '+enemy+'.'+ '\n')
            write(name+ ' dealt '+str(ATK)+' damage to the '+enemy+'.'+ '\n')
            if hpMob>0:
                HP -=atkMob
                write(enemy+ ' dealt '+str(atkMob)+' damage to '+name+'.'+ '\n')
            input("> ")
        elif choice == '2':
            if pot>0:
                pot-=1
                heal(30)
                HP -=atkMob
                write(enemy+ ' dealt '+str(atkMob)+' damage to '+name+'.'+ '\n')
            else:
                write("You have no potions! \n")
            input("> ")   
        elif choice == '3':
            if elisir>0:
                elisir-=1
                heal(50)
                HP -=atkMob
                write(enemy+ ' dealt '+str(atkMob)+' damage to '+name+'.'+ '\n')
            else:
                write("You have no elisir! \n")
            input("> ")
        
            write(enemy + " defeated "+ name + "..."+ '\n')
            draw()
            fight=False
            play = False
            run = False
            write('GAME OVER'+ '\n')
            input('> ')
            quit()
        
        if hpMob <= 0 :
            write(name + " defeated "+ enemy + "!"+ '\n')
            draw()
            fight=False
            gold+=goldMob
            write("You've found " +str(goldMob) +" gold!"+ '\n')
            if random.randint(0,100)<30:
                pot+=1
                write("You've found a potion! Number of potion: "+str(pot)+ '\n')
            if enemy == "CyberDragon":
                draw()
                print("Congratulations, you've finished the game")
                boss = False
                play = False
                run = False
            input('> ')
    clear()

def shop():
    global buy,gold,pot,elisir,ATK

    while buy:
        clear()
        draw()
        write('Welcome to the shop!\n')
        draw()
        write('Gold: '+str(gold)+"\n")
        write('Potions: '+str(pot)+"\n")
        write('Elisir: '+str(elisir)+"\n")
        write('Attack: '+str(ATK)+"\n")
        draw()
        write('1: Buy Potion (30HP) for 5 gold\n')
        write('2: Buy Elisir (50HP) for 8 gold\n')
        write('1: Upgrade Weapon (+2ATK) for 10 gold\n')
        write('4: Leave the shop\n')
        draw()

        choice = input("> ")

        if choice == "1":
            if gold>=5:
                pot+=1
                gold-=5
                write("You've bought 1 potion! Number of potions: "+str(pot)+'\n')
            else:
                write("Not enough gold...")
                input("> ")
        if choice == "2":
            if gold>=8:
                elisir+=1
                gold-=8
                write("You've bought 1 elisir! Number of elisirs: "+str(elisir)+'\n')   
            else:
                write("Not enough gold...")
                input("> ")
        if choice == "3":
            if gold>=10:
                ATK+=2
                gold-=10
                write("You've upgraded your weapon! Damage: "+str(ATK)+'\n')   
            else:
                write("Not enough gold...")
                input("> ")   
        if choice == "4":
            buy=False 
    clear()        

def mayor():
    global speak, key
    clear()
    draw()
    write("Hello there, "+name+"!\n")
    if ATK < 10:
        write("You're not ready to face the Dragon now...\n")
        key=False
    elif not key:
        write("Oh,I saw that you trained a lot, interesting. You might want to take on the dragon now. Take this key that can take you to the Dragon's Cave\n")
        key=True
    else:
        write(name+", I already gave you the key, what are you waiting for?\n ")
    
    draw()
    write("1: Leave\n")
    choice = input("> ")

    if choice == '1':
        speak = False
    clear()

def dragon():

    global boss, key, fight

    key=False

    while boss:
        clear()
        draw()
        write("You've arrived to the cave of the Dragon. What will you do?\n")
        if key:
            write("1: Use Key\n")
        write("2: Turn back\n")
        draw()

        choice = input("> ")

        if choice == "1":
            if key:
                fight = True
                battle()
        elif choice == "2":
            boss = False

greeting()

while run :

    #menu 
    while menu :
        clear()
        if not history:
            printMenu()
        draw()

        
        if history:
            printHistory() 
            history = False
            choice =  "" 
            write("Type anything to continue ")
            input("> ")
        else:
            choice = input("> ") 

        if choice == "1" :
            write(">What's your name, CyberCavia? ")
            name = input('>')
            menu = False
            play = True

        elif choice == "2":
            try:
                f = open('load.txt','r')
                load_list = f.readlines()
                if len(load_list)== 9:
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    pot = int(load_list[3][:-1])
                    elisir = int(load_list[4][:-1])
                    gold = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = bool(load_list[8][:-1])
                    clear()
                    write('Welcome back, '+ name+'!\n')
                    write("Type 0 to continue\n")
                    input('> ')
                    menu = False
                    play = True
                else:
                    write("Corrupt save file!\n")
                    input('>')
            except OSError:
                    write("No loadable save file!\n")
                    input('>')
        elif choice == "3":
            history = True
        elif choice == "4":
            quit() 

    #play
    while play:
        save()
        clear()
        write("Location: "+ biom[map[x][y]]['t']+"\n")
        write("Are enemies present in this location? ")
        if biom[map[x][y]]['e']:
            write("Yes\n")
        else:
            write("No\n")
        if biom[map[x][y]]['e']:
            write("Percentage of spawning mobs: "+str(biom[map[x][y]]['c'])+'\n')
        if not standing:
            if biom[map[x][y]]['e']:
                if random.randint(0,100) <=biom[map[x][y]]['c']:
                    fight = True
                    battle()
                else:
                    write("You haven't encountered enemy! \n")
        
        if play: 
            draw()
            printStats()
            draw()
            printMovement()
            draw()

            dest = input("> ")

            if dest == "0":
                play = False
                menu = True
                save()
            elif dest == '1':
                if y>0:
                    y-=1
                    standing=False
                else:
                    y=y_len
                    standing=False
            elif dest == '2':
                if x<x_len:
                    x+=1
                    standing=False
                else:
                    x=0
                    standing=False
            elif dest == '3':
                if y<y_len:
                    y+=1
                    standing=False
                else:
                    y=0
                    standing=False
            elif dest == '4':
                if x>0:
                    x-=1
                    standing=False
                else:
                    x=x_len
                    standing=False
            elif dest == '5':
                pot-=1
                heal(30)
            elif dest == '6':
                elisir-=1
                heal(50)
            elif dest == '7':
                if map[x][y] == 'CyberShop':
                    write("You can buy potions and upgrade your weapons")
                    buy=True
                    shop()
                if map[x][y] == 'CyberMayor':
                    write("You can talk to the mayor to know if you can defeat the CyberDragon\n")
                    speak=True
                    mayor()
                if map[x][y] == 'CyberDragonCave':
                    write("You need 10 ATK Damage to enter the dungeon\n")
                    boss=True 
                    dragon() 
            else:
                standing=True
