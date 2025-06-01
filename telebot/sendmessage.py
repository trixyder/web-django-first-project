import requests
from .models import TeleSettings






def sendTelegram(name, phone):
    try:
        settings = TeleSettings.objects.get(pk=1)
    except TeleSettings.DoesNotExist:
        print("Настройки телеграмм не найдены")
        return False
    

    token = str(settings.tg_token)
    chat_id = str(settings.tg_chat)
    text = f'Новая заявка! Имя : {name}, телефон : {phone}'
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'
    
    try:
        req = requests.post(method, data={
            'chat_id' : chat_id,
            'text' : text,
        })  
        if req.status_code != 200:
            print (f'Ошибка телеграмм апи, текст : {req.text}!')
            return False
        return True
    except requests.RequestException as e:
        print(f'Ошибка:{e} ')
        return False