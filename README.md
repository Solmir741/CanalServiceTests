## Описание работы сервиса обновления данных из документа Google Sheets
### Техническое решение
Работа сервиса построена на из работы нескольких микросервисов:
1.	Сервис обновления данных из google документа. Реализован в модуле getData.py
2.	Сервис обновления данных БД PostgreSQL. Реализован в модуле gsUpdate.py
3.	Сервис обновления данных курса валют и рассылки сообщений в Telegram. Реализован в модуле infoUpdate.py
4.	Основной сервис обмена информацией, работы с БД. Реализован с использованием Фреймворка Django.
5.	Frond-end сервис. Реализован с использованием Фреймворка React. Основной модуль сервиса Order_table.jsx

Рабочий образец работы сервиса доступен по ссылке https://investpn.ru/canalservice/
Пользователь amkolotov@gmail.com добавлен (чтение, запись)
Сервис не собирался в контейнер ввиду предоставление рабочей модели онлайн.
### Детальное описание работы модулей.
###### 1.	Сервис обновления данных из google документа.
Сервисы, указанные в п.п. 1-4 содержатся в папке Back_end.
Прежде чем запускать данный сервис, необходимо настроить Google API согласно официальной документации.
Код сервиса взят из типового шаблона официальной документации. Настраиваем API, сохраняем токен OAuth авторизации в файл credentials.json.  При первичном запуске кода, откроется окно авторизации (протокол OAuth). Далее код сохраняет токен авторизации в файл token.json и участие в последующих авторизациях не требуется.
Читаемый диапазон ячеек указывается в константе SAMPLE_RANGE_NAME.
###### 2.	Сервис обновления данных БД PostgreSQL.
Сервис работает путем обмена данными с сервером Django через post – запросы. В теле запроса передается информация, полученная из предыдущего модуля. 
_Важно! Здесь и далее использована минимальная защита, реализованная посредством передачи PASSKEY (секретного слова). По, хорошему в промышленной эксплуатации, необходима полноценная авторизация с использованием, например, x-csrftoken в запросах, но это выходит за рамки тестового задания. Минимальная реализованная защита позволяет избежать случайных запросов/сканеров._
Код сервиса реализован в модуле gsUpdate.py.
Код обработки запросов реализован модуле views.py (стандарный модуль Django) в функции TablUpd. Функция выполняет минимальную проверку типа данных, их выравнивание.
Работа в сервисе ведётся с БД PostgreSQL. Это видно из файла настроек Django settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'investpn_db',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5599'
    }
}

Поскольку данные google sheets не имеют уникальных id, будем считать, что номер заказа уникален. Обновление записей ведется по номеру заказа, поэтому, строки с одинаковыми номерами заказов учитывается в виде первой попавшейся строки, остальные не учитываются.
Обновление информации просходит с использованием метода update_or_create Django ORM.
###### 3.	Сервис обновления данных курса валют и рассылки сообщений в Telegram. 
Реализован в модуле infoUpdate.py
Сервис содержит 2 фунции 
usd_update – обновляем курс доллара. Обновляет информация из официального API ЦБ РФ. Передает обновленные данные для внесения в БД через post-запрос на сервер Django. Запрос обрабатывает функция UsdUpd модуля views.py.
telegram – отправляем сообщение в телеграм – бот о просроченных заказах.
В данный момент сервис настроен на обновление информации 1 раз в сутки, однако этот параметр варьируется.
___Важно! Для проверки работы телеграм-бота, необходимо предоставить номер телефона для регистрации в сервисе.___
Функция telegram отправляет get-запрос на сервер Django и в ответ получает данные о просроченных заказах. Запросы обрабатывает функция telegram_send модуля views.py.
На демонстрационном сервере, оба сервиса (модули gsUpdate.py и infoUpdate.py) запущены в виду демонов (daemon) в ОС Debian. Со скриптом демонов можно ознакомится в файлах /system/ cananservice_gsUpdate.service и /system/ cananservice_infoUpdate.service
Однако при запуске сервера в тестовом режиме, можно просто запустить файлы через команду (необходимо предварительно войти в виртуальное окружение)
python3 gsUpdate.py 
python3 infoUpdate.py 
###### 4.	Основной сервис обмена информацией, работы с БД. 
Реализован с использованием Фреймворка Django. Все основные моменты работы были описаны выше. Для тестового запуска файлов, необходимо создать новое приложение в Django, набрав
python3 startapp app_name
затем перенести файлы из папки Back_end в это приложение.
###### 5.	Frond-end сервис. Реализован с использованием Фреймворка React.
Файлы сервиса находятся в папке Front_end. Туда помещена папка src – стандарная папка для разработки во фреймворке React.
Код страницы реализован в модуле /components/order_table/ Order_table.jsx
Постоянное обновление информации страницы реализовано посредством хука useEffect по таймеру (периодичность обновления 2 с). Запросы обслуживает функция web_request модуля views.py. На странице приведена таблица заказов. Так же присутствует общая сумма заказов. Вся информация обновляется в онлайн режиме посредством хуков useState.
Для проверки, необходимо создать новый React – проект

npx create-react-app app_name
и поместить содержимое папки src в одноименную папку созданного проекта.
