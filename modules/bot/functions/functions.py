from aiogram import types


def clear_MD(text):
    text = str(text)
    symbols = ['_', '-', '*', '~', '[', ']', '(', ')', '`', '.']

    for sym in symbols:
        text = text.replace(sym, f"\{sym}")

    return text

def get_text_and_url(text: str) -> list[tuple[str, str]]:
    res = []
    buttons = text.split('\n')[-1]
    for button in buttons.split(']')[0:-1]:
        res.append((button.split('[')[0], button.split('[')[1]))

    return res
