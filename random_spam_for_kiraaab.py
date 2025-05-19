import requests
import random

url = "https://docs.google.com/forms/d/e/1FAIpQLSchpxl_0Z6GuOd8wC0gXzJeOelrvDBIwmLRCUJy4PvC4WxTSg/formResponse"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "https://docs.google.com/forms/d/e/1FAIpQLSchpxl_0Z6GuOd8wC0gXzJeOelrvDBIwmLRCUJy4PvC4WxTSg/viewform?fbzx=-3778376709519874690",
    "Cookie": "S=spreadsheet_forms=8r_M14zpPggjmGm4Qdhv6Euw80xreVZ4jaxEE6r7Km0; COMPASS=spreadsheet_forms=CjIACWuJVyptrCsm1UjIJ3sKZ0C4_8tTIvr3lwp6yRz7BUIl7A2Z711lZI6xOzmM48BPwBCRza3BBho0AAlriVef6W-dbtM79pHKJLYSaS0quAGWa4R7ijKFoS1N0caaYzOXXHnV3N4VYai5OHhPjQ==; NID=524=pLz0mD6_x4AVzx4ACSoJz6MBy4Lgds_02eu9Y71FlPqOkv8o1qD4mrmVEwKTCb5r2Bhf-XSfbRL3gsdQHGTdtG9T9yFG0ngSlFpbO71Mrj4NcK5dHoxPqO1IUvuflXmleabcjGe7ALbLQoYMyOw6iV_zve415BGogtSbM0PTCSIoS1bqwxxL_9W4bzVwA1ihlQ"
}

resp_pregunta1 = ["18", "19", "20"]
resp_pregunta2 = ["bien", "mal"]
resp_pregunta3 = ["Hola1", "Hola2", "Hola3", "Hola4", "Hola5"]

for i in range(10):
    pregunta1 = random.choice(resp_pregunta1)
    pregunta2 = random.choice(resp_pregunta2)
    pregunta3 = random.choice(resp_pregunta3)

    data = f"entry.1111111111={pregunta1}&entry.2222222222={pregunta2}&entry.3333333333={pregunta3}"

    r = requests.post(url, headers=headers, data=data)
    print(f"[{i+1}] pregunta1={pregunta1}, pregunta2={pregunta2}, pregunta3={pregunta3} | status -> [{r.status_code}]")
