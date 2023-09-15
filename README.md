# currency_exchanger

Автор проекта - Константин Мельник.

***

Проект представляет собой API сервис для конвертации валют. Курс при каждом запросе автоматически подтягивается [отсюда](https://www.x-rates.com).

***

Пример эндпойта для обращения по API:

http://127.0.0.1:8000/api/rates?from=USD&to=EUR&value=1

- from - валюта, которая переводится. Обязательное значение.
- to - валюта, в которую переводится. Необязательное значение.
- value - количество денег в той валюте, которая переводится. Необязательное значение, по умолчанию 1.

### Локальный запуск проекта:

```text
git clone git@github.com:abyxez/currency_exchanger.git
```

Создать и активировать виртуальное окружение:

```text
python3 -m venv venv
```
Linux/macOS: 
```text
source venv/bin/activate
```
Windows: 
```text
source venv/Scripts/activate
```

```text
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements:

```text
pip install -r requirements.txt
```

Выполнить миграции:

```text
cd money_exchange/

python3 manage.py makemigrations

python3 manage.py migrate
```

Запустить проект:

```text
python3 manage.py runserver
```

В проекте также настроена админка, через которую можно добавить новые валюты.
***
По умолчанию для параметра 'from' доступны только EUR, USD, RUB.

http://127.0.0.1:8000/admin/

Создать суперпользователя для входа в админку:

```text
python3 manage.py createsuperuser
```
