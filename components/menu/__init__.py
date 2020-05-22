from typing import NoReturn, Callable


def main_menu(header: Callable[[], NoReturn],
              flatFiguresMenu: Callable[[], NoReturn]) -> NoReturn:
    '''
    Main menu of all the functions.
    Don't need any params and don't have return,
    this function just print the options and execute the choice.
    '''

    header()

    print("""
[1] Área das figuras planas
    """)

    choice = input('➤ ')

    if choice == '1':
        flatFiguresMenu()
