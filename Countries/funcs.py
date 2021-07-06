import requests as req
import csv
import json
import os
from languages import languages 


real_path = os.path.dirname(__file__)

def menu():
    print("COUNTRIES".center(50, "-"))
    print("1. COUNTRY")
    print("2. REGION")
    print("3. COUNTRYS BY LANGUAGE")
    print("4. DOWNLOAD FLAG")
    print("5. HISTORY")
    print("Q. QUIT")

def regions():
    regions = ["Asia", "Africa", "America", "Europe", "Oceania"]
    for region in regions:
        print(region)    

def get_by_name(country_name): #Buscar por país
    res = req.get(f"https://restcountries.eu/rest/v2/name/{country_name}").json()

    if type(res) == list:
        country = res[0]
        result = [country["name"], country["capital"], country["region"], country["population"], country["area"], country["languages"][0]["name"], country["flag"]]
        return result

    elif type(res) == dict:
        return res["mesage"]   

def write_csv(country):
    if type(country) == list:
        with open(f"{real_path}/record.csv", "a", encoding="utf8", newline="") as file: #"a" es de append, para añadir los elementos que se vayan escribiendo en el archivo recordcsv
            csv_writer = csv.writer(file, delimiter=",")  #csv_writer va a ser un escritor de csv, que toma como parámetro file. writer, permite escribir en el recordcsv, por eso se pone csv.writer
            csv_writer.writerow(country)


def get_by_region(region_name): #Buscar por continente
    res = req.get(f"https://restcountries.eu/rest/v2/region/{region_name}").json()
    return res  #Nos devuelve la lista que es el dato que necesitamos para escribir en json 

def write_json(data, json_name):  #Escribes el fichero
    if type(data) == list:
        with open(f"{real_path}/{json_name}.json", "w", encoding="utf8") as file: #Esto es para escribir Json
            json.dump({"data": data},file, ensure_ascii=False, indent=4) #<-----{"data": data}
            
def read_json(json_name):  #Lees el fichero
    with open(f"{real_path}/{json_name}.json", "r", encoding="utf8") as file:
        return json.load(file)["data"] #Devuelves el fichero


def get_total_region(region): #Esta función hace que con la lectura anterior, calcula la población
    result = 0
    for country in region:
        result += country["population"]
    return result

def get_iso(language):
    for tupla in languages:  
        if tupla[1].lower().find(language) == 0:
            return tupla[0]  

    # result = list(filter(lambda tupla:tupla[1].lower().find(user_language) == 0 ,languages)) OTRA FORMA DISTINTA DE HACERLO
    # return result[0][0] 

    # return next(tupla[0]for tupla in languages if tupla[1].lower().find(user_language) == 0) OTRA FORMA DISTINTA DE HACERLO
    # return next(iso)

def get_by_language(iso_language):
    if iso_language:
        res = req.get(f"https://restcountries.eu/rest/v2/lang/{iso_language}").json()
        return f"{len(res)} countries speaks {iso_language}"
    else:
        return f"No matches for your search"    


def download_flag(country):
    if type(country) == list:
        res = req.get(country[-1]).content
        name_flag = country[-1][-7:] # -7: es así porque arg.svg son 7. arg.svg viene de la url de la bandera del país que se elija
        with open(f"{real_path}/img/{name_flag}", "wb") as file:
            file.write(res)

# def get_by_history(): #Buscarlo de una manera más corta
#     result = []
#     with open(f"{real_path}/record.csv", encoding="utf8") as file: 
#        csv_reader = csv.reader(file)
#        for row in csv_reader:
#            if row[0] != "name":
#                 print(f"name: {row[0]} - value: {row[3]}")
           

    #De esta manera llamas funciones dentro de otras funciones. Es una forma más larga
def read_csv(data): #Esta función devuelve todas las filas que tenemos en data
    result = []
    with open(f"{real_path}/{data}", encoding="utf8") as file: #Se abre el fichero data con el encoding correcto
        csv_reader = csv.reader(file) #Se usa la librería csv para poder leer el csv
        for row in csv_reader: #por cada una de las filas en el csv reader, haceos un resultado.append de las filas
                result.append(row)

    return result #Devuelves resultado
def show_record(data):
    rows = read_csv(data) #Llamas a csv y guardas todas las filas(row)
    for row in rows: #iteras sobre las filas
        print(f"name: {row[0]} - value: {row[3]}")  



def biggest_10(data):  #4.Encontrar los 10 países más grandes
    return sorted(data, key = lambda country: country["area"] if country["area"] else 0, reverse=True)[0:11]


def get_by_density(data): #5.Encontrar los 10 paises más densamente poblados
    return sorted(data, key = lambda country: country["population"]/country["area"] if country["area"] and country["population"] else 0, reverse=True)[0:11]


 
def top_language(data):  #6. ¿Cuál es el idioma oficial más hablado?
    result = {}
    for country in data:
        language = country["languages"][0]["name"]
        try:
            result [language] += 1
        except KeyError:
                result[language] = 1
    return dict(sorted(result.items(), key=lambda tupla: tupla[1], reverse=True))           
