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