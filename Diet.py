import mysql.connector
conn = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="dietpedia")
cursor=conn.cursor()

class Pengguna():
    def __init__(self, idPengguna, nama, usia, jenisKelamin, beratBadanAwal, beratBadanImpian, email, password):
        self.idPengguna=idPengguna
        self.nama=nama
        self.usia=usia
        self.jenisKelamin=jenisKelamin
        self.beratBadanAwal=beratBadanAwal
        self.beratBadanImpian=beratBadanImpian
        self.email=email
        self.password=password

    def showInfo(self):
        print("Nama = {}\nUsia = {}\nJenis kelamin = {}\nBerat Badan Saat Ini = {}\nBerat Badan Impian = {}\nEmail = {}\nPassword = {}".format(self.nama,self.usia,self.jenisKelamin,self.beratBadanAwal, self.beratBadanImpian, self.email, self.password))

    def ubahData(self, ubah):
        if ubah==1:
            namaBaru=str(input("Masukkan nama baru : "))
            query = "update daftar set nama = '{}' where idPengguna = '{}'".format(namaBaru, self.idPengguna)
            cursor.execute(query)
            conn.commit()
        elif ubah==2:
            usiaBaru=int(input("Masukkan usia baru : "))
            query = "update daftar set usia = '{}' where idPengguna = '{}'".format(namaBaru, self.idPengguna)
            cursor.execute(query)
            conn.commit()
        elif ubah==3:
            jenisKelaminBaru=str(input("Masukkan jenis kelamin baru : "))
            query = "update daftar set JenisKelamin = '{}' where idPengguna = '{}'".format(jenisKelaminBaru, self.idPengguna)
            cursor.execute(query)
            conn.commit()

#menambahkan data diri pengguna
def Registrasi():
    Nama=str(input("Masukkan Nama: "))
    Usia=int(input("Masukkan Usia: "))
    JenisKelamin=str(input("Masukkan Jenis Kelamin: "))
    BeratBadanAwal=int(input("Masukkan Berat Badan Anda Sekarang:"))
    BeratBadanImpian=int(input("Masukkan Berat Badan Impian Anda:"))
    Email=str(input("Masukkan Email: "))
    Password=str(input("Masukkan Password: "))

    query="Insert into daftar values('','{}',{},'{}',{},{},'{}','{}')".format(Nama,Usia,JenisKelamin,BeratBadanAwal,BeratBadanImpian,Email,Password)
    cursor.execute(query)
    conn.commit()
    print("Registrasi Berhasil, Silahkan Login")
# Registrasi()

def Login():
    for x in range(3):
        Email=str(input("Masukkan Email\t\t: "))
        Password=str(input("Masukkan Password\t: "))
        print()
        query= "select idPengguna from daftar where email='{}' and password='{}'".format(Email,Password)
        cursor.execute(query)
        id=cursor.fetchall()
        try:
            return id[0][0]
        except:
            print("Data Anda Masukkan Salah")
    print("Anda telah gagal Login Sebanyak 3 Kali")
    return False

def Beranda():
    while True:
        main=int(input("Beranda \n1. Pilih Paket \n2. Target \n3. Informasi Akun \n4. Keluar \nPilih menu di atas : "))
        print()
        if main==1:
            pass
            # PaketDiet()
        elif main==2:
            pass
            # target()
        elif main==3:
            dataAkun=cursor.fetchall()[0]
            user=Pengguna(dataAkun[0], dataAkun[1], dataAkun[2], dataAkun[3], dataAkun[4],dataAkun[5], dataAkun[6], dataAkun[7])
            user.showInfo()
            print()
            menuAkun=int(input("1. Ubah data \n2. Kembali \nPilih Menu : "))
            print()
            if menuAkun==1:
                ubah=int(input("1. Nama \n2. Usia \n3. Jenis kelamin \n4. Berat badan saat ini \n5. Berat badan tujuan \n6. Email \n7. password \nPilih data yang akan diubah : "))
                user.ubahData(ubah)
            elif menuAkun==2:
                Beranda()
        else:
            print("Menu yang anda pilih tidak tersedia")

def programBerjalan():
    while True:
        main=int(input("1. Login \n2. Registrasi \n3. Logout \n Pilih menu di atas : "))
        print()
        if main==1:
            id=Login()
            query="select * from daftar where idPengguna="+str(id)
            cursor.execute(query)
            Beranda()
        elif main==2:
            Registrasi()
        elif main==3:
            exit()
        else:
            print("Menu yang anda pilih tidak tersedia")
programBerjalan()