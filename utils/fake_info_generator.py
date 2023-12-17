from faker import Faker
import time
from helper import printer, timer


class Generate:
    @timer.timer
    def __init__(self):
        fake = Faker()
        printer.info("Generating fake information...")
        time.sleep(1)
        printer.success(f"Fake name : {fake.name()}")
        printer.success(f"Fake address : {fake.address()}")
        printer.success(f"Fake email : {fake.email()}")
        printer.success(f"Fake phone number : {fake.phone_number()}")
        printer.success(f"Fake job : {fake.job()}")
        printer.success(f"Fake company : {fake.company()}")
        printer.success(f"Fake credit card number : {fake.credit_card_number()}")
        printer.success(f"Fake credit card security code : {fake.credit_card_security_code()}")
        printer.success(f"Fake credit card expiration date : {fake.credit_card_expire()}")
        printer.success(f"Fake credit card type : {fake.credit_card_provider()}")
        printer.success(f"Fake IBAN : {fake.iban()}")
        printer.success(f"Fake BIC : {fake.bban()}")
        printer.success(f"Fake country : {fake.country()}")
        printer.success(f"Fake city : {fake.city()}")
