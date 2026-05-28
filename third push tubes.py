# ============================================================
# SELECTION SORT (Mengurutkan Formalitas)
# ============================================================
def selection_sort_formalitas():
    n = len(lemari)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if lemari[j]["formalitas"] > lemari[max_idx]["formalitas"]:
                max_idx = j
        lemari[i], lemari[max_idx] = lemari[max_idx], lemari[i]
        
    print("\n[OK] Lemari berhasil diurutkan dari yang Paling Formal ke Casual.")
    lihat_lemari()

# ============================================================
# INSERTION SORT (Mengurutkan Tanggal)
# ============================================================
def insertion_sort_tanggal():
    for i in range(1, len(lemari)):
        key = lemari[i]
        j = i - 1

        while j >= 0 and key["tanggal"] < lemari[j]["tanggal"]:
            lemari[j + 1] = lemari[j]
            j -= 1
        lemari[j + 1] = key
        
    print("\n[OK] Lemari berhasil diurutkan berdasarkan Tanggal Terlama (Rotasi Baju).")
    lihat_lemari()