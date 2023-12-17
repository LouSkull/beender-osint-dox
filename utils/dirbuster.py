import asyncio
import aiohttp
import requests
from helper import printer, url_helper, timer
from utils import randomuser


class Scan:
    @timer.timer
    def __init__(self, domain):
        self.domain = domain
        self.url_set = set()

        printer.info(f"Scanning for valid URLs for '{domain}'..!")
        self.scan_urls()
        printer.success(f"Scan Complete..! Found {len(self.url_set)} valid URLs!")

    @staticmethod
    def get_wordlist():
        try:
            content = url_helper.read_local_content("resources/wordlist.txt")
            return {line.strip() for line in content.splitlines() if line.strip()}
        except requests.exceptions.ConnectionError:
            return None

    async def fetch_url(self, session, path):
        url = f"https://{self.domain}/{path}"
        headers = {"User-Agent": f"{randomuser.IFeelLucky()}"}
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                printer.success(f"Found a valid URL - {url}")
                self.url_set.add(url)

    async def scan_async(self, paths):
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_url(session, path) for path in paths]
            await asyncio.gather(*tasks)

    def scan_urls(self):
        paths = self.get_wordlist()
        if paths is None:
            printer.error("Connection Error..!")
            return

        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.scan_async(paths))
        except KeyboardInterrupt:
            printer.error("Cancelled..!")
