import phonenumbers as p
from phonenumbers import carrier, geocoder, timezone
from helper import printer, timer
import time


class LookUp:
    @timer.timer
    def __init__(self, no):
        print("\n")
        try:
            ph_no = p.parse(no)
            country = p.region_code_for_country_code(ph_no.country_code)
            no_carrier = carrier.name_for_number(ph_no, "en")
            no_valid = p.is_valid_number(ph_no)
            no_possible = p.is_possible_number(ph_no)
            time_zone = timezone.time_zones_for_number(ph_no)
            region = geocoder.description_for_number(ph_no, "en")

            printer.info(f"Trying to find the information of '{no}'")
            time.sleep(1)
            printer.success("Phone Number -", no)
            printer.success(f"Valid Number -", no_valid)
            printer.success(f"Possible Number -", no_possible)
            printer.success(f"Sim Provider -", no_carrier)
            printer.success(f"Country -", country)
            printer.success(f"Region -", region)
            printer.success(f"Time Zone -", time_zone)
        except Exception as e:
            printer.error(f"Error : ", e)
