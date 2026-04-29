#commands are help, ver, notepad, infinity, changelog, dice, calculator
import random
print("|Type a command type help for cmds|\n"
      "▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")
while True:
    cmd = input("► ")
    match cmd:
        case "help":
            print("commands are: \n◇help,\n◇ver,\n◇notepad,\n◇infinity, \n◇changelog,\n◇dice,\n◇calculator")
        case "ver":
            print("pyethonOS 1.2.1")
        case "notepad":
            print("▪▪▪▪▪▪Notepad(Type exit to quit)▪▪▪▪▪▪")
            while True:
                text = input("| ")
                if text == "exit": break
        case "infinity":
                while True:
                    print("this will run forever")
        case "changelog":
            print("bug fixes\n ❒now you can finally use as many commands as you want without re-running the program\n ❒changed some ui")
        case "dice":
            print("you rolled a...", random.randrange(1, 6))
        case "calculator":
            try:
                n1 = float(input("type 1st number: "))
                op = input("type 1 for add, 2 for subtract, 3 for multiply, 4 for divid: ")
                n2 = float(input("type 2nd number: "))
                result = (lambda n1, op, n2: 
                          n1 + n2 if op == '1' else 
                          n1 - n2 if op == '2' else 
                          n1 * n2 if op == '3' else 
                          n1 / n2 if op == '4' else "Invalid")(n1, op, n2)
                print("Result:", result)
            except ValueError:
                print("Invalid input")
        case "":
            print("►")
        case _:
            print("invalid command")
#yippe it work