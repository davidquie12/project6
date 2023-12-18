import asyncio
import logging
import re
import sys
from typing import IO
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup
import aiofiles
import aiohttp
from collections import Counter
from aiohttp import ClientSession



#STAP 1
async def fetch_ap(url: str, session: ClientSession) -> str:
    # html dom
    resp = await session.request(method="GET", url=url)
    resp.raise_for_status()
    html = await resp.text()
    return html

async def parse(html : str):
    soup = BeautifulSoup(html, "html.parser")
    text_tag = soup.find_all(text=True)
    reg = r'\w+'
    all_words = re.findall(reg,' '.join(text_tag))  
    word_count = Counter(all_words) 

    for word, count in word_count.items():
        print(f"{word}: {count}")

    all_links = [link.get("href") for link in soup.find_all("a", href=True)]

    print("\nList of all links:")
    for link in all_links:
        print(link)
        
async def chain():
    async with ClientSession() as session:
        try:
            html = await fetch_ap(url="https://www.ap.be",session=session)
            await parse(html)
            
        except (
        aiohttp.ClientError,
        aiohttp.ClientConnectionError,
    ) as e:
            e.add_note("connection error with site ")

async def main():
    await asyncio.gather(chain()) 
    

            
if __name__ == "__main__":
    asyncio.run(main())
    
print("--------------------------------------------------")    
# STAP 2
