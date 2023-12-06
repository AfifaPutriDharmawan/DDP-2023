import math

def Segitiga(A,T,S):
    luas= 1/2*A*T
    keliling= S*S*S
    print("Hasil Luas dari Segitia adalah",luas)
    print("Hasil Keliling dari Segitia adalah",keliling)

def Persegi(S):
    luas = S*S
    keliling = 4*S
    print("Hasil Luas dari Persegi adalah",luas)
    print("Hasil Keliling dari Persegi adalah",keliling)

def Persegi_Panjang(P,L):
    luas = P*L
    keliling= 2*(P+L)
    print("Hasil Luas dari Persegi Panjang adalah",luas)
    print("Hasil Keliling dari Persegi Panjang adalah",keliling)

def Belah_Ketupat(d1,d2,S):
    luas = 1/2*d1*d2
    Keliling = 4*S
    print("Hasil Luas dari Persegi Panjang adalah",luas)
    print("Hasil Keliling dari Persegi Panjang adalah",Keliling)

def Jajar_Genjang(A,T,SM):
    luas = A*T
    Keliling = 2*(A+SM)
    print("Hasil Luas dari Jajar Genjang adalah",luas)
    print("Hasil Keliling dari Jajar Genjang adalah",Keliling)

def Layang_layang(d1,d2,s1,s2):
    luas = 1/2*d1*d2
    Keliling = 2*s1+s2
    print("Hasil Luas dari Layang-layang adalah",luas)
    print("Hasil Keliling dari Layang-layang  adalah",Keliling)
    
def Trapesium(SA,SB,SM,T):
    luas = 1/2*(SA+SB)*T
    Keliling = SA+SB+SM+T
    print("Hasil Luas dari Trapesium adalah",luas)
    print("Hasil Keliling dari Trapesium adalah",Keliling)