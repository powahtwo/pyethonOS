import random
helptext = "commands are help, ver, notepad, calculator, infinity, clitest, changelog, dice"
# this is what the user types on. \n is a new line
cmd = input("|Type a command type help for cmds|\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n► ")
if cmd not in helptext:
    print("invalid command")
elif "help" in cmd:
  print(helptext)
  print("re-run program to type new command↺ ")
elif "ver" in cmd:
  print("pyethonOS 1.0")
elif "notepad" in cmd:
    while True:
     text = input("| ")
    print(text)
elif "infinity" in cmd:
    while True:
     print("This will run forever.")
elif "changelog" in cmd:
    print("full release\n ❒refreshed look\n ❒bug fixes\n ❒re-named to pyethonOS")
elif "commands" in cmd:
    print("invalid command")
elif "are" in cmd:
    print("invalid command")
elif "clitest" in cmd:
    print('\033[?25h', end="▮") # Show cursor
    print('\033[?25l', end="") # Hide cursor
elif "dice" in cmd:
    print(random.randrange(1, 6))
elif "calculator" in cmd:
    def add(n1, n2): return n1 + n2
def sub(n1, n2): return n1 - n2
def mul(n1, n2): return n1 * n2
def div(n1, n2): return n1 / n2

print("Select:\n 1.add\n 2.subtract\n 3.multiply\n 4.divide\n")
sel = int(input("Select (1-4): "))
n1 = int(input("First number: "))
n2 = int(input("Second number: "))

if sel == 1: print(n1 + n2)
elif sel == 2: print(n1 - n2)
elif sel == 3: print(n1 * n2)
elif sel == 4: print(n1 / n2)
else: print("invalid number")
