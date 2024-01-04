from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет! Я бот-приветствие. Как я могу помочь вам?")


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Вы можете использовать следующие команды:\n"
                              "/start - Начать взаимодействие с ботом\n"
                              "/help - Получить справочную информацию")


def main() -> None:
    token = "YOUR_TELEGRAM_BOT_TOKEN"

   
    updater = Updater(token)

    
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    
    updater.start_polling()

  
    updater.idle()

if __name__ == '__main__':
    main()
