#!/usr/bin/env python3
'''
Requests caching and tracking data
'''
import requests
import redis
import time


def get_page(url: str) -> str:
    """Initialize Redis connection"""
    r = redis.Redis()

    """Increment access count for the URL"""
    count_key = f"count:{url}"
    r.incr(count_key)

    """Check if the page content is cached"""
    cached_content = r.get(url)
    if cached_content:
        return cached_content.decode('utf-8')

    """Retrieve the page content from the URL"""
    response = requests.get(url)
    page_content = response.text

    """Cache the page content with expiration time of 10 seconds"""
    r.setex(url, 10, page_content)

    return page_content
