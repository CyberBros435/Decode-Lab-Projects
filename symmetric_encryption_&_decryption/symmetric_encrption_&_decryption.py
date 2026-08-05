import random
from colorama import Fore, Style
import pyfiglet
import time as t


class E_And_D:
    def __init__(self):
        self.alphabates = "abcdefghijklmnopqrstuvwxyz"
        self.secret_key = ""
        self.generate_new_key()

    def generate_new_key(self):
        self.list_alphabates = list(self.alphabates)
        random.shuffle(self.list_alphabates)
        self.secret_key = "".join(self.list_alphabates)

    def banner(self):
        self.banner_text = pyfiglet.figlet_format(
            text="Symmetric Encryption", font="slant"
        )
        print(f"{Fore.YELLOW}{self.banner_text}{Style.RESET_ALL}")

    def encrypt(self, plain_text, secret_key):
        self.encrypted_text = ""

        for letter in plain_text:
            if letter in self.alphabates:
                self.position = self.alphabates.index(letter)
                self.scrumbled_letter = self.secret_key[self.position]
                self.encrypted_text += self.scrumbled_letter
            else:
                self.encrypted_text += letter

        return self.encrypted_text

    def decrypt(self, cypher_text, secret_key):
        self.decrypted_text = ""
        for letter in cypher_text.lower():
            if letter in self.secret_key:
                self.letter_position = secret_key.index(letter)
                self.original_text = self.alphabates[self.letter_position]
                self.decrypted_text += self.original_text
        return self.decrypted_text


obj = E_And_D()


def main():
    while True:
        obj.banner()
        obj.generate_new_key()
        print(f"{Fore.GREEN}Key is generating...{Style.RESET_ALL}")
        t.sleep(1)
        user_message = input("Enter your message...\t")
        print(f"{Fore.GREEN}Message Encrypting... {Style.RESET_ALL}")
        t.sleep(1)
        data_in_transit = obj.encrypt(user_message, obj.secret_key)
        print(f"{Fore.YELLOW}Message Encrypted!!!{Style.RESET_ALL}")
        t.sleep(1)
        print(f"Data Encrypted:\t{Fore.GREEN}{data_in_transit}{Style.RESET_ALL}")
        t.sleep(1)
        print(f"{Fore.GREEN}Message Decrypting...{Style.RESET_ALL}")
        t.sleep(1)
        data_decrypted = obj.decrypt(data_in_transit, obj.secret_key)
        print(f"{Fore.YELLOW}Message Decrypted!!!{Style.RESET_ALL}")
        t.sleep(1)
        print(f"Data Decrypted:\t{Fore.GREEN}{data_decrypted}{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
