import os
import pprint

def capital_cities(list_of_cities):
    try:
        with open(list_of_cities, mode="r", encoding="UTF-8") as data:
            countries = data.readlines()
    except FileNotFoundError:
        print(
            f"Soubor {list_of_cities} nenalezen",
            f"Adresar: {os.getcwd()}",
            f"Obsah slozky: {os.listdir()}",
            sep="\n"
        )
        return None
    else: 
        return countries
    finally:
        print("Konec funkce")

def zformatuj_nazvy():   
    cities = capital_cities("countries_and_cities.txt")  # Corrected filename
    if cities is not None:
        capitalize_cities = []
        for udaj in cities:
            parts = udaj.strip().split(",")  # Split by comma
            if len(parts) > 1:  # Ensure there is a second part
                city = parts[1].strip()  # Strip whitespace from the city name
                capitalize_cities.append(city.title())  # Capitalize each word
    return capitalize_cities
                
formatted_cities = zformatuj_nazvy()

# print(zformatuj_nazvy())
with open("capitalize_cities.txt", "w", encoding="UTF-8") as data:
    for city in formatted_cities:
        data.write(f"{city}\n")  
    

