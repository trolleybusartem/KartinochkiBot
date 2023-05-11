from aiogram import Bot, Dispatcher, executor, types
from icrawler.builtin import GoogleImageCrawler
import os

# Переменные бота

bot = Bot(token='6282103425:AAEiPwT6d-i2YmWVVotUxVEfL7knqRw5QEo')
dp = Dispatcher(bot)

# битбокс котята

google_crawler = GoogleImageCrawler(storage={'root_dir':"image"})

# Код

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(f"Привет, {message.from_user.first_name}👌! Я могу генерировать изображения по вашему запросу! Просто напиши мне запрос и мы попробуем сгенерировать ваше изображение!")

@dp.message_handler()
async def get_image(message: types.Message):
    amount = 1
    words = message.text
    google_crawler.crawl(keyword=words, max_num=amount)
    a = os.listdir("image")

    with open('image/' + a[0], 'rb') as img_file:
        img_data = img_file.read()
    await bot.send_photo(chat_id=message.chat.id, photo=img_data)
    os.remove('image/' + a[0])

executor.start_polling(dp, skip_updates=True)


