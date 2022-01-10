teks = 'hhiwwdf[dfgg)bqwwci}dfi'
kurung1 = 0
kurung2 = 0
kurung3 = 0
for i in teks:   
    if i == '(' or i == ')':
        kurung1 += 1
    elif i == '{' or i == '}':
        kurung2 += 1
    elif i == '[' or i == ']':
        kurung3 == 1
if kurung1%2 == 0 and kurung2%2 == 0 and kurung3%2 == 0:
    print('Ya')
else:
    print('Tidak')
