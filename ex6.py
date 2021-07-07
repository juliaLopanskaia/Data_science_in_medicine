a = int(input('сколько км ты пробежал сегодня? '))
b = int(input('сколько км ты хочешь пробежать? '))
n = 0 # day
while a <= b:
    a *= 1.1
    n +=1
print(n)
