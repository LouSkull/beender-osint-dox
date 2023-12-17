import os
import json
from instagram_private_api import Client
from helper import printer, timer


class Scrape:
    @timer.timer
    def __init__(self, username, password, target):
        self.username = username
        self.password = password

        temp_dir = '/tmp'
        credentials_file = os.path.join(temp_dir, "dontlookhere.json")
        if os.name == "posix" and not os.path.exists(credentials_file):
            self.save_credentials(username, password)

        try:
            api = Client(username, password)
            data = api.username_info(target)
            printer.info(f"Logged in as '{username}'.")
        except Exception as e:
            printer.error(f"Error : {e}")
            return

        self.print_account_info(data)

    @staticmethod
    def save_credentials(username, password):
        if os.name == "posix":
            temp_dir = '/tmp'
            credentials_file = os.path.join(temp_dir, "dontlookhere.json")
            credentials = {"username": username, "password": password}
            with open(credentials_file, "w") as file:
                json.dump(credentials, file)

            printer.info(f"Credentials saved temporarily in {credentials_file}.")
        else:
            printer.warning("Win system! Not saving...")

    @staticmethod
    def safe_get(data, key, default=None):
        keys = key.split('.')
        for k in keys:
            if k in data:
                data = data[k]
            else:
                return default
        return data

    def print_account_info(self, data):
        try:
            user = data.get('user', {})
            printer.info(f"Scraping data from the account '{user.get('username')}'...")

            printer.success(f"Username - {user.get('username')}")
            printer.success(f"Full Name - {user.get('full_name')}")
            printer.success(f"Id - {user.get('pk')}")
            printer.success(f"Biography - {user.get('biography')}")
            printer.success(f"External Url - {user.get('external_url')}")
            printer.success(f"Is Private? - {user.get('is_private')}")
            printer.success(f"Is Verified? - {user.get('is_verified')}")
            printer.success(f"Is Business? - {user.get('is_business')}")
            printer.success(f"Business Category - {user.get('category')}")

            if user.get('is_business'):
                printer.success(f"Can Direct Message? - {user.get('direct_messaging')}")
                printer.success(f"Email - {user.get('public_email')}")
                printer.success(f"Phone Number - {user.get('public_phone_country_code')} {user.get('public_phone_number')}")

            for link in self.safe_get(user, 'bio_links', []):
                printer.success(f"Bio Link(s) - {link.get('url')}")

            printer.success(f"Total Posts - {user.get('media_count')}")
            printer.success(f"Followers - {user.get('follower_count')}")
            printer.success(f"Following - {user.get('following_count')}")

            chain_suggestions = user.get('chaining_suggestions', [])
            for idx, chain in enumerate(chain_suggestions, 1):
                printer.success(f"{idx} Chaining Suggestion(s) - {chain.get('username')} - {chain.get('full_name')} ({chain.get('pk')})")

            printer.success(f"Media(s) - {user.get('media_count')}")
            printer.success(f"IGTV Video(s) - {user.get('total_igtv_videos')}")
            printer.success(f"Profile Pic Url - {self.safe_get(user, 'hd_profile_pic_url_info.url')}")
            printer.success(f"Profile Url - https://www.instagram.com/{user.get('username')}")
        except Exception as e:
            printer.error(f"Error: {e}")
