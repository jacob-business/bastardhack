#omg i can't believe i'm doing computer programming For Fun .i hate myself. not really its fine
import random
import math

print("Bastard Hack Character Generator version 01. 12.19.19")
print()
#random or not input str("")
    #If random = Yes

STATS = {}
MOD={}
#otherstats:
ATTACK_melee=0
ATTACK_ranged=0
DEFENSE=0
ARMOR=0
DEFENSE=0
ATTACK_melee=0
ATTACK_ranged=0
TRAITS=[]

def GenerateName():
    NameFile=open("Names.txt","r")
    NameList=NameFile.readlines()
    name=NameList[random.randint(0,len(NameList)-1)]
    return name
def GenerateStats(STATS,MOD):
    STATS['STR']=random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
    MOD['STR']=(STATS['STR']//3)-3
    STATS['DEX']=random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
    MOD['DEX']=(STATS['DEX']//3)-3
    STATS['CON']=random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
    MOD['CON']=(STATS['CON']//3)-3
    STATS['INT']=random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
    MOD['INT']=(STATS['INT']//3)-3
    STATS['WIS']=random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
    MOD['WIS']=(STATS['WIS']//3)-3
    STATS['CHA']=random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
    MOD['CHA']=(STATS['CHA']//3)-3
    for stat in STATS:
        if MOD[stat]<0:
            print(stat, STATS[stat], MOD[stat])
        else:
            print(stat, " ", STATS[stat], " +", MOD[stat], sep='')
#what info should ur race hold? maybe each race = dictionary with the name being the key and the values being a mixed list of number stat bonuses and string powers etc.

def GenerateRace():
    num=random.randint(1,20)
    Racelist = ["Human","Halfling","Elf","Dwarf","Tiefling","Gnome","Goblin"]
    Unusual = ["Undead","Frogman","Lizardman","Kobold","Orc","Troll"]
    if num>=1 and num<=10:
        RACE=Racelist[0]
    if num>=11 and num<=12:
        RACE=Racelist[1]
    if num>=13 and num<=14:
        RACE=Racelist[2]
    if num>=15 and num<=16:
        RACE=Racelist[3]
    if num==17:
        RACE=Racelist[4]
    if num==18:
        RACE=Racelist[5]
    if num==19:
        RACE=Racelist[6]
    if num==20:
        num2=random.randint(0,5)
        RACE=Unusual[num2]
    return RACE

def GenerateClass():
#should you store the info for classes as actual Classes? what info does class give: HD, Magic Dice, Ability/Trait,Curses, Allegiances, etc.
    classlist=["Witch","Cleric","Cultist","Wizard","Warlock","Druid","Wanderer","Fighter","Knight","Barbarian","Rogue","Assassin"]
    STARTINGCLASS=classlist[random.randint(0,11)]
    return STARTINGCLASS

STARTINGCLASS=GenerateClass()

print ("Name:", GenerateName())
print (GenerateRace(), STARTINGCLASS)
GenerateStats(STATS,MOD)

DEFENSE=DEFENSE+ARMOR+MOD["DEX"]
ATTACK_melee=ATTACK_melee+MOD["STR"]
ATTACK_ranged=ATTACK_ranged+MOD["WIS"]


print("MELEE ATTACK", ATTACK_melee)
print("RANGED ATTACK", ATTACK_ranged)
print("DEFENSE", DEFENSE)
