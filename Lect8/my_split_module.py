def mysplit_function(string):
    # Проверяем пустая ли строка.
    if string == "":
        return []
    
    # Создаем переменные для работы.
    words = []
    current_word = ""
    
    # Итерируем каждый символ в строке.
    for char in string:
        # Проверяем пустой ли символ.
        if char.isspace():
            # Если слово не является пустым добавляем его в список слов.
            if current_word:
                words.append(current_word)
                current_word = ""
        else:
            # ЕЕсли символ не пробел то добовляем его к текущему слову.
            current_word += char
    
    # Возвращаем список.
    return words




if __name__ == "__main__":
    print("mysplit_module.py -- Запущена как самостоятельная программа.\n")
    print(mysplit_function("To be or not to be, that is the question"))
    print(mysplit_function("To be or not to be,that is the question"))
    print(mysplit_function(" "))
    print(mysplit_function(" abc "))
    print(mysplit_function(""))
else:
    print("mysplit_module.py -- Запущена как импорт.")
