# -*- coding: utf-8 -*-
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Вставьте здесь токен вашего телеграм-бота
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# Обработчик команды /start
def start(update: Update, _: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr"Привет, {user.mention_markdown_v2()}!",
        reply_markup=ForceReply(selective=True),
    )

# Обработчик обычных текстовых сообщений
def echo(update: Update, _: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main() -> None:
    # Создаем экземпляр Updater и передаем токен
    updater = Updater(TOKEN)

    # Получаем объекты для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем обработчики команды /start и текстовых сообщений
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Запускаем бота
    updater.start_polling()

    # Останавливаем бота, если нажата Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
