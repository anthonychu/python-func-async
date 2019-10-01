import logging
import asyncio
import time
import concurrent.futures
import azure.functions as func

executor = concurrent.futures.ThreadPoolExecutor(max_workers=50)

async def main(req: func.HttpRequest) -> func.HttpResponse:
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(executor, time.sleep, 5)
    return func.HttpResponse(f"OK")