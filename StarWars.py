import sys
import time
import numpy as np
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
class StarWars:
    def __init__(self, name, types, moves, EVs, health='==================='):
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE'] 
        self.health = health
        self.bars = 20
    def fight(self, StarWars2):
        print("-----STAR WARS BATTLE-----")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3*(1+np.mean([self.attack,self.defense])))
        print("\nVS")
        print(f"\n{StarWars2.name}")
        print("TYPE/", StarWars2.types)
        print("ATTACK/", StarWars2.attack)
        print("DEFENSE/", StarWars2.defense)
        print("LVL/", 3*(1+np.mean([StarWars2.attack,StarWars2.defense])))
        time.sleep(2)
        version = ['Strongest Force Battling Meditation','Duelist and Redemption Force', 'Extremely Strongest Telekinetic Force Combat']
        for i,k in enumerate(version):
            if self.types == k:
                if StarWars2.types == k:
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts not very effective...'
                if StarWars2.types == version[(i+1)%3]:
                    StarWars2.attack *= 2
                    StarWars2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts super effective!'
                if StarWars2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    StarWars2.attack /= 2
                    StarWars2.defense /= 2
                    string_1_attack = '\nIts super effective!'
                    string_2_attack = '\nIts not very effective...'
        while (self.bars > 0) and (StarWars2.bars > 0):
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{StarWars2.name}\t\tHLTH\t{StarWars2.health}\n")
            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)
            StarWars2.bars -= self.attack
            StarWars2.health = ""
            for j in range(int(StarWars2.bars+.1*StarWars2.defense)):
                StarWars2.health += "="
            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{StarWars2.name}\t\tHLTH\t{StarWars2.health}\n")
            time.sleep(.5)
            if StarWars2.bars <= 0:
                delay_print("\n..." + StarWars2.name + ' fainted.')
                break
            print(f"Go {StarWars2.name}!")
            for i, x in enumerate(StarWars2.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{StarWars2.name} used {StarWars2.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack) 
            self.bars -= StarWars2.attack
            self.health = ""     
            for j in range(int(self.bars+.1*self.defense)):
                self.health += "=" 
            time.sleep(1)  
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{StarWars2.name}\t\tHLTH\t{StarWars2.health}\n")
            time.sleep(.5)
            if self.bars <= 0:
                delay_print("\n..." + self.name + ' fainted.') 
                break   
        delay_print(f"\n{StarWars2.name} Loss The STAR WARS Battle.\n")
        delay_print(f"\n{self.name} Wins The STAR WARS Battle.\n")
if __name__ == '__main__':
    Luke_Skywalker = StarWars('Luke_Skywalker', 'Strongest Force Battling Meditation', ['Force Blast', 'Lightning', 'Telekinesis', 'Force Projection'], {'ATTACK':12, 'DEFENSE': 8})
    Anankin_Skywalker = StarWars('Anankin_Skywalker', 'Duelist and Redemption Force' , ['Jedi Reflex', 'Force Taming', 'Cybernetic Hand', 'Sith LightSaber Attacking'],{'ATTACK': 10, 'DEFENSE':10})
    Darth_Vader = StarWars('Darth_Vader', 'Extremely Strongest Telekinetic Force Combat', ['Jedi Reflex', 'Sith LightSaber Attacking', 'Telekinesis Force Attacking', 'Rage Focusing'],{'ATTACK':8, 'DEFENSE':12})

    Rey_Skywalker = StarWars('Rey_Skywalker', 'Strongest Force Battling Meditation', ['Force Lightning', 'Psychic Force Attack', 'LightSaber Attacking', 'Force Juggernaut'],{'ATTACK':2, 'DEFENSE':4})
    Qui_Gon_Jinn = StarWars('Qui-Gon Jinn', 'Duelist and Redemption Force', ['Jedi Reflex', 'Force Taming', 'Cybernetic Hand', 'Force Projection'],{'ATTACK':4, 'DEFENSE':2})
    Obi_Wan_Kenobi = StarWars('Obi_Wan_Kenobi', 'Extremely Strongest Telekinetic Force Combat', ['Telekinesis Force Hypnotism', 'Telekinesis Force Attacking', 'Force Blast By Meditating', 'Sith LightSaber Attacking'],{'ATTACK': 3, 'DEFENSE':3})

    Kylo_Ren = StarWars('Kylo_Ren\t', 'Strongest Force Battling Meditation', ['Force Jumping', 'Psychic Force Attack', 'LightSaber Attacking', 'Force Juggernaut'],{'ATTACK':4, 'DEFENSE':6})
    Han_Solo = StarWars('Han_Solo', 'Duelist and Redemption Force', ['Rapid Shooting', 'Heavy Blaster Pistol', 'Force Blast', 'Force Projection'],{'ATTACK':6, 'DEFENSE':5})
    Yoda = StarWars('Yoda', 'Extremely Strongest Telekinetic Force Combat', ['Force Taming', 'Jedi Reflex', 'Telekinesis Force Attacking', 'Sith LightSaber Attacking'],{'ATTACK': 5, 'DEFENSE':5})
    print("Choose The Jedi Warriors By Pressing Number According To List Below:-")
    print("1.Luke Skywalker")
    print("2.Anankin Skywalker")
    print("3.Darth Vader")
    print("4.Princess Leia")
    print("5.Obi Wan Kenobi")
    print("6.Rey Skywalker")
    print("7.Han Solo")
    print("8.Yoda")
    print("9.Kylo Ren")
    Opponent1=int(input("The First Opponent For Star Wars Battle Choose From Above List By Pressing The Number:"))
    Opponent2=int(input("The First Opponent For Star Wars Battle Choose From Above List By Pressing The Number: "))
    if(Opponent1==1):
        Opponent1st=Luke_Skywalker
    elif(Opponent1==2):
        Opponent1st=Anankin_Skywalker
    elif(Opponent1==3):
        Opponent1st=Darth_Vader
    elif(Opponent1==4):
        Opponent1st=Qui_Gon_Jinn
    elif(Opponent1==5):
        Opponent1st=Obi_Wan_Kenobi
    elif(Opponent1==6):
        Opponent1st=Rey_Skywalker
    elif(Opponent1==7):
        Opponent1st=Han_Solo
    elif(Opponent1==8):
        Opponent1st=Yoda
    elif(Opponent1==9):
        Opponent1st=Kylo_Ren
    else:
        print("No Jedi Warrior According To Chosen Number")
    if(Opponent2==1):
        Opponent2nd=Luke_Skywalker
    elif(Opponent2==2):
        Opponent2nd=Anankin_Skywalker
    elif(Opponent2==3):
        Opponent2nd=Darth_Vader
    elif(Opponent2==4):
        Opponent2nd=Qui_Gon_Jinn
    elif(Opponent2==5):
        Opponent2nd=Obi_Wan_Kenobi
    elif(Opponent2==6):
        Opponent2nd=Rey_Skywalker
    elif(Opponent2==7):
        Opponent2nd=Han_Solo
    elif(Opponent2==8):
        Opponent2nd=Yoda
    elif(Opponent2==9):
        Opponent2nd=Kylo_Ren
    else:
        print("No Jedi Warrior According To Chosen Number")
    Opponent1st.fight(Opponent2nd) 