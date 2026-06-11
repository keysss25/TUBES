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