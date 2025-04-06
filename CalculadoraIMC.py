def calcular_imc(peso, altura): #funcion para calcular IMC
  imc = peso / (altura ** 2) # fórmla IMC = peso/(altura^2)
  return imc

def interpretar_imc(imc):#categorías IMC
  if imc < 18.5:
    return "Bajo peso"
  elif 18.5 <= imc < 24.9:
    return "Peso normal"
  elif 25 <= imc < 24.9:
    return "Sobrepeso"
  else:
    return "Obesidad"

def obtener_num_valido(dato): #captura numeros
  while True:
    
      try:
    
        valor = float(input(dato))
        if valor <= 0:
          print("Ingresa un número mayor que 0")
        else:
          return valor

      except ValueError:
        print("Error. Ingcresa un número válido")

while True:
  print("\n Calculadora de IMC")
  print("\nEscribe 'Salir para cerrar programa.")

  comando = input("\n¿Calcula tu Indice de Masa corporal. Presiona cualquier tecla para continuar\n(Escribe 'Salir' para finalizar)").strip()
  if comando.lower() == 'salir':
    print("Hasta pronto")
    break


#Obtener datos de entrada
  peso = obtener_numero_valido("Ingresa tu peso en kilogramos: ")
  altura = obtener_numero_valido("Ingresa tu altura en metros")
#condicion para solicitar salida

 #calcular IMC
  imc = calcular_imc(peso, altura)
 

  #Muestra resultados
  print(f"\nTu IMC es: {imc:.2f}")
  print(interpretar_imc(imc))

