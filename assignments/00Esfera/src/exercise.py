import math

def main():
    #escribe tu código abajo de esta línea
    print('Área y volúmen de una esfera')

    r = float(input('Dame el radio: '))

    a = 4* math.pi* math.pow(r,2)
    v = (4/3)* math.pi* math.pow(r,3)
    
    print(f'El área es: {a}')
    print(f'El volúmen es: {v}')


if __name__=='__main__':
    main()
