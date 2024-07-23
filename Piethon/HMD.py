import pyfiglet
import random

fonts = ['standard', 'digital', 'slant', 'smscript']
colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
selected_font = random.choice(fonts)
selected_color = random.choice(colors)
message = pyfiglet.figlet_format("Happy Mother's Day!", font=selected_font)
print(f"\033[1;{colors.index(selected_color)+31}m{message}\033[0m")
