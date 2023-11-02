# nama: Muhamad Farhan Habibi
# kelas: XI TKJ 
# No Absen: 17
# Soal: Sebagai seorang sistem administrator, Anda bertanggung jawab untuk memeriksa apakah suatu file di server sudah ada atau belum sebelum menggantinya.

# Daftar file di server
daftar_file_di_server = ["file1.txt", "file2.txt", "data.txt", "file3.txt"]

# Input nama file dari pengguna
nama_file = input("Masukkan nama file: ")

# Periksa apakah nama_file ada dalam daftar_file_di_server
if nama_file in daftar_file_di_server:
    print("File sudah ada")
else:
    print("File belum ada")