import bot.replies.btntxt as btntxt
import re

def escape_chars(text: str) -> str:
    """Escapes specific cahrs for MARDOWN_V2"""
    return re.sub(r'([|{~}+#>\(\)!=\-.])', r'\\\1', text)

def welcome_back(name:str) -> str:
    return escape_chars(f"""С возвращением, {name}!""")

def welcome_message() -> str:
    return escape_chars(
        """Привет! Я бот, который поможет распарсить резюме.
Отправьте мне резюме в любом формате, и я попробую его распарсить."""
    )

def parsing_result(result: str) -> str:
    return escape_chars(
        f"""*Результат парсинга:*
{result}

*Корректно ли все нашли?*"""
)

def parsing_ok() -> str:
    return escape_chars(
        f"""*Спасибо за фидбэк!*
Мы рады, что все нашли!"""
    )

def error_in_parsing() -> str:
    return escape_chars(
        f"""*Ошибка в парсинге*
Нажмите на кнопку с местом, в котором ошибка"""
    )

def error_reply() -> str:
    return escape_chars(
        f"""*Спасибо за фидбэк!*
Мы записали вашу ошибку. В следующей версии модели будем исправлять!"""
    )