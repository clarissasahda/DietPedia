import mysql.connector
conn = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="dietpedia")
cursor=conn.cursor()

class Pengguna():
    def __init__(self, idPengguna, nama, usia, jenisKelamin,tinggiBadan, beratBadanAwal, beratBadanImpian, email, password, listMakanan, listOlahraga):
        self.idPengguna=idPengguna
        self.nama=nama
        self.usia=usia
        self.jenisKelamin=jenisKelamin
        self.tinggiBadan=tinggiBadan
        self.beratBadanAwal=beratBadanAwal
        self.beratBadanImpian=beratBadanImpian
        self.email=email
        self.password=password
        self.listMakanan=listMakanan
        self.listOlahraga=listOlahraga

    def showInfoUser(self):
        print("Nama = '{}'\nUsia = {}\nJenis kelamin = '{}'\nTinggi Badan = {}\nBerat Badan Saat Ini = {}\nBerat Badan Impian = {}\nEmail = '{}'\nPassword = '{}'".format(self.nama,self.usia,self.jenisKelamin,self.tinggiBadan,self.beratBadanAwal, self.beratBadanImpian, self.email, self.password))
    
    def ubahData(self, ubah):
        if ubah==1:
            namaBaru=str(input("Masukkan nama baru : "))
            query = "update daftar set nama = '{}' where idPengguna = {}".format(namaBaru, self.idPengguna)
            cursor.execute(query)
            conn.commit()
        elif ubah==2:
            usiaBaru=int(input("Masukkan usia baru : "))
            query = "update daftar set usia = '{}' where idPengguna = {}".format(usiaBaru, self.idPengguna)
            cursor.execute(query)
            conn.commit()
        elif ubah==3:
            jenisKelaminBaru=str(input("Masukkan jenis kelamin baru : "))
            query = "update daftar set JenisKelamin = '{}' where idPengguna = {}".format(jenisKelaminBaru, self.idPengguna)
            cursor.execute(query)
            conn.commit()
        elif ubah==4:
            tinggiBadanBaru=str(input("Masukkan tinggi badan baru : "))
            query = "update daftar set tinggiBadan = {} where idPengguna = {}".format(tinggiBadanBaru, self.idPengguna)
            cursor.execute(query)
            conn.commit()
        elif ubah==5:
            beratBadanAwalBaru=str(input("Masukkan berat badan awal baru : "))
            query = "update daftar set BeratBadanAwal = {} where idPengguna = {}".format(beratBadanAwalBaru, self.idPengguna)
            cursor.execute(query)
            conn.commit()
        elif ubah==6:
            beratBadanImpianBaru=str(input("Masukkan berat badan tujuan baru : "))
            query = "update daftar set BeratBadanImpian = {} where idPengguna = {}".format(beratBadanImpianBaru, self.idPengguna)
            cursor.execute(query)
            conn.commit()
        elif ubah==7:
            passwordBaru=str(input("Masukkan password baru : "))
            query = "update daftar set Password = '{}' where idPengguna = {}".format(passwordBaru, self.idPengguna)
            cursor.execute(query)
            conn.commit()
        else :
            print("Menu yang anda pilih tidak tersedia")
    
    def Target(self):
        print("Berat badan saat ini : {}\nBerat badan tujuan : {}".format(self.beratBadanAwal, self.beratBadanImpian))
        self.bmr=66+(13.7*self.beratBadanAwal)+(5*self.tinggiBadan)-(5.68*self.usia)
        self.targetnya=(self.beratBadanAwal-self.beratBadanImpian)
        self.batasKalori=self.bmr-300
        print("BMR : {}\nTarget penurunan berat badan : {} kg\n Batas konsumsi kalori per hari : {}".format(self.bmr,self.targetnya,self.batasKalori))
        print()
    
    def UbahTarget(self):
        self.beratBadanAwal=int(input("Masukkan berat anda saat ini : "))
        self.beratBadanImpian=int(input("Masukkan berat tujuan : "))
        query = "update daftar set BeratBadanAwal = {}, BeratBadanImpian = {} where idPengguna = {}".format(self.beratBadanAwal, self.beratBadanImpian, self.idPengguna)
        cursor.execute(query)
        conn.commit()

    def pilihMenu(self):
        from makanan import MenuMakan
        self.listMakanan=MenuMakan()
        query = "update daftar set ListMakanan = '{}' where idPengguna={}".format(self.listMakanan,self.idPengguna)
        cursor.execute(query)
        conn.commit()
    
    def pilihOlahraga(self):
        from makanan import Olahraga
        self.listOlah=Olahraga()
        query = "update daftar set ListOlahraga = '{}' where idPengguna={}".format(self.listOlahraga,self.idPengguna)
        cursor.execute(query)
        conn.commit()

#menambahkan data diri pengguna
def Registrasi():
    Nama=str(input("Masukkan Nama: "))
    Usia=int(input("Masukkan Usia: "))
    JenisKelamin=str(input("Masukkan Jenis Kelamin: "))
    TinggiBadan=int(input("Masukkan Tinggi Badan: "))
    BeratBadanAwal=int(input("Masukkan Berat Badan Anda Sekarang:"))
    BeratBadanImpian=int(input("Masukkan Berat Badan Impian Anda:"))
    Email=str(input("Masukkan Email: "))
    Password=str(input("Masukkan Password: "))

    query="Insert into daftar values('','{}',{},'{}',{},{},{},'{}','{}','','')".format(Nama,Usia,JenisKelamin,TinggiBadan,BeratBadanAwal,BeratBadanImpian,Email,Password)
    cursor.execute(query)
    conn.commit()
    print("Registrasi Berhasil, Silahkan Login")
# Registrasi()

def Login():
    for x in range(3):
        Email=str(input("Masukkan Email\t\t: "))
        Password=str(input("Masukkan Password\t: "))
        print()
        if Email==("Admin") and Password==("123456"):
            from admin import programBerjalanAdmin
            programBerjalanAdmin()
        query= "select idPengguna from daftar where email='{}' and password='{}'".format(Email,Password)
        cursor.execute(query)
        id=cursor.fetchall()
        try:
            return id[0][0]
        except:
            print("Data Yang Anda Masukkan Salah")
    print("Anda telah gagal Login Sebanyak 3 Kali")
    return False

def Beranda():
    while True:
        main=int(input("1. Login \n2. Registrasi \n3. Logout \n Pilih menu di atas : "))
        print()
        if main==1:
            id=Login()
            while id!=False:
                query="select * from daftar where idPengguna="+str(id)
                cursor.execute(query)
                dataAkun=cursor.fetchall()[0]
                user=Pengguna(dataAkun[0], dataAkun[1], dataAkun[2], dataAkun[3], dataAkun[4],dataAkun[5], dataAkun[6], dataAkun[7], dataAkun[8], dataAkun[9], dataAkun[10])
                menu=int(input("Beranda \n1. Pilih Menu Diet \n2. Target \n3. Informasi Akun \n4. Keluar \nPilih menu di atas : "))
                print()
                if menu==1:
                    user.pilihMenu()
                    user.pilihOlahraga()
                elif menu==2:
                    user.Target()
                    ubahTarget=int(input("1. Ubah target : \n2. Kembali : \nPilih menu : "))
                    print()
                    if ubahTarget==1:
                        user.UbahTarget()
                    elif ubahTarget==2:
                        pass
                    else:
                        print("Menu tidak tersedia")
                elif menu==3:            
                    user.showInfoUser()
                    print()
                    menuAkun=int(input("1. Ubah data \n2. Kembali \nPilih Menu : "))
                    print()
                    if menuAkun==1:
                        ubah=int(input("1. Nama \n2. Usia \n3. Jenis kelamin \n4. Berat badan saat ini \n5. Berat badan tujuan \n6. Email \n7. Password \nPilih data yang akan diubah : "))
                        user.ubahData(ubah)
                    elif menuAkun==2:
                        pass
                elif menu==4:
                    exit()
                else:
                    print("Menu yang anda pilih tidak tersedia")
                    return False
        elif main==2:
            Registrasi()
        elif main==3:
            exit()
        else:
            print("Menu yang anda pilih tidak tersedia")
            
Beranda()