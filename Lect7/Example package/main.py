from packages.summa.plus_mod import plus 

a = 100
b = 300

print(plus(a, b))

if __name__ == '__main__':
    print("main.py - Запущена как самостоятельный модуль.")
else:
    print("main.py - Запущена как импортируемый модуль.")
