from aiogram import Bot, types, utils
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle
from youtube_search import YoutubeSearch

import hashlib

TOKEN = '*'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def hello_message(message):
    await bot.send_message(message.chat.id, "Сәлам, это бот, который показывает столицы и флаги стран")
    await bot.send_message(message.chat.id,
                           "Функции:"
                           "\n /menu - основные функции бота\n /button - выбор страны\n "
                           "/help - опять показать все функции")


@dp.message_handler(commands=['help'])
async def button_message(message):
    await bot.send_message(message.chat.id,
                           "Функции:"
                           "\n /menu - основные функции бота\n /button - выбор страны\n "
                           "/help - опять показать все функции")


@dp.message_handler(commands=['menu'])
async def button_message1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = types.KeyboardButton("Сделать админом")
    item_2 = types.KeyboardButton("Статистика чата")
    item_3 = types.KeyboardButton("Уход бота")
    item_4 = types.KeyboardButton("Забанить тыкальщика")
    item_5 = types.KeyboardButton("Разбанить тыкальщика")
    markup.add(item_1, item_2, item_3, item_4, item_5)
    await bot.send_message(message.chat.id, "Выбери что сделать", reply_markup=markup)


@dp.message_handler(commands=['button'])
async def button_message2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ctr1 = types.KeyboardButton("Россия")
    ctr2 = types.KeyboardButton("Австралия")
    ctr3 = types.KeyboardButton("Австрия")
    ctr4 = types.KeyboardButton("Азербайджан")
    ctr5 = types.KeyboardButton("Албания")
    ctr6 = types.KeyboardButton("Алжир")
    ctr7 = types.KeyboardButton("Англия")
    ctr8 = types.KeyboardButton("Андорра")
    ctr9 = types.KeyboardButton("Аргентина")
    ctr10 = types.KeyboardButton("Армения")
    ctr11 = types.KeyboardButton("Афганистан")
    ctr12 = types.KeyboardButton("Белоруссия")
    ctr13 = types.KeyboardButton("Бельгия")
    ctr14 = types.KeyboardButton("Болгария")
    ctr15 = types.KeyboardButton("Бразилия")
    ctr16 = types.KeyboardButton("Ватикан")
    ctr17 = types.KeyboardButton("Венгрия")
    ctr18 = types.KeyboardButton("Венесуэла")
    ctr19 = types.KeyboardButton("Вьетнам")
    ctr20 = types.KeyboardButton("Гаити")
    ctr21 = types.KeyboardButton("Гвинея")
    ctr22 = types.KeyboardButton("Германия")
    ctr23 = types.KeyboardButton("Гонконг")
    ctr24 = types.KeyboardButton("Греция")
    ctr25 = types.KeyboardButton("Грузия")
    ctr26 = types.KeyboardButton("Дания")
    ctr27 = types.KeyboardButton("Доминикана")
    ctr28 = types.KeyboardButton("Египет")
    ctr29 = types.KeyboardButton("Израиль")
    ctr30 = types.KeyboardButton("Индия")
    ctr31 = types.KeyboardButton("Иран")
    ctr32 = types.KeyboardButton("Италия")
    ctr33 = types.KeyboardButton("Канада")
    ctr34 = types.KeyboardButton("Сша")
    ctr35 = types.KeyboardButton("Украина")
    ctr36 = types.KeyboardButton("Франция")
    markup.add(ctr1, ctr2, ctr3, ctr4, ctr5, ctr6, ctr7, ctr8, ctr9, ctr10, ctr11,
               ctr12, ctr13, ctr14, ctr15, ctr16, ctr17, ctr18, ctr19, ctr20, ctr21, ctr22, ctr23, ctr24, ctr25, ctr26,
               ctr27,
               ctr28, ctr29, ctr30, ctr31, ctr32, ctr33, ctr34, ctr35, ctr36)
    await bot.send_message(message.chat.id, 'Выбирай страну прекрасный пользователь', reply_markup=markup)


@dp.message_handler(content_types='text')
async def message_reply(message):
    if message.text == "Россия":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcPJjdPTU4ihNhrJHZa8Yg31u63f4JQACgwsAAjAqwUlv__NIytDL0SsE')
        await bot.send_message(message.chat.id, "дада")
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcR9jdP84_uZnAQXSQ1R4CPRTHjZBMAACdBcAApxUUUrjuK59Q8iCeisE')
        await bot.send_message(message.chat.id, "все мы знем столицу расии")
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcSFjdP-_6GHTA51yz3G0UOTgoDqWcQACYxgAAsxNUUogE6-eeub21isE')
    elif message.text == "Австралия":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcQVjdPZo4lGpgatzOJoCECHOkaXHjAACsQsAAi0ZwUklwPt_f0Pr7isE')
    elif message.text == "Австрия":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcQljdPdbLUq8wwx9Ju6tB4gksNaBiAACyA4AAqT_wElScgnHnJ2Q4SsE')
    elif message.text == "Азербайджан":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcQ9jdPwmmp2MBkGsuzfQrGuj9-wdKAACLwsAAn-vwEncVY5ToS5oGSsE')
    elif message.text == "Албания":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcRNjdPxbf_-DZb4fPzfjzs7tE_4FBQACdwwAAmNnwEmKQuXFbLgFDysE')
    elif message.text == "Алжир":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcRVjdPxd1k5xK0H1_howT2nFFXRG0gACRg4AAlaQwEkPncMeSaImVCsE')
    elif message.text == "Англия":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcRdjdP2Sac7y6_de-iN5d1PkiIH2xQACiRIAAgaawUn42UxAfFLukisE')
    elif message.text == "Андорра":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcRljdP2UVjffkxum-uIuKDHFImooEgACLAsAAif3wUnw_frWmQQqXSsE')
    elif message.text == "Аргентина":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcRtjdP2VpzxBytxFrQGAAAGwbSSrzYQAAm0LAAIBD8BJRAABnj1ToEVGKwQ')
    elif message.text == "Армения":
        await bot.send_photo(message.chat.id, 'http://www.pravoslavie.ru/sas/image/101147/114735.b.jpg')
        await bot.send_message(message.chat.id, "ой соре, не то")
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcR1jdP2XjNX5XWkezJJQulTAis5SkAACWg4AAhy7wUnN_xuj3Rw-mysE')
    elif message.text == "Афганистан":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcSNjdQABBuzNbqX84TPt8rb8T0I7GVoAAlgMAALKLMBJA5THpnCYVvErBA')
    elif message.text == "Белоруссия":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcSVjdQABCBlxRkR5IcSh62BXHQw-leoAAj0MAAImIMBJ4oWO3ljRZ5MrBA')
    elif message.text == "Бельгия":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcSdjdQABChpYlovZfCYeh9J8wooBLrIAAu4NAAJzhcBJUzFyxrBNR-4rBA')
    elif message.text == "Болгария":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcSljdQABDO1RooQwewABBYk96UTUzNZEAAJODQACIg_BSVRqjcb9sDyuKwQ')
    elif message.text == "Бразилия":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcStjdQABDvY6WAYYjqKjozkNaje3GA0AAo4PAAIJ6MFJGiEu-wrvCoErBA')
    elif message.text == "Ватикан":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcS1jdQABEHKHamvBC_74-CW2XsozDl0AAqkLAALuocFJVydtDHhC0NgrBA')
    elif message.text == "Венгрия":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcS9jdQABEkkPytzOdpUfAjjRO6QoMOEAAsAMAAJ28cBJzBdf0EdYt7MrBA')
    elif message.text == "Венесуэла":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcTFjdQABFHT7MEhJCmNzKhNtpZnvSx0AAvsMAAIxe8FJ1ZW__k6BPG4rBA')
    elif message.text == "Вьетнам":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcTNjdQABFsk2OP59gjvm59irHVk2x9sAAlQLAAItosFJrl038kAnc2crBA')
    elif message.text == "Гаити":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcTVjdQABGAEWjjirnpPPW0tDh1U0p2MAAj0LAAIZPsFJ3J03RaItS6MrBA')
    elif message.text == "Гвинея":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcTdjdQABbRNGUIBZ9z46HnhOCdt9ZF8AAgwKAAJk_8FJZqU7v81aUQIrBA')
    elif message.text == "Германия":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcTljdQABb6KdQVSmMDojuGj2CwI-SnIAAp0LAALc-LhJhsJcOlNYQj0rBA')
    elif message.text == "Гонконг":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcTtjdQABcW19XsUMQYEpQ8gknKqjWWsAAkUMAAIuVsFJ0iAtAuh9wE0rBA')
    elif message.text == "Греция":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcT1jdQABc4zWpcGCVT-ZJ8KIIoyDoTsAAqULAAKcRcBJWPDJSVcZYzkrBA')
    elif message.text == "Грузия":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcT9jdQABdFUeipuzTuAip28bzYeemyoAAl4ZAALzcsFJvg2-HT2RTLkrBA')
    elif message.text == "Дания":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcUFjdQABl_nCKVwH-tym1kg2xOShdJUAAlMMAAKwlblJUxlWPrpQNu0rBA')
    elif message.text == "Доминикана":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcUNjdQABmIwiwJeW0tmX-5V9izFdBscAAicOAAIOV8BJctQR6NYJuXkrBA')
    elif message.text == "Египет":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcUVjdQABmo_OGRk7Jv9RIorrW12S1OAAAvUJAAL88MBJF9YwNqETIWUrBA')
    elif message.text == "Израиль":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcUdjdQABnHq9aS2nGGnkrOpyv7FQ380AAvQMAAJ2McFJEPNYi8wR48crBA')
    elif message.text == "Индия":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcUljdQABn9cdK8BIMDbxt9qcomqkAAEKAAJRCwACHibBSbCAVF1-T89FKwQ')
    elif message.text == "Иран":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcUtjdQABwJJGrQJ0NwOaj0HP3S6lrWEAApsLAAKi6cBJPAAB1WYBqrQqKwQ')
    elif message.text == "Италия":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcU1jdQABwes7vdrsbzVxXi7QZpr8kC0AAhYLAAJN8MBJScdUrcwzKIcrBA')
    elif message.text == "Канада":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcU9jdQABw45ZIJRbkAh4GbGZa_pqbwQAApYNAAKMFMBJeGd3hwJ_6qcrBA')
    elif message.text == "Сша":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcVFjdQAB1pfeBMBTMIcgsVtTQyxFns4AAsIKAALdHMFJDhHaYPxchQwrBA')
    elif message.text == "Украина":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcVNjdQAB6s3yyr_nRaXDpjKwFRw3nFwAAh4JAALDn8BJ7SnS6jgujPIrBA')
    elif message.text == "Франция":
        await bot.send_sticker(message.chat.id,
                               'CAACAgIAAxkBAAEGcVVjdQAB8sZfOMyjplXRPf6mfMYt73QAAm8MAALOFcFJkgceP39CajYrBA')
    elif message.text == "Уход бота":
        await bot.leave_chat(message.chat.id)
    elif message.text == "Статистика чата":
        man1 = await bot.get_chat_member_count(message.chat.id)
        man = str(man1)
        adm = await bot.get_chat_administrators(message.chat.id)
        all_amd = []
        for i in adm:
            all_amd.append(i.user.username)
        a = str('\n'.join(all_amd))
        await bot.send_message(message.chat.id,
                               f'Пользователей: {man} \nАдминов: {len(all_amd)} \nСписок админов: {a}')
    elif message.text == 'Забанить тыкальщика':
        man = await bot.get_chat_member(message.chat.id, message.from_user.id)
        bot_id1 = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        if bot_id1.status != 'administrator' and man.status != 'creator' and man.status != 'administrator':
            await bot.send_message(message.chat.id,
                                   'Выдай сначала админку боту, потом пробуй еще раз')
        elif man.status != 'creator' and man.status != 'administrator':
            await bot.ban_chat_member(message.chat.id, message.from_user.id)
            await bot.send_message(message.chat.id, 'Бан выписан')
        else:
            await bot.send_message(message.chat.id, 'Нельзя забанить, это админ')
    elif message.text == 'Разбанить тыкальщика':
        await bot.unban_chat_member(message.chat.id, message.from_user.id)
        await bot.send_message(message.chat.id, 'Разбанен')
    elif message.text == 'Сделать админом':
        man2 = await bot.get_chat_member(message.chat.id, message.from_user.id)
        bot_id = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        if bot_id.status != 'administrator' and man2.status != 'creator' and man2.status != 'administrator':
            await bot.send_message(message.chat.id,
                                   'Выдай сначала админку боту (c разрешением на добавление админов), потом пробуй еще раз')
        elif bot_id.status == 'administrator' and man2.status != 'creator':
            await bot.promote_chat_member(message.chat.id, message.from_user.id, True, True, True)
            await bot.send_message(message.chat.id, 'Админка выдана')
        else:
            await bot.send_message(message.chat.id, 'Этот пользователь уже админ')


def f(text):
    ans = YoutubeSearch('Антошка', max_results=5).to_dict()
    return ans


@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    text = query.query or 'echo'
    links = f(text)

    name = [types.InlineQueryResultArticle(  # что будет отображаться при вызове inline
        id=hashlib.md5(f'{i["id"]}'.encode()).hexdigest(),
        title=f'{i["title"]}',
        url=f'https://www.youtube.com/watch?v={i["id"]}',
        thumb_url=f'{i["thumbnails"][0]}',
        input_message_content=types.InputTextMessageContent(
            message_text=f'https://www.youtube.com/watch?v={i["id"]}')
    ) for i in links]

    await query.answer(name, cache_time=60, is_personal=True)


if __name__ == '__main__':
    print("bot started")
    executor.start_polling(dp)
