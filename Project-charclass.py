from random import randint
import random
#parent class for race holding the base stats of the object
class race:
    def __init__(self):
        self.Damage = random.randint(25,30)
        self.Swiftness = random.randint(19,23)
        self.Health = random.randint(160,180)
        self.Armor = random.randint(60,75)
    def getDamage(self):
        return self.Damage
    def getSwiftness(self):
        return self.Swiftness
    def getHealth(self):
        return self.Health
    def getArmor(self):
        return self.Armor
#child classes of race that inherit and change the base stats
class Human(race):
    def __init__(self):
        super().__init__()
        self.Health += 20
class Elf(race):
    def __init__(self):
        super().__init__()
        self.Swiftness += 10
class Dwarf(race):
    def __init__(self):
        super().__init__()
        self.Damage += 5
#parent class for the classes holding the base stats of the object
class classs:
    def __init__(self):
        constantbase = 5
        self.Damage = constantbase
        self.Swiftness = constantbase
        self.Health = constantbase
        self.Armor = constantbase
    def getDamage(self):
        return self.Damage
    def getSwiftness(self):
        return self.Swiftness
    def getHealth(self):
        return self.Health
    def getArmor(self):
        return self.Armor
#child classes of class that inherit and change the base stats
class Archer(classs):
    def __init__(self):
        super().__init__()
        self.Swiftness += 10
        self.Health -= 15
class Soldier(classs):
    def __init__(self):
        super().__init__()
        self.Health += 20
        self.Swiftness -= 9
#parent class for the weapons holding the base stats
class weapon():
    def __init__(self):
        self.Damage = 8
        self.Swiftness = 10
        self.Health = 30
        self.Armor = 10
    def getDamage(self):
        return self.Damage
    def getSwiftness(self):
        return self.Swiftness
    def getHealth(self):
        return self.Health
    def getArmor(self):
        return self.Armor
#child class of weapon that inherits the base stats and changes them
class rangew(weapon):
    def __init__(self):
        super().__init__()
        self.Damage -= 3
        self.Swiftness += 5
#child classes of rangew that inherits the base stats and changes them
class Bow(rangew):
    def __init__(self):
        super().__init__()
        self.Damage -= 1
        self.Swiftness += 2
class Crossbow(rangew):
    def __init__(self):
        super().__init__()
        self.Damage += 3
        self.Swiftness -= 6
#child class of weapon that inherits the base stats and changes them
class closew(weapon):
    def __init__(self):
        super().__init__()
        self.Damage += 4
        self.Swiftness -= 6
#child classes of closew that inherits the base stats and changes them
class Club(closew):
    def __init__(self):
        super().__init__()
        self.Damage += 4
        self.Swiftness -= 4
class Sword(closew):
    def __init__(self):
        super().__init__()
        self.Damage += 1
        self.Swiftness += 3
#class that creates your character after asking you whatrace,class and weapon you want
class Character:
    def __init__(self,race,classs,weapon):
        self.Damage = race.getDamage() + classs.getDamage() + weapon.getDamage()
        self.Swiftness = race.getSwiftness() + classs.getSwiftness() + weapon.getSwiftness()
        self.Health = race.getArmor() + classs.getArmor() + weapon.getArmor() + race.getHealth() + classs.getHealth() + weapon.getHealth()
        print("Damage is: ", self.Damage,"\nSwiftness is: ",self.Swiftness,"\nHealth is: ",self.Health)
        global Statslist
        Statslist = [self.Damage,self.Swiftness,self.Health]
#parent class of monster that contains the base stats
class Monsters:
    def __init__(self):
        self.Damage = 25
        self.Swiftness = 40
        self.Health = 40
        self.Armor = 15
    def getDamage(self):
        return self.Damage
    def getSwiftness(self):
        return self.Swiftness
    def getHealth(self):
        return self.Health
    def getArmor(self):
        return self.Armor
#child classes of monster that inherit the base stats and change them
class Zombie(Monsters):
    def __init__(self):
        super().__init__()
        self.Damage += 6
class Spider(Monsters):
    def __init__(self):
        super().__init__()
        self.Swiftness += 10
class Ogre(Monsters):
    def __init__(self):
        super().__init__()
        self.Health += 10
#class that creates the monsters in the game
class Monster:
    def __init__(self,race):
        self.Damage = race.getDamage()
        self.Swiftness = race.getSwiftness()
        self.Health = race.getHealth() + race.getArmor()
        print("Damage is: ", Damage,"\n","Swiftness is: ",Swiftness,"\n","Health is: ",Health)
        global Statslist
        Statslist = [Damage,Swiftness,Health,Armor]


'''combat system'''
#code that calls and builds the 3 monsters who are all objects
listofmonst = [Zombie(),Spider(),Ogre()]
myMonster1 = listofmonst[random.randint(0,2)]
myMonster2 = listofmonst[random.randint(0,2)]
myMonster3 = listofmonst[random.randint(0,2)]
#Lets the player choose his character class,race and
racechoice = input("1: Human \n2: Elf \n3: Dwarf")
if racechoice == '1':
    raceactual = Human()
elif racechoice == '2':
    raceactual = Elf()
else:
    raceactual = Dwarf()

classchoice = input("1: Archer \n2: Soldier")
if classchoice == '1':
    classactual = Archer()
else:
    classactual = Soldier()


weaponchoice = input("1: Bow \n2: Crossbow \n3: CLub \n4: Sword")
if weaponchoice == '1':
    weaponactual = Bow()
elif weaponchoice == '2':
    weaponactual = Crossbow()
elif weaponchoice == '3':
    weaponactual = Club()
else:
    weaponactual = Sword()




#calls the character
myPlayer1 = Character(raceactual,classactual,weaponactual)

healthpots = 2
global healthlost
healthlost = 0
global points
points = 0
def fight(monstnumb,healthlost,myPlayer1):
    global points
    global healthpots
    global monstersalive
    alive = True
    print("Your enemies stats are: \nDamage:",monstnumb.Damage," \nSwiftness:",monstnumb.Swiftness," \nHealth:",monstnumb.Health)
    myPlayer1.Health += healthlost
    healthtrue = myPlayer1.Health
    while alive == True and myPlayer1.Health > 0:
        fightchoice = int(input("\n \nIf you want to attack type: 1 \nIf you want to use a health pot type: 2"))
        if fightchoice == 1:
            if myPlayer1.Swiftness > monstnumb.Swiftness:
                monstnumb.Health -= myPlayer1.Damage
                print("your enemies health is at",monstnumb.Health)
                if monstnumb.Health > 0:
                    myPlayer1.Health -= monstnumb.Damage
                print("your health is at",myPlayer1.Health)
            else:
                myPlayer1.Health -= monstnumb.Damage
                print("your health is at",myPlayer1.Health)
                if myPlayer1.Health > 0:
                    monstnumb.Health -= myPlayer1.Damage
                print("your enemies health is at",monstnumb.Health)
        else:
            if healthpots > 0:
                healthpots -= 1
                myPlayer1.Health += 65
                myPlayer1.Damage += 9
                myPlayer1.Health -= monstnumb.Damage
                print("your health is at",myPlayer1.Health)
            else:
                print("sorry, you have no healthpots left")
        if monstnumb.Health < 1:
                    points += 5
                    monstersalive -= 1
                    alive = False
                    break
    healthlost += (healthtrue - myPlayer1.Health)
difficultymonst = int(input('''Easy: 1
Medium: 2
Hard: 3
Difficulty level:'''))
monstersalive = 3
arrayofmonst = [myMonster1,myMonster2,myMonster3]
for i in range(len(arrayofmonst)):
    if difficultymonst == 2:
        arrayofmonst[i - 1].Health += 60
    elif difficultymonst == 3:
        arrayofmonst[i - 1].Damage += 20
        arrayofmonst[i - 1].Health += 65
while myPlayer1.Health > 0:
    if monstersalive == 3:
        print("This is your first fight out of 3:")
        fight(myMonster1,healthlost,myPlayer1)
    elif monstersalive == 2:
        print("This is your second fight out of 3:")
        fight(myMonster2,healthlost,myPlayer1)
    elif monstersalive == 1:
        print("This is your final fight out of 3:")
        fight(myMonster3,healthlost,myPlayer1)
    else:
        if difficultymonst == 1:
            print("Well done, you defeated all 3 monsters. You scored",points,"points")
        elif difficultymonst == 2:
            points = points * 2
            print("Well done, you defeated all 3 monsters. You scored",points,"points")
        else:
            points = points * 3
            print("Well done, you defeated all 3 monsters. You scored",points,"points")
        break
if myPlayer1.Health < 1:
    if difficultymonst == 1:
        print("you didnt kill all the monsters. You scored",points,"points.There was",monstersalive,"monsters left.")
    elif difficultymonst == 2:
        points = points * 2
        print("you didnt kill all the monsters. You scored",points,"points.There was",monstersalive,"monsters left.")
    else:
        points = points * 3
        print("you didnt kill all the monsters. You scored",points,"points.There was",monstersalive,"monsters left.")
