import asyncio
import azure.functions as func


async def main(req: func.HttpRequest) -> func.HttpResponse:
    await asyncio.sleep(5)
    return func.HttpResponse(f"OK")