while True:
    numw = int(input('Deseja ver a tabuada de qual número? '))
    if numw < 0:
        break
    print('-'*20)
    for c in range(1, 11):
        print(f'{numw} x {c} = {numw*c}')
    print('-'*20)
print(f'O valor {numw} é um valor invalido e por isso o programa tabuada encerrada')