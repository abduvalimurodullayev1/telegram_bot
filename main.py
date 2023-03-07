import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types





API_TOKEN = '6165457619:AAGRn-YV2jiojLYEXjb0KEn_Xq5cEC838D0'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("salom !\nmen abduvalini botiman!\npython dasturlash tilda yozilganman.")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)