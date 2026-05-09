#commands are help, ver, notepad, infinity, changelog, dice, calculator
import tqdm
import rich
import art
import datetime
import random
print("|Type a command type help for cmds|\n"
      "▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")
while True:
    cmd = input("► ")
    match cmd:
        case "help":
            print("commands are: \n◇help,\n◇ver,\n◇notepad, \n◇changelog,\n◇dice,\n◇calculator")
        case "ver":
            print("pyethonOS 1.4")
        case "notepad":
            print("▪▪▪▪▪▪Notepad(Type exit to quit, type save to save)▪▪▪▪▪▪")
            while True:
                text2 = []
                text = input("| ")
                if text == "exit": break
                if text == "save":
                    with open("textfile.txt", "a") as f:
                        f.write("\n".join(text2))
                    with open("textfile.txt") as f:
                        print(f.read())
                        rich.print("[bold Cyan]saved :D")
        case "changelog":
            print("major update\n ❒now you can save notepad as a file\n ❒added betterdice\n ❒added time\n ❒added some secret commands try to find them")
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
            try:
            	r1 = int(input("minimum roll: "))
            	r2 = int(input("maximun roll: "))
            	print("you rolled a...", random.randrange(r1, r2 + 1))
            except ValueError:
            	rich.print("[bold Green]yep thats a error")
        case "":
            print("►")
        case "time":
            time = datetime.datetime.now()
            print(time)
        case "logo":
        	art.tprint("pyethonOS",font='small')
        case "richtext":
        	rich.print("Hello [bold Blue]im blue,",":smiley:" )
        case "bar":
        	for i in tqdm.tqdm(range(100000000)):
        		...
        case "sudo":
        	rich.print("[bold Red]what did you think was going to happen this isn't linux")
        case "SELECT":
        	rich.print("[bold Red]bro thinks this is sql:skull:]")
        case "ID":
        	rich.print("[bold Red]bro thinks this is sql:skull:]")
        case _:
            print("invalid command")
#yippe it workt