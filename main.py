while True:
  try:
    nota = int(input())
    
    if 0 <= nota < 1:
      print('E')
      continue
    elif 1 <= nota <= 35:
      print('D')
      continue
    elif 36 <= nota <= 60:
      print('C')
      continue
    elif 61 <= nota <= 85:
      print('B')
      continue
    elif 86 <= nota <= 100:
      print('A')
      continue
  except ValueError:
    print("Somente são aceitos números inteiro")
    break


