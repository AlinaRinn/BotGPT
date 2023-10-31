import logging
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
import g4f
from threading import Thread
response = ""
user_message = ""

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)   


def gpt():
    global response
    response = g4f.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "Nika", "content": user_message}])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Здарова семпай! Задай мне вопрос или дай задание <3")


async def question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global user_message
    user_message = update.message.text
    print("User prompt:", user_message)
    gpt_thread = Thread(target=gpt)
    gpt_thread.start()
    gpt_thread.join()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)


if __name__ == '__main__':
    application = ApplicationBuilder().token('1612505318:AAEV8qY4yiFFNAF84EZABgxjjkbMj7aLYhY').build()
    
    start_handler = CommandHandler('start', start)
    question_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), question)

    application.add_handler(start_handler)
    application.add_handler(question_handler)
    application.run_polling()