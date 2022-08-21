# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	print(" Ingresar la cantidad de datos:")
	num1 = float(input())
	acum = 0
	for i in range(1,num1+1):
		print("ingrese dato ",i,":")
		dato = float(input())
		acum = acum+dato
	prom = acum/num1
	print("el promedio es: ",prom)

