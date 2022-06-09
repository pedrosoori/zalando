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
    # @bot.command()
    # @commands.is_owner()
    # async def say(ctx,id_chat: int,* , message):
    #         if ctx.author.id == 274197666961817601 or ctx.author.id == 777843948382191616:
    #             channel = bot.get_channel(id_chat)
    #             embed=discord.Embed(
    #                 description=(message),
    #                 color=discord.Color.blue()
    #             )
    #             try:  
    #                 await ctx.message.delete()
    #                 await channel.send(embed=embed)  
    #             except:
    #                 await ctx.message.delete()
    #                 await ctx.send("Canal no encontrado")
    
    
    @bot.command()
    @commands.is_owner()
    async def say(ctx,* , text):
        if ctx.author.id == 274197666961817601 or ctx.author.id == 777843948382191616:
            message = ctx.message
            await message.delete()
            await ctx.send(f"{text}")
    
    @bot.command(pass_context=True)
    @commands.is_owner()
    async def codigos(ctx, num: int):
        if ctx.channel.id == 960659202253140089:
            discount.datos(num)
            await ctx.reply(embed=discord.Embed(title='**DESCUENTOS GENERADOS**', color=0x2ecc71))
    
    @bot.command(pass_context=True)
    @commands.is_owner()
    async def scraper(ctx):
        if ctx.channel.id == 960659202253140089:
            email_scraper.setup()
            await ctx.reply(embed=discord.Embed(title='**Correos revisados**', color=0x2ecc71))
    
    @bot.command(pass_context=True)
    @commands.is_owner()
    async def status(ctx):
        await ctx.reply(embed=discord.Embed(title='**BOT ONLINE**', color=0x552E12))
    
    @bot.command()
    async def generate(ctx, num: int):
        
        g=github.Github("7f4298e4fd054e97ad8f6f59cd1b2134b4293440")
        repo = g.get_user().get_repo("zalando")
        file1 = repo.get_contents("datos.json")
        
        if ctx.channel.id == 942152678094540902:
            
            fecha=datetime.date.today()
            fecha=str(fecha)
            
            try:
                
                f=file1.decoded_content.decode()
                hora=json.loads(f)
                    
                if hora[str(ctx.author.id)][1] + num <= 20:
                    
                    await ctx.reply(embed=discord.Embed(title='**ENVIANDO CODIGO. MIRA TUS DM**', color=0x2ecc71))
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
                    
                    else:
                        
                        if num < 21:
                            
                            await ctx.reply(embed=discord.Embed(title='**ENVIANDO CODIGO. MIRA TUS DM**', color=0x2ecc71))
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
                            hora[str(ctx.author.id)][1]=num
                            encode=json.dumps(hora)
                            repo.update_file(path=file1.path, message="Update datos", content=encode, sha=file1.sha)
                            
                            email_scraper.setup()
                            discount.datos(num+2)
                            
                        else:
                            
                            await ctx.reply(embed=discord.Embed(title='**TIENES QUE PEDIR MENOS DE 20**', color=0xe74c3c))
                        
                        
            
            except KeyError:

                r=file1.decoded_content.decode()
                hora=json.loads(r)
                
                if num <21: 
                    
                    await ctx.reply(embed=discord.Embed(title='**ENVIANDO CODIGO. MIRA TUS DM**', color=0x2ecc71))
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
                    
            except github.GithubException:
                
                print('sobresaturado')
                g=github.Github("7f4298e4fd054e97ad8f6f59cd1b2134b4293440")
                repo = g.get_user().get_repo("zalando")
                file1 = repo.get_contents("datos.json")
                
                try:
                    
                    f=file1.decoded_content.decode()
                    hora=json.loads(f)
                    hora[str(ctx.author.id)][0]=fecha
                    hora[str(ctx.author.id)][1]+=num
                    encode=json.dumps(hora)
                except KeyError:
                    
                    r=file1.decoded_content.decode()
                    hora=json.loads(r)
                    hora[str(ctx.author.id)]=[1,1]
                    hora[str(ctx.author.id)][0]=fecha
                    hora[str(ctx.author.id)][1]=num
                
                repo.update_file(path=file1.path, message="Update datos sobresaturados", content=encode, sha=file1.sha)
                
            except IndexError:
                print('error en el promocode.json')
                await ctx.reply(embed=discord.Embed(title='**Error con el catchall. Avisa a un admin.**', color=0xe74c3c))
            
    
        if ctx.channel.id == 960659202253140089:
            
            email_scraper.setup()
            discount.datos(num+2)
            embed = discord.Embed(
                title='Aqui tienes tus codigos:',
                description=randomCode(num),
                color=0x2ecc71)
            embed.set_thumbnail(
            url="https://i.postimg.cc/G2zwytRB/GORRO-PNG.png")
            embed.set_footer(text="@Sori#0001",
                              icon_url="https://media1.tenor.com/images/bcebfc84143c63f127c7fd80826f01bf/tenor.gif?itemid=22297787")
            await ctx.reply(embed=embed)
            
    
    TOKEN = "ODk0ODU0NzUxOTcwMjkxNzQy.GzzPvR.9UMGwzolFex8flSe99-AXCuRGC8Vp8BAgaG0jU"
    bot.run(TOKEN)
            
    
if __name__ == '__main__':
    comandoescrito()
