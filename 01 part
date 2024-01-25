import pyphen

import tkinter as tk
from tkinter import ttk

MAGIC_ALPHABET = {
  'A': ('𐐅', 'to'),
  'B': ('𐐆', 'ta'),
  'C': ('𐐇', 'nes'),
  'Ç': ('😔', 'não'),
  'D': ('𐐈', 'nas'),
  'E': ('𐐉', 'nos'),
  'F': ('𐐊', 'tes'),
  'G': ('𐐋', 'la'),
  'H': ('𐐌', 'me'),
  'I': ('𐐍', 'mo'),
  'J': ('𐐎', 'ma'),
  'K': ('𐐏', 'le'),
  'L': ('𐐐', 'lo'),
  'M': ('𐐑', 'sa'),
  'N': ('£', 'se'),
  'O': ('𐐓', 'so'),
  'P': ('𐐔', 'ba'),
  'Q': ('€', 'be'),
  'R': ('𐐖', 'bo'),
  'S': ('𐐗', 'sko'),
  'T': ('𐐘', 'ska'),
  'U': ('𐐙', 'pa'),
  'V': ('𐐚', 'po'),
  'W': ('%', 'pe'),
  'X': ('𐐜', 'chi'),
  'Y': ('𐐝', 'cho'),
  'Z': ('𐐞', 'cha'),
}


def dividir_silabas(palavra):
  dic = pyphen.Pyphen(lang='pt_BR')
  silabas = dic.inserted(palavra).split('-')
  return silabas


def inverter_silaba(silaba):
  return silaba[::-1]


def latim_para_magico(frase_latim):
  palavras = frase_latim.split()
  palavras_invertidas = []

  process_description = ""

  for palavra in palavras:
    silabas = dividir_silabas(palavra)
    process_description += f"\nDivisão de sílabas de '{palavra}': {silabas}\n"

    silabas_invertidas = [inverter_silaba(silaba) for silaba in silabas]
    process_description += f"Sílabas invertidas: {silabas_invertidas}\n"

    palavra_invertida = ".".join(silabas_invertidas)
    palavras_invertidas.append(palavra_invertida)

  frase_invertida = " ".join(palavras_invertidas[::-1])
  process_description += f"\nFrase invertida: {frase_invertida}\n"

  frase_magica = ""
  frase_fonemas = ""
  palavra_fonemas = ""
  for idx, char in enumerate(frase_invertida.upper()):
    if char == " ":
      frase_magica += char
      frase_fonemas += palavra_fonemas.strip() + " "
      palavra_fonemas = ""
    elif char in MAGIC_ALPHABET:
      frase_magica += MAGIC_ALPHABET[char][0]
      if idx == 0 or frase_invertida[idx - 1] == " ":
        palavra_fonemas += MAGIC_ALPHABET[char][1]
      else:
        if frase_invertida[idx - 1] == ".":
          palavra_fonemas += MAGIC_ALPHABET[char][1]
        else:
          palavra_fonemas += MAGIC_ALPHABET[char][1]
    else:
      frase_magica += char

  frase_fonemas += palavra_fonemas.strip()

  return frase_magica, frase_fonemas.strip(), process_description


def magico_para_latim(frase_magica):
  REVERSE_MAGIC_ALPHABET = {v[0]: k for k, v in MAGIC_ALPHABET.items()}
  frase_invertida = " "
  process_description = ":\n"

  for idx, char in enumerate(frase_magica):
    if char in REVERSE_MAGIC_ALPHABET:
      frase_invertida += REVERSE_MAGIC_ALPHABET[char]
    else:
      frase_invertida += char

  process_description += f"Frase invertida: {frase_invertida}\n"
  palavras_invertidas = frase_invertida.split()
  palavras = []

  for palavra_invertida in palavras_invertidas:
    silabas_invertidas = palavra_invertida.split(".")
    silabas = [inverter_silaba(silaba) for silaba in silabas_invertidas]
    palavra = "".join(silabas)
    palavras.append(palavra)

  frase_latim = " ".join(palavras[::-1])
  process_description += f"Frase em latim: {frase_latim}\n"
  return frase_latim, process_description
