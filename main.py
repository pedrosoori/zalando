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

import discount
import email_scraper
import datetime
import github

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



def randomCode(num):
        g=github.Github("7f4298e4fd054e97ad8f6f59cd1b2134b4293440")
        repo = g.get_user().get_repo("zalando")
        file2 = repo.get_contents("promocode.json")
        
        f=file2.decoded_content.decode()
        datos=json.loads(f)
        
        i=0
        cupones=""
        score=datos["cupones"]
        while i<num:
            random_item_from_list = random.choice(score)
            cupones=cupones+str(random_item_from_list)+"\n"
            score.remove(random_item_from_list)
            i=i+1
        
        print(cupones)     
        number_of_elements = len(score)
        print(number_of_elements)  
        
        datos["cupones"]=score
        encode=json.dumps(datos)
        repo.update_file(path=file2.path, message="Update promocode", content=encode, sha=file2.sha)
        
        time.sleep(5)
        
        return cupones



client = discord.Client()
intents = discord.Intents.default()
intents.members = True


def comandoescrito():
    @bot.command(pass_context=True)
    @commands.is_owner()
    async def status(ctx):
        await ctx.reply(embed=discord.Embed(title='**BOT ONLINE**', color=0x552E12))
    
    @bot.command()
    async def generate(ctx, num: int):
        g=github.Github("7f4298e4fd054e97ad8f6f59cd1b2134b4293440")
        repo = g.get_user().get_repo("zalando")
        file1 = repo.get_contents("datos.json")
        
        if ctx.channel.id == 942152678094540902 or ctx.channel.id == 960659202253140089:
            fecha=datetime.date.today()
            fecha=str(fecha)
            try:
                #f=open("datos.json", "r")
                #hora=json.loads(f)
                f=file1.decoded_content.decode()
                hora=json.loads(f)
                
                #if num >20:
                #    await ctx.reply(embed=discord.Embed(title='**TIENES QUE PEDIR MENOS DE 20**'))
                    
                if hora[str(ctx.author.id)][1] + num <= 20:
                    await ctx.reply(embed=discord.Embed(title='**ENVIANDO CODIGO. MIRA TUS DM**', color=0x2ecc71))
                    await ctx.send(embed=discord.Embed(title='**Opcion 1**', color=0x2ecc71))
                    embed = discord.Embed(
                        title='Aqui tienes tus codigos:',
                        description=randomCode(num),
                        color=0x3498db)
                    embed.set_thumbnail(
                    url="https://i.postimg.cc/G2zwytRB/GORRO-PNG.png")
                    embed.set_footer(text="@Sori#0001",
                                      icon_url="https://media1.tenor.com/images/bcebfc84143c63f127c7fd80826f01bf/tenor.gif?itemid=22297787")
                    await ctx.author.send(embed=embed)
                    
                    hora[str(ctx.author.id)][0]=fecha
                    hora[str(ctx.author.id)][1]+=num
                    encode=json.dumps(hora)
                    repo.update_file(path=file1.path, message="Update datos", content=encode, sha=file1.sha)
                    
                    email_scraper.setup()
                    discount.datos(num+2)
                    
                      
                    
                elif hora[str(ctx.author.id)][1] + num > 20:
                    if hora[str(ctx.author.id)][0] == fecha:
                        msg = '**ERROR: Tienes un limite de 20 cupones. Llevas pedidos: **'+str(hora[str(ctx.author.id)][1])
                        await ctx.reply(embed=discord.Embed(title=msg, color=0xe74c3c))
                        await ctx.send(embed=discord.Embed(title='**Opcion 2**', color=0x2ecc71))
                    else:
                        if num < 21:
                            await ctx.reply(embed=discord.Embed(title='**ENVIANDO CODIGO. MIRA TUS DM**', color=0x2ecc71))
                            await ctx.send(embed=discord.Embed(title='**Opcion 3**', color=0x2ecc71))
                            embed = discord.Embed(
                                title='Aqui tienes tus codigos:',
                                description=randomCode(num),
                                color=0x3498db)
                            embed.set_thumbnail(
                            url="https://i.postimg.cc/G2zwytRB/GORRO-PNG.png")
                            embed.set_footer(text="@Sori#0001",
                                              icon_url="https://media1.tenor.com/images/bcebfc84143c63f127c7fd80826f01bf/tenor.gif?itemid=22297787")
                            await ctx.author.send(embed=embed)
                            
                            #f=open("datos.json", "w")
                            hora[str(ctx.author.id)][0]=fecha
                            hora[str(ctx.author.id)][1]=num
                            encode=json.dumps(hora)
                            repo.update_file(path=file1.path, message="Update datos", content=encode, sha=file1.sha)
                            
                            email_scraper.setup()
                            discount.datos(num+2)
                            
                        else:
                            await ctx.reply(embed=discord.Embed(title='**TIENES QUE PEDIR MENOS DE 20**', color=0xe74c3c))
                            await ctx.send(embed=discord.Embed(title='**Opcion 4**', color=0x2ecc71))
                        
                        
            
            except KeyError:
                #r=open("datos.json", "r")
                r=file1.decoded_content.decode()
                hora=json.loads(r)
                
                if num <21: 
                    await ctx.reply(embed=discord.Embed(title='**ENVIANDO CODIGO. MIRA TUS DM**', color=0x2ecc71))
                    await ctx.send(embed=discord.Embed(title='**Opcion 5**', color=0x2ecc71))
                    embed = discord.Embed(
                        title='Aqui tienes tus codigos:',
                        description=randomCode(num),
                        color=0x3498db)
                    embed.set_thumbnail(
                    url="https://i.postimg.cc/G2zwytRB/GORRO-PNG.png")
                    embed.set_footer(text="@Sori#0001",
                                      icon_url="https://media1.tenor.com/images/bcebfc84143c63f127c7fd80826f01bf/tenor.gif?itemid=22297787")
                    await ctx.author.send(embed=embed)
                
                    hora[str(ctx.author.id)]=[1,1]
                    hora[str(ctx.author.id)][0]=fecha
                    hora[str(ctx.author.id)][1]=num
                    encode=json.dumps(hora)
                    repo.update_file(path=file1.path, message="Update datos", content=encode, sha=file1.sha)
                    
                    email_scraper.setup()
                    discount.datos(num+2)
                    
                else:
                    await ctx.reply(embed=discord.Embed(title='**TIENES QUE PEDIR MENOS DE 20**', color=0xe74c3c))
                    await ctx.send(embed=discord.Embed(title='**Opcion 6**', color=0x2ecc71))
            
    
        #if ctx.channel.id == 960659202253140089:
        #    email_scraper.setup()
        #    discount.datos(num+2)
        #    embed = discord.Embed(
        #        title='Aqui tienes tus codigos:',
        #        description=randomCode(num),
        #        color=0x2ecc71)
        #    embed.set_thumbnail(
        #    url="https://i.postimg.cc/G2zwytRB/GORRO-PNG.png")
        #    embed.set_footer(text="@Sori#0001",
        #                      icon_url="https://media1.tenor.com/images/bcebfc84143c63f127c7fd80826f01bf/tenor.gif?itemid=22297787")
        #    await ctx.reply(embed=embed)
            
    
    #update=open("datos.json", "r").read()
    #repo.update_file(path=file1.path, message="Update datos", content=update, sha=file1.sha)            
    TOKEN = "ODk0ODU0NzUxOTcwMjkxNzQy.GzzPvR.9UMGwzolFex8flSe99-AXCuRGC8Vp8BAgaG0jU"
    bot.run(TOKEN)
            

if __name__ == '__main__':
    #discordbotReaction()
    comandoescrito()
        
      


