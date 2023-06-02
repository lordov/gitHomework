import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_TO_SAVE = "KEKL.txt"
PATH_TO_SAVE = os.path.join(ROOT_DIR, FILE_TO_SAVE)
SEP = "\n"

print(ROOT_DIR)
print(FILE_TO_SAVE)
print(PATH_TO_SAVE)

li = [li for li in range(5)]
di = {1: 'Задача № '}
results = f'{li} + {SEP} + {di}'

with open(PATH_TO_SAVE, 'w', encoding="utf-8") as file:
    file.write(results)
