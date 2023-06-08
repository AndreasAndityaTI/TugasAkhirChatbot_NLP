# McBot
import pandas as pd
import numpy as np
import aiml, os, marshal
from pprint import pprint
df = pd.read_csv("mcd.csv")
df.fillna(0, inplace=True)
df.replace(to_replace = np.nan, value = 0)
promos = df[df["R/L"]==1]

def tunjukkan_promo():
    string=""
    promo =""
    for i in range(len(promos)):        
        harga = str(int(promos.iloc[i,3]))
        if promos.iloc[i,3]== 0.0:     
            harga = str(int(promos.iloc[i,4]))
            if promos.iloc[i,4] == 0.0:
                harga = str(int(promos.iloc[i,2]))            
        promo += str("\n\t"+promos.iloc[i,1]+ " Rp "+harga)
    return promo

kern = aiml.Kernel()
id_sessi = "123456"
BOT_SESSION_PATH = "/py/coba/"
if os.path.isfile("bot_brain.brn"):
        kern.bootstrap(brainFile = "bot_brain.brn", commands = "MCBOT")
else:
    kern.bootstrap(learnFiles = "McBot.xml", commands = "MCBOT")
    kern.saveBrain("bot_brain.brn")        
kern.setPredicate("promo",tunjukkan_promo(),id_sessi)
while True:
    # doesn't work. can't write session and create the files, and got session error
    # if os.path.isfile(BOT_SESSION_PATH + id_sessi + ".ses"):
    #     kern.bootstrap(brainFile = "bot_brain.brn")
    #     sessionFile = open(BOT_SESSION_PATH + id_sessi + ".ses", "rb")
    #     sessionData = marshal.load(sessionFile)
    #     sessionFile.close()
    #     for pred, value in sessionData.items():
    #         kern.setPredicate(pred, value, id_sessi)
    # else:
    #     kern.bootstrap(learnFiles = "McBot.xml")
    #     kern.saveBrain("bot_brain.brn")
    #     print("brain set")         
    #     user_input = kern.respond(input("USER > "), id_sessi)
    #     user_input.upper()
    #     sessionData = kern.getSessionData(id_sessi)
    #     pprint(sessionData)
    #     sessionFile = open(BOT_SESSION_PATH + id_sessi + ".ses", "wb")
    #     marshal.dump(sessionData, sessionFile)
    #     sessionFile.close()

    # if user_input:
    #     pprint("Bot > "+ user_input)
    # else:
    #     pprint("Bot > Maaf Ka, saya kurang mengerti. Bisakah diulangi lagi?"+user_input)
    
    
    user_input = kern.respond(input("USER > "),id_sessi)
    if user_input:
        print("Bot > ", user_input)
    else:
        print("Bot > Maaf Ka, saya kurang mengerti. Bisakah diulangi lagi?", )