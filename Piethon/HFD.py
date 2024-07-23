import pyfiglet
import random

def generate_wish():
    message = "Happy Father's Day!"
    fonts = pyfiglet.FigletFont.getFonts()
    selected_font = random.choice(fonts)
    ascii_art = pyfiglet.figlet_format(message, font=selected_font)
    return ascii_art

wish = generate_wish()
print(wish)
