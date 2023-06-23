import colorama
import sys
from colorama import init,  Fore, Back, Style, AnsiToWin32
init()
init(autoreset=True)
'''automatically returns to the original version of the text'''

print(Fore.MAGENTA + 'changes text color')
print(Back.BLACK + 'adds background to text')
print(Style.DIM + 'changes brightness')
print(Style.RESET_ALL + 'returns the initial version of the text')
print('Possible colors:')
print(Fore.YELLOW + 'of text - Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.')
print(Back.BLACK + 'background - Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.')
print(Fore.BLUE + Back.RESET + Style.DIM + 'text brightness and master reset - Style: DIM, NORMAL, BRIGHT, RESET_ALL')
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream
print(stream, Fore.RED + 'red text sent to stderr')
print(Fore.RED + 'red text sent to stderr', file=stream)
