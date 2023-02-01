import telebot
from config import configure

if __name__ == '__main__':
    token = configure['bot_token']
    bot = telebot.TeleBot(token)


    @bot.message_handler(content_types=['document'])
    def handle_docs_photo(message):
        try:
            chat_id = message.chat.id

            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            src = message.document.file_name;
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)

            bot.reply_to(message, "Пожалуй, я сохраню это")
        except Exception as e:
            bot.reply_to(message, e)


    bot.infinity_polling()
