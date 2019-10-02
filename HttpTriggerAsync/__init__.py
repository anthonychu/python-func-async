from aiohttp_requests import requests
import azure.functions as func


async def main(req: func.HttpRequest) -> func.HttpResponse:
    response = await requests.get("https://raw.githubusercontent.com/anthonychu/python-func-async/master/host.json")
    return func.HttpResponse(await response.text())