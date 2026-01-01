import requests
import time

url = "https://docs.google.com/forms/d/e/1FAIpQLSc7G4zNjbRYUUA0rDvMxqSYYLIETEfPj6CvH8GkuTsm7ucA_g/formResponse"

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

actividades = [
    ("Ahorro energético: CPC validación de parametros", "Refrigeración"),
    ("Ahorro energetico: Verificación visual de evaporadores, condensador, puertas y cortinas de los cuartos", "Refrigeración"),
    ("Ahorro energetico: Revisión de ajustes de borneras y recalentamiento en cableados del sistema electrico del rack", "Eléctrico"),
    ("Ahorro energetico: Revisión de calibración y ajuste de controles de trabajo de compresores", "Eléctrico"),
]

with open("estado.txt", "r") as f:
    inicio = int(f.read().strip())

fin = inicio + 2

for correo, tienda in tiendas[inicio:fin]:
    for descripcion, especialidad in actividades:
        data = {
            "entry.902733400": "Ing Brayan Herazo",
            "entry.1898105446": correo,
            "entry.430365269": descripcion,
            "entry.1509004283": tienda,
            "entry.1162794890": especialidad,
            "entry.151546273": "CUARTO DE RACK",
            "entry.838636106": "RACK",
            "entry.1908331127": "1"
        }
        requests.post(url, data=data)
        time.sleep(21)

nuevo_inicio = fin if fin < len(tiendas) else 0

with open("estado.txt", "w") as f:
    f.write(str(nuevo_inicio))
