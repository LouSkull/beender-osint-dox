import time
import requests
from bs4 import BeautifulSoup
from utils import randomuser
from helper import printer, timer

headers = {
    "User-Agent": f"{randomuser.IFeelLucky()}",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://duckduckgo.com/"
}


class Search:
    @timer.timer
    def __init__(self, query):
        url = f"https://duckduckgo.com/html/?q={query}"

        try:
            response = self.send_request(url)
            if response is not None:
                self.parse_and_print_results(response.text, query)
        except requests.exceptions.RequestException as e:
            printer.error(f"Error : {e}")
        except KeyboardInterrupt:
            printer.error("Cancelled..!")

    @staticmethod
    def send_request(url):
        try:
            with requests.get(url, headers=headers) as response:
                response.raise_for_status()
                return response
        except requests.exceptions.RequestException:
            return None

    def parse_and_print_results(self, response_text, query):
        soup = BeautifulSoup(response_text, "html.parser")
        results = soup.find_all("div", {"class": "result__body"})

        if not results:
            printer.error(f"No results found for '{query}'..!")
            return

        printer.info(f"Searching for '{query}' -- With the agent '{headers['User-Agent']}'")
        time.sleep(1)
        for result in results:
            self.print_search_result(result)

    def print_search_result(self, result):
        title = result.find("a", {"class": "result__a"}).text
        link = result.find("a", {"class": "result__a"})["href"]
        status_code = self.get_status_code(link)
        printer.success(f"'{title}' - {link} - [{status_code}]")

    @staticmethod
    def get_status_code(url):
        try:
            with requests.get(url, stream=True) as response:
                response.raise_for_status()
                return response.status_code
        except requests.exceptions.RequestException:
            return None
