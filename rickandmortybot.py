#загружаю библиотеки для чтения файла и создания бота
import json
import requests
from aiogram import Bot, Dispatcher, executor, types

#привязка программы к конкретному боту через токен
tg_bot_token = ('5319929269:AAH8ajCwqReDIoSR7ZdBP9y2cfaENN44BOU')
bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

#общение с ботом
@dp.message_handler(commands=['start'])
async def starter(message: types.Message):
   await message.reply(f"About which 'Rick and Morty' character do you want to know?")

#ответки бота через спаршенный api
@dp.message_handler()
async def inforickandmorty(message: types.Message):
   try:
      r = requests.get(f'https://rickandmortyapi.com/api/character/?name={message.text}')
      character = r.json()['results'][0]['name']
      deadoralive = r.json()['results'][0]['status']
      vid = r.json()['results'][0]['species']
      pol = r.json()['results'][0]['gender']
      roja = r.json()['results'][0]['image']
      await message.reply(f'Character: {character} \n Status: {deadoralive} \n Species: {vid} \n Gender: {pol} \n Looks like: {roja}')

   except:
      await message.reply(f'Something went wrong')


if __name__ == '__main__':
   executor.start_polling(dp)


