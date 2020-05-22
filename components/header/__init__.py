from typing import NoReturn


def header() -> NoReturn:
    '''
    Clears the screen and display the header, containing the banner and credits.
    '''
    import os
    os.system('clear')
    print("""
▒█▀▀█ █▀▀ █▀▀█ █▀▄▀█ █▀▀ ▀▀█▀▀ █▀▀█ █░░█ 　 ▒█▀▄▀█ █▀▀█ ▀▀█▀▀ █░░█ 
▒█░▄▄ █▀▀ █░░█ █░▀░█ █▀▀ ░░█░░ █▄▄▀ █▄▄█ 　 ▒█▒█▒█ █▄▄█ ░░█░░ █▀▀█ 
▒█▄▄█ ▀▀▀ ▀▀▀▀ ▀░░░▀ ▀▀▀ ░░▀░░ ▀░▀▀ ▄▄▄█ 　 ▒█░░▒█ ▀░░▀ ░░▀░░ ▀░░▀ 
""")
    print(('-'*28).center(66))
    print('by: Mateus Felipe'.center(66))
    print('https://github.com/mateusfg7'.center(66))
    print(('-'*28).center(66))
    print('\n')
