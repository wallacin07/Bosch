import matplotlib.pyplot as plt
import pyodbc

# Conexão com o banco de dados
server = 'CA-C-00657\\SQLEXPRESS'
database = 'IoT_DB'
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
cursor = cnxn.cursor()

# Obtendo dados do banco de dados
cursor.execute("SELECT Temperatura FROM Sensor")
list_temp = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT Humidade FROM Sensor")
list_hum = [row[0] for row in cursor.fetchall()]

cursor.execute('SELECT DISTINCT LEFT(CONVERT(VARCHAR, timestamp, 108), 5) AS Horario FROM Sensor;')
horarios = [row[0] for row in cursor.fetchall()]

print(horarios)

# Criando o gráfico
plt.figure(figsize=(10, 8), layout='constrained')
plt.axis((horarios[0], horarios[len(horarios) - 1], 0, 25))
plt.plot(list_hum, label="Humidade")
plt.plot(list_temp, label="Temperatura")
plt.legend()
plt.title("Dados")
plt.grid(linestyle='dashed')
# Obtendo horários do banco de dados e eliminando duplicatas

# Definindo as posições e rótulos dos horários
posicoes = range(len(horarios))
labels = horarios

# Configurando o espaçamento dos rótulos do eixo X
plt.xticks(posicoes, labels, rotation=45)

plt.tight_layout()  # Ajusta automaticamente o layout para evitar sobreposição
plt.show()