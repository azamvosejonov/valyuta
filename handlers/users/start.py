from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
import requests
from keyboards.inline.valyuta_in import key,key_back
from loader import dp
from states.valyuta_st import Valyuta
from aiogram.dispatcher import FSMContext



@dp.message_handler(CommandStart())
async def valyuta(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\nBu valyuta bot\n barcha valyuta malumotlarni ko`rmoqchi\n bo`lsangiz /valyuta deb yozing!!!")
    await message.answer("Valyutani tanlang", reply_markup=key)
    await Valyuta.choice.set()


@dp.callback_query_handler(lambda c: c.data in ["eur", "usd", "rub", "kwd"], state=Valyuta.choice)
async def handle_currency_choice(call: CallbackQuery, state: FSMContext):
    if call.data == "eur":
        response = "yevro"
    elif call.data == "usd":
        response = "dollar"
    elif call.data == "rub":
        response = "rubl"
    elif call.data == "kwd":
        response = "quvayt"
    else:
        response = "Xatolik"
    await state.update_data({'choice': response})
    await call.message.delete()
    await call.message.answer("Miqdorni kiriting")
    await Valyuta.amount.set()


@dp.message_handler(state=Valyuta.amount)
async def handle_amount(message: types.Message, state: FSMContext):
    try:
        num = int(message.text)
    except ValueError:
        await message.answer("Faqat son kiriting!")
        await state.finish()
        return

    # Fetch exchange rates
    response = requests.get(url='https://cbu.uz/uz/arkhiv-kursov-valyut/json/')
    dt = response.json()

    # Retrieve user's choice from state
    datao = await state.get_data()
    currency = datao['choice']
    rate = None

    # Match the selected currency
    if currency == 'yevro':
        rate = float(dt[2]['Rate'])
    elif currency == 'dollar':
        rate = float(dt[1]['Rate'])
    elif currency == 'rubl':
        rate = float(dt[3]['Rate'])
    elif currency == 'quvayt':
        rate = float(dt[37]['Rate'])

    if rate:
        javob = num * rate
        await message.answer(f"{num} {currency} -> {javob:.2f} so'm",reply_markup=key_back)
    else:
        await message.answer("Xatolik yuz berdi!")

    # Finish state
    await state.finish()

@dp.callback_query_handler(text="orqa")
async def course_callback_message(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Kursni tanlang", reply_markup=key)




flags = {
    "USD": "🇺🇸",
    "EUR": "🇪🇺",
    "RUB": "🇷🇺",
    "GBP": "🇬🇧",
    "JPY": "🇯🇵",
    "AZN": "🇦🇿",
    "BDT": "🇧🇩",
    "BGN": "🇧🇬",
    "BHD": "🇧🇭",
    "BND": "🇧🇳",
    "BRL": "🇧🇷",
    "BYN": "🇧🇾",
    "CAD": "🇨🇦",
    "CHF": "🇨🇭",
    "CNY": "🇨🇳",
    "CUP": "🇨🇺",
    "CZK": "🇨🇿",
    "DKK": "🇩🇰",
    "DZD": "🇩🇿",
    "EGP": "🇪🇬",
    "AFN": "🇦🇫",
    "ARS": "🇦🇷",
    "GEL": "🇬🇪",
    "HKD": "🇭🇰",
    "HUF": "🇭🇺",
    "IDR": "🇮🇩",
    "ILS": "🇮🇱",
    "INR": "🇮🇳",
    "IQD": "🇮🇶",
    "IRR": "🇮🇷",
    "ISK": "🇮🇸",
    "JOD": "🇯🇴",
    "AUD": "🇦🇺",
    "KGS": "🇰🇬",
    "KHR": "🇰🇭",
    "KRW": "🇰🇷",
    "KWD": "🇰🇼",
    "KZT": "🇰🇿",
    "LAK": "🇱🇦",
    "LBP": "🇱🇧",
    "LYD": "🇱🇾",
    "MAD": "🇲🇦",  # Marokash dirhami
    "MDL": "🇲🇩",  # Moldaviya leyi
    "MMK": "🇲🇲",  # Myanma k'yati
    "MNT": "🇲🇳",  # Mongoliya tugriki
    "MXN": "🇲🇽",  # Meksika pesosi
    "MYR": "🇲🇾",  # Malayziya ringgiti
    "NOK": "🇳🇴",  # Norvegiya kronasi
    "NZD": "🇳🇿",  # Yangi Zelandiya dollari
    "OMR": "🇴🇲",  # Ummon riali
    "PHP": "🇵🇭",  # Filippin pesosi
    "PKR": "🇵🇰",  # Pokiston rupiyasi
    "PLN": "🇵🇱",  # Polsha zlotiysi
    "QAR": "🇶🇦",  # Qatar riali
    "RON": "🇷🇴",  # Ruminiya leyi
    "RSD": "🇷🇸",  # Serbiya dinori
    "AMD": "🇦🇲",  # Armaniston drami
    "SAR": "🇸🇦",  # Saudiya Arabistoni riali
    "SDG": "🇸🇩",  # Sudan funti
    "SEK": "🇸🇪",  # Shvetsiya kronasi
    "SGD": "🇸🇬",  # Singapur dollari
    "SYP": "🇸🇾",  # Suriya funti
    "THB": "🇹🇭",  # Tailand bati
    "TJS": "🇹🇯",  # Tojikiston somonisi
    "TMT": "🇹🇲",  # Turkmaniston manati
    "TND": "🇹🇳",  # Tunis dinori
    "TRY": "🇹🇷",  # Turkiya lirasi
    "UAH": "🇺🇦",  # Ukraina grivnasi
    "AED": "🇦🇪",  # BAA dirhami
    "UYU": "🇺🇾",  # Urugvay pesosi
    "VES": "🇻🇪",  # Venesuela bolivari
    "VND": "🇻🇳",  # Vetnam dongi
    "XDR": "🌐",    # SDR
    "YER": "🇾🇪",  # Yaman riali
    "ZAR": "🇿🇦"   # Janubiy Afrika randi

}

@dp.message_handler(commands=['valyuta'])
async def bot_start(message: types.Message):
    url = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
    response = url.json()

    valyutalar = []
    for item in response:
        valyuta_nomi = item['CcyNm_UZ']
        valyuta_kursi = item['Rate']
        valyuta_code = item['Ccy']

        bayroq = flags.get(valyuta_code, "")

        valyutalar.append(f"{bayroq} 1 {valyuta_nomi} ~ {valyuta_kursi}\n")

    await message.answer("\n".join(valyutalar))

@dp.message_handler(commands='onesatart')
async def bot_start(message: types.Message):
    urls = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
    emanzil = urls.json()
    bayrak = []
    await message.reply("davlatni kiriting!!!")


    for items in emanzil:
        valyutanomi=items['CcyNm_UZ']
        valyutakursi=items['Rate']
        valyutakode=items['Ccy']

        bayroqlar = flags.get(valyutakode, "")

        bayrak.append(f"{bayroqlar} 1 {valyutanomi} ~ {valyutakursi}\n")

        if bayrak:
            await message.answer("\n".join(bayrak))
        else:
            await message.answer("Ma'lumotlar mavjud emas.")

