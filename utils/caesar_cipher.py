from helper import printer


class CaesarCipher:
    def __init__(self, text: str, shift: int, mode: str):
        self.text = text
        self.shift = shift
        self.mode = mode

        if self.mode in ("encrypt", "e"):
            printer.info(f"Encrypting '{self.text}'...")
            encrypted_text = self.caesar_encrypt(self.text, self.shift)
            printer.success(f"'{self.text}' in Caesar's code : {encrypted_text}")
        elif self.mode in ("decrypt", "d"):
            printer.info(f"Decrypting '{self.text}'...")
            decrypted_text = self.caesar_decrypt(self.text, self.shift)
            printer.success(f"'{self.text}' in plain text : {decrypted_text}")
        elif self.mode in ("bruteforce", "b"):
            printer.info(f"Brute forcing '{self.text}'...")
            self.brute_force(self.text)
        else:
            printer.error("Invalid mode, please choose either 'encrypt' , 'decrypt' or 'bruteforce'..!")

    @staticmethod
    def caesar_encrypt(text, shift):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                is_upper = char.isupper()
                char = char.lower()
                encrypted_char = chr(((ord(char) - 97 + shift) % 26) + 97)
                if is_upper:
                    encrypted_char = encrypted_char.upper()
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        return encrypted_text

    @staticmethod
    def caesar_decrypt(encrypted_text, shift):
        decrypted_text = ""
        for char in encrypted_text:
            if char.isalpha():
                is_upper = char.isupper()
                char = char.lower()
                decrypted_char = chr(((ord(char) - 97 - shift) % 26) + 97)
                if is_upper:
                    decrypted_char = decrypted_char.upper()
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
        return decrypted_text

    @staticmethod
    def brute_force(encrypted_text):
        for i in range(26):
            decrypted_text = ""
            for char in encrypted_text:
                if char.isalpha():
                    is_upper = char.isupper()
                    char = char.lower()
                    decrypted_char = chr(((ord(char) - 97 - i) % 26) + 97)
                    if is_upper:
                        decrypted_char = decrypted_char.upper()
                    decrypted_text += decrypted_char
                else:
                    decrypted_text += char
            printer.success(f"Shift: {i} | Decrypted text: {decrypted_text}")
