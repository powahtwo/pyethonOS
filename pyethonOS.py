import random
helptext = "commands are help, ver, notepad, infinity, changelog, dice, calculator"
# this is a the user types on. \n is a new line
cmd = input("|Type a command type help for cmds|\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n► ")
if cmd not in helptext:
    print("invalid command")
elif "help" in cmd:
  print(helptext)
  print("re-run program to type new command↺ ")
elif "ver" in cmd:
  print("pyethonOS 1.2")
elif "notepad" in cmd:
    while True:
     text = input("| ")
    print(text)
elif "infinity" in cmd:
    while True:
     print("This will run forever.")
elif "changelog" in cmd:
    print("bug fixes\n ❒added calculator")
elif "commands" in cmd:
    print("invalid command")
elif "are" in cmd:
    print("invalid command")
elif "dice" in cmd:
    print("you rolled a...")
    print(random.randrange(1, 6))
elif "calculator" in cmd:
    print((lambda n1, op, n2: n1 + n2 if op == "1" else n1 - n2 if op == "2" else n1 * n2 if op == "3" else n1 / n2 if op == "4" else "Invalid")(float(input("type 1st number: ")), input("type 1 for add\ntype 2 for subtract\ntype 3 for multiply\ntype 4 for divide: "), float(input("type 2nd number: "))))

"""
 the old calculator code
    num1 = float(input("type 1st number: ")) 
calc1 = input("type 1 for add\ntype 2 for subtract\ntype 3 for multiply\ntype 4 for divide: ")
num2 = float(input("type 2nd number: "))
if calc1 == "1":
    print(num1 + num2)
elif calc1 == "2":
    print(num1 - num2)
elif calc1 == "3":
    print(num1 * num2)
elif calc1 == "4":
    print(num1 / num2)
"""