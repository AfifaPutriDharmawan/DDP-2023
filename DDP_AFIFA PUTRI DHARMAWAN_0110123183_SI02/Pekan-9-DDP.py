def profil(nama, alamat, gender, umur, hoby):
    print("DATA DIRI")
    print("Nama", nama)
    print("Alamat", alamat)
    print("Gender", gender)
    print("Umur", umur)
    print("Hoby", hoby)
profil("Afifa Putri Dharmawan","Jln. Irigasi RT.003/RW.07","Permpuan","19","Desain dan Memasak")
print()

def Kelulusan(nilai):
    if nilai <= 60:
        print("Gagal")
    elif nilai >= 61 and nilai <= 70:
        print("Baik")
    elif nilai >= 71 and nilai <= 80:
        print("Sangat Baik")
    elif nilai >= 81 and nilai <= 100:
        print("Istimewa")
Kelulusan(90)
print()

def ganjil(n):
    i = 1
    while i <= n:
        if i % 2 != 0:
            print(i)
        i+= 1
ganjil(100)