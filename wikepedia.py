import wikipedia
import logging
from aiogram import Bot, Dispatcher, executor, types

# Configure logging
logging.basicConfig(level=logging.INFO)
API_TOKEN = '6165457619:AAGRn-YV2jiojLYEXjb0KEn_Xq5cEC838D0'
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
wikipedia.set_lang("uz")

# print(wikipedia.search("python"))
# print(wikipedia.search("qarshi"))



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("salom !\nmen abduvalini botiman!\npython dasturlash tilda yozilganman.")



@dp.message_handler()
async def echo(message: types.Message):
    try:
        wiki = wikipedia.summary(message)
        await message.answer(wiki)
    except:
        await message.answer("bunaqa malumot topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)