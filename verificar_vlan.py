def verificar_vlan(vlan_id):
    if 1 <= vlan_id <= 1005:
        return f"La VLAN {vlan_id} está en el rango NORMAL (1-1005)."
    elif 1006 <= vlan_id <= 4094:
        return f"La VLAN {vlan_id} está en el rango EXTENDIDO (1006-4094)."
    else:
        return f"La VLAN {vlan_id} está fuera de los rangos válidos (1-4094)."


if __name__ == "__main__":
    try:
        vlan = int(input("Ingrese número de VLAN: "))
        print(verificar_vlan(vlan))
    except ValueError:
        print("⚠️ Debes ingresar un número válido.")
