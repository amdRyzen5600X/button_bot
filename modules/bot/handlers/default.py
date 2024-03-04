from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from modules.bot.functions.functions import get_text_and_url

from ...logger import Logger
from ..keyboards.default import add_custom_button


@Logger.log_msg
async def start(message: types.Message, state: FSMContext):
    text = """это бот для создания постов с кнопками

напиши текст для поста и в конце через отдельным параграфом через пробел укажи текст для кнопки в квадратных скобках укажи саму ссылку

пример: 
<blockquote>текст для длинного поста

кнопка1[link1.com] кнопка2[link2.org] кнопка3[link3.kz]</blockquote>"""
    await message.reply(text)
    await state.finish()

@Logger.log_msg
async def handle_post(message: types.Message, state: FSMContext):
    text = message.text
    buttons = get_text_and_url(text)
    kb: types.InlineKeyboardMarkup | None = None
    for button in buttons:
        kb = add_custom_button(text=button[0], link=button[1], kb=kb)

    Logger.info(str(kb))
    
    await message.answer(text='\n'.join(text.split('\n')[0:-1]), reply_markup=kb)

def register_handlers_default(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start", "help"], state="*")
    dp.register_message_handler(handle_post, state="*")
