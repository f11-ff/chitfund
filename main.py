from src.blueprint import *

chit_manager = ChitManager()
def add_members(chitlist):
    n = int(input("Enter the number of members: "))
    for i in range(n):
        chitlist.add_member()

def chitlist_operations(chitlist):
    while True:
        print("---")
        print("1. Add Members\n2. Show Members\n3. Ongoing month\n4. Lottery\n5. Set month\n6. View creation time\n7. View outstading fees\n444.Exit")
        print("---")
        choice = input()

        match(choice):
            case '1':
                add_members(chitlist)
            case '2':
                chitlist.display_members()
            case '3':
                print("Current month is ", chitlist.month)
            case '4':
                chitlist.lottery()
            case '5':
                chitlist.set_month()
            case '6':
                chitlist.display_creation_time()
            case '7':
                chitlist.current_month_pay()
            case '444':
                return
            case _:
                print("Enter a valid number")


def main():
    choice = 0
    while True:
        print("---")
        print("1. Create ChitList\n2. Display Chitlists\n3. Chitlist Ops.\n444.Exit")
        print("---")
        choice = input()
        match(choice):
            case '1':
                chit_manager.create_chitlist()
            case '2':
                chit_manager.display_chitlists()
            case '3':
                if not chit_manager.display_chitlists():
                    print("There is no list please make one.")
                    continue
                i = int(input("Enter an id (left index is id): "))
                chitlist_operations(chit_manager.chitlists[i-1])
            case '444':
                break


if __name__ == "__main__":
    main()
