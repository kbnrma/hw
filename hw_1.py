# 1) Напишите телеграмм бот который загадывает случайное число с помощью
# библиотеки random и вы должны угадать его.
# Бот: Я загадал число от 1 до 3 угадайте
# Пользователь: Вводит число 2, если число правильное то выводит “Правильно вы
# отгадали”
# ДОП ЗАДАНИЕ:
# 2) Загрузить файлы в GitHub с .gitignore


from aiogram import Bot, Dispatcher, types, executor
import random
from config import token

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands = 'start')
async def start(message:types.Message):
    await message.answer(f"Я загадал число от 1 до 3 угадайте,` {message.from_user.full_name}!")
 
@dp.message_handler()
async def guess_number(message: types.Message):
    user_number = message.text.strip()
    if not user_number.isdigit():
        await message.answer("Пожалуйста, введите только число.")
        return

    user_number = int(user_number)
    bot_number = random.randint(1, 3)

    if user_number == bot_number:
        await message.answer("Правильно, вы отгадали!")
    else:
        await message.answer(f"Неверно. Я загадал число {bot_number}.")

if __name__ == '__main__':
    executor.start_polling(dp)



