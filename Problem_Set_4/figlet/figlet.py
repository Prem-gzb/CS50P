from pyfiglet import Figlet
import sys, random

figlet = Figlet()

fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font = random.choice(fonts))
elif len(sys.argv) == 3 and (sys.argv[1] in ['-f','--font']) and sys.argv[2] in fonts:
    figlet.setFont(font = sys.argv[2])
else:
    sys.exit('Invalid Usage')

user_input = input('Input: ')
print(figlet.renderText(user_input))