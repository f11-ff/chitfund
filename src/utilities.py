
def valid_20(num):

    while True:
        if not (1 <= num <= 20):
            print("Invalid")
            num = int(input("Enter a valid number: (1 to 20)"))
        else:
            break
    return num
