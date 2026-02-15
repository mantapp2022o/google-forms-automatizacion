import requests
import time

# URL del Google Form (formResponse)
url = "https://docs.google.com/forms/d/e/1FAIpQLSc7G4zNjbRYUUA0rDvMxqSYYLIETEfPj6CvH8GkuTsm7ucA_g/formResponse"

# Lista de tiendas (correo, número)
tiendas = [
    ("asto101@olimpica.com.co", "1101"),
    ("asto102@olimpica.com.co", "1102"),
    ("asto103@olimpica.com.co", "1103"),
    ("asto104@olimpica.com.co", "1104"),
    ("asao105@olimpica.com.co", "1105"),
    ("asto106@olimpica.com.co", "1106"),
    ("asto107@olimpica.com.co", "1107"),
    ("asto108@olimpica.com.co", "1108"),
    ("asto109@olimpica.com.co", "1109"),
    ("asto110@olimpica.com.co", "1110"),
    ("asao112@olimpica.com.co", "1112"),
    ("asto113@olimpica.com.co", "1113"),
    ("asto114@olimpica.com.co", "1114"),
    ("asto115@olimpica.com.co", "1115"),
    ("asto116@olimpica.com.co", "1116"),
    ("asto117@olimpica.com.co", "1117"),
    ("asto118@olimpica.com.co", "1118"),
    ("asto119@olimpica.com.co", "1119"),
    ("asto120@olimpica.com.co", "1120"),
    ("asto122@olimpica.com.co", "1122"),
    ("asto123@olimpica.com.co", "1123"),
    ("asto124@olimpica.com.co", "1124"),
    ("asto125@olimpica.com.co", "1125"),
    ("dsto126@olimpica.com.co", "1126"),
    ("dsto127@olimpica.com.co", "1127"),
    ("asto128@olimpica.com.co", "1128"),
    ("dsto129@olimpica.com.co", "1129"),
    ("asto609@olimpica.com.co", "1609"),
    ("asto610@olimpica.com.co", "1610"),
    ("asdo613@olimpica.com.co", "1613"),
    ("dsto141@olimpica.com.co", "1141"),
]

# ⚙️ SERVICIOS CONFIGURABLES
# Cada servicio es un diccionario con todos sus valores personalizables
servicios = [
    {
        "descripcion": "Ahorro energético: CPC validación de parametros",
        "especialidad": "Refrigeración",
        "area": "CUARTO DE RACK",
        "equipo": "RACK",
        "cantidad": "1"
    },
    {
        "descripcion": "Ahorro energetico: Verificación visual de evaporadores, condensador, puertas y cortinas de los cuartos",
        "especialidad": "Refrigeración",
        "area": "CUARTO DE RACK",
        "equipo": "RACK",
        "cantidad": "1"
    },
    {
        "descripcion": "Ahorro energetico: Revisión de ajustes de borneras y recalentamiento en cableados del sistema electrico del rack",
        "especialidad": "Eléctrico",
        "area": "CUARTO DE RACK",
        "equipo": "RACK",
        "cantidad": "1"
    },
    {
        "descripcion": "Ahorro energetico: Revisión de calibración y ajuste de controles de trabajo de compresores",
        "especialidad": "Eléctrico",
        "area": "CUARTO DE RACK",
        "equipo": "RACK",
        "cantidad": "1"
    },
    {
        "descripcion": "Ahorro energetico: Inspección de válvulas de expansión y presostatos",
        "especialidad": "Refrigeración",
        "area": "CUARTO DE RACK",
        "equipo": "RACK",
        "cantidad": "1"
    },
    {
        "descripcion": "Servicio preventivo: Ascensor Montacargas de recibo",
        "especialidad": "Metalmecánico",
        "area": "RECIBO",
        "equipo": "MONTACARGAS",
        "cantidad": "2"
    },
]

# ⚙️ CONFIGURACIÓN: Cambia este número para ajustar cuántas tiendas procesar por día
TIENDAS_POR_DIA = 5

# Leer estado actual
with open("estado.txt", "r") as f:
    inicio = int(f.read().strip())

total_tiendas = len(tiendas)

print(f"Inicio actual: {inicio}")
print(f"Total tiendas: {total_tiendas}")
print(f"Tiendas a procesar por día: {TIENDAS_POR_DIA}")
print(f"Servicios por tienda: {len(servicios)}")

# Seleccionar tiendas con wrap-around
bloque_tiendas = []
for i in range(TIENDAS_POR_DIA):
    idx = (inicio + i) % total_tiendas
    bloque_tiendas.append(tiendas[idx])

print("\nTiendas a procesar hoy:")
for _, tienda in bloque_tiendas:
    print(f"- {tienda}")

# Envío de formularios
for correo, tienda in bloque_tiendas:
    for servicio in servicios:
        data = {
            "entry.902733400": "Ing Brayan Herazo",
            "entry.1898105446": correo,
            "entry.430365269": servicio["descripcion"],
            "entry.1509004283": tienda,
            "entry.1162794890": servicio["especialidad"],
            "entry.151546273": servicio["area"],
            "entry.838636106": servicio["equipo"],
            "entry.1908331127": servicio["cantidad"]
        }
        response = requests.post(url, data=data)
        print(f"Enviado → Tienda {tienda} | {servicio['descripcion'][:50]}... | HTTP {response.status_code}")
        time.sleep(21)

# Actualizar estado (avanza según TIENDAS_POR_DIA, circular)
nuevo_inicio = (inicio + TIENDAS_POR_DIA) % total_tiendas

with open("estado.txt", "w") as f:
    f.write(str(nuevo_inicio))

print(f"\nNuevo inicio guardado: {nuevo_inicio}")
print(f"Total de envíos realizados: {len(bloque_tiendas) * len(servicios)}")
