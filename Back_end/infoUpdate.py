# Модуль обновляет данные курса USD и отправляем сообщения в Telegram
import requests, time, datetime, telegram_send as ts, json
from bs4 import BeautifulSoup

# получаем актуальный курс доллара
def usd_update():
    response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp?date_req={}'.format(datetime.date.today().strftime("%d/%m/%Y")))
    data = response.content
    soup = BeautifulSoup(data, features="xml")
    try:
        for tag in soup.findAll('Valute'):
            if tag['ID'] == 'R01235':
                return float((tag.Value.text).replace(',','.'))
    except:
        return None

# Отсылваем сообщения в телеграм
def telegram():
    response = requests.get('http://localhost:8000/canalservice/tgmsg/?pk=1bRT3njCRVcLayIqkMS0nCE_p_gw1ea6f5P_sLwOl9o8')
    data = json.loads(response.text)[0]
    for msg in data:
        ts.send(messages=['Нарушение срока поставки заказа № {}'.format(msg.get('order'))])

while True:
    try:
        # Передаём данные серверу Django
        response = requests.post('http://localhost:8000/canalservice/usdupd/', data={'passkey': '1bRT3njCRVcLayIqkMS0nCE_p_gw1ea6f5P_sLwOl9o8', 'usd': usd_update()})
        # Отсылваем сообщения в телеграм
        telegram()
    except:
        pass
    time.sleep(86400)# программа засыпает на сутки, этот параметр варируется !!!
