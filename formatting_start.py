from datetime import datetime

def main():
    # Date Formatting
    now = datetime.now()
    print(now.strftime("%a %d %B, %Y"))
    # print(now.strftime()) # takes  a string arg that takes one or more codes as placeholders

    print(now.strftime("Locale Time %c"))
    print(now.strftime("Locale Time %x"))
    print(now.strftime("Locale Time %X"))


    print(now.strftime("Current Time: %I:%M:%S %p"))
    print(now.strftime("24-hour Time: %H:%M"))



if __name__ == "__main__":
    main()