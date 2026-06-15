def rekomendasi_ootd():
    print("\n ===== ASISTEN REKOMENDASI OOTD =====")
    acara = input("Jenis Acara (Formal / Casual / Sporty) : ").capitalize()
    cuaca = input("Kondisi Cuaca (Panas / Hujan) : ").capitalize()
    
    kandidat = []
    
    if acara == "Formal":
        kandidat = [baju for baju in lemari if baju["formalitas"] >= 7]
    elif acara == "Casual":
        kandidat = [baju for baju in lemari if 3 <= baju["formalitas"] <= 6]
    elif acara == "Sporty":
        kandidat = [baju for baju in lemari if baju["kategori_pakaian"].capitalize() == "Sporty"]
    else:
        print("\n[!] Kategori acara tidak dikenal. Menampilkan pilihan Smart-Casual.")
        kandidat = [baju for baju in lemari if 4 <= baju["formalitas"] <= 6]

    if cuaca == "Hujan":
        print("\n[Saran Asisten]: Cuaca dingin/hujan. Pastikan OOTD Anda menggunakan Outer/Jaket!")
    elif cuaca == "Panas":
        # Mengeliminasi pakaian berbahan tebal (misal menghapus Jersey lengan panjang jika ada)
        kandidat = [baju for baju in kandidat if "jaket" not in baju["nama_pakaian"].lower()]

    if len(kandidat) > 0:
        print(f"\n >>> REKOMENDASI PAKAIAN UNTUK ANDA ({acara.upper()} - {cuaca.upper()}) <<<")
        lihat_lemari(kandidat)
    else:
        print("\n [!] Maaf, tidak ada koleksi di lemari yang cocok untuk kombinasi ini.")
