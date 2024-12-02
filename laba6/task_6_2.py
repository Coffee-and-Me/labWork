import re

st = input('Строка: ')
st = st.strip().lower().capitalize()

st = re.sub(r'[\.\?\!]+$', '', st)
st += '.'

print(st)