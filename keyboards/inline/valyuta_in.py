from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

key=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="EUR🇪🇺",callback_data='eur'),
            InlineKeyboardButton(text="USD🇺🇸",callback_data='usd')
        ],
        [
            InlineKeyboardButton(text="RUB🇷🇺",callback_data='rub'),
            InlineKeyboardButton(text='KWD🇰🇼',callback_data='kwd')
        ]
    ]
)


key_back=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Orqaga🔙",callback_data='orqa'),

        ]
    ]
)