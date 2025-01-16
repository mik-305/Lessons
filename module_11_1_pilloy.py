from PIL import Image
from PIL import ImageFilter


# ---------------- ГРАФИКА -------------------------
filename = "cat.jpg"                    # Входной файл с изображением
with Image.open(filename) as img:
    img.load()

img.show()

cropped_img = img.crop((130, 200, 900, 900))

low_res_img = cropped_img.reduce(2)     # Уменьшенное изображение
low_res_img.show()

cropped_img.size
(400, 850)                              # Обрезка изображения по координатам
cropped_img.show()                      # Показ результирующего изображения
cropped_img.save("cat_cropped.jpg")

gray_img = img.convert("L")  # Grayscale # В градациях серого
gray_img.show()                         # Показ результирующего изображения

blur_img = img.filter(ImageFilter.BLUR)
img.filter(ImageFilter.BoxBlur(20)).show()  # Размытое изображение

img_gray = img.convert("L")
edges = img_gray.filter(ImageFilter.FIND_EDGES)
img_gray_smooth = img_gray.filter(ImageFilter.SMOOTH)
edges_smooth = img_gray_smooth.filter(ImageFilter.FIND_EDGES)
edges_smooth.show()                         # В режиме обнаружения границ

rotated_img = img.rotate(45, expand=True)    # Поворот изобразения на 45 градусов
rotated_img.show()                      # Показ результирующего изображения
rotated_img.save("cat_45.jpg")

#img.show()
