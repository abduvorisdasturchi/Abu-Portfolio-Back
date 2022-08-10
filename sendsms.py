def sendTelegram(xabar):
    import requests
    api="5429358928:AAE8UcYw8MzTALJLdFZGv_I-6hml1dcUXk8v"
    url=f'https://api.telegram.org/bot5429358928:AAE8UcYw8MzTALJLdFZGv_I-6hml1dcUXk8/sendMessage?chat_id=1990786081&text={xabar}'
    requests.get(url)
