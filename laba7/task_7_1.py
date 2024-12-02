vec = 0

try:
    print('Координаты первого вектора')
    vec1 = list(map(int, input().split()))
    print('Координаты второго вектора')
    vec2 = list(map(int, input().split()))
except ValueError:
    print('error')
    exit()

if len(vec1) != len(vec2):
    print('Разная размерность')
    exit()

for i in range(len(vec1)):
    vec += vec1[i] * vec2[i]

print(vec)