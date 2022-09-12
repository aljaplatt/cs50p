import sys
import random

from pyfiglet import Figlet
figlet = Figlet()

# get cli args
# Zero if the user would like to output text in a random font.
# only arg is file name - no font specified
if len(sys.argv) == 1:
    isRandom = True
# if font specified then len should == 3
#? 1. filename 2. -f or --font 3.fontname
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    isRandom = False
else:
    print("Invalid usage")
    sys.exit(1)

if isRandom == False:
    try:
        #You can set the font with code like this, wherein font is taken from the cli args[2]
        font = figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    #You can set the font with code like this, wherein f is the font’s name as a str:
    font = random.choice(figlet.getFonts())

#You can then get a list of available fonts with code like this:
# figlet.getFonts()


# Get user input
text = input("Input: ")

#And you can output text in that font with code like this, wherein msg is that text as a str:
output = figlet.renderText(text)

print("Output: ")
print(output)