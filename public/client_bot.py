from pickle import*
from time import*
# Clint Chating
client_msg = input("Chat Here => ")


# My taille
fc = open("../db/count.dat","rb")
x = load(fc)
n = x["taille"]
# Programme
while True:
    ok = False
    # Read From Api
    bot_api = open("../db/api1.dat","rb")
    
        
    for i in range(n):
        
        bot_msg_get = load(bot_api)
        sleep(1)
        # request / response [Bot chat]
        bot_msg_req = bot_msg_get["req"]
        bot_msg_res = bot_msg_get["res"]
    
        if client_msg.lower() == bot_msg_req.lower():
            ok = True
            break
    bot_api.close()
        
    if ok == True:
        print(bot_msg_res)
        client_msg = input("Chat Here => ")
        
    else:
        print("i'am not understened what you went ,  ask me again with other question if you went !")
        client_msg = input("Chat Here => ")

