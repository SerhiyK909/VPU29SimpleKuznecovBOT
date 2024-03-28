# import os
#
# from dotenv import load_dotenv
#
# load_dotenv()  # take environment variables from .env.
#
# print(os.getenv('TELEGRAM_TOKEN'))



import os
from dotenv import load_dotenv
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def question(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'how are you')
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(f'perfectly')
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text.lower()

    if 'привіт' in message:
        reply_text = f'привіт {update.effective_user.first_name} {update.effective_user.last_name}'
    elif 'допобачення' in message:
        reply_text = f'допобачення {update.effective_user.first_name} {update.effective_user.last_name}'
    else:
        reply_text = f'я вас не розумію!'

    await update.message.reply_text(reply_text)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("question", question))
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()