import requests
import time

API_KEY = "51917d11-bcf5-4912-aa8b-23adf638e873"

def geocode(ciudad):
    url = "https://graphhopper.com/api/1/geocode"
    params = {
        "q": ciudad,
        "locale": "es",
        "limit": 1,
        "key": API_KEY
    }
    resp = requests.get(url, params=params)
    if resp.status_code == 200 and resp.json()["hits"]:
        hit = resp.json()["hits"][0]
        lat = hit["point"]["lat"]
        lng = hit["point"]["lng"]
        return f"{lat},{lng}"
    else:
        print(f"❌ No se pudo geolocalizar: {ciudad}")
        return None

def get_travel_data(origen_coords, destino_coords, vehiculo):
    url = f"https://graphhopper.com/api/1/route"
    params = {
        "point": [origen_coords, destino_coords],
        "vehicle": vehiculo,
        "locale": "es",
        "instructions": "true",
        "calc_points": "true",
        "key": API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        path = data['paths'][0]

        distancia_metros = path['distance']
        duracion_segundos = path['time'] / 1000
        distancia_km = distancia_metros / 1000
        distancia_millas = distancia_km * 0.621371
        duracion_min = duracion_segundos / 60
        narrativa = path['instructions']

        return distancia_km, distancia_millas, duracion_min, narrativa
    else:
        print("❌ Error al consultar la API")
        print("Código de respuesta:", response.status_code)
        print("Mensaje:", response.text)
        return None, None, None, None

def main():
    while True:
        print("\nPresiona 's' para salir.")
        origen = input("📍 Ingrese ciudad de origen (Ej: Santiago, Chile): ")
        if origen.lower() == 's':
            break
        destino = input("📍 Ingrese ciudad de destino (Ej: Mendoza, Argentina): ")
        if destino.lower() == 's':
            break

        print("🚗 Elija medio de transporte:\n1. Auto (car)\n2. Bicicleta (bike)\n3. Caminando (foot)")
        opcion = input("Ingrese opción (1/2/3): ")
        transporte = {"1": "car", "2": "bike", "3": "foot"}.get(opcion, "car")

        print("\n🔄 Geolocalizando ciudades...")
        origen_coords = geocode(origen)
        destino_coords = geocode(destino)

        if not origen_coords or not destino_coords:
            print("❌ Error al obtener coordenadas. Intente con otras ciudades.")
            continue

        print("\n🔄 Consultando ruta...")
        time.sleep(1)

        km, millas, duracion, instrucciones = get_travel_data(origen_coords, destino_coords, transporte)

        if km:
            print(f"✅ Distancia: {km:.2f} km / {millas:.2f} millas")
            print(f"⏱️ Duración estimada: {duracion:.2f} minutos")
            print("📜 Instrucciones del viaje:")
            for paso in instrucciones[:5]:
                print(f"- {paso['text']}")
        else:
            print("No se pudo calcular la ruta. Revisa los datos ingresados.")

if __name__ == "__main__":
    main()
