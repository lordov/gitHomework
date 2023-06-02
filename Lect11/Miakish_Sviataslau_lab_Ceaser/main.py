from PIL import Image
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_TO_READ = "tiger.png"
PATH_TO_READ = os.path.join(ROOT_DIR, FILE_TO_READ)


def main():
    for key in range(0, 255, 25):
        im = Image.open(PATH_TO_READ)
        imag = im.load()

        width, height = im.size  # Определяем размер картинки в пикселях.
        for wdt in range(0, width):  # x - от 0 до размера картинки в пикселях.
            # y - от 0 до размера картинки в пикселях.
            for hgt in range(0, height):
                # Извлекаем значения RGB пикселя находящегося по координатам wdt/hgt.
                (Red, Green, Blue) = imag[wdt, hgt]
            # Мегяем RGB значения пикселей по Цезарю.
                Red, Green, Blue = (
                    (Red + key) % 255,
                    (Green + key) % 255,
                    (Blue + key) % 255,
                )
            # Сохраняем значения RGB для пикселя по координатам wdt/hgt
                imag[wdt, hgt] = (Red, Green, Blue)
        im.save(os.path.join(ROOT_DIR, f'cezar_tiger-{key}.png'))


if __name__ == "__main__":
    print('Ceaser')
    main()
