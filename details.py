import pymysql.cursors


connection = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='deficientes_projeto'
)


cursor = connection.cursor()


comando_SQL = 'SELECT * FROM lugar'
cursor.execute(comando_SQL)
valores_lidos = cursor.fetchall()
lista = []
for c in valores_lidos:
    lista.append(c)

print(lista)