import json
import time
from datetime import datetime
import aiohttp
import asyncio
from utils import randomuser
from helper import printer, url_helper, timer


class Search:
    """
    Performs a search for the given username.

    :param username: The username to search for.
    """
    @timer.timer
    def __init__(self, username):
        self.username = username
        try:
            self.scan(self.username)
        except KeyboardInterrupt:
            printer.error("Cancelled..!")
            pass

    def scan(self, username):
        start_time = time.time()
        printer.info(f"Searching for '{username}' across {len(url_helper.read_local_json_content('resources/data.json')['sites'])} sites...")

        results = []
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.make_requests(username, results))

        now = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        execution_time = round(time.time() - start_time, 1)
        user_json = {
            "search-params": {
                "username": username,
                "sites-number": len(url_helper.read_local_json_content('resources/data.json')['sites']),
                "date": now,
                "execution-time": execution_time
            },
            "sites": results
        }

        # print_results(user_json)

        return user_json

    async def make_requests(self, username, results):
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=20)) as session:
            tasks = []
            for u in url_helper.read_local_json_content('resources/data.json')["sites"]:
                task = asyncio.ensure_future(self.make_request(session, u, username, results))
                tasks.append(task)
            await asyncio.gather(*tasks)

    @staticmethod
    async def make_request(session, u, username, results):
        url = u["url"].format(username=username)
        json_body = None
        headers = {"User-Agent": f"{randomuser.IFeelLucky()}"}
        if 'headers' in u:
            headers.update(eval(u['headers']))
        if 'json' in u:
            json_body = u['json'].format(username=username)
            json_body = json.loads(json_body)
        try:
            async with session.request(u["method"], url, json=json_body, proxy=None, headers=headers,
                                       ssl=False) as response:
                if eval(u["valid"]):
                    printer.success(
                        f'- #{u["id"]} {u["app"]} - Account found - {url} [{response.status} {response.reason}]')
                    results.append({
                        "id": u["id"],
                        "app": u['app'],
                        "url": url,
                        "response-status": f"{response.status} {response.reason}",
                        "status": "FOUND",
                        "error-message": None
                    })
                else:
                    results.append({
                        "id": u["id"],
                        "app": u['app'],
                        "url": url,
                        "response-status": f"{response.status} {response.reason}",
                        "status": "NOT FOUND",
                        "error-message": None
                    })
        except:
            pass

    @staticmethod
    def print_results(user_json):
        for site in user_json["sites"]:
            printer.success(f"ID: {site['id']}")
            printer.success(f"App: {site['app']}")
            printer.success(f"URL: {site['url']}")
            printer.success(f"Response Status: {site['response-status']}")
            printer.success(f"Status: {site['status']}")
            printer.error(f"Error Message: {site['error-message']}\n")
