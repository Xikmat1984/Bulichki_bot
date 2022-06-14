from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardMarkup,InlineKeyboardButton,CallbackQuery
Bosh_sahifa=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Buluchkalar"),
            KeyboardButton(text="Boshqa shirinliklar"),
            KeyboardButton(text="Buluchkalar"),
        ],
    ], resize_keyboard=True
)

types_bulochka=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kremli buluchka",callback_data="krem"),
            InlineKeyboardButton(text="Oddiy buluchka",callback_data="Oddiy")],
        [
            InlineKeyboardButton(text="Xitoy ko'k paket  bulochka",callback_data="Xitoy_sariq"),
            InlineKeyboardButton(text="Xitoy Sariq paket  bulochka",callback_data="Xitoy_kok")
        ]

    ]

)
raqamlar=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1"),
            KeyboardButton(text="2"),
            KeyboardButton(text="3")

        ],
        [
            KeyboardButton(text="4"),
            KeyboardButton(text="5"),
            KeyboardButton(text="6")

        ],
        [
            KeyboardButton(text="7"),
            KeyboardButton(text="8"),
            KeyboardButton(text="9")

        ],
        [
            KeyboardButton(text="10"),
            KeyboardButton(text="15"),
            KeyboardButton(text="20")

        ],

    ],resize_keyboard=True

)