import logging
from aiogram.utils import executor
import dotenv
import os
from aiogram import Bot, Dispatcher, types


dotenv.load_dotenv()
logging.basicConfig(level=logging.INFO)

bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
bot = Bot(token=bot_token)
dp = Dispatcher(bot)

@dp.chat_join_request_handler()
async def join_request(update: types.ChatJoinRequest):
    print(update)
    user_id=update.from_user.id
    await bot.send_message(user_id, 'Реклама')
    await update.approve()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
