import re

st = input('Номер авто: ')

reg = re.match(r'^[a-zA-Z]{2}[0-9]{3}[a-zA-Z]$', st)
if reg:
    print('Да, такой номер подходит')
else:
    print('Номер не подходит')