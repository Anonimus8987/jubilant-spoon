from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import RegexHandler


PHONE, LOCATION = range(2)


user_data = {}


def start(update: Update, context: CallbackContext) -> int:
    user_id = update.message.from_user.id
    if user_id not in user_data:
        user_data[user_id] = {}
    update.message.reply_text("Привет! Для регистрации отправь мне свой номер телефона.", reply_markup=ReplyKeyboardRemove())
    return PHONE

def get_phone(update: Update, context: CallbackContext) -> int:
    user_id = update.message.from_user.id
    user_data[user_id]['phone'] = update.message.contact.phone_number
    update.message.reply_text(f"Спасибо! Теперь отправь мне свою локацию.", reply_markup=ReplyKeyboardRemove())
    return LOCATION


def get_location(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_data[user_id]['location'] = update.message.location
    user_data[user_id]['first_name'] = update.message.from_user.first_name

    update.message.reply_text(f"Спасибо, {user_data[user_id]['first_name']}! "
                              f"Ты успешно зарегистрирован.\n"
                              f"Телефон: {user_data[user_id]['phone']}\n"
                              f"Локация: {user_data[user_id]['location']}")
    


def main() -> None:
  
    token = "YOUR_TELEGRAM_BOT_TOKEN"

    updater = Updater(token)

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            PHONE: [MessageHandler(Filters.contact & ~Filters.command, get_phone)],
            LOCATION: [MessageHandler(Filters.location & ~Filters.command, get_location)]
        },
        fallbacks=[]
    )

    dispatcher.add_handler(conv_handler)

    
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
