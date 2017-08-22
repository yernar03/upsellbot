import telebot
from telebot import types
token = '345646960:AAH2yDeY8RY-dHd_4jQLkrLpQbIbAcIc4c0'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def keyboard(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('🔥Заказать бота🔥')
    markup.row("❓Вопросы","Примеры🚀")
    markup.row('📞Заказать звонок')
    
    bot.send_message(message.chat.id, '''{name},приветствую!
Мы занимаемся созданием виртуальных помощников, задачи которых:
✅Увеличение продаж
✅Снижение затрат на персонал
✅Автоматизация бизнес-процессов''',reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '🔥Заказать бота🔥')
def command_text_hi(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Написать Whatsapp", url="https://api.whatsapp.com/send?phone=77785333373&text=%20%D0%9F%D1%80%D0%B8%D0%B2%D0%B5%D1%82,%20%D0%AF%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D0%B2%D0%BE%D0%B4%D1%83%20%D1%87%D0%B0%D1%82-%D0%B1%D0%BE%D1%82%D0%B0")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Вы сможете написать на наш Whatsapp, нажав кнопку ⬇️", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == '📞Заказать звонок')
def phone(message):
    # Эти параметры для клавиатуры необязательны, просто для удобства
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить📲", request_contact=True)
    keyboard.add(button_phone)
    bot.send_message(message.chat.id, "Отправить номер телефона мне чтобы позвонили⬇️", reply_markup=keyboard)


if __name__ == '__main__':
    bot.polling(none_stop=True)
