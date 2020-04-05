#!/usr/bin/python3
import feedparser
from concurrent.futures import ThreadPoolExecutor

def grabfeed(feedurl):
    return feedparser.parse(feedurl)

