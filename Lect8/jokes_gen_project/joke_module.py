import emoji
import pyjokes
import random
from googletrans import Translator


def get_jokes():
    '''
    Функция, которая выводит рандомные шутки
    на английскоми и переводит их на русский язык.
    '''
    # Создаем список смайлов исходя из таблицы из интернета.
    emoji_list = [
    ":laughubg:",
    ":flushed:",
    ":sweat_smile:",
    ":joy:",
    ":alien:",
    ":thumbsup:",
    ":fire:",
    ]
    # Получаем шутки на английском языке.
    kekl_joke = pyjokes.get_joke(language="en", category="neutral")
    # Облагораживаем шутки смайликами(emoji).
    emoji_for_kekl = emoji_list[random.randint(
        0, len(emoji_list)-1)] * random.randint(0, 4)
    # Соеденяем получившуюся шутку и наши смайлы.
    final_kekl_eng = f'{kekl_joke} {emoji_for_kekl}'
    # Выводим шутку на английском языке.
    print(emoji.emojize(final_kekl_eng, language="alias"))
    print()
    
    # Подключаемся к переводчику.
    translator = Translator(service_urls=["translate.googleapis.com"])
    # Задаем переводчику что и на какой язык переводить.
    final_kekl_rus = translator.translate(kekl_joke, dest="ru")
    # Соединяем переведенный текст и смайлики.
    final_kekl_rus = f"{final_kekl_rus.text} {emoji_for_kekl}"
    # Распечатываем перевод.
    print(emoji.emojize(final_kekl_rus, language="alias"))
    print(len(final_kekl_rus)* "_")



if __name__ == "__main__":
    print("Joke_module.py Запущен самостоятельно")
else:
    print("Joke_module.py Запущен как импорт")
