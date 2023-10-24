#Ex. 1
def exercicio1(n):
  for i in range(1, n + 1):
      for x in range(1, i + 1):
          print(x, end=" ")
      print()

def principal():
  n = int(input("Digite o valor de n: "))
  exercicio1(n)

if __name__ == "__principal__":
  principal()


#Ex. 2
def exercicio2(n):
  n_string = str(n)
  qntd_digitos = len(n_string)
  return qntd_digitos


n = int(input("Digite um número : "))
x = exercicio2(n)
print(f"O número {n} tem {x} dígitos.")




#Ex. 3
try:
  
  n1 = int(input("Digite o primeiro número: "))
  n2 = int(input("Digite o segundo número: "))

  
  resultado = n1 / n2

except ValueError:
  print("Error: Números inválidos.")

except ZeroDivisionError:
  print("Error: Divisão por zero.")

else:
  print(f"Resultado : {resultado}")

finally:
  print("Encerrado.")
