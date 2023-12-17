import base64
from helper import printer


class BaseXX:
    def __init__(self, message, mode, encoding):
        self.message = message
        self.mode = mode
        self.encoding = encoding

        if self.mode in ("encode", "e"):
            printer.info(f"Encoding '{self.message}' into Base{encoding}...")
            self.encode()
        elif self.mode in ("decode", "d"):
            printer.info(f"Decoding '{self.message}' from Base{encoding}...")
            self.decode()
        else:
            printer.error("Invalid mode, please choose either 'encode' or 'decrypt'..!")

    def encode(self):
        try:
            if self.encoding == "64":
                self.encoded_message = base64.b64encode(self.message.encode("ascii")).decode("ascii")
            elif self.encoding == "32":
                self.encoded_message = base64.b32encode(self.message.encode("ascii")).decode("ascii")
            elif self.encoding == "16":
                self.encoded_message = base64.b16encode(self.message.encode("ascii")).decode("ascii")
            else:
                printer.error("Invalid encoding, please choose either '64' or '32' or '16'..!")
            printer.success(f"'{self.message}' in Base{self.encoding} : {self.encoded_message}")
        except UnicodeEncodeError:
            printer.error("Invalid character, please only use ASCII characters.")

    def decode(self):
        try:
            if self.encoding == "64":
                self.decoded_message = base64.b64decode(self.message.encode("ascii")).decode("ascii")
            elif self.encoding == "32":
                self.decoded_message = base64.b32decode(self.message.encode("ascii")).decode("ascii")
            elif self.encoding == "16":
                self.decoded_message = base64.b16decode(self.message.encode("ascii")).decode("ascii")
            printer.success(f"'{self.message}' in plain text : {self.decoded_message}")
        except Exception:
            printer.error("Error while decoding, please make sure the message is encoded in Base64.")
