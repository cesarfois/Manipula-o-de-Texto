
# 1. Utilizando caracteres ANSI

BRANCO = "\033[1;39m"
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
YELLOW = "\033[1;33m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"


print(RED + "ERROR! "  + "Something went wrong...")

#pip install termcolor


from termcolor import colored

print(colored('Error Test!!!', 'red'))
print(colored('Warning Test!!!', 'yellow'))
print(colored('Success Test!!!', 'green'))
 