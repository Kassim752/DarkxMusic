import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("18641113"))
API_HASH = getenv("bc5fea81e7bf9f3c0784a0a7d35f9c71")
BOT_USERNAME = getenv("Darlzzmusic_bot")
BOT_TOKEN = getenv("5720344802:AAEE_DIgIURq2fOKiqOKS1t6lqDwnu2g09c")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("AQB3tug1W3QN2BubdcyIFJbwT_h4xBD8IthfV3Hhh6DhRh5bqxaF9aWVxQ7zQD-omaBRAAzYrvQIhNr2dwutM9hbvbl0JmVJOvMJNfNSVBerZ3XZVKksKkNiz7GiPPX9yIHjt6quvjr8vjKHQ69ABHi9WmKoTYraf6TDd66KDBHTPwpimrbqS5KxEEDibWw41nDi1BNNvPK7v5TPHpsCuoNax4LghjN1zpHBDWzcpm2a6VlU8rpMAoWa5qzPSpFmLCWzbvfnz_IfNZdIcvcOfz2Jc9c_O_iqdfdRXkMAivTluM8Lt1fyZHxeRWjle-lWWfXryLraKW_wXa9-ZNGOLUQuAAAAAVQudpIA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5323266323").split()))
aiohttpsession = aiohttp.ClientSession()
