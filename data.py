dictionary = {
    '1': 'meat.txt',
    '2': 'meat.txt',
    '3': 'fish.txt',
    '4': 'vegetable.txt',
    '5': 'vegetable.txt',
    '6': 'soup.txt'
}
count = 0
with open('read.txt', 'r', encoding='utf-8') as file:
    line = file.readline()
    while line:
        if '：' in line:
            food = line.split('：')[0]
            with open(dictionary.get(str(count)), 'a', encoding='utf-8') as wf:
                wf.write(food + '\n')
        else:
            count += 1
        line = file.readline()
