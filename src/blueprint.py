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
    def __init__(self):
        self.chitlists = []
    def create_chitlist(self):
        try:
            chit_amount = int(input("Enter 1 or 2 or 2.5 or 5: "))
            if not ChitManager.tally(chit_amount):
               return
        except ValueError:
            print("Invalid Value. Returning..")
            return
        chitlist = Chit(chit_amount)
        self.chitlists.append(chitlist)
        print("Chitlist created successfully, creation time: ", chitlist.creation_time)
    def display_chitlists(self):
        if not self.chitlists:
            print("No chitlists created.")
            return
        for i,chitlist in enumerate(self.chitlists):
            print(i+1,". chitlist ", chitlist.creation_time)
class Chit:
    total_chit_lists = 0
    def __init__(self,chit_amount):
        self.chit_amount = chit_amount
        self.chitlist = dict() #dict to store members: sequentially maps members from 1 to n in the order of creation
        self.creation_time = str(datetime.now()) #Stores Creation Time
        self.names_set = set() #Used for quickly checking if a name already exists.
        self.counter = 1 #Counts Members objects, use: sequentially store members
        self.winners_map = dict() #maps month (key) to winner (member object)
        self.not_winners = [] #Holds member objects who haven't won yet. Note: total months - current month = len(not_winners) is a necessary condition
        self.month = 1 #Keep tracks of current month
        Chit.total_chit_lists += 1
    def remove(self,i):
        self.not_winners[i] = self.not_winners[-1]
        if not len(self.not_winners) == 0:
            self.not_winners.pop()
        return
    def add_member(self):
        if len(self.chitlist) >= ChitManager.tally(self.chit_amount):
            print("Max Member Reached.. Returning..")
            return
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
        self.chitlist[self.counter] = member
        self.not_winners.append(member)
        self.counter  += 1
    def display_members(self):
        print("ChitList ", self.creation_time)
        if not self.chitlist:
            print("Chitlist is empty.")
            return
        for i in range(1,len(self.chitlist) + 1):
            print(i, " ", self.chitlist.get(i).name)
    def current_month_pay(self):
        chit_amount = self.chit_amount * 100000
        total_people = ChitManager.tally(self.chit_amount)
        if not self.chitlist:
            print("Chitlist is empty.")
            return
        for i in range(1,len(self.chitlist)+1):
            member = self.chitlist[i]
            if member in self.not_winners:
                current_month_pay = chit_amount/total_people
            else:
                current_month_pay = chit_amount/total_people + (chit_amount * 0.01)
            print(member.id, " ", member.name, ": ", current_month_pay)
    def display_creation_time(self):
        print(self.creation_time)
    def display_note(self, id):
        member = self.chitlist.get(id)
        if not member:
            print("Invalid ID")
            return
        print("Note for ", member.name, " is ", member.note)
    def add_note(self, id):
        member = self.chitlist.get(id)
        if not member:
            print("Invalid ID")
            return
        note = input(f"Enter note for {member.name}: ")
        member.note = note
    def lottery(self):
        if not self.not_winners:
            print("There are no members left to win.")
            return
        winner = choice(self.not_winners)
        print("Winner is \nId: ", winner.id, "Name: ", winner.name)
        i = self.not_winners.index(winner)
        self.remove(i)
        self.winners_map[self.month] = winner
        self.month += 1  
    def set_month(self):
        if not self.not_winners:
            print("There are no members left to win.")
            return
        for i in self.not_winners:
            print("ID: ", i.id, " Name ",i.name)
        print("Select a member")
        id = int(input("Enter id: "))
        winner = self.chitlist[id]
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
    chit_manager = ChitManager()
    chit_manager.create_chitlist()    
    chit_manager.create_chitlist()
    chit_manager.create_chitlist()    
    chit_manager.display_chitlists()