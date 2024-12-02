st_1 = input()
st_2 = input()

while 1:
    st_res = st_1.replace(st_2, '', 1)
    if st_2 in st_res:
        st_1 = st_res
    else:
        break

print(st_1)
