import random
import cursor
helptext = "commands are help, ver, notepad, infinity, clitest, changelog, dice"
# this is what the user types on. \n is a new line
cmd = input("|Type a command type help for cmds|\n▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪\n► ")
if cmd not in helptext:
    print("invalid command")
elif "help" in cmd:
  print(helptext)
  print("re-run program to type new command↺ ")
elif "ver" in cmd:
  print("pyethonOS 1.0.1")
elif "notepad" in cmd:
    while True:
     text = input("| ")
    print(text)
elif "infinity" in cmd:
    while True:
     print("This will run forever.")
elif "changelog" in cmd:
    print("bug fixes\n ❒removed calculator,qmight be back soon")
elif "commands" in cmd:
    print("invalid command")
elif "are" in cmd:
    print("invalid command")
elif "clitest" in cmd:
	cursor.hide()
	cursor.show()
elif "dice" in cmd:
    print("you rolled a...")
    print(random.randrange(1, 6))
    