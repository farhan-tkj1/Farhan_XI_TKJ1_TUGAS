#Muhamad Farhan Habibi
#11 TKJ1
#18
#Kode dibawah menjelaskan tentang diskon, dimana 10% diskon jika mencapai minimal total belanja 500000, diskon 5% jika total belanja diantara 300-500 ribu, dan tidak mendapat diskon jika total belanja dibawah 300 ribu




# Membaca total belanjaan dari pelanggan
total_belanjaan = float(input("Masukkan total belanjaan pelanggan: "))

# Inisialisasi variabel diskon
diskon = 0

# Memeriksa aturan diskon
if total_belanjaan > 500000:
    diskon = 0.10  # Diskon 10% untuk total belanjaan lebih dari 500.000
elif 300000 <= total_belanjaan <= 500000:
    diskon = 0.05  # Diskon 5% untuk total belanjaan antara 300.000 dan 500.000

# Menghitung total yang harus dibayar setelah diskon
total_setelah_diskon = total_belanjaan - (total_belanjaan * diskon)

# Menampilkan total belanjaan, diskon, dan total setelah diskon
print(f"Total Belanjaan: Rp {total_belanjaan:,.2f}")
print(f"Diskon: {diskon * 100}%")
print(f"Total Setelah Diskon: Rp {total_setelah_diskon:,.2f}")
