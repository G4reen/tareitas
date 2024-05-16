import os
import time


pikachuroll_price=4500.0
otakuroll_price=5000.0
pulporoll_price=5200.0
Anguilaroll_price=4800.0


print("*****************************")
print("*Bienvenido a delivery sushi*")
print("*****************************")
input("Presione para continuar")
while True:
    total=0
    code_descuento="cualquiercosa"
    descuento="cualquiercosa"
    totalproductos=0
    totalpika=0
    totalotaku=0
    totalpulpo=0
    totalanguila=0
    des_detotal=0
    des_aplicado=0
    while True:
        os.system("cls")
        match int(input("Que desea pedir?:\n[1]Pikachu roll $4500\n[2]Otaku roll $5000\n[3]Pulpo Venenoso roll $5200\n[4]Anguila Eléctrica roll $4800\n[0]Terminar\n>>>")):
            case 1:
                total +=pikachuroll_price
                os.system("cls")
                totalproductos+=1
                totalpika+=1
            case 2:
                total +=otakuroll_price
                os.system("cls")
                totalproductos+=1
                totalotaku+=1
            case 3:
                total +=pulporoll_price
                os.system("cls")
                totalproductos+=1
                totalpulpo+=1
            case 4:
                total +=Anguilaroll_price
                os.system("cls")
                totalproductos+=1
                totalanguila+=1
            case 0:
                os.system("cls")
                break

    while code_descuento=="x" or code_descuento!="soyotaku":        
        descuento=int(input("posee usted un codigo de descuento?\n[1]Si\n[2]No\n>>>"))
        if descuento ==1:
            while True:
                code_descuento=input('Ingrese su codigo de descuento(si desea salir ingrese "x"):\n>>>')
                if code_descuento=="soyotaku" or code_descuento=="x":
                    os.system("cls")
                    break
                else:
                    print("ingrese un codigo valido..."),input("")
                    os.system("cls")
        else:
            os.system("cls")
            break
        if code_descuento=="soyotaku":
            des_detotal= total*0.1 
            des_aplicado = total-des_detotal
    print("******************************")
    print(f"TOTAL PRODUCTOS:{totalproductos}")
    print("******************************")
    print(f"Pikachu Roll : {totalpika}\nOtaku Roll : {totalotaku}\nPulpo Venenoso Roll: {totalpulpo}\nAnguila Eléctrica Roll: {totalanguila}")
    print("****************************** ")
    print(f"Subtotal por pagar: ${total}")
    if code_descuento == "soyotaku":
        print(f"Descuento por codigo: ${des_detotal}\n")
        print(f"TOTAL: ${des_aplicado}")
    else:
        print(f"TOTAL: ${total}")
    
    continuar=int(input("Desea realizar otro pedido?\n[1]Si\n[2]No\n>>>"))
    if continuar==2:
        break

    
    
    
        