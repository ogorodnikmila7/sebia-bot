# Бот «Себя не терять» — инструкция по запуску

## Требования
- Python 3.10+
- Токен бота от BotFather

---

## Установка

```bash
pip install -r requirements.txt
```

---

## Запуск

### Вариант А — напрямую (для теста на своём компьютере)

```bash
BOT_TOKEN="123456789:AAF..." python bot.py
```

Или отредактируйте строку в bot.py:
```python
BOT_TOKEN = "123456789:AAF..."
```

---

### Вариант Б — на VPS/сервере (постоянная работа)

1. Залейте файлы на сервер (scp, git, FTP)
2. Установите зависимости: `pip install -r requirements.txt`
3. Запустите через systemd или screen:

**screen (проще):**
```bash
screen -S bot
BOT_TOKEN="ваш_токен" python bot.py
# Ctrl+A, затем D — отключиться, бот продолжит работу
```

**systemd (надёжнее):**
Создайте файл `/etc/systemd/system/sebia-bot.service`:
```
[Unit]
Description=Sebia ne teryat Bot
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/bot.py
Restart=always
Environment=BOT_TOKEN=ваш_токен

[Install]
WantedBy=multi-user.target
```
Затем:
```bash
systemctl enable sebia-bot
systemctl start sebia-bot
```

---

### Вариант В — бесплатный хостинг (Railway / Render)

1. Зайдите на [railway.app](https://railway.app) или [render.com](https://render.com)
2. Создайте новый проект из этой папки
3. Добавьте переменную окружения `BOT_TOKEN`
4. Deploy — готово

---

## После запуска

1. Найдите бота в Telegram по username
2. Нажмите /start
3. Появится кнопка «Пройти тест» — она открывает тест прямо внутри Telegram

---

## Прямая ссылка (без бота)

Если хотите поделиться ссылкой напрямую — используйте формат:
```
https://t.me/ВАШ_БОТ_USERNAME?startapp
```
Это откроет Mini App сразу при переходе по ссылке.
