import asyncio
import aiohttp
from bs4 import BeautifulSoup
from helper import printer, timer
from utils import randomuser


class Scrape:
    @timer.timer
    def __init__(self, url):
        try:
            printer.info(f"Trying to scrape links from '{url}'...")
            asyncio.run(self.scrape_links(url))
            printer.success(f"Scraping completed..!")
        except Exception as e:
            printer.error(f"Error: {e}")

    @staticmethod
    async def fetch(session, url):
        headers = {"User-Agent": f"{randomuser.IFeelLucky()}"}
        async with session.get(url, headers=headers) as response:
            return await response.text()

    @staticmethod
    async def parse_links(content):
        soup = BeautifulSoup(content, "html.parser")
        links = soup.find_all("a")
        return [(link.get("href"), link.text) for link in links]

    async def scrape_links(self, url):
        async with aiohttp.ClientSession() as session:
            html_content = await self.fetch(session, url)

            # TODO This part can be further improved by using ThreadPoolExecutor to parse links concurrently.
            links = await self.parse_links(html_content)

            count = 0
            for href, text in links:
                count += 1
                printer.success(f"found {count} link(s): {href} - {text}")
