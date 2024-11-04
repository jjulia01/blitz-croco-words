import os#подключаем библиотеку os
from pptx import Presentation#ипортируем и подключаем из библиотеки pptx класс Presentation
FILE_NAME='Osennyaya_igra_3.pptx'#объявляем и инициализируем переменную FILE_NAME файлом 'Osennyaya_igra_3.pptx'

current_file=os.path.realpath(__file__)#объявляем и инициализируем переменную current_file результатом функции os.path.realpath(__file__)
current_directory=os.path.dirname(current_file)#объявляем и инициализируем переменную current_directory результатом функции os.path.dirname(current_file)
print(current_file) #выводим значение переменной current_file
prs = Presentation('Osennyaya_igra_3.pptx')#открфваем файл Osennyaya_igra_3.pptx' и переносим данные в переменную prs

prs = Presentation(FILE_NAME)#равнозначно команде prs = Presentation('Osennyaya_igra_3.pptx')
for slide in prs.slides:#запускаем цикл for prs.slides по slide
    for shape in slide.shapes:#запускаем цикл for slide.shapes по shape
        if not shape.has_text_frame:#условие выполняется не shape.has_text_frame
            continue#продолжить
        print(shape.text_frame)#выводим результат shape.text_frame