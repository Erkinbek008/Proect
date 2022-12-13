from pathlib import Path

print("Assalomu aleykum!")

print('''Bizdagi xizmatlar:
1. Papkaga kirish 
2. Fayl yaratish 
3. Papka yaratish 
4. Faylni boshqa faylga o`tkazish
5. Papka o`chirish
''')
ask = input("Qaysi xizmatni tanlaysiz: ")
def kirish(papka: str):
    print(Path.home() /"Desktop"/papka)

def fayl_yaratish(file_yaratish: str):
    try:
        ds = Path.home() / "Desktop"/file_yaratish
        ds.touch()
    except FileExistsError:
        print("File allaqachon yaratilgan!")

def papka_yaratish(papka_yarat: str):
    try:
        desk = Path.home() /"Desktop"/papka_yarat
        desk.mkdir()
    except FileExistsError:
        print("Papka allaqachon yaratilgan!") 
def fayl_ozgartirish(old_papka: str,new_papka,file: str):
    try:
        desk = Path.home()/"Desktop"
        new = desk /old_papka / file
        old = desk / new_papka / file
        new.replace(old)
    except FileNotFoundError:
        print("File o`zgartirib bo`lingan")
def ochirish(delate_papka: str):
    try:
        delate_desk =Path.home() /"Desktop" /delate_papka
        delate_desk.rmdir()
    except FileNotFoundError:
        print("Papka o`chirib bo`lingan")