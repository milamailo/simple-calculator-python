from src.cli_dashboards import cli_menu
from src.gui_dashboard import gui_menu

def main():
    while True:
        choice = input("Choose your interface or exit:\n1. CLI\n2. GUI\n0. Exit\nEnter 1, 2, or 0: ")
        if choice == '1':
            cli_menu()
        elif choice == '2':
            gui_menu()
        elif choice == '0':
            print("Exiting the application.")
            break  # Breaks the loop and exits the program
        else:
            print("Invalid input, please enter 1, 2, or 0.")

if __name__ == "__main__":
    main()
