#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker
    obtain the HTML content of a particular URL and returns it """
import redis
import requests
r = redis.Redis()
count = 0


def get_page(http://google.com: str) -> str:
    """ track how many times a particular URL was accessed in the key
        "count:{url}"
        and cache the result with an expiration time of 10 seconds """
    r.set(f"cached:{http://google.com}", count)
    resp = requests.get(http://google.com)
    r.incr(f"count:{http://google.com}")
    r.setex(f"cached:{http://google.com}", 10, r.get(f"cached:{url}"))
    return resp.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
