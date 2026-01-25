# Dictionary adalah tipe data yang digunakan untuk menyimpan data dalam bentuk pasangan kunci-nilai (key-value pair).

mahasiswa = {
    "nama": "Raafa",
    "umur": 21,
    "jurusan": "Informatika",
    "pekerjaan": "Data Scientist"
}

print(mahasiswa["nama"])
print(mahasiswa.get("umur"))

for key, value in mahasiswa.items():
    print(key, ":", value)