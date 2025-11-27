import hashlib
import time
from functools import wraps
from typing import Any, Callable
from fastapi import FastAPI, HTTPException, Request

app = FastAPI()


def rate_limit(max_calls: int, period: int):
    def decorator(func: Callable[[Request], Any]) -> Callable[[Request], Any]:
        usage: dict[str, list[float]] = {}

        @wraps(func)
        async def wrapper(request: Request) -> Any:
            # Get the client's IP address
            if not request.client:
                raise ValueError("Request has no client information")
            ip_address: str = request.client.host

            # Create unique identifier for the client
            unique_id: str = hashlib.sha256(ip_address.encode()).hexdigest()

            # Update the timestamp
            now = time.time()
            if unique_id not in usage:
                usage[unique_id] = []

            timestamps = usage[unique_id]
            timestamps[:] = [t for t in timestamps if now - t < period]

            if len(timestamps) < max_calls:
                timestamps.append(now)
                return await func(request)

            wait = period - (now - timestamps[0])
            raise HTTPException(
                status_code=429, detail=f"Rate limit exceeded. Please try again in {wait:.2f} seconds")

        return wrapper
    return decorator


@app.get("/")
@rate_limit(max_calls=10, period=60)
async def index(request: Request) -> Any:
    return {"message": "Hello, World!"}
