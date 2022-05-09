from time import sleep

line = True
file = open("README.md", "r")   # Open the file to read ("r"

while line:
    line = file.read()          # Read the file and save it in a variable
    print(line)                 # Print to the console
    sleep(1)                    # Print to the console every second