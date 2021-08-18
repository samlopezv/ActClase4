import math

def main():
    #escribe tu código abajo de esta línea
    print('Este programa calcula el área de un triángulo')

    a= int(input('Dame el valor de a:'))
    b= int(input('Dame el valor de b:'))
    c= int(input('Dame el valor de c:'))

    s = (a+b+c)/2
    area = math.sqrt (s*(s-a)*(s-b)*(s-c))
    
    print(f'El área del trángulo es: {area}')

if __name__=='__main__':
    main()
