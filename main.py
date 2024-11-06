import os#подключаем библиотеку os
from pathlib import Path
from zipfile import ZipFile
from helpers import get_words_form_file, check_spelling, save_words_to_file

ZIP_FILENAME = "croco-blitz-source.zip"

def is_not_valid(text: str) -> bool:
    return ' ' in text or '-' in text or ':' in text or 'СУПЕРКРОКО' in text

def read_zip_file():
    current_folder = os.path.dirname(os.path.realpath(__file__))#в переменную записываем путь к текущему файлу

    words: set[str] = set()

    with ZipFile(Path(current_folder) / 'src' / ZIP_FILENAME) as archive:
        for f in archive.namelist():
            words.update(get_words_form_file(archive.open(f)))

    checked_words_in_string: list[str] = check_spelling(words)
    save_words_to_file(checked_words_in_string, 'words.txt')

if __name__ == "__main__":
    read_zip_file()


# import os#подключаем библиотеку os
# from pathlib import Path
# from zipfile import ZipFile
# from pptx import Presentation#ипортируем и подключаем из библиотеки pptx класс Presentation
# FILE_NAME='Osennyaya_igra_3.pptx'#записываем в переменную FILE_NAME путь к файлу 'Osennyaya_igra_3.pptx'

# def is_not_valid(text: str) -> bool:
#     return ' ' in text or '-' in text or ':' in text or 'СУПЕРКРОКО' in text

# def read_zip_file():
#     words = list()
#     current_file=os.path.realpath(__file__)#в переменную записываем путь к текущему файлу
#     print(f'{current_file=}')#выводим путь текущего файла
#     current_directory=os.path.dirname(current_file)#в переменную записываем путь к текущей директории
#     print(f'{current_directory=}')#выводим путь текущей директории  
#     prs = Presentation(FILE_NAME)#записываем в переменную данные из файла
#     for slide in prs.slides:#перебираем слайды
#         for shape in slide.shapes:#перебираем форму
#             if not shape.has_text_frame:#условие, чтобы на слайде не было текста
#                 continue#если условие выполняется, продолжаем перебирать слайды
#             if is_not_valid(shape.text):    
#                 continue
#             words.append(shape.text)#если условие не выполняется, то выводим текст со слайда 



# with open("words.txt", "w", encoding="utf-8") as file:
#     print(*words, file=file)

