#1
def lulus_saja(data): 
    lulus = []
    for siswa in data:
        if siswa["nilai"] > 65:
            lulus.append(siswa["nama"])
    return lulus

hasil_akhir = [
    {'nama':'Reza', 'nilai':70},
    {'nama':'Ciut', 'nilai':63},
    {'nama':'Dian', 'nilai':80},
    {'nama':'Badu', 'nilai':40}
]

lulus = lulus_saja(hasil_akhir)
print(lulus)
print()

#2
def balikan(buah):
  balikan = []
  for i in range(len(buah) - 1, -1, -1):
    balikan.append(buah[i])
  return balikan

buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
balikan = balikan(buah)
print(balikan)
print()

#3
def duplikasi(nama_buah):
    daftar_buah_terduplikasi = []
    for buah in nama_buah:
        daftar_buah_terduplikasi.extend([buah, buah])
    return daftar_buah_terduplikasi

buah_asli = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
buah_terduplikasi = duplikasi(buah_asli)
print(buah_terduplikasi)
print()

#4
def fungsi(kalimat): 
    huruf_vokal = "aiueoAIUEO" 
    hasil = "" 
    for huruf in kalimat: 
        if huruf not in huruf_vokal: 
            hasil += huruf 
    return hasil 
 
print(fungsi('NurulFikri'))