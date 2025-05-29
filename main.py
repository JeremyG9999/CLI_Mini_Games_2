import os
import time

from scripts.blackjack import JeremysBlackjack
from scripts.hide_seek import Hide_And_Seek
from scripts.needle_haystack import NeedleHaystack

class Menu:
    def main_menu(self):
        while True:
            print("\nSelect a program:")
            print("1. Blackjack Game")
            print("2. Hide and Seek Game")
            print("3. Needle and Haystack Game")
            print("4. Clear Terminal")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.cls()
                JeremysBlackjack().main_menu()
            elif choice == "2":
                self.cls()
                Hide_And_Seek().main_menu()
            elif choice == "3":
                self.cls()
                NeedleHaystack().main_menu()
            elif choice == "4":
                self.cls()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

    def cls(self):
        time.sleep(0.2)
        os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    Menu().main_menu()