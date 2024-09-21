def custom_write(file_name):
    n = 0
    strings_position = {}
    for i in info:
        file = open(file_name, 'a', encoding='utf-8')
        tell = (file.tell())
        n += 1
        file.write(f'{i}\n')
        file.close()
        strings_position.update({(n, tell): i})
    return strings_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt')
for elem in result.items():
    print(elem)
