import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, Text
from aiogram.exceptions import TelegramBadRequest
from contextlib import suppress


from buttons import *
from config import TOKEN

# logging start
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()



@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Выберите раздел:', reply_markup=await chapter())



# ANIMALS
@dp.callback_query(F.data == 'animals')
async def data_animals(call: types.CallbackQuery):
    await call.answer()
    if call.message:
        await call.message.edit_text('Выберите подраздел:', reply_markup=await animals_chapter())

# animals dog
@dp.callback_query(F.data == 'dog')
async def data_animals_dog(call: types.CallbackQuery):
    await call.answer()
    if call.message:
        await call.message.edit_text('Выберите вид:', reply_markup=await animals_chapter_dog())

# animals dog bulldog
@dp.callback_query(F.data == 'bulldog')
async def data_animals_dog_bulldog(call: types.CallbackQuery):
    await call.answer()
    if call.message:
        await call.message.edit_text('хорошая собака', reply_markup=await animals_chapter_dog_bulldog())

# back to dog
@dp.callback_query(F.data == 'bulldog_back')
async def back_to_chapter_animals_dog(call: types.CallbackQuery):
    await call.answer()
    if call.message:
        await call.message.edit_text('Выберите вид:', reply_markup=await animals_chapter_dog())

# animals mouse
@dp.callback_query(F.data == 'mouse')
async def data_animals_mouse(call: types.CallbackQuery):
    await call.answer()
    if call.message:
        await call.message.edit_text('Выберите вид:', reply_markup=await animals_chapter_mouse())

# animals cat
@dp.callback_query(F.data == 'cat')
async def data_animals_cat(call: types.CallbackQuery):
    await call.answer()
    if call.message:
        await call.message.edit_text('Выберите вид:', reply_markup=await animals_chapter_cat())

# back to animals
@dp.callback_query(F.data == 'back_chapter_animals')
async def back_to_chapter_animals(call: types.CallbackQuery):
    await call.answer()
    if call.message:
        await call.message.edit_text('Выберите раздел:', reply_markup=await animals_chapter())



# PLANTS
@dp.callback_query(F.data == 'plants')
async def data_plants(call: types.CallbackQuery):
    await call.answer()
    if call.message:
        await call.message.edit_text('Выберите подраздел:', reply_markup=await plants_chapter())

# plants flower
@dp.callback_query(F.data == 'flower')
async def data_animals_flower(call: types.CallbackQuery):
    await call.answer()
    if call.message:
        await call.message.edit_text('Выберите вид:', reply_markup=await plants_chapter_flower())

# plants grass
@dp.callback_query(F.data == 'grass')
async def data_animals_grass(call: types.CallbackQuery):
    await call.answer()
    if call.message:
        await call.message.edit_text('Выберите вид:', reply_markup=await plants_chapter_grass())

# plants tree
@dp.callback_query(F.data == 'tree')
async def data_animals_tree(call: types.CallbackQuery):
    await call.answer()
    if call.message:
        await call.message.edit_text('Выберите вид:', reply_markup=await plants_chapter_tree())

# back to plants
@dp.callback_query(F.data == 'back_chapter_plants')
async def back_to_chapter_plants(call: types.CallbackQuery):
    await call.answer()
    if call.message:
        await call.message.edit_text('Выберите раздел:', reply_markup=await plants_chapter())



# BIRDS
@dp.callback_query(F.data == 'birds')
async def data_birds(call: types.CallbackQuery):
    await call.answer()
    if call.message:
        await call.message.edit_text('Выберите подраздел:', reply_markup=await birds_chapter())

# birds parrot
@dp.callback_query(F.data == 'parrot')
async def data_birds_parrot(call: types.CallbackQuery):
    await call.answer()
    if call.message:
        await call.message.edit_text('Выберите вид:', reply_markup=await birds_chapter_parrot())

# birds eagle
@dp.callback_query(F.data == 'eagle')
async def data_birds_eagle(call: types.CallbackQuery):
    await call.answer()
    if call.message:
        await call.message.edit_text('Выберите вид:', reply_markup=await birds_chapter_eagle())

# birds chicken
@dp.callback_query(F.data == 'chicken')
async def data_birds_chicken(call: types.CallbackQuery):
    await call.answer()
    if call.message:
        await call.message.edit_text('Выберите вид:', reply_markup=await birds_chapter_chicken())

# back to birds
@dp.callback_query(F.data == 'back_chapter_birds')
async def back_to_chapter_birds(call: types.CallbackQuery):
    await call.answer()
    if call.message:
        await call.message.edit_text('Выберите раздел:', reply_markup=await birds_chapter())


# BACK
# button back to chapter
@dp.callback_query(F.data == 'back_chapter')
async def back_to_chapter(call: types.CallbackQuery):
    await call.answer()
    if call.message:
        await call.message.edit_text('Выберите раздел:', reply_markup=await chapter())



# polling start
async def main():
    await bot.send_message(chat_id="1905209181", text="Bot started")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

