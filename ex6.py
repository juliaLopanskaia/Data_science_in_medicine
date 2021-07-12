def int_func(word):
    print(word.title(), end=' ')



words = input('>>> ')
for word in words.split():
    int_func(word)
print()
