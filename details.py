import requests
import json
from airtable import Airtable

key = 'keyda2y1mcH9pIIOS'

airtable = Airtable('appXVFxRam3NYPQlM/', 'Table 1', key)

lugar = []

lugar.append(str(input('Qual o nome do lugar? ')))
lugar.append(str(input('Qual o nome do seu estado? ')))
lugar.append(str(input('Qual o tipo de deficiência? ')))
airtable.insert({'Lugar':f'{lugar[0]}', 'Estado': f'{lugar[1]}', 'Deficiencia': f'{lugar[2]}'})
print(lugar)