n = int(input('Digite um numero: '))
i = 0
print('-' * 15)
while (i<=10):
    print('{} x {:2} = {}'.format(n, i, (n * i)))
    i = i + 1
print('-' * 15)
print('Essa é a tabuado do {}'.format(n))

