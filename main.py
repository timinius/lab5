print('Введите текст:')
text = str(input())
print('Введите сдвиг:')
num = int(input())

list_text = list(text)
list_text1 = list(text)
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

for i in range(0, (len(list_text))):
    if list_text[i] in alphabet:
        list_text[i] = alphabet[alphabet.index(list_text[i]) + num]
    else:
        if list_text[i].lower() in alphabet:
            list_text[i] = alphabet[alphabet.index(list_text[i].lower()) + num].upper()

for i in range(0, (len(list_text1))):
    if list_text1[i] in alphabet:
        list_text1[i] = alphabet[alphabet.index(list_text1[i]) - num]
    else:
        if list_text1[i].lower() in alphabet:
            list_text1[i] = alphabet[alphabet.index(list_text1[i].lower()) - num].upper()


print('''Зашифрованный с помощью шифра Цезаря текст:''', '\n')
print(''.join(list_text), '\n')
print('''Разшифрованный с помощью шифра Цезаря текст:''', '\n')
print(''.join(list_text1))