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
        i=0
        cupones=""
        with open("promocode.json", 'r') as f:
         score = json.load(f)
         score=score["cupones"]
         while i<num:
             random_item_from_list = random.choice(score)
             cupones=cupones+str(random_item_from_list)+"\n"
             score.remove(random_item_from_list)
             i=i+1
        
        print(cupones)     
        number_of_elements = len(score)
        print(number_of_elements)  
        
        lista={}
        lista["cupones"]=score
        
        with open("promocode.json", 'w') as f:
         json.dump(lista, f)
        return cupones



client = discord.Client()
intents = discord.Intents.default()
intents.members = True


def discordbot():
        @client.event
        async def on_ready():
            print('We have logged in as {0.user}'.format(client))
            channel = client.get_channel(960659202253140089)
            embed = discord.Embed(
                title='Izi Cookz Code Promo',
                description='Clique sur 🎫 pour recevoir un code Promo de -10% sur le site de Zalando ! ⚠️ Merci de ne pas spam le bot ⚠️ !')
            embed.set_thumbnail(
            url="https://i.postimg.cc/G2zwytRB/GORRO-PNG.png")
            embed.set_footer(text="Made by JLM for Izi Cookz",
                             icon_url="https://media1.tenor.com/images/bcebfc84143c63f127c7fd80826f01bf/tenor.gif?itemid=22297787")
            msg = await channel.send(embed=embed)
            await msg.add_reaction("🎫")
            await msg.add_reaction("🎟️")
            await msg.add_reaction("📇")

            
def discordbotReaction():
        @client.event
        async def on_raw_reaction_add(payload):
            #discount.datos()
            if(payload.message_id == 980653836077264896 and payload.emoji.name == "🎫"):  
                msg = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
                member = discord.utils.get(msg.reactions, emoji="🎫")
    
                user = payload.member
                print(payload)
                await msg.remove_reaction("🎫", user)
                time.sleep(3)
                embed = discord.Embed(
                    title='Aqui tienes tus codigos:',
                    description=randomCode())
                embed.set_thumbnail(
                url="https://i.postimg.cc/G2zwytRB/GORRO-PNG.png")
                embed.set_footer(text="@Sori#0001",
                                 icon_url="https://media1.tenor.com/images/bcebfc84143c63f127c7fd80826f01bf/tenor.gif?itemid=22297787")
                msg = await user.send(embed=embed)
            
 
            if(payload.message_id == 980653836077264896 and payload.emoji.name == "🎟️"):  
                user = payload.member 
                role = discord.utils.find(lambda r: r.name == 'Premium GOLD', user.roles)
                msgGold = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
                if role in user.roles:  
                    memberGold = discord.utils.get(msgGold.reactions, emoji="🎟️")
                    userGold = payload.member
                    print(payload)
                    message = "[Génération des codes]"
                    await userGold.send(message)
                    await msgGold.remove_reaction("🎟️", userGold)
                    time.sleep(3)
                    i = 0
                    waitingMsg = ("Voici tes codes :")
                    await userGold.send(waitingMsg)
                    while i < 3:
                        Codes = (randomCode())
                        await userGold.send(Codes)
                        i = i+1
                else:
                    userGold = payload.member
                    
                    await userGold.send(":octagonal_sign: Tu n'est pas encore GOLD ! :octagonal_sign:")
                userGold = payload.member
                await msgGold.remove_reaction("🎟️", userGold)
            
            if(payload.message_id == 980653836077264896 and payload.emoji.name == "📇"):  
                user = payload.member
                role = discord.utils.find(lambda r: r.name == 'Premium PLATINE', user.roles)
                msgPLATINE = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
                if role in user.roles:  
                    memberPLATINE = discord.utils.get(msgPLATINE.reactions, emoji="📇")
                    userPLATINE = payload.member
                    print(payload)
                    message = "[Génération des codes]"
                    await userPLATINE.send(message)
                    await msgPLATINE.remove_reaction("📇", userPLATINE)
                    time.sleep(3)
                    i = 0
                    waitingMsg = ("Voici tes codes :")
                    await userPLATINE.send(waitingMsg)
                    while i < 5:
                            Codes = (randomCode())
                            await userPLATINE.send(Codes)
                            i = i+1
                else:
                    userPLATINE = payload.member
                    await userPLATINE.send(":octagonal_sign:  Tu n'est pas encore PLATINE :octagonal_sign: ")
                userPLATINE = payload.member
                await msgPLATINE.remove_reaction("📇", userPLATINE)



        TOKEN = "ODk0ODU0NzUxOTcwMjkxNzQy.GzzPvR.9UMGwzolFex8flSe99-AXCuRGC8Vp8BAgaG0jU"
        client.run(TOKEN)

def comandoescrito():
    @bot.command(pass_context=True)
    @commands.is_owner()
    async def status(ctx):
        await ctx.reply(embed=discord.Embed(title='**BOT ONLINE**'))
    
    @bot.command()
    async def generate(ctx, num: int):
        g=github.Github("7f4298e4fd054e97ad8f6f59cd1b2134b4293440")
        repo = g.get_user().get_repo("zalando")
        file1 = repo.get_contents("datos.json")
        
        if ctx.channel.id == 942152678094540902:
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
                    await ctx.reply(embed=discord.Embed(title='**ENVIANDO CODIGO. MIRA TUS DM**'))
                    embed = discord.Embed(
                        title='Aqui tienes tus codigos:',
                        description=randomCode(num))
                    embed.set_thumbnail(
                    url="https://i.postimg.cc/G2zwytRB/GORRO-PNG.png")
                    embed.set_footer(text="@Sori#0001",
                                      icon_url="https://media1.tenor.com/images/bcebfc84143c63f127c7fd80826f01bf/tenor.gif?itemid=22297787")
                    await ctx.author.send(embed=embed)
                    discount.datos(num)
                    email_scraper.setup()
                    
                    #f=open("datos.json", "w")
                    hora[str(ctx.author.id)][0]=fecha
                    hora[str(ctx.author.id)][1]+=num
                    #json.dump(str(hora), f)
                    
                      
                    
                elif hora[str(ctx.author.id)][1] + num > 20:
                    if hora[str(ctx.author.id)][0] == fecha:
                        msg = '**ERROR: Tienes un limite de 20 cupones. Llevas pedidos: **'+str(hora[str(ctx.author.id)][1])
                        await ctx.reply(embed=discord.Embed(title=msg))
                    else:
                        await ctx.reply(embed=discord.Embed(title='**ENVIANDO CODIGO. MIRA TUS DM**'))
                        embed = discord.Embed(
                            title='Aqui tienes tus codigos:',
                            description=randomCode(num))
                        embed.set_thumbnail(
                        url="https://i.postimg.cc/G2zwytRB/GORRO-PNG.png")
                        embed.set_footer(text="@Sori#0001",
                                          icon_url="https://media1.tenor.com/images/bcebfc84143c63f127c7fd80826f01bf/tenor.gif?itemid=22297787")
                        await ctx.author.send(embed=embed)
                        discount.datos(num)
                        email_scraper.setup()
                        
                        #f=open("datos.json", "w")
                        hora[str(ctx.author.id)][0]=fecha
                        hora[str(ctx.author.id)][1]=num
                        #json.dump(str(hora), f)
                        
                        
                
                encode=json.dumps(hora)
                repo.update_file(path=file1.path, message="Update datos", content=encode, sha=file1.sha)

            
            except:
                #r=open("datos.json", "r")
                r=file1.decoded_content.decode()
                hora=json.loads(r)
                hora[str(ctx.author.id)]=[1,1]
                hora[str(ctx.author.id)][0]=fecha
                hora[str(ctx.author.id)][1]=num
                #f=open("datos.json", "w")
                #json.dump(hora, f)
                #update=open("datos.json", "r").read()
                encode=json.dumps(hora)
                repo.update_file(path=file1.path, message="Update datos", content=encode, sha=file1.sha)
                
                if num <20: 
                    await ctx.reply(embed=discord.Embed(title='**ENVIANDO CODIGO. MIRA TUS DM**'))
                    embed = discord.Embed(
                        title='Aqui tienes tus codigos:',
                        description=randomCode(num))
                    embed.set_thumbnail(
                    url="https://i.postimg.cc/G2zwytRB/GORRO-PNG.png")
                    embed.set_footer(text="@Sori#0001",
                                      icon_url="https://media1.tenor.com/images/bcebfc84143c63f127c7fd80826f01bf/tenor.gif?itemid=22297787")
                    await ctx.author.send(embed=embed)
                    discount.datos(num)
                    email_scraper.setup()
                else:
                    await ctx.reply(embed=discord.Embed(title='**TIENES QUE PEDIR MENOS DE 20**'))
            
    
        if ctx.channel.id == 960659202253140089:
            embed = discord.Embed(
                title='Aqui tienes tus codigos:',
                description=randomCode(num))
            embed.set_thumbnail(
            url="https://i.postimg.cc/G2zwytRB/GORRO-PNG.png")
            embed.set_footer(text="@Sori#0001",
                              icon_url="https://media1.tenor.com/images/bcebfc84143c63f127c7fd80826f01bf/tenor.gif?itemid=22297787")
            await ctx.reply(embed=embed)
            discount.datos(num)
            email_scraper.setup()
    
    #update=open("datos.json", "r").read()
    #repo.update_file(path=file1.path, message="Update datos", content=update, sha=file1.sha)            
    TOKEN = "ODk0ODU0NzUxOTcwMjkxNzQy.GzzPvR.9UMGwzolFex8flSe99-AXCuRGC8Vp8BAgaG0jU"
    bot.run(TOKEN)
            

if __name__ == '__main__':
    #discordbotReaction()
    comandoescrito()
        
      


