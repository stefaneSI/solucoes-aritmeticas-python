def vetor(x):
  n = 9
  vet = []
  for i in range (n):
    vet[i] = x
    x = x*2
        #square = i*i
    print("%i^2 = %i" %(i, x))

try:
  x = int(input())
  print(vetor(x))
except ValueError:
  print("Somente são aceitos números inteiro")


  