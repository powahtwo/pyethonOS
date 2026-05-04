#commands are help, ver, notepad, infinity, changelog, dice, clculator
import art
import datetime
import random
print("|Type a command type help for cmds|\n"
      "▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")
while True:
    cmd = input("► ")
    match cmd:
        case "help":
            print("commands are: \n◇help,\n◇ver,\n◇notepad,\n◇infinity, \n◇changelog,\n◇dice,\n◇calculator")
        case "ver":
            print("pyethonOS 1.3")
        case "notepad":
            print("▪▪▪▪▪▪Notepad(Type exit to quit, type save to save)▪▪▪▪▪▪")
            while True:
                text = input("| ")
                if text == "exit": break
                if text == "save":
                    with open("textfile.txt", "a") as f:
                        f.write(text)
                    with open("textfile.txt") as f:
                        print(f.read())
        case "changelog":
            print("major update\n ❒now you can save notepad as a file\n ❒added betterdice\n ❒added time")
        case "dice":
            print("you rolled a...", random.randrange(1, 7))
        case "calculator":
            try:
                n1 = int(input("type 1st number: "))
                op = input("type 1 for add, 2 for subtract, 3 for multiply, 4 for divid: ")
                n2 = int(input("type 2nd number: "))
                result = (lambda n1, op, n2: 
                          n1 + n2 if op == '1' else 
                          n1 - n2 if op == '2' else 
                          n1 * n2 if op == '3' else 
                          n1 / n2 if op == '4' else "Invalid")(n1, op, n2)
                print("Result:", result)
            except ValueError:
                print("Invalid input")
        case "betterdice":
            r1 = int(input("minimum roll: "))
            r2 = int(input("maximun roll: "))
            print("you rolled a...", random.randrange(r1, r2))
        case "":
            print("►")
        case "time":
            time = datetime.datetime.now()
            print(time)
        case "logo":
        	art.tprint("pyethonOS",font='small')
        case _:
            print("invalid command")
#yippe it work