import logging
import asyncio
import requests
import concurrent.futures
import azure.functions as func


executor = concurrent.futures.ThreadPoolExecutor(max_workers=50)

async def main(req: func.HttpRequest) -> func.HttpResponse:
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(executor, requests.get, "https://raw.githubusercontent.com/anthonychu/python-func-async/master/host.json")
    return func.HttpResponse(response.text)