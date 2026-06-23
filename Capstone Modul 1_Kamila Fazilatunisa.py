# Capstone Project Modul 1
# Sistem Data Penjualan Toko Makeup
# Kamila Fazilatunisa - 007

# data produk disimpen di list of dictionary
dataProduk = [
    {
        "Kode": "P001",
        "Nama": "Concealer",
        "Merek": "Pixy",
        "Harga": 40000,
        "Stok": 20
    },
    {
        "Kode": "P002",
        "Nama": "Eyeshadow",
        "Merek": "Pinkflash",
        "Harga": 80000,
        "Stok": 15
    },
    {
        "Kode": "P003",
        "Nama": "Foundation",
        "Merek": "Luxcrime",
        "Harga": 90000,
        "Stok": 10
    },
    {
        "Kode": "P004",
        "Nama": "Lipstick",
        "Merek": "Dearmebeauty",
        "Harga": 60000,
        "Stok": 5
    },
    {
        "Kode": "P005",
        "Nama": "Maskara",
        "Merek": "Somethinc",
        "Harga": 85000,
        "Stok": 5
    }
]


# ---------- HELPER ----------

def cek_kode_duplikat(kode): # menerima satu parameter -> kode yang mau dicek
    for produk in dataProduk:
        if produk["Kode"].lower() == kode.lower():
            return True # kode sudah dipakai
    return False # kalo looping gak ketemu

def tampil_satu_produk(produk): # supaya detail lebih rapi
    print(f"  Kode    : {produk['Kode']}")
    print(f"  Nama    : {produk['Nama']}")
    print(f"  Merek   : {produk['Merek']}")
    print(f"  Harga   : Rp{produk['Harga']:,}")
    print(f"  Stok    : {produk['Stok']}")
    if produk["Stok"] <= 3: # kalo stoknya kurang dari 3
        print(f" STOK HAMPIR HABIS!")
    print("-" * 35)

def tampil_tabel_semua():
    # nampilin semua data dalam bentuk tabel sederhana
    print(f"\n{'='*65}")
    print(f"{'No':<5} {'Kode':<8} {'Nama':<15} {'Merek':<15} {'Harga':>12} {'Stok':>6}")
    print(f"{'='*65}")
    for i, p in enumerate(dataProduk, 1):
        warning = " stok hampir habis" if p["Stok"] <= 3 else ""
        print(f"{i:<5} {p['Kode']:<8} {p['Nama']:<15} {p['Merek']:<15} Rp{p['Harga']:>9,} {p['Stok']:>5}{warning}")
    print(f"{'='*65}")


# ---------- READ ----------

def read_menu():
    while True:
        print("\n--- LIHAT DATA PRODUK ---")
        print("1. Tampilkan semua produk")
        print("2. Cari produk by kode")
        print("3. Cari produk by nama / merek")
        print("4. Kembali ke menu utama")
        pilihan = input("Pilih: ").strip()

        if pilihan == "1":
            if not dataProduk:
                print("Data tidak ada.")
            else:
                tampil_tabel_semua()

        elif pilihan == "2":
            if not dataProduk:
                print("Data tidak ada.")
                continue
            kode = input("Masukkan kode produk: ").strip().upper()
            ketemu = False
            for p in dataProduk:
                if p["Kode"] == kode:
                    print()
                    tampil_satu_produk(p)
                    ketemu = True
                    break
            if not ketemu:
                print("Produk tidak ditemukan.")

        elif pilihan == "3":
            if not dataProduk:
                print("Data tidak ada.")
                continue
            keyword = input("Masukkan nama atau merek produk: ").strip().lower()
            hasil = [p for p in dataProduk if keyword in p["Nama"].lower() or keyword in p["Merek"].lower()]
            if hasil:
                print(f"\nDitemukan {len(hasil)} produk:")
                print("-" * 35)
                for p in hasil:
                    tampil_satu_produk(p)
            else:
                print("Produk tidak ditemukan.")

        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid.")


# ---------- CREATE ----------

def create_menu():
    while True:
        print("\n--- TAMBAH PRODUK BARU ---")
        print("1. Tambah produk")
        print("2. Kembali ke menu utama")
        pilihan = input("Pilih: ").strip()

        if pilihan == "1":
            print("\nMasukkan data produk baru:")

            # input kode
            while True:
                kode = input("Kode Produk (contoh: P006): ").strip().upper()
                if not kode:
                    print("Kode tidak boleh kosong.")
                elif cek_kode_duplikat(kode):
                    print("Kode sudah ada, gunakan kode lain.")
                else:
                    break

            nama = input("Nama Produk: ").strip()
            merek = input("Merek: ").strip()

            # validasi harga & stok harus angka
            while True:
                try:
                    harga = int(input("Harga (Rp): ").strip())
                    if harga < 0:
                        print("Harga tidak boleh negatif.")
                        continue
                    break
                except ValueError:
                    print("Harga harus berupa angka.")

            while True:
                try:
                    stok = int(input("Stok: ").strip())
                    if stok < 0:
                        print("Stok tidak boleh negatif.")
                        continue
                    break
                except ValueError:
                    print("Stok harus berupa angka.")

            produk_baru = {
                "Kode": kode,
                "Nama": nama,
                "Merek": merek,
                "Harga": harga,
                "Stok": stok
            }

            print("\nData yang akan disimpan:")
            tampil_satu_produk(produk_baru)

            konfirmasi = input("Simpan data? (y/n): ").strip().lower()
            if konfirmasi == "y":
                dataProduk.append(produk_baru)
                print(" Data berhasil disimpan!")
            else:
                print("Penambahan dibatalkan.")

        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid.")


# ---------- UPDATE ----------

def update_menu():
    while True:
        print("\n--- UPDATE DATA PRODUK ---")
        print("1. Update data produk")
        print("2. Kembali ke menu utama")
        pilihan = input("Pilih: ").strip()

        if pilihan == "1":
            if not dataProduk:
                print("Data tidak ada.")
                continue

            kode = input("Masukkan kode produk yang mau diubah: ").strip().upper()
            produk_target = None
            for p in dataProduk:
                if p["Kode"] == kode:
                    produk_target = p
                    break

            if not produk_target:
                print("Data yang kamu cari tidak ada.")
                continue

            print("\nData saat ini:")
            tampil_satu_produk(produk_target)

            lanjut = input("Lanjut update? (y/n): ").strip().lower()
            if lanjut != "y":
                print("Update dibatalkan.")
                continue

            # kolom yang bisa diubah
            kolom_valid = ["Nama", "Merek", "Harga", "Stok"]
            print(f"\nKolom yang bisa diubah: {', '.join(kolom_valid)}")
            kolom = input("Kolom mana yang mau diubah: ").strip().capitalize()

            if kolom not in kolom_valid:
                print("Kolom tidak valid.")
                continue

            nilai_baru = input(f"Masukkan nilai baru untuk {kolom}: ").strip()

            # konversi tipe data kalau kolom Harga atau Stok
            if kolom in ["Harga", "Stok"]:
                try:
                    nilai_baru = int(nilai_baru)
                    if nilai_baru < 0:
                        print("Nilai tidak boleh negatif.")
                        continue
                except ValueError:
                    print("Nilai harus berupa angka.")
                    continue

            konfirmasi = input(f"Update {kolom} jadi '{nilai_baru}'? (y/n): ").strip().lower()
            if konfirmasi == "y":
                produk_target[kolom] = nilai_baru
                print(" Data berhasil diupdate!")
                print("\nData terbaru:")
                tampil_satu_produk(produk_target)
            else:
                print("Update dibatalkan.")

        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid.")


# ---------- DELETE ----------

def delete_menu():
    while True:
        print("\n--- HAPUS DATA PRODUK ---")
        print("1. Hapus produk")
        print("2. Kembali ke menu utama")
        pilihan = input("Pilih: ").strip()

        if pilihan == "1":
            if not dataProduk:
                print("Data tidak ada.")
                continue

            kode = input("Masukkan kode produk yang mau dihapus: ").strip().upper()
            produk_target = None
            idx_target = None

            for i, p in enumerate(dataProduk):
                if p["Kode"] == kode:
                    produk_target = p
                    idx_target = i
                    break

            if not produk_target:
                print("Data yang kamu cari tidak ada.")
                continue

            print("\nData yang akan dihapus:")
            tampil_satu_produk(produk_target)

            konfirmasi = input("Yakin mau hapus? (y/n): ").strip().lower()
            if konfirmasi == "y":
                dataProduk.pop(idx_target)
                print(" Data berhasil dihapus!")
            else:
                print("Penghapusan dibatalkan.")

        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid.")

# ---------- MAIN MENU ----------

def main():
    while True:
        print("\n" + "="*40)
        print("   SISTEM DATA PENJUALAN TOKO MAKEUP")
        print("="*40)
        print("1. Lihat Data Produk")
        print("2. Tambah Produk Baru")
        print("3. Update Data Produk")
        print("4. Hapus Produk")
        print("5. Keluar")
        print("-"*40)

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            read_menu()
        elif pilihan == "2":
            create_menu()
        elif pilihan == "3":
            update_menu()
        elif pilihan == "4":
            delete_menu()
        elif pilihan == "5":
            print("\nTerima kasih! Sampai jumpa kembali")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")


# jalanin program
main()

