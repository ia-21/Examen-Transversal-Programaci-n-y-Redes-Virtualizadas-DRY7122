import requests

API_KEY = "7a18436d-614a-4cdf-9ae1-66d161eca0ea"

def obtener_coordenadas(ciudad):
    url = f"https://graphhopper.com/api/1/geocode"
    params = {
        "q": ciudad,
        "locale": "es",
        "limit": 1,
        "key": API_KEY
    }
    r = requests.get(url, params=params)
    data = r.json()

    if data['hits']:
        punto = data['hits'][0]['point']
        return punto['lat'], punto['lng']
    else:
        return None, None

def calcular_ruta(origen, destino, transporte):
    lat_o, lng_o = obtener_coordenadas(origen)
    lat_d, lng_d = obtener_coordenadas(destino)

    if lat_o is None or lat_d is None:
        print("❌ No se pudo obtener coordenadas.")
        return

    url = "https://graphhopper.com/api/1/route"
    params = {
        "point": [f"{lat_o},{lng_o}", f"{lat_d},{lng_d}"],
        "vehicle": transporte,
        "locale": "es",
        "instructions": "true",
        "key": API_KEY
    }

    r = requests.get(url, params=params)
    data = r.json()

    if "paths" in data:
        ruta = data['paths'][0]
        print("\n🛣️ Resumen del viaje:")
        print(f"- Distancia: {round(ruta['distance']/1000, 2)} km / {round(ruta['distance']/1609.34, 2)} millas")
        print(f"- Duración: {round(ruta['time']/60000, 2)} minutos")

        print("\n📍 Instrucciones:")
        for step in ruta['instructions']:
            print("→", step['text'])
    else:
        print("❌ No se pudo calcular la ruta.")

if __name__ == "__main__":
    while True:
        print("\n=== Cálculo de Ruta ===")
        ciudad_origen = input("Ciudad de origen (ej: Santiago): ")
        if ciudad_origen.lower() == "s":
            break
        ciudad_destino = input("Ciudad de destino (ej: Buenos Aires): ")
        if ciudad_destino.lower() == "s":
            break
        transporte = input("Medio de transporte (car, bike, foot): ").lower()
        if transporte not in ["car", "bike", "foot"]:
            print("⚠️ Transporte inválido. Usando 'car' por defecto.")
            transporte = "car"
        calcular_ruta(ciudad_origen, ciudad_destino, transporte)
        salir = input("\nPresiona 's' para salir o Enter para continuar: ")
        if salir.lower() == "s":
            break
