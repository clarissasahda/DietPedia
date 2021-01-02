import mysql.connector
conn = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="dietpedia")
cursor=conn.cursor()

class Admin():
    def __init__(self, idMakan, idOlahraga, namaMakanan, namaOlahraga, jumlahKalori, kaloriTerbakar):
        self.idMakan=idMakan
        self.idOlahraga=idOlahraga
        self.namaMakanan=namaMakanan
        self.namaOlahraga=namaOlahraga
        self.jumlahKalori=jumlahKalori
        self.kaloriTerbakar=kaloriTerbakar
    
    # def ubahMakanan(self):
    #     self.namaMakanan=str(input("Masukkan nama olahraga baru : "))
    #     self.jumlahKalori=str(input("Masukkan jumlah kalori terbakar baru : "))
    #     query = "update makanan set namaMakanan ='{}', jumlahKalori = {} where IdMakan = {}".format(self.namaMakanan,self.jumlahKalori, self.idMakan)
    #     cursor.execute(query)
    #     conn.commit()
    
    # def ubahOlahraga(self):
    #     self.namaOlahraga=str(input("Masukkan nama olahraga baru : "))
    #     self.kaloriTerbakar=str(input("Masukkan jumlah kalori terbakar baru : "))
    #     query = "update olahraga set namaOlahraga ='{}', kaloriTerbakar = {} where IdOlahraga = '{}'".format(self.namaOlahraga,self.kaloriTerbakar, self.idOlahraga)
    #     cursor.execute(query)
    #     conn.commit()
    

def tambahMakanan():
    namaMakanan=str(input("Masukkan nama makanan : "))
    jumlahKalori=int(input("Masukkan kalori makanan : "))
    query="Insert into makanan values('','{}',{})".format(namaMakanan,jumlahKalori)
    cursor.execute(query)
    conn.commit()

def MenuMakan():
    print("Pilih menu dibawah ini")
    query = "Select * From makanan"
    cursor.execute(query)
    dataMakanan=cursor.fetchall()
    makanan=(dataMakanan[0],dataMakanan[1],dataMakanan[2])
    inputMakan=[]
    for i in dataMakanan:
        print("{}. Nama makanan = {}\n   Jumlah kalori = {} kkal\n".format(i[0],i[1],i[2]))
        inputMakan.append([i[1],i[2]])
    print()

def Olahraga():
    print("Pilih menu dibawah ini")
    query = "Select * From olahraga"
    cursor.execute(query)
    dataOlahraga=cursor.fetchall()
    olahraga=(dataOlahraga[0],dataOlahraga[1],dataOlahraga[2])
    inputOlahraga=[]
    for i in dataOlahraga:
        print("{}. Nama olahraga = {}\n   Jumlah kalori terbakar = {} kkal\n".format(i[0],i[1],i[2]))
        inputOlahraga.append([i[1],i[2]])
    print()

def tambahOlahraga():
        namaOlahraga=str(input("Masukkan nama olahraga : "))
        kaloriTerbakar=int(input("Masukkan jumlah kalori terbakar : "))
        query="Insert into olahraga values('','{}',{})".format(namaOlahraga,kaloriTerbakar)
        cursor.execute(query)
        conn.commit()
    
def programBerjalanAdmin():
    while True:
        main=int(input("1. Lihat Makanan \n2. Ubah Makanan \n3. Tambahkan Makanan \n4. Lihat Olahraga \n5. Ubah Olahraga \n6. Tambahkan Olahraga \n7. Keluar \nPilih menu di atas : "))
        print()
        if main==1:
            MenuMakan()
        elif main==2:
            MenuMakan()
            # ubahMakanan()
        elif main==3:
            tambahMakanan()
        elif main==4:
            Olahraga()
        elif main==5:
            Olahraga()
            # ubahOlahraga()
        elif main==6:
            tambahOlahraga()
        elif main==7:
            exit()
        else:
            print("Menu yang anda pilih tidak tersedia")
programBerjalanAdmin()
