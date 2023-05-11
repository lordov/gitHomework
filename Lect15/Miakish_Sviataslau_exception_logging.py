import logging


def main():
    logging.basicConfig(filename='exc.log', filemode='w')
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    li = [x for x in range(0,50)]
    li_op = [0 if op % 2 == 0 else 1 for op in range(0, 50)]

    for a, b in zip(li, li_op):
        try:
            c = a / b
        except Exception as e:
            # Вариант 1.
            # logger.error(f'Exception occured: {a} / {b} --> {e}')
            # Вариант 2.
            logger.exception('Exception occured:')


if __name__ == "__main__":
    main() 
    print('Программа заупщена самостоятельно.')
else:
    print('Программа запущена как модуль.')
