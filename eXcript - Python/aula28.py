num1=55 # int(input("Informe um número: "))

if(num1>10):
    print("O valor é maior que 10")
    if(num1<15):
        print("Maior que 10, porém menor que 15")
    else:
        if(num1<=50):
            print("O valor é maior que 10 e menor que 50")
        else:
            print("O valor é maior que 50")
else:
    if(num1>5):
        print("O número é menor que 10 e maior que 5")
        if(num1==7):
            print("O número é igual a 7")
    else:
        print("O número é menor que 5")
