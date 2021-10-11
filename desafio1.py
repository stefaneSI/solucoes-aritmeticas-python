def converteNota(note):
  if 0 <= note < 1:
    return 'E'
  elif 1 <= note <= 35:
    return 'D'
  elif 36 <= note <= 60:
    return 'C'
  elif 61 <= note <= 85:
    return 'B'
  elif 86 <= note <= 100:
    return 'A'

try:
  nota = int(input())
  print(converteNota(nota))
except ValueError:
  print("Somente são aceitos números inteiro")
  