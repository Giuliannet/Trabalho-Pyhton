'''
variável = 2

lista = [1,2,3]

matriz = [
    [1,2,3],
    [8,9,10]
]

'''






       
def aula ():
    matriz =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
    print(matriz[1][2])

    matriz[0][0] = 10

    for i in range(3):
        for p in range (len(matriz[i])):
            
            print(f'{matriz[i][p]}',end='') 
        print('') 
aula()

 