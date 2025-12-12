from random import randint

class Member:
    def __init__(self,name,chit_id,month_taken,note):
        self.name = name
        self.chit_id = chit_id # 1- 1 lakh 2- 2 lakh 3- 5 lakh
        self.month_taken = month_taken
        self.note = note
    
    def display_note(self):
        print(f"{self.name}: {self.note}")
    def update_note(self):
        new_note = input("Enter a note: ")
        self.note = new_note
        print("Updated")

class Chitfund:
    month = 0
    def __init__(self,chit_id):
        self.chit_id = chit_id
        self.chit_list = []
        self.names = set()
    def create_member(self):
        while True:
            name = input("Enter name: ")
            if name in self.names:
                print("Name exists! Please check the name and/or modify it slightly. Thank you.")
            else:
                self.names.add(name)
                break
        member = Member(name,self.chit_id,-1,"")
        self.chit_list.append(member)
    def display_members(self):
        print("Members:")
        for i,member in enumerate(self.chit_list):
            print(f"{i+1}.", member.name)
    def lottery(self):
        winner = randint(0,19)
        print("Name: ", self.chit_list[winner].name)
