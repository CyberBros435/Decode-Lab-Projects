import re
import random
import pyfiglet
from colorama import Fore, Style


class PasswordSecurityChecker:
    def __init__(self):
        # Move static data out of the loop
        self.common = [
            "password",
            "password123",
            "admin123",
            "qwerty",
            "letmein",
            "wellcome",
        ]

    def banner(self):
        # Fixed naming conflict (method vs attribute)
        banner_text = pyfiglet.figlet_format(text="Password Security Checker")
        print(f"{Fore.GREEN}{banner_text}{Style.RESET_ALL}\n")

    def password_checking(self):
        while True:
            self.banner()
            self.userpassword = input(
                f"{Fore.BLUE}Enter Your Password (0 -> exit):\t{Style.RESET_ALL}"
            )

            if self.userpassword == "0":
                print(f"{Fore.GREEN}Exiting...{Style.RESET_ALL}")
                break

            self.length = len(self.userpassword)

            # Correct use of any() checking individual characters
            self.has_upper = any(char.isupper() for char in self.userpassword)
            self.has_lower = any(char.islower() for char in self.userpassword)
            # Use regex to find any character that is NOT a letter or digit
            self.has_symbol = any(
                bool(re.match(r"[^a-zA-Z0-9]", char)) for char in self.userpassword
            )
            self.has_digit = any(char.isdigit() for char in self.userpassword)

            try:
                # 1. Check common passwords first so they don't get bypassed
                if self.userpassword.lower() in self.common:
                    print(
                        f"{Fore.CYAN}Password Strength: {Fore.RED}Weak (Common Password){Style.RESET_ALL}"
                    )
                    color = Fore.RED

                # 2. Check for weak length (less than 6 characters)
                elif self.length < 6:
                    print(
                        f"{Fore.CYAN}Password Strength: {Fore.RED}Weak{Style.RESET_ALL}"
                    )
                    color = Fore.RED

                # 3. Check for strong password criteria (All conditions must be True)
                elif (
                    self.length >= 12
                    and self.has_upper
                    and self.has_lower
                    and self.has_symbol
                    and self.has_digit
                ):
                    print(
                        f"{Fore.CYAN}Password Strength: {Fore.GREEN}Strong{Style.RESET_ALL}"
                    )
                    color = Fore.GREEN

                # 4. Catch everything else as medium
                else:
                    print(
                        f"{Fore.CYAN}Password Strength: {Fore.YELLOW}Medium{Style.RESET_ALL}"
                    )
                    color = Fore.YELLOW

                # Reusable print block to avoid massive code repetition
                print(f"{Fore.MAGENTA}Password Details:{Style.RESET_ALL}")
                print(f"{Fore.CYAN}Length: {color}{self.length}{Style.RESET_ALL}")
                print(
                    f"{Fore.CYAN}Upper Case in Password: {color}{self.has_upper}{Style.RESET_ALL}"
                )
                print(
                    f"{Fore.CYAN}Lower Case in Password: {color}{self.has_lower}{Style.RESET_ALL}"
                )
                print(
                    f"{Fore.CYAN}Digits in Password: {color}{self.has_digit}{Style.RESET_ALL}"
                )
                print(
                    f"{Fore.CYAN}Special Symbols in Password: {color}{self.has_symbol}{Style.RESET_ALL}\n"
                )

            except Exception as error:
                print(f"An error occurred: {error}")


obj = PasswordSecurityChecker()


def main():
    obj.password_checking()


if __name__ == "__main__":
    main()
