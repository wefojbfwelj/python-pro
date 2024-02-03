meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            "BAMBIK": "Osoba początkująca, niezdarna lub dziwna",
            "ROFL": "Odpowiedź na żart",
            "SHEESH": "Lekka dezaprobata",
            "CREEPY": "Straszny, złowieszczy",
            "AGGRO": "Stać się agresywnym/zły",
            "DELULU": "Osoba, która ma obsesję na czyimś punkcie",
            "ODKLEJKA": "Stan oderwania od rzeczywistości",
            "RIZZ": "Umiejętności czarowania lub uwodzenia potencjalnego partnera"
            }
            
word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Tego słowa nie ma w słowniku")
