from __future__ import print_function
from asyncio.tasks import wait
import os.path
from discord import member, message
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import pickle
import os.path
import base64
from bs4 import BeautifulSoup
from lxml.html.soupparser import fromstring
from lxml.etree import tostring
from discord.ext import commands, tasks
import discord
import random
import json
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
from faker import Faker
import dotenv

import datetime
import github
import imaplib
import email
import time

import requests
import os
import random

"""
logs
"""
# logging.basicConfig(filename='MonitoLog.log', filemode='a', format='%(asctime)s - %(name)s - %(message)s',
#                     level=logging.DEBUG)
"""
configurations
"""
CONFIG = dotenv.dotenv_values()
TOKEN = "ODk0ODU0NzUxOTcwMjkxNzQy.GzzPvR.9UMGwzolFex8flSe99-AXCuRGC8Vp8BAgaG0jU"

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

bot = commands.Bot(command_prefix='!')




def comandoescrito():
    f=open('txt.txt', 'r')
    texto=f.readlines()
    f.close()
    print(texto)
    
    f=open('txt.txt', 'w')
    texto='1234'
    f.write(texto)

comandoescrito()
