# 🐾 CatBot

Простой Telegram-бот для детей.
Бот показывает меню с кнопками и реагирует на действия — можно погладить кота, обнять кота и посмотреть историю действий.
Все фото хранятся в папке `media/`.

## 📂 Структура проекта
````
CatAndBot/
│── .env 
│── .venv
│── .gitignore
│── requirements.txt
│── main.py 
│
├── media
│
├── handlers/ 
│ ├── start.py
│ ├── actions.py
│ └── history.py
│
└── keyboards/ 
└── main_menu.py
````


## 🚀 Установка и запуск

**Клонируем проект:**

```bash
git clone https://github.com/username/catandbot.git
cd catandbot
```

## Создаём виртуальное окружение:
````
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
````

## Устанавливаем зависимости:

```bazaar
pip install -r requirements.txt
```

## Создаём файл .env и указываем токен:

```bazaar
TOKEN=твой_токен_бота
```

## Запускаем:

```bazaar
python main.py
```


## Функционал
````
/start — приветствие и показ кота 

Погладить кота — фото и подпись «Кот доволен »

Обнять кота — фото и подпись «Кот мурчит »

История выбора — показывает все действия пользователя

## Технологии
Python 3.10+

python-telegram-bot==13.15

python-dotenv
````
