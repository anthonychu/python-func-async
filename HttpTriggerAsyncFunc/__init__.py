import azure.functions as func
import requests


async def main(req: func.HttpRequest) -> func.HttpResponse:
    response = requests.get("https://raw.githubusercontent.com/anthonychu/python-func-async/master/host.json")
    return func.HttpResponse(response.text)