def main_menu(header, flatFiguresMenu) -> None:
    header()

    print("""
[1] Área das figuras planas
    """)

    choice = input('➤ ')

    if choice == '1':
        flatFiguresMenu()
