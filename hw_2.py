# 1) Напишите телеграмм бот для IT курса. Бот предназначен для предоставления
# информации для пользователя о IT курсах.
# В боте есть 5 команды (backend, frontend, uxui, android, ios)
# Каждая команда выдает 3 информации (информация о направлении, стоимость курса,
# месяц обучения) Пользователь: Нажимает кнопку запустить
# Бот: Приветствует пользователя и выдает 5 кнопок (backend, frontend, uxui, android, ios)
# Пользователь: Пользователь нажимает backend Бот выдает сообщение:
# Backend — это внутренняя часть сайта и сервера и т.д Стоимость 10000 сом в месяц
# Обучение: 5 месяц ДОП ЗАДАНИЕ:
# 2) Загрузить код в GitHub и сделать кнопки для направлени


from aiogram import Bot, Dispatcher, types, executor
from config import token

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    buttons = ['backend', 'frontend', 'uxui', 'android', 'ios']
    keyboard.add(*buttons)
    await message.answer("Приветствую! Выберите одно из направлений:", reply_markup=keyboard)

@dp.message_handler(content_types=types.ContentType.TEXT)
async def handle_text(message: types.Message):
    text = message.text.lower()
    if text == 'backend':
        response = "Backend — это внутренняя часть сайта и сервера и т.д\nСтоимость: 10000 сом в месяц"
    elif text == 'frontend':
        response = "Frontend — это клиентская часть сайта, которую видит пользователь\nСтоимость: 9000 сом в месяц"
    elif text == 'uxui':
        response = "UX/UI — это дизайн интерфейса пользователя\nСтоимость: 8000 сом в месяц"
    elif text == 'android':
        response = "Android — разработка мобильных приложений для операционной системы Android\nСтоимость: 11000 сом в месяц"
    elif text == 'ios':
        response = "iOS — разработка мобильных приложений для операционной системы iOS\nСтоимость: 12000 сом в месяц"
    else:
        response = "Пожалуйста, выберите одно из предложенных направлений."

    await message.answer(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)