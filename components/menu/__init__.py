from components.header import header
from components.menu.FlatFiguresMenu import flat_figures_menu

def main_menu():
    header()

    print("""
[1] Área das figuras planas
    """)

    choice = input('➤ ')

    if choice == '1':
        flat_figures_menu()
