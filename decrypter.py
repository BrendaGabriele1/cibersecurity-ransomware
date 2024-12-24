import os 
import pyaes

## ABRIR O ARQUIVO CRIPTOGRAFADO

file_name = 'teste.txt.ransomwaretroll'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## CHAVE DE DESCRIPTOGRAFIA

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## REMOVER O ARQUIVO CRIPTOGRAFADO

os.remove(file_name)

## CRIAR UM NOVO ARQUIVO DESCRIPTOGRAFADO

new_file = 'teste.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypt_data)
new_file.close()
