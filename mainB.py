import asyncio
from aiogram import Bot, Dispatcher, executor

from configB import BOT_TOKEN

loop = asyncio.new_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)

if __name__ == '__main__':
    from handlersB import dp
    executor.start_polling(dp)

'''
URL_IPHONE13 = f'https://www.apple.com/shop/buy-iphone/iphone-13-pro'
URL_MACBOOK = f'https://www.apple.com/shop/buy-mac/macbook-pro/16-inch'
URL_AIRPODS = f'https://www.apple.com/shop/product/MLWK'
'''