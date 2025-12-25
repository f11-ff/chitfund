class ChitManager:
    pass
class Chit:
    pass
class Member:
    def __init__(self,name,note = ""):
        self.name = name;
        self.note = note;
    def display_name(self):
        print("Name: ", self.name)
    def display_note(self):
        if not self.note:
            print("No note")
        print("Note: ",self.note)
    def update_note(self,note):
        print("Updating note to ", note)
        self.note = note
    

