from aiogram import Bot
from aiogram.types import Message, FSInputFile
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
from core.handlers.apsched import send_message_middleware, send_message_middleware_2


async  def get_start(message: Message, bot: Bot, apscheduler: AsyncIOScheduler):
    await bot.send_message(message.from_user.id, f'<b>Привет {message.from_user.first_name}. Нажимайте на файлик,'
                                                 f' в нем вас ждет подробная инструкция открытия своего заведения'
                                                 f' по шагам.</b>')
    document = FSInputFile(path=r'C:\Users\k.lavkin\Desktop\План!.docx')
    await bot.send_document(message.chat.id, document=document)
    apscheduler.add_job(send_message_middleware, trigger='date', run_date=datetime.now() + timedelta(seconds=10),
                        kwargs={'bot': bot, 'chat_id': message.from_user.id})
    apscheduler.add_job(send_message_middleware_2, trigger='date', run_date=datetime.now() + timedelta(seconds=20),
                        kwargs={'bot': bot, 'chat_id': message.from_user.id})
