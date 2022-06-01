import imaplib
import email
import json
import time
import github



def setup():
    g=github.Github("7f4298e4fd054e97ad8f6f59cd1b2134b4293440")
    repo = g.get_user().get_repo("zalando")
    file1 = repo.get_contents("promocode.json")
    file2 = repo.get_contents("txt.txt")
    
    #borrar
    repo.update_file(path=file2.path, message="Update txt", content="", sha=file2.sha) #borrar
    
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
    
    codigos=[]
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
                
    repo.update_file(path=file2.path, message="Update txt", content=texto, sha=file2.sha)
    
    
    
    for mail in mail_id_list:
        my_mail.store(mail, '+X-GM-LABELS', '\\Trash')
    my_mail.expunge()
    
    
    f =open("txt.txt", 'r')
    datafile = f.readlines()
    for line in datafile:
        if '=09[=E2=86=92]' in line:
            cupon=line.split()
            codigos.append(cupon[0])
    #print(codigos)        
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
    #except:
    #    r=file1.decoded_content.decode()
    #    encode=json.dumps(datos)
    #    repo.update_file(path=file1.path, message="Update datos", content=encode, sha=file1.sha)
    
    
    
    #update=open("promocode.json", "r").read()
    #repo.update_file(path=file1.path, message="Update promocode", content=update, sha=file1.sha)
        
# while True:
#     setup()
#     print('buscando emails')
#     time.sleep(10)
