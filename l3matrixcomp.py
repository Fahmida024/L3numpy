import numpy as np

array=np.arange(1,5)
matrix1=array.reshape(2,2)
print(matrix1)

array2=np.arange(6,10)
matrix2=array2.reshape(2,2)
print(matrix2)

while True:
    print('Choose the operation type, 1 for *, 2 for +. 3 for -, 4 for / and 5 for exit')
    choice=int(input('Enter the number of the operation you want to choose '))

    if choice==1:
        result=matrix1*matrix2
        print(result)
    elif choice==2:
        result=matrix1+matrix2
        print(result)
    elif choice==3:
        matrix1-matrix2
        print(result)
    elif choice==4:
        result=matrix1/matrix2
        print(result)
    elif choice==5:
        exit()
        print(result)
    else:
        print('Wrong choice')
    

  


