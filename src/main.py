from blueprint import *

"""
features:
create member
Display members
Ongoing Month
lottery
"""

chitlist_1 = Chitfund(1)

def add_members():
    n = int(input("Enter the number of members: "))
    for i in range(n):
        chitlist_1.create_member()
def main():
    choice = 0
    while True:
        print("---")
        print("1. Add Members\n2. Show Members\n3. Ongoing month\n4. Lottery\n444.Exit")
        print("---")
        choice = input()

        match(choice):
            case '1':
                add_members()
            case '2':
                chitlist_1.display_members()
            case '3':
                print("Current month is ", Chitfund.month)
            case '4':
                chitlist_1.lottery()
            case '444':
                break
            case _:
                print("Enter a valid number")

if __name__ == "__main__":
    main()
