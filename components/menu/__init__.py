def main_menu(header, flatFiguresMenu):
    header()

    print("""
[1] Área das figuras planas
    """)

    choice = input('➤ ')

    if choice == '1':
        flatFiguresMenu()
