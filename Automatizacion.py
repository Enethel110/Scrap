from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time as tm
import pandas as pd 

# Ruta al archivo CSV
archivo_csv = 'C:/Users/enechiki/Downloads/Scrap/datos.csv'

# Configurar las opciones para usar Brave
options = Options()
options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Ruta a Brave

# Ruta del archivo chromedriver.exe
service = Service('C:/chrome/chromedriver.exe')

# Iniciar el navegador Brave con el driver de Chrome
driver = webdriver.Chrome(service=service, options=options)


try:
    # Intentamos leer el archivo CSV con la codificación 'latin-1'
    df = pd.read_csv(archivo_csv, encoding='latin-1')
    print(df)
except FileNotFoundError:
    print(f"Error: El archivo '{archivo_csv}' no se encuentra.")
except pd.errors.EmptyDataError:
    print("Error: El archivo CSV está vacío.")
except pd.errors.ParserError:
    print("Error: El archivo CSV tiene un formato incorrecto.")
except UnicodeDecodeError as e:
    print(f"Error de decodificación: {e}")
except Exception as e:
    print(f"Se ha producido un error: {e}")

for row, datos in df.iterrows():
    index = datos['ID']
    nombre = datos['Nombres']
    apePa = datos['Apellido Paterno']
    apeMa = datos['Apellido Materno']
    sexo = datos['Sexo']
    email = datos['Email']
    rubro = datos['Rubro']
    ##Abrir formulario.
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLScqDqor3CtkVs5Sx2iL8zXIOV90iYX6dAmdcYHrJtxV-4ZoSg/viewform?usp=sf_link')
    tm.sleep(2)
    ##Cargar los datos
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(index)
    tm.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(nombre)
    tm.sleep(2) 
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(apePa)
    tm.sleep(2) 
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(apeMa)
    tm.sleep(2) 
    sexo_dic = {"F":'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span',
                "M":'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
                "N":'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span'}
    driver.find_element(By.XPATH,sexo_dic[sexo]).click()
    tm.sleep(2) 
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(email)
    tm.sleep(2) 
    ##Abrir lista de rubros
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[1]/div[1]/span').click()
    tm.sleep(3) 
    rubro_dic = {'Tecnología':'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[2]/div[3]',
                'Salud':'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[2]/div[4]',
                'Educación':'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[2]/div[5]',
                'Construcción':'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[2]/div[6]',
                'Finanzas':'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[2]/div[7]',
                'Comercio':'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[2]/div[8]',
                'Arte':'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[2]/div[9]'}
    driver.find_element(By.XPATH, rubro_dic[rubro]).click()
    tm.sleep(2) 
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
    tm.sleep(1)
