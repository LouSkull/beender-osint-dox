import time
import subprocess
from helper import printer, timer


class Holehe:
    """
    Searches for the email address in various websites using holehe.

    Thanks to Holehe, https://github.com/megadose/holehe

    :param email: The email address to search for.
    """
    @timer.timer
    def __init__(self, email):
        printer.info(f"Trying to find sites where '{email}' is used, thanks to holehe.")
        time.sleep(1)
        try:
            result = subprocess.run(["holehe", email], capture_output=True, text=True, check=True)
            result.stdout = "\n".join(result.stdout.split("\n")[4:])
            result.stdout = "\n".join(result.stdout.split("\n")[:-4])
            result.stdout = "\n".join([f"\033[92m{line}\033[0m" if "[+]" in line else line for line in result.stdout.split("\n")])
            result.stdout = "\n".join([f"\033[91m{line}\033[0m" if "[-]" in line else line for line in result.stdout.split("\n")])
            result.stdout = "\n".join([f"\033[93m{line}\033[0m" if "[x]" in line else line for line in result.stdout.split("\n")])
            # ^^^ moms spaghetti ^^^

            if result.stdout:
                printer.nonprefix(result.stdout)
                printer.nonprefix("Credits to megadose (Palenath) for holehe.")
            else:
                printer.error("No results found..!")
        except FileNotFoundError:
            printer.error("Error : 'holehe' command not found. Please make sure you have holehe installed and in your PATH.")
            printer.error("You can install holehe using 'pip install holehe'.")
        except subprocess.CalledProcessError as e:
            printer.error(f"Error : {e}")
        except Exception as e:
            printer.error(f"Unexpected error : {e}")
