import time
import azure.functions as func


async def main(req: func.HttpRequest) -> func.HttpResponse:
    time.sleep(5)
    return func.HttpResponse(f"OK")