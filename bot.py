"""
Telegram бот для теста «Себя не терять»
Запускает тест как Mini App (Web App)

Зависимости: pip install python-telegram-bot==20.7
"""

import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# ──────────────────────────────────────────────────────────────
# КОНФИГУРАЦИЯ — заполните перед запуском
# ──────────────────────────────────────────────────────────────

BOT_TOKEN = os.getenv("BOT_TOKEN", "8745568389:AAFfYQPScAFvsjv2Me80I1wv_B9oC4PXnls")

# URL вашего теста (уже задеплоен — менять не нужно)
TEST_URL = "https://lighthearted-macaron-6d8b10.netlify.app/"

# ──────────────────────────────────────────────────────────────

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start — отправляет кнопку запуска теста."""
    user = update.effective_user
    name = user.first_name if user else "друг"

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            text="🪞 Пройти тест",
            web_app=WebAppInfo(url=TEST_URL)
        )]
    ])

    await update.message.reply_text(
        f"Привет, {name} 👋\n\n"
        "Этот тест поможет понять — сохраняете ли вы себя в отношениях, "
        "или постепенно растворяетесь в партнёре.\n\n"
        "20 вопросов о смехе, мнениях, хобби и ценностях. "
        "Займёт 5–7 минут. Анонимно.\n\n"
        "Нажмите кнопку, чтобы начать ↓",
        reply_markup=keyboard
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Отправьте /start чтобы открыть тест.\n\n"
        "Тест анонимный — ответы нигде не сохраняются."
    )


def main() -> None:
    if BOT_TOKEN == "ВСТАВЬТЕ_ТОКЕН_СЮДА":
        raise ValueError("Укажите токен бота: BOT_TOKEN='ваш_токен' python bot.py")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    logger.info("Бот запущен. Нажмите Ctrl+C для остановки.")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
