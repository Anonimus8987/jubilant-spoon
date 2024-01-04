from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет! Этот бот конвертирует сумму в евро, доллары и рубли. Введите сумму для конвертации:")


def convert(update: Update, context: CallbackContext) -> None:
    
    amount = float(update.message.text)
    
   
    euro_rate = 0.85
    dollar_rate = 1.0
    ruble_rate = 75.0
    
  
    euro_amount = amount / dollar_rate * euro_rate
    dollar_amount = amount
    ruble_amount = amount * ruble_rate
    
  
    update.message.reply_text(f"{amount} долларов = {euro_amount} евро, {dollar_amount} долларов, {ruble_amount} рублей")

def main() -> None:
  
    token = "YOUR_TELEGRAM_BOT_TOKEN"
    
    
    updater = Updater(token)

    
    dispatcher = updater.dispatcher

   
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, convert))

   
    updater.start_polling()

    
    updater.idle()

if __name__ == '__main__':
    main()
