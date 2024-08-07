import requests
import json
import time
import pyodbc
import matplotlib.pyplot as plt
proxies = {'https': "http://disrct:etsps2024401@10.224.200.26:8080"}

user = 'Wallace'
SECRET_KEY = ""
url = 'https://iiot-7276b-default-rtdb.firebaseio.com/.json'
FIrebaseURL = 'https://iiot-7276b-default-rtdb.firebaseio.com/'
url2 = FIrebaseURL + "/Wallace.json"
def InserirBD(Temperatura, Umidade):
    server = 'CA-C-0065D\SQLEXPRESS'
    database = 'IoT_DBS'
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+'; DATABASE='+database+';Trusted_Connection=yes')
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO Prova (Temperatura, Umidade) VALUES (?, ?)", (Temperatura, Umidade))
    cnxn.commit()  
    cnxn.close()                                  
    print("Inserido com sucesso!")

def getBD():
    server = 'CA-C-0065D\SQLEXPRESS'
    database = 'IoT_DBS'
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+'; DATABASE='+database+';Trusted_Connection=yes')
    cursor = cnxn.cursor()
    cursor.execute(f"SELECT * FROM Prova")
    dataBD = cursor.fetchall()
    # print("catei")
    return dataBD



def fazerGrafico():
    server = 'CA-C-0065D\SQLEXPRESS'
    database = 'IoT_DBS'
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
    cursor = cnxn.cursor()

    cursor.execute("SELECT Temperatura FROM Prova")
    list_temp = [row[0] for row in cursor.fetchall()]
    plt.plot(list_temp, label="Temperatura")
    time.sleep(0.5)
    cursor.execute("SELECT Umidade FROM Prova")
    list_hum = [row[0] for row in cursor.fetchall()]
    plt.plot(list_hum, label="Humidade")
    time.sleep(0.5)
    cursor.execute('SELECT Ordem_dados FROM Prova;')
    ordemDeRegistro = [row[0] for row in cursor.fetchall()]
    time.sleep(0.5)
    # plt.axis((horarios[0], horarios[len(horarios) - 1], 0, 25))
    # print(horarios)

    # plt.figure(figsize=(10, 8), layout='constrained')
    plt.axis((ordemDeRegistro[0], ordemDeRegistro[len(ordemDeRegistro) - 1], 0, 100))
    plt.legend()
    plt.title("Dados")
    plt.grid(linestyle='dashed')
    posicoes = range(len(ordemDeRegistro))
    labels = ordemDeRegistro
    plt.xticks(posicoes, labels, rotation=45)
    plt.show()

while True:
    inf = requests.get(url, proxies=proxies).content
    inf2 = json.loads(inf)['Wallace']
    sinal = inf2
    InserirBD(sinal['Temperatura'],sinal['Umidade'])
    print(getBD())
    fazerGrafico()
    time.sleep(31)



    

 