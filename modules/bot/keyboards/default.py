from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)


def add_custom_button(
        text: str,
        link: str,
        kb: InlineKeyboardMarkup | None = None,
) -> InlineKeyboardMarkup:
    if kb is None:
        kb = InlineKeyboardMarkup()

    button = InlineKeyboardButton(text, url=link)
    kb.add(button)

    return kb
