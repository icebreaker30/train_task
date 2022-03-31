file = open('input.txt')
words = {}  # создаем пустой список
for line in file:  # пройдем по строкам файла
    text = list(map(str, line.split()))  # превращаем в список
    for word in text:  # проходимся по каждому слову
        if word not in words:  # 1
            print(0, end=' ')
            words[word] = words.get(word, 0) + 1
        else:  # если слово уже есть в словар
            print(words[word], end=' ')
            words[word] = words.get(word, 0) + 1
