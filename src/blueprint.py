from datetime import datetime
from random import choice


class ChitManager:
    @staticmethod
    def tally(chit_amount):
        if(chit_amount == 1 or chit_amount == 2):
            return 20 #Standard for my use case
        elif(chit_amount == 5 or chit_amount == 2.5):
            return 25
        else:
            return 0
class Chit:
    total_chit_lists = 0
    def __init__(self,chit_amount):
        self.chit_amount = chit_amount
        self.chit_list = dict()
        self.creation_time = str(datetime.now())
        self.names_set = set() #Used for quickly checking if a name already exists.
        self.counter = 1 #Counts Members objects, sequentially store members
        self.winners_map = dict() #maps month (key) to winner (member object)
        self.not_winners = [] #Holds member objects who haven't won yet. Note: total months - current month = len(not_winners) is a necessary condition
        self.month = 1
        Chit.total_chit_lists += 1
    def remove(self,id):
        self.not_winners[id] = self.not_winners[-1]
        if not len(self.not_winners) == 0:
            self.not_winners.pop()  
        return
    def add_member(self):
        while True:
            name = input("Enter name: ")
            if name in self.names_set:
                print("Name exists! Please check the name and/or modify it.")
            else:
                self.names_set.add(name)
                break
        print("Adding Member ", name)
        member = Member(name)
        member.id = self.counter
        self.chit_list[self.counter] = member
        self.not_winners.append(member)
        self.counter  += 1
    def display_members(self):
        print("ChitList ", self.creation_time)
        for i in range(1,len(self.chit_list) + 1):
            print(i, " ", self.chit_list.get(i).name)
    def current_month_pay(self):
        self.display_members()
        for i in self.chit_list:
            if i in self.not_winners:
                current_month_pay = (self.chit_amount * 100000) / ChitManager.tally(self.chit_amount)
            else:
                current_month_pay = ((self.chit_amount * 100000) / ChitManager.tally(self.chit_amount)) * 1.01
            print(i.id, " ", i.name, ": ", current_month_pay)
    def display_creation_time(self):
        print(self.creation_time)
    def display_note(self, id):
        member = self.chit_list.get(id)
        if not member:
            print("Invalid")
            return
        print("Note for ", member.name, " is ", member.note)
    def add_note(self, id):
        member = self.chit_list.get(id)
        if not member:
            print("Invalid id")
            return
        note = input(f"Enter note for {member.name}: ")
        member.note = note
    def lottery(self):
        winner = choice(self.not_winners)
        print("Winner is \nId: ", winner.id, "Name: ", winner.name)
        i = self.not_winners.index(winner)
        self.remove(i)
        self.winners_map[self.month] = winner
        self.month += 1  
    def set_month(self):
        for i in self.not_winners:
            print("ID: ", i.id, " Name ",i.name)
        print("Select a member")
        id = int(input("Enter id: "))
        winner = self.chit_list[id]
        i = self.not_winners.index(winner)
        self.remove(i)
        print("Set ",winner.name, " as winner")
        self.winners_map[self.month] = winner
        self.month += 1

class Member:
    def __init__(self,name,note = ""):
        self.name = name
        self.note = note
        self.id = -1
        self.creation_time = str(datetime.now())


if __name__ == "__main__": #Temporary: Testing/Debugging 
    chitlist = Chit(1)
    chitlist.add_member()
    chitlist.add_member()
    chitlist.add_member()
    chitlist.add_member()
    chitlist.add_member()

    #chitlist.display_creation_time()
    chitlist.display_members()
    #chitlist.add_note(1)
    #chitlist.display_note(1)
    chitlist.lottery()
    print([i.name for i in chitlist.not_winners])
    chitlist.lottery()
    print([i.name for i in chitlist.not_winners])

    chitlist.lottery()
    print([i.name for i in chitlist.not_winners])

    chitlist.lottery()
    print([i.name for i in chitlist.not_winners])


    print(len(chitlist.not_winners))