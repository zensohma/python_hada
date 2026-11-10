import pandas as pd

data = {
    "Nama": ["Hada", "Sanatang", "Syuna", "Alice"],
    "Usia": [20, 23, 12, 20],
    "Pekerjaan": ['Ilmuwam', 'Desainer', 'Guru', 'Dosen']
}

df = pd.DataFrame(data)

print(df)