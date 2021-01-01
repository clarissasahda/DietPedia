import mysql.connector
conn = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="dietpedia")
cursor=conn.cursor()

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
    jumlahMenu=int(input("Masukkan jumlah menu yang ingin anda pilih : "))
    noMakanan=[]
    for x in range(jumlahMenu):
        pilihMakan=int(input("Pilih menu ke {} : ".format(x+1)))
        noMakanan.append(pilihMakan)
    totalKalori=0
    listMakanan=""
    print("List Makanan : ")
    for makanan in noMakanan:
        print("Nama makanan = ",inputMakan[makanan][0])
        totalKalori+=inputMakan[makanan][1]
        listMakanan = listMakanan + "\n" + inputMakan[makanan][0]
    listMakanan = listMakanan + "\nTotal Kalori = " + str(totalKalori)
    print("Total kalori = ",totalKalori)
    return listMakanan

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
    jumlahOlahraga=int(input("Masukkan jumlah olahraga yang ingin anda pilih : "))
    noOlahraga=[]
    for x in range(jumlahOlahraga):
        pilihOlahraga=int(input("Pilih olaharaga ke {} : ".format(x+1)))
        noOlahraga.append(pilihOlahraga)
    totalKalori=0
    listOlahraga=""
    print("List Olahraga : ")
    for olahraga in noOlahraga:
        print("Nama olahraga = ",inputOlahraga[olahraga][0])
        totalKalori+=inputOlahraga[olahraga][1]
        listOlahraga = listOlahraga + "\n" + inputOlahraga[olahraga][0]
    listOlahraga = listOlahraga + "\nTotal Kalori terbakar = " + str(totalKalori)
    print("Total kalori terbakar = ",totalKalori)
    return listOlahraga


    