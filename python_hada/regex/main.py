import re

teks = "Nomor darurat adalah 112 dan 911"
pola = r"\d+"

hasil = re.findall(pola, teks)

print(hasil)