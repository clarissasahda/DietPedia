import mysql.connector
conn = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="dietpedia")
cursor=conn.cursor()

def aksesAdmin():
    while True:
        query = "Select * From paketdiet"
        cursor.execute(query)
        data = cursor.fetchall()
        admin=int(input("Menu Admin \n1. Melihat Paket \n2. Mengubah Paket \n3. Menambah Paket \n4. Menghapus Paket \n5. Keluar \nPilih hal yang ingin diakses : "))
        print()
        if admin==1:
            TampilkanPaket()
        elif admin==2:
            pass
aksesAdmin()
            
            # target()
        # elif admin==3:
        #     dataAkun=cursor.fetchall()[0]
        #     user=Pengguna(dataAkun[0], dataAkun[1], dataAkun[2], dataAkun[3], dataAkun[4],dataAkun[5], dataAkun[6], dataAkun[7])
        #     user.showInfo()
        #     print()
        #     menuAkun=int(input("1. Ubah data \n2. Kembali \nPilih Menu : "))
        #     print()
        #     if menuAkun==1:
        #         ubah=int(input("1. Nama \n2. Usia \n3. Jenis kelamin \n4. Berat badan saat ini \n5. Berat badan tujuan \n6. Password \nPilih data yang akan diubah : "))
        #         user.ubahData(ubah)
        #     elif menuAkun==2:
                # Beranda()
        # else:
        #     print("Menu yang anda pilih tidak tersedia")

# def ubahNamaPaket():
#         NamaPaket = str(input("input nama paket yang ingin dirubah : "))
#         cekPaket = "select NamaPaket from paketdiet where NamaPaket = '{}'".format(NamaPaket)
#         cursor.execute(cekPaket)
#         cekPaket = cursor.fetchall()
#         print("\npaket ditemukan dengan nama :",cekPaket[0][0])

#         adminInput = int(input("\nubah paket diet berdasarkan\n1. Nama Paket\n2. Isi Paket\nMasukkan pilihan  Anda : "))
#         if adminInput == 1:
#             try:
#                 NamaPaketBaru = str(input("Masukkan nama paket baru : "))
#                 query = "update paketdiet set NamaPaket = '{}' where NamaPaket = '{}'".format(NamaPaketBaru,NamaPaket)
#                 cursor.execute(query)
#                 conn.commit()
#                 print("\nNama Paket berhasil diubah :)\n")

#             except:
#                 print("\nNama Paket tidak ditemukan!\n")
# ubahNamaPaket()

def TampilkanPaket():
    
    for i in data: 
        print(i)

    # dataPaket=cursor.fetchall()[0]
    #         paketdiet=NamaPaket(dataPaket[0], dataPaket[1], dataPaket[2], dataPaket[3])
    #         paketdiet.showInfo()
    #         print()
    
    
    

        # elif adminInput == 2:
        #     try:
        #         query = "Select * From paketdiet"
        #         cursor.execute(query)
        #         data = cursor.fetchall()
        #         for i in data: 
        #             print(i)
        #         ubahIsiPaket = int(input("Masukkan paket yang isinya ingin diubah : "))
        #         cekPaket = "select * from paketdiet where NamaPaket = '{}'".format(NamaPaket)
        #         cursor.execute(cekPaket)
        #         cekPaket = cursor.fetchall()
        #         print("\npaket ditemukan dengan nama :",cekPaket[0][0])



        #         query = "update  set penulis = '{}' where judul = '{}'".format(penulisBaru,judulBuku)
        #         cursor.execute(query)
        #         conn.commit()
        #         print("\ndata buku berhasil dirubah :)\n")

        #     except:
        #         print("\njudul tersebut tidak ada!\n")
        # elif adminInput == 3:
        #     try:
        #         lokasiBaru = str(input("input penulis buku baru : "))
        #         query = "update buku set lokasi = '{}' where judul = '{}'".format(lokasiBaru,judulBuku)
        #         cursor.execute(query)
        #         conn.commit()
        #         print("\ndata buku berhasil dirubah :)\n")

        #     except:
        #         print("\njudul tersebut tidak ada!\n")

        # elif adminInput == 4:
        #     return True