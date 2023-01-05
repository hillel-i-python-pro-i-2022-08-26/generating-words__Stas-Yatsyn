import string
word_size = int(input('Введіть довжину слова==>'))
alphabet = list(string.ascii_lowercase + string.digits)

final_list = []
black_list = []
for r in alphabet:
    final_list.append(r)
if word_size == 1:
    print('Файл з словами згенеровано УСПІШНО!!!')
elif word_size > 1:
    for i in range(word_size-1):
        for k in alphabet:
            for j in final_list:
                black_list.append(f'{k}{j}')
        final_list = []
        for p in black_list:
            final_list.append(p)
            print(f'Генерую ==> {p}')
        black_list = []
    print('Файл з словами згенеровано УСПІШНО!!!')

elif word_size < 1:
    print('Число має бути більше або == 1')

with open("123.txt", "w") as file:
    print(*final_list, file=file, sep="\n")