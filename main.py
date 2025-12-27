from src.blueprint import *

chitlist_1 = Chit(1)

def add_members():
    n = int(input("Enter the number of members: "))
    for i in range(n):
        chitlist_1.add_member()
def main():
    choice = 0
    while True:
        print("---")
        print("1. Add Members\n2. Show Members\n3. Ongoing month\n4. Lottery\n5. Set month\n444.Exit")
        print("---")
        choice = input()

        match(choice):
            case '1':
                add_members()
            case '2':
                chitlist_1.display_members()
            case '3':
                print("Current month is ", chitlist_1.month)
            case '4':
                chitlist_1.lottery()
            case '5':
                chitlist_1.set_month()
            case '444':
                break
            case _:
                print("Enter a valid number")

if __name__ == "__main__":
    main()
