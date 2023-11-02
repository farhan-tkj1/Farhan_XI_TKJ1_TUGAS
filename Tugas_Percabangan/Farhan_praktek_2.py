# nama: Muhamad Farhan Habibi
# kelas: XI TKJ 
# No Absen: 17
# Soal: Sebagai seorang manajer proyek, Anda harus menentukan apakah suatu proyek akan selesai tepat waktu atau terlambat.
from datetime import datetime

# Masukkan estimasi waktu selesai proyek dalam format tanggal (YYYY-MM-DD)
estimasi_selesai = input("Masukkan estimasi waktu selesai (YYYY-MM-DD): ")
estimasi_selesai = datetime.strptime(estimasi_selesai, "%Y-%m-%d")

# Input tanggal target selesai proyek dalam format tanggal (YYYY-MM-DD)
tanggal_target = input("Masukkan tanggal target selesai (YYYY-MM-DD): ")
tanggal_target = datetime.strptime(tanggal_target, "%Y-%m-%d")

# Periksa apakah estimasi waktu selesai lebih awal atau sama dengan tanggal target
if estimasi_selesai <= tanggal_target:
    print("Tepat waktu")
else:
    print("Terlambat")