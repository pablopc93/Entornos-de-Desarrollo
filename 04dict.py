def transformar_acentos(frase):
  """
  Transforma las vocales con acentos en su versión sin acento.
  """
  acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
  for k, v in acentos.items():
    frase = frase.replace(k, v)
  return frase

def transformar_acentos_map(frase):
  """
  Transforma las vocales con acentos en su versión sin acento usando map.
  """
  acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
  return ''.join(map(lambda x: acentos.get(x, x), frase))

def transformar_acentos_map_no_lambda(frase):
  """
  Transforma las vocales con acentos en su versión sin acento usando map sin lambda.
  """
  acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
  def cambiar_acento(caracter):
    return acentos.get(caracter, caracter)
  return ''.join(map(cambiar_acento, frase))

def es_palindromo(frase):
  frase = frase.replace(" ", "").lower()
  frase == frase[::-1]
  frase == transformar_acentos
  return frase
  #return list(frase) == list(reversed(frase)) --> Pa dar la vuelta a la frase

entrada_usuario = "ána"

if es_palindromo(transformar_acentos(entrada_usuario)):
  print(f"{entrada_usuario} es un palíndromo.")
else:
  print(f"{entrada_usuario} no es un palíndromo.")