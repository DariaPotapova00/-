shortest_word = None
longest_word = None

while True:
    word = input()
    if word == 'стоп':
        break

    if shortest_word is None or len(word) < len(shortest_word):
        shortest_word = word
    if longest_word is None or len(word) > len(longest_word):
        longest_word = word

if set(shortest_word).issubset(longest_word):
    print('ДА')
else:
    print('НЕТ')


