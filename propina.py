print("Bienvenido a la calculadora de propina")
bill=input("Cual fue la factura total? $")
percentage=input("Cual porcentaje de propina desea? 10,12 or 15? ")
people=input("Cuantas personas se repartiran el pago? ")
result=(float(bill)/float(people))*float("1."+percentage)
print(f"Cada persona debera pagar: ${round(result,2)}")
#otra forma de redondear
result2 = "{:.2f}".format(result)
print(f"Cada persona debera pagar: ${result2}")

