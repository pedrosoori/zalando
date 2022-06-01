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



def getCode(catchall,regione):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
            'content-type': 'application/json',

    }

    data = {
    "id":"06fe5b50b4218612aa3fa8494df326aef7ff35a75a8563b3455bb53c15168872","variables":{"input":{"email": catchall,"preference":{"category":"MEN","topics":[{"id":"item_alerts","isEnabled":bool(True)},{"id":"survey","isEnabled":bool(True)},{"id":"recommendations","isEnabled":bool(True)},{"id":"fashion_fix","isEnabled":bool(True)},{"id":"follow_brand","isEnabled":bool(True)},{"id":"subscription_confirmations","isEnabled":bool(True)},{"id":"offers_sales","isEnabled":bool(True)}]},"referrer":"nl_subscription_banner_one_click","clientMutationId":"1620930739401"}}


    }



    url =  "https://www.zalando."+str(regione)+"/api/graphql/"
    s = requests.Session()

    resp = s.post(url,headers=headers,json=data)

    response  = resp.json()

    email = response["data"]['subscribeToNewsletter']['isEmailVerificationRequired']

    if (email == False):
        print ("discount generated")

    else:print ("yooo WTF there was an error"+str(resp.status_code))


def datos(quantita):
    #quantita = input('insert quantity: ')
    
    catchall = '@soori.shop'
    
    os.system('cls')
    
    #quantita = 5
    
    nomi = ['Alessandro','Riccardo','Diego','Tommaso','Matteo','Lorenzo','Gabriele','Samuele','Giacomo','beatrice','sofia','ginevra','gaia']
    cognomi=['Rossi','Ferrari','Russo','Bianchi','Romano','Gallo','Costa','Fontana','conti','esposito','ricci','bruno','greco']
    
    i=0
    
    while (i < quantita):
    
        num = random.randint(1111,9999999)
    
        indice=random.randint(0,12)
    
        eml = (nomi[indice]+str(cognomi[indice])+str(num)+str(catchall))
    
        getCode(eml,'es')
    
    
        i+=1
    time.sleep(2)
    print ("finished")



def update():
    g=github.Github("7f4298e4fd054e97ad8f6f59cd1b2134b4293440")
    repo = g.get_user().get_repo("zalando")
    file1 = repo.get_contents("promocode.json")
    
    
    
    codigos=[]
    f =open('txt.txt', 'r')
    datafile = f.readlines()
    for line in datafile:
        if '=09[=E2=86=92]' in line:
            cupon=line.split()
            codigos.append(cupon[0])
    print(codigos)
    f.close()        
    
    datos = {}
    datos["cupones"]=codigos
    
    #try:          
    r=file1.decoded_content.decode()
    score = json.loads(r)
    lista=score["cupones"]
    for cupon in codigos:
        if cupon not in lista:
            lista.append(cupon)
    score["cupones"]=lista
    encode=json.dumps(score)
    repo.update_file(path=file1.path, message="Update datos", content=encode, sha=file1.sha)



def setup():
    g=github.Github("7f4298e4fd054e97ad8f6f59cd1b2134b4293440")
    repo = g.get_user().get_repo("zalando")
    file2 = repo.get_contents("txt.txt")
    
    
    user, password = "sooriraffles1@gmail.com", "moqeasdqrwslccqo"
    
    imap_url = "imap.gmail.com"
    my_mail=imaplib.IMAP4_SSL(imap_url)
    my_mail.login(user, password)
    
    my_mail.select("Inbox")
    _, data=my_mail.search(None, '(FROM "info@service-mail.zalando.es")')
    
    mail_id_list=data[0].split()
    
    msgs=[]
    for num in mail_id_list:
        typ, data = my_mail.fetch(num, '(RFC822)')
        msgs.append(data)
    
    texto=""
    
    for msg in msgs[::-1]:
        for response_part in msg:
            if type(response_part) is tuple:
                my_msg=email.message_from_bytes((response_part[1]))
                for part in my_msg.walk():
                    #print(part.get_content_type())
                    if part.get_content_type() == 'text/plain':
                        #print(part.get_payload())
                        texto+=part.get_payload()
                
    repo.update_file(path=file2.path, message="Update txt", content=str(texto), sha=file2.sha)
    
    
    
    for mail in mail_id_list:
        my_mail.store(mail, '+X-GM-LABELS', '\\Trash')
    my_mail.expunge()
    
    #file2 = repo.get_contents("txt.txt")
    #borrar
    #repo.update_file(path=file2.path, message="Update txt", content="", sha=file2.sha) #borrar
    
    #except:
    #    r=file1.decoded_content.decode()
    #    encode=json.dumps(datos)
    #    repo.update_file(path=file1.path, message="Update datos", content=encode, sha=file1.sha)
    
    
    
    #update=open("promocode.json", "r").read()
    #repo.update_file(path=file1.path, message="Update promocode", content=update, sha=file1.sha)




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
                #f=open("datos.json", "r")
                #hora=json.loads(f)
                f=file1.decoded_content.decode()
                hora=json.loads(f)
                
                #if num >20:
                #    await ctx.reply(embed=discord.Embed(title='**TIENES QUE PEDIR MENOS DE 20**'))
                    
                if hora[str(ctx.author.id)][1] + num <= 20:
                    await ctx.reply(embed=discord.Embed(title='**ENVIANDO CODIGO. MIRA TUS DM**', color=0x2ecc71))
                    update()
                    setup()
                    datos(num+2)
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
                    hora[str(ctx.author.id)][1]+=num
                    #json.dump(str(hora), f)
                    
                      
                    
                elif hora[str(ctx.author.id)][1] + num > 20:
                    if hora[str(ctx.author.id)][0] == fecha:
                        msg = '**ERROR: Tienes un limite de 20 cupones. Llevas pedidos: **'+str(hora[str(ctx.author.id)][1])
                        await ctx.reply(embed=discord.Embed(title=msg, color=0xe74c3c))
                    else:
                        await ctx.reply(embed=discord.Embed(title='**ENVIANDO CODIGO. MIRA TUS DM**', color=0x2ecc71))
                        update()
                        setup()
                        datos(num+2)
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
                        #json.dump(str(hora), f)
                        
                        
                
                encode=json.dumps(hora)
                repo.update_file(path=file1.path, message="Update datos", content=encode, sha=file1.sha)

            
            except:
                #r=open("datos.json", "r")
                r=file1.decoded_content.decode()
                hora=json.loads(r)
                
                if num <21: 
                    await ctx.reply(embed=discord.Embed(title='**ENVIANDO CODIGO. MIRA TUS DM**', color=0x2ecc71))
                    update()
                    setup()
                    datos(num+2)
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
                else:
                    await ctx.reply(embed=discord.Embed(title='**TIENES QUE PEDIR MENOS DE 20**', color=0xe74c3c))
            
    
        if ctx.channel.id == 960659202253140089:
            update()
            setup()
            datos(num+2)
            embed = discord.Embed(
                title='Aqui tienes tus codigos:',
                description=randomCode(num),
                color=0x2ecc71)
            embed.set_thumbnail(
            url="https://i.postimg.cc/G2zwytRB/GORRO-PNG.png")
            embed.set_footer(text="@Sori#0001",
                              icon_url="https://media1.tenor.com/images/bcebfc84143c63f127c7fd80826f01bf/tenor.gif?itemid=22297787")
            await ctx.reply(embed=embed)
            
    
    #update=open("datos.json", "r").read()
    #repo.update_file(path=file1.path, message="Update datos", content=update, sha=file1.sha)            
    TOKEN = "ODk0ODU0NzUxOTcwMjkxNzQy.GzzPvR.9UMGwzolFex8flSe99-AXCuRGC8Vp8BAgaG0jU"
    bot.run(TOKEN)
            

if __name__ == '__main__':
    #discordbotReaction()
    comandoescrito()
        
      


