# DDP LAB-3

print("NIM\t\t : 0110220045")
print("Nama\t :Evry Nazyli Ciptanto")
print("Program Studi Teknik Informatika\n")

# SOAL 1 - Gunting-Batu-Kertas
# Tuliskan program untuk Soal 1 di bawah ini

print("SOAL 1 - Gunting-Batu-Kertas")
# mendapatkan input user player 1 dan 2 dan disimpan di variabel user 1 dan user 2
user1 = input('Masukkan pilihan Player-1: ')
user2 = input('Masukkan pilihan Player-2: ')
# lower - > case insensitive
# jika user 1 gunting
if (user1.lower()=="gunting"):
  # jika user 2 gunting
  if user2.lower()=="gunting":
    # menampilkan pesan seri
    print("Pertandingan seri.")
  # jika user 2 batu
  elif user2.lower()=="batu":
  # player 2 menang
    print("Player-2 menang.")
  # jika user 2 kertas
  elif user2.lower()=="kertas":
  # player 1 menang
    print("Player-1 menang.")
  # jika player 2 salah input
  else:
    print("Player 2 - Input tidak terdaftar")
# jika player 1 kertas
elif (user1.lower()=="kertas"):
  # jika player 2 gunting
  if user2.lower()=="gunting":
    # player 2 menang
    print("Player-2 menang.")
  # jika player 2 batu
  elif user2.lower()=="batu":
    # player 1 menang
    print("Player-1 menang.")
  #  jika player 2 kertas
  elif user2.lower()=="kertas":
    # pertandingan seri
    print("Pertandingan seri.")
  else:
    # jika player 2 salah input
    print("Player 2 - Input tidak terdaftar")
# jika player 1 batu
elif (user1.lower()=="batu"):
  # jika player 2 gunting
  if user2.lower()=="gunting":
    # player 1 menang
    print("Player-1 menang.")
  # jika player 2 batu
  elif user2.lower()=="batu":
    # pertandingan seri
    print("Pertandingan seri.")
  # jika player 2 kertas
  elif user2.lower()=="kertas":
    # player 2 menang
    print("Player-2 Menang.")
  else:
    # jika player 2 salah input
    print("Player 2 - Input tidak terdaftar")
else:
    print("Player 1 - Input tidak terdaftar")

# lower() ->
# sumber : https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison

# SOAL 2 - Toko Buku Bekas
# Tuliskan program untuk Soal 2 di bawah ini

print("\nSOAL 2 - Toko Buku Bekas")
# mendapatkan input user dan menyimpan ke variable buku
buku = int(input("Masukkan banyaknya buku yang akan dibeli: "))
harga = 0
# jika buku kurang dari sama dengan 10
if (buku <=10):
  # harga dikali 20.000 per buku
  harga = buku * 20000
#jika buku antara 11-25 
elif (buku>10) and (buku <=25):
  # harga dikali 18.000 per buku
  harga = buku * 18000
elif (buku>25) and (buku <=50):
  # harga dikali 15.000 per buku 
  harga = buku * 15000
# jika buku lebih dari 50 
elif (buku>50):
  # harga dikali 10.000 per buku
  harga = buku * 10000

print("Harga yang harus dibayar =", harga,"rupiah")


# SOAL 3 - Mencetak Persegi
# Tuliskan program untuk Soal 3 di bawah ini

print("\nSOAL 3 - Mencetak Persegi")
# mendapatkan input user dan menyimpan ke variable persegi
persegi = int(input("Masukkan sebuah bilangan bulat: "))
for i in range(1,persegi+1):
  # cek apakah dia bilangan ganjil
  if i % 2!=0:
    # jika ganjil print #
    print("# " * persegi)
  else:
    # jika genap print $
    print("$ " * persegi)



