
import requests as req
import csv
import json
import os
import funcs


# res = req.get("https://restcountries.eu/rest/v2/all").json()
# print(res[0])

user = 0
while user != "Q":
    funcs.menu()
    user = input("Select: ")

    if user == "1": #BY COUNTRY. BUSCAR PAÍS
        user = input("Country: ") 
        country = funcs.get_by_name(country)
        print(country)
        funcs.write_csv(country)
    # elif user == "2":  #Buscar por continente
    #     funcs.regions()
    #     region = input("Region: ")
    #     population = funcs.get_total_region(funcs.read_json(region))
    #     print(population)
    #     result = funcs.get_by_region(region) #esto se encarga de traer todo el contenido del continente
    #     funcs.write_json(result, region) # esta es la parte que se encarga de escribir el json
    elif user == "2":
        funcs.ls_regions()
        region = input("Region: ")
        try:
            population = funcs.get_total_region(funcs.reaad_json(region))
            print(population)
        except FileNotFoundError:
            result = funcs.get_by_region(region)
            population = funcs.get_total_region(funcs.read_json(region))
            print(population)

    elif user== "3":
        language = input("Search by language: ")
        print(funcs.get_iso(language))
        iso_language = funcs.get_iso(language)
        print(funcs.get_by_language(iso_language)) 
    elif user == "4":
        user = input("Country: ") 
        country = funcs.get_by_name(user)
        funcs.download_flag(country)
    # elif user == "5":
    #     print("History: ")
    #     funcs.get_by_history()
        
    elif user == "5":
        funcs.show_record("record.csv")

    elif user == "6":  #Se unen el ejer 4 y 5
        result = funcs.get_by_density(req.get(f"https://restcountries.eu/rest/v2/all").json())
        print(result)

    elif user == "7":
        result = funcs.top_language(req.get(f"https://restcountries.eu/rest/v2/all").json())
        print(result)
        
    elif user == "q" or user == "Q":
        user = "Q"
