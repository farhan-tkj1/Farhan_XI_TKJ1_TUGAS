# nama: Muhamad Farhan Habibi
# kelas: XI TKJ 
# No Absen: 17
# Soal: Di sebuah toko online, Anda bertanggung jawab untuk menghitung diskon berdasarkan jumlah total belanjaan pelanggan.

# Masukkan total belanjaan
total_belanja = float(input("Masukkan total belanja dari pelanggan: "))

# Diskon
diskon = 0

# Cek diskon
if total_belanja > 500000:
    diskon = 0.10  # Diskon 10% untuk total belanja pelanggan melebihi 500.000
elif total_belanja >= 300000:
    diskon = 0.05  # Diskon 5% untuk total belanja pelanggan di antara 300.000 dan 500.000

# Hitung total belanja pelanggan setelah mendapatkan diskon
total_setelah_mendapat_diskon = total_belanja - (total_belanja * diskon)

# Cetak total belanjaan dan total setelah diskon
print("Total belanja pelanggan: Rp", total_belanja)
print("Mendapatkan diskon sebesar", int(diskon * 100), "%")
print("Total setelah mendapatkan diskon: Rp", total_setelah_mendapat_diskon)