import re

while 1:
    st = input()
    if st == '':
        exit()
    res = re.fullmatch(r'^[^<>\\|?*]+(\.txt|\.doc|\.docx|\.odt|\.rtf)$', st)
    if res:
        print('Данная строка может быть названием файла')
    else:
        print('Данная строка не может быть названием файла')
