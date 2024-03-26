from aiogram import Bot
from aiogram.types import FSInputFile

from core.keyboards.inline import plan, plan_2


async def send_message_time(bot: Bot, chat_id: int):
    await bot.send_message(chat_id, f'Это сообщение отправлено через несколько секунд после старта бота')

async def send_message_cron(bot: Bot, chat_id: int):
    await bot.send_message(chat_id, f'Это сообщение будет отправляться ежедневно в указанное время')


async def send_message_interval(bot: Bot, chat_id: int):
    await bot.send_message(chat_id, f'Это сообщение будет отправляться с интервалом в 1 минуту')


async  def send_message_middleware(bot: Bot, chat_id: int):
    await  bot.send_message(chat_id, f'А как реализовывать план?🧐\n'
                                     f'Это мы разбираем на бесплатном мастер-классе.\n'
                                     f'Регистрируйтесь, чтобы понять, как действовать правильно. Кроме этого расскажем, '
                                     f'где взять деньги для открытия своего заведения уже в этом году👇🏼',
                            reply_markup=plan)


async  def send_message_middleware_2(bot: Bot, chat_id: int):
    # await  bot.send_message(chat_id, f'А мы не договорили…\n'
    #                                  f'При создании своего заведения мало пользы не бывает!\n'
    #                                  f'Больше разборов, полезных рекомендаций и историй студентов — на нашем '
    #                                  f'youtube-канале. И это все бесплатно🤯\n'
    #                                  f'Подписывайтесь👇🏼', reply_markup=plan_2)
    photo = FSInputFile(path=r'C:\Users\k.lavkin\Desktop\2.jpeg')
    await  bot.send_photo(chat_id, photo=photo, caption=f'А мы не договорили…\n'
                                     f'При создании своего заведения мало пользы не бывает!\n'
                                     f'Больше разборов, полезных рекомендаций и историй студентов — на нашем '
                                     f'youtube-канале. И это все бесплатно🤯\n'
                                     f'Подписывайтесь👇🏼', reply_markup=plan_2)
