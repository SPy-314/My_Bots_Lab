import random
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


MAGIC_8_BALL_ANSWERS = [
    "Бесспорно", "Предрешено", "Никаких сомнений",
    "Определённо да", "Можешь быть уверен в этом",
    "Мне кажется — да", "Вероятнее всего", "Хорошие перспективы",
    "Знаки говорят — да", "Да",
    "Пока не ясно, попробуй снова", "Спроси позже", "Лучше не рассказывать",
    "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять",
    "Даже не думай", "Мой ответ — нет", "По моим данным — нет",
    "Перспективы не очень хорошие", "Весьма сомнительно"
]


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = ''

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands="start"))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


# Этот хэндлер заменяет echo на магический шар
@dp.message()
async def magic_8_ball(message: Message):
    answer = random.choice(MAGIC_8_BALL_ANSWERS)
    await message.reply(answer)



if __name__ == '__main__':
    dp.run_polling(bot)