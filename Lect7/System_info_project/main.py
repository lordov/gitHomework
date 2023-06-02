import functions_module


def main():
    functions_module.display_conditions()

    platfrom_operation = input("Доступные операции 1 2 3 4 5, exit, help:")

    while platfrom_operation != "exit":
        if platfrom_operation == "1":
            print(functions_module.pyt_v())
        elif platfrom_operation == "2":
            print(functions_module.bits_32_or_64())
        elif platfrom_operation == "3":
            print(functions_module.processor())
        elif platfrom_operation == "4":
            print(functions_module.pyth_impl())
        elif platfrom_operation == "5":
            print(functions_module.pyth_version_str())
        elif platfrom_operation == "help":
            print(functions_module.display_conditions())
        else:
            print("Не понимаю!")

        platfrom_operation = input("Доступные операции 1 2 3 4 5, exit, help:")


if __name__ == "__main__":
    print("main.py - Запущена как самостоятельный модуль.")
    main()
else:
    print("main.py - Запущена как импортируемый модуль.")
