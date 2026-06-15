lemari = [
    {
        "id" : 1,
        "nama_pakaian" : "Jersey",
        "kategori_pakaian" : "Sporty",
        "warna" : "Putih",
        "formalitas" : 3,
        "tanggal" : 20260101
    },
    {
        "id" : 2,
        "nama_pakaian" : "Kaos putih",
        "kategori_pakaian" : "Casual",
        "warna" : "Putih",
        "formalitas" : 2,
        "tanggal" : 20260122
    },
    {
        "id" : 3,
        "nama_pakaian" : "Kemeja Putih",
        "kategori_pakaian" : "Formal",
        "warna" : "Putih",
        "formalitas" : 8,
        "tanggal" : 20260304
    },
    {
        "id" : 4,
        "nama_pakaian" : "Celana Chino",
        "kategori_pakaian" : "Casual",
        "warna" : "Cream",
        "formalitas" : 6,
        "tanggal" : 20260608
    },
    {
        "id" : 5,
        "nama_pakaian" : "Kemeja Batik",
        "kategori_pakaian" : "Formal",
        "warna" : "Cokelat",
        "formalitas" : 7,
        "tanggal" : 20260708
    },
    {
        "id" : 6,
        "nama_pakaian" : "Legging Sport",
        "kategori_pakaian" : "Sporty",
        "warna" : "Hitam",
        "formalitas" : 2,
        "tanggal" : 20260710
    },
    {
        "id" : 7,
        "nama_pakaian" : "Kemeja Satin Silk",
        "kategori_pakaian" : "Formal",
        "warna" : "Maroon",
        "formalitas" : 8,
        "tanggal" : 20260812
    },
    {
        "id" : 8,
        "nama_pakaian" : "Cardigan Rajut",
        "kategori_pakaian" : "Casual",
        "warna" : "Milo",
        "formalitas" : 3,
        "tanggal" : 20260901
    },
    {
        "id" : 9,
        "nama_pakaian" : "Dress Kondangan",
        "kategori_pakaian" : "Formal",
        "warna" : "Sage Green",
        "formalitas" : 10,
        "tanggal" : 20260915
    },
    {
        "id" : 10,
        "nama_pakaian" : "Oversized T-Shirt",
        "kategori_pakaian" : "Casual",
        "warna" : "Putih",
        "formalitas" : 1,
        "tanggal" : 20261005
    },
    {
        "id" : 11,
        "nama_pakaian" : "Blouse Floral",
        "kategori_pakaian" : "Casual",
        "warna" : "Putih",
        "formalitas" : 4,
        "tanggal" : 20260101
    },
    {
        "id" : 12,
        "nama_pakaian" : "Rok Plisket",
        "kategori_pakaian" : "Casual",
        "warna" : "Cream",
        "formalitas" : 4,
        "tanggal" : 20260122
    },
    {
        "id" : 13,
        "nama_pakaian" : "Blazer Kerja",
        "kategori_pakaian" : "Formal",
        "warna" : "Hitam",
        "formalitas" : 9,
        "tanggal" : 20260304
    },
    {
        "id" : 14,
        "nama_pakaian" : "Celana Kulot",
        "kategori_pakaian" : "Formal",
        "warna" : "Hitam",
        "formalitas" : 7,
        "tanggal" : 20260608
    },
    {
        "id" : 15,
        "nama_pakaian" : "Crop Top Jersey",
        "kategori_pakaian" : "Sporty",
        "warna" : "Pink",
        "formalitas" : 2,
        "tanggal" : 20260708
    }

]

# ============================================================
# Menampilkan isi lemari
# ============================================================
def lihat_lemari(data = None):
    if data is None:
        data = lemari
    if len(data) == 0:
        print("\n [!] Lemari kosong dan data tidak ditemukan")
        return

    print("\n ===== DAFTAR PAKAIAN =====")

    print(f"{'ID':<6} {'nama_pakaian':<20} {'kategori_pakaian':<20} {'warna':<10} {'formalitas':<12} {'tanggal':<12}")

    print("=" * 90)

    for baju in data:
        print(
            f"{baju['id']:<6} "
            f"{baju['nama_pakaian']:<20} "
            f"{baju['kategori_pakaian']:<20} "
            f"{baju['warna']:<10} "
            f"{baju['formalitas']:<12} "
            f"{baju['tanggal']:<12} "
        )

# ============================================================
# Tambah Pakaian
# ============================================================
def tambah_pakaian():
    print("\n ===== TAMBAH PAKAIAN =====")

    nama = input("nama_pakaian : ")
    kategori = input("kategori_pakaian : ")
    warna = input("Warna : ")
    formalitas = int(input("Formalitas : "))
    tanggal = int(input("Tanggal dalam format (YYYYMMDD) : "))

    id_baru = lemari[-1]['id'] + 1 if lemari else 1

    data_baru = {
        "id" : id_baru,
        "nama_pakaian" : nama,
        "kategori_pakaian" : kategori,
        "warna" : warna,
        "formalitas" : formalitas,
        "tanggal" : tanggal 
    }

    lemari.append(data_baru)

    print("\n[OK] Pakaian berhasil ditambahkan")

# ============================================================
# EDIT PAKAIAN
# ============================================================
def edit_pakaian():
    lihat_lemari()
    edit_id = int(input("\n Masukkan ID yang ingin diedit : "))

    for baju in lemari :
        if baju['id'] == edit_id:
            print("\n Masukkan data id pakaian yang baru : ")

            baju["nama_pakaian"] = input("Nama baju baru : ")
            baju["kategori_pakaian"] = input("Kategori baru : ")
            baju["warna"] = input("Warna baru : ")
            baju["formalitas"] = int(input("Level baru : "))
            baju["tanggal"] = int(input("Tanggal baru : "))

            print("\n[OK] Data berhasil diubah")
            return

    print("\n [!] ID tidak ditemukan dan tidak terdaftar")

# ============================================================
# HAPUS PAKAIAN
# ============================================================
def hapus_pakaian():
    lihat_lemari()
    hapus_id = int(input("\n Masukkan ID yang ingin dihapus : "))

    for baju in lemari:
        if baju['id'] == hapus_id:
            lemari.remove(baju)
            print("\n[OK] Baju berhasil dihapus")
            return
    print("\n[i] ID Tidak Ditemukan")

    def sequential_search():
    cari = input("\n Masukkan warna yang ingin dicari : ").lower()
    hasil = []

    for baju in lemari:
        if baju["warna"].lower() == cari:
            hasil.append(baju)

    print("\n [HASIL PENCARIAN]")

    if len(hasil) > 0:
        lihat_lemari(hasil)
    else:
        print("\n [!] Data Tidak Ditemukan")

# ============================================================
# SEQUENTIAL SEARCH (berdasarkan warna)
# ============================================================
def sequential_search():
    cari = input("\n Masukkan warna yang ingin dicari : ").lower()
    hasil = []

    for baju in lemari:
        if baju["warna"].lower() == cari:
            hasil.append(baju)

    print("\n [HASIL PENCARIAN]")

    if len(hasil) > 0:
        lihat_lemari(hasil)
    else:
        print("\n [!] Data Tidak Ditemukan")

# ============================================================
# BINARY SEARCH (Cari kategori)
# ============================================================
def binary_search():
    data = sorted(lemari, key=lambda x: x["kategori_pakaian"])
    target = input("\n Masukkan kategori yang dicari : ").capitalize()

    kiri = 0
    kanan = len(data) - 1
    ditemukan = False

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if data[tengah]["kategori_pakaian"] == target:
            print("\n [DATA DITEMUKAN]")
            lihat_lemari([data[tengah]])
            ditemukan = True
            break
        elif data[tengah]["kategori_pakaian"] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    
    if ditemukan == False:
        print("\n [!] Data Tidak Ditemukan")

# ============================================================
# SELECTION SORT (Mengurutkan Formalitas - Descending)
# ============================================================
def selection_sort_formalitas():
    n = len(lemari)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            # Mencari tingkat formalitas tertinggi
            if lemari[j]["formalitas"] > lemari[max_idx]["formalitas"]:
                max_idx = j
        # Tukar posisi data di dalam list lemari
        lemari[i], lemari[max_idx] = lemari[max_idx], lemari[i]
        
    print("\n[OK] Lemari berhasil diurutkan dari yang Paling Formal ke Casual.")
    lihat_lemari()

# ============================================================
# INSERTION SORT (Mengurutkan Tanggal/Rotasi - Ascending)
# ============================================================
def insertion_sort_tanggal():
    for i in range(1, len(lemari)):
        key = lemari[i]
        j = i - 1
        
        # Membandingkan angka integer tanggal (YYYYMMDD)
        while j >= 0 and key["tanggal"] < lemari[j]["tanggal"]:
            lemari[j + 1] = lemari[j]
            j -= 1
        lemari[j + 1] = key
        
    print("\n[OK] Lemari berhasil diurutkan berdasarkan Tanggal Terlama (Rotasi Baju).")
    lihat_lemari()

# ============================================================
# ENGINE REKOMENDASI OOTD (Conditional Rule-Based Logic)
# ============================================================
def rekomendasi_ootd():
    print("\n ===== ASISTEN REKOMENDASI OOTD =====")
    acara = input("Jenis Acara (Formal / Casual / Sporty) : ").capitalize()
    cuaca = input("Kondisi Cuaca (Panas / Hujan) : ").capitalize()
    
    kandidat = []
    
    # Filter Tahap 1: Pembatasan berdasarkan kriteria acara dan level formalitas
    if acara == "Formal":
        kandidat = [baju for baju in lemari if baju["formalitas"] >= 7]
    elif acara == "Casual":
        kandidat = [baju for baju in lemari if 3 <= baju["formalitas"] <= 6]
    elif acara == "Sporty":
        kandidat = [baju for baju in lemari if baju["kategori_pakaian"].capitalize() == "Sporty"]
    else:
        print("\n[!] Kategori acara tidak dikenal. Menampilkan pilihan Smart-Casual.")
        kandidat = [baju for baju in lemari if 4 <= baju["formalitas"] <= 6]

    # Filter Tahap 2: Penyesuaian rekomendasi terhadap faktor cuaca
    if cuaca == "Hujan":
        print("\n[Saran Asisten]: Cuaca dingin/hujan. Pastikan OOTD Anda menggunakan Outer/Jaket!")
    elif cuaca == "Panas":
        # Mengeliminasi pakaian berbahan tebal (misal menghapus Jersey lengan panjang jika ada)
        kandidat = [baju for baju in kandidat if "jaket" not in baju["nama_pakaian"].lower()]

    # Menampilkan hasil keputusan engine rekomendasi
    if len(kandidat) > 0:
        print(f"\n >>> REKOMENDASI PAKAIAN UNTUK ANDA ({acara.upper()} - {cuaca.upper()}) <<<")
        lihat_lemari(kandidat)
    else:
        print("\n [!] Maaf, tidak ada koleksi di lemari yang cocok untuk kombinasi ini.")

# ============================================================
# INTERFACE MENU UTAMA (INTEGRASI UTUH SISTEM)
# ============================================================
def main():
    while True:
        print("=" * 50)
        print("      APLIKASI SMART wardrobe & OOTD PLANNER")
        print("=" * 50)
        print(" 1. Lihat Isi Lemari Baju")
        print(" 2. Tambah Koleksi Pakaian Baru")
        print(" 3. Edit Data Pakaian")
        print(" 4. Hapus Pakaian Dari Lemari")
        print(" 5. Cari Pakaian")
        print(" 6. Urutkan Susunan Lemari")
        print(" 7. Dapatkan Rekomendasi OOTD Hari Ini")
        print(" 0. Keluar dan Tutup Aplikasi")
        print("=" * 50)
        
        pilihan = input(" Masukkan nomor menu pilihan Anda: ")
        
        if pilihan == "1":
            lihat_lemari()
        elif pilihan == "2":
            tambah_pakaian()
        elif pilihan == "3":
            edit_pakaian()
        elif pilihan == "4":
            hapus_pakaian()
        elif pilihan == "5":
            print("\n >> PILIHAN METODE PENCARIAN <<")
            print(" 1. Cari Berdasarkan Warna   [Sequential Search]")
            print(" 2. Cari Berdasarkan Kategori [Binary Search]")
            sub_cari = input(" Pilih metode (1/2): ")
            if sub_cari == "1":
                sequential_search()
            elif sub_cari == "2":
                binary_search()
            else:
                print("\n [!] Pilihan sub-menu salah.")
        elif pilihan == "6":
            print("\n >> PILIHAN METODE PENGURUTAN <<")
            print(" 1. Urutkan Tingkat Formalitas [Selection Sort]")
            print(" 2. Urutkan Kronologi Tanggal  [Insertion Sort]")
            sub_urut = input(" Pilih metode (1/2): ")
            if sub_urut == "1":
                selection_sort_formalitas()
            elif sub_urut == "2":
                insertion_sort_tanggal()
            else:
                print("\n [!] Pilihan sub-menu salah.")
        elif pilihan == "7":
            rekomendasi_ootd()
        elif pilihan == "0":
            print("\n [Sistem Selesai] Lemari pakaian telah dikunci kembali. Terima kasih!")
            break
        else:
            print("\n [!] Kode menu tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()