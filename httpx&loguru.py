import httpx
from loguru import logger

data = (
    httpx.get("https://jsonplaceholder.typicode.com/todos/1").raise_for_status().json()
)
logger.info(f"{data}")

not_found = httpx.get("https://httpbin.org/status/404").raise_for_status().json()
logger.trace(f"{not_found}")


# logger.critical("Critical")
# logger.trace("trace")
# logger.debug("debug")
# logger.warning("warning")
# logger.error("Something went wrong!")
