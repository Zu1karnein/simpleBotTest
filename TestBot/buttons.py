from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


async def chapter():
    keyboard = InlineKeyboardBuilder()

    keyboard.add(*[
        InlineKeyboardButton(text="Животные", callback_data="animals"),
        InlineKeyboardButton(text="Растения", callback_data="plants"),
        InlineKeyboardButton(text="Птицы", callback_data="birds")
    ])

    return keyboard.as_markup()

# ANIMALS
async def animals_chapter():
    keyboard = InlineKeyboardBuilder()

    keyboard.row(*[
        InlineKeyboardButton(text="Собака", callback_data="dog"),
        InlineKeyboardButton(text="Мышь", callback_data="mouse"),
        InlineKeyboardButton(text="Кошка", callback_data="cat")
    ])

    keyboard.row(*[
        InlineKeyboardButton(text="Назад", callback_data="back_chapter")
    ])


    return keyboard.as_markup()

# animals dog
async def animals_chapter_dog():
    keyboard = InlineKeyboardBuilder()

    keyboard.row(*[
        InlineKeyboardButton(text="Бульдог", callback_data="bulldog"),
        InlineKeyboardButton(text="Бигль", callback_data="Beagle"),
        InlineKeyboardButton(text="Басенджи", callback_data="Basenji")
    ])

    keyboard.row(*[
        InlineKeyboardButton(text="Назад", callback_data="back_chapter_animals")
    ])


    return keyboard.as_markup()

# animals dog bulldog
async def animals_chapter_dog_bulldog():
    keyboard = InlineKeyboardBuilder()

    keyboard.add(*[
        InlineKeyboardButton(text="Назад", callback_data="bulldog_back")
    ])

    return keyboard.as_markup()

# animals mouse
async def animals_chapter_mouse():
    keyboard = InlineKeyboardBuilder()

    keyboard.row(*[
        InlineKeyboardButton(text="Полевая", callback_data="Agrarius"),
        InlineKeyboardButton(text="Желтогорлая", callback_data="flavicollis"),
        InlineKeyboardButton(text="Травяная", callback_data="niloticus")
    ])

    keyboard.row(*[
        InlineKeyboardButton(text="Назад", callback_data="back_chapter_animals")
    ])


    return keyboard.as_markup()

# animals cat
async def animals_chapter_cat():
    keyboard = InlineKeyboardBuilder()

    keyboard.row(*[
        InlineKeyboardButton(text="Абиссинская", callback_data="abyssinian"),
        InlineKeyboardButton(text="Бомбейская", callback_data="bombay"),
        InlineKeyboardButton(text="Бенгальская", callback_data="bengal")
    ])

    keyboard.row(*[
        InlineKeyboardButton(text="Назад", callback_data="back_chapter_animals")
    ])


    return keyboard.as_markup()

# PLANTS
async def plants_chapter():
    keyboard = InlineKeyboardBuilder()

    keyboard.row(*[
        InlineKeyboardButton(text="Цветы", callback_data="flower"),
        InlineKeyboardButton(text="Трава", callback_data="grass"),
        InlineKeyboardButton(text="Дерево", callback_data="tree")
    ])

    keyboard.row(*[
        InlineKeyboardButton(text="Назад", callback_data="back_chapter")
    ])


    return keyboard.as_markup()

# plants flower
async def plants_chapter_flower():
    keyboard = InlineKeyboardBuilder()

    keyboard.row(*[
        InlineKeyboardButton(text="Роза", callback_data="rose"),
        InlineKeyboardButton(text="Тюльпан", callback_data="tulip"),
        InlineKeyboardButton(text="Орхидея", callback_data="orchid")
    ])

    keyboard.row(*[
        InlineKeyboardButton(text="Назад", callback_data="back_chapter_plants")
    ])


    return keyboard.as_markup()

# plants grass
async def plants_chapter_grass():
    keyboard = InlineKeyboardBuilder()

    keyboard.row(*[
        InlineKeyboardButton(text="Овсяница красная", callback_data="redFescue"),
        InlineKeyboardButton(text="Хьонк", callback_data="cheremsha"),
        InlineKeyboardButton(text="Мятлик луговой", callback_data="bluegrassMeadow")
    ])

    keyboard.row(*[
        InlineKeyboardButton(text="Назад", callback_data="back_chapter_plants")
    ])


    return keyboard.as_markup()

# plants tree
async def plants_chapter_tree():
    keyboard = InlineKeyboardBuilder()

    keyboard.row(*[
        InlineKeyboardButton(text="Клён", callback_data="maple"),
        InlineKeyboardButton(text="Липа", callback_data="linden"),
        InlineKeyboardButton(text="Ольха", callback_data="alder")
    ])

    keyboard.row(*[
        InlineKeyboardButton(text="Назад", callback_data="back_chapter_plants")
    ])


    return keyboard.as_markup()

# BIRDS
async def birds_chapter():
    keyboard = InlineKeyboardBuilder()

    keyboard.row(*[
        InlineKeyboardButton(text="Попугай", callback_data="parrot"),
        InlineKeyboardButton(text="Орел", callback_data="eagle"),
        InlineKeyboardButton(text="Курица", callback_data="chicken")
    ])

    keyboard.row(*[
        InlineKeyboardButton(text="Назад", callback_data="back_chapter")
    ])


    return keyboard.as_markup()

# birds parrot
async def birds_chapter_parrot():
    keyboard = InlineKeyboardBuilder()

    keyboard.row(*[
        InlineKeyboardButton(text="Ара", callback_data="ara"),
        InlineKeyboardButton(text="Жако", callback_data="jaco"),
        InlineKeyboardButton(text="Лори", callback_data="lori")
    ])

    keyboard.row(*[
        InlineKeyboardButton(text="Назад", callback_data="back_chapter_birds")
    ])


    return keyboard.as_markup()

# birds eagle
async def birds_chapter_eagle():
    keyboard = InlineKeyboardBuilder()

    keyboard.row(*[
        InlineKeyboardButton(text="Воинственный хохлатый орёл", callback_data="aquila africana"),
        InlineKeyboardButton(text="Ястребиный орёл", callback_data="aquila fasciata"),
        InlineKeyboardButton(text="Беркут", callback_data="aquila chrysaetos")
    ])

    keyboard.row(*[
        InlineKeyboardButton(text="Назад", callback_data="back_chapter_birds")
    ])


    return keyboard.as_markup()

# birds chicken
async def birds_chapter_chicken():
    keyboard = InlineKeyboardBuilder()

    keyboard.row(*[
        InlineKeyboardButton(text="Азиль", callback_data="azil"),
        InlineKeyboardButton(text="Амрокс", callback_data="amrox"),
        InlineKeyboardButton(text="Анкона", callback_data="ancona")
    ])

    keyboard.row(*[
        InlineKeyboardButton(text="Назад", callback_data="back_chapter_birds")
    ])


    return keyboard.as_markup()
