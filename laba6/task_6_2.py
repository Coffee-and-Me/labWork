import re

st = input()
st = st.strip().lower().capitalize()


st = re.sub(r'[\.\?\!]+$', '', st)
st +='.'

print(st)