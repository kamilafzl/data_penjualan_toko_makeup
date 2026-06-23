# Data Penjualan Toko Makeup
Python-based CRUD application for managing makeup store sales data with inventory tracking and reporting features.
1. Judul/tema aplikasi :
Data Penjualan Toko Makeup

2. Deskripsi aplikasi :
Aplikasi pencatatan data penjualan pada suatu toko makeup. Aplikasi ini dibuat untuk memenuhi syarat kelulusan Capstone Project Module 1 Purwadhika.

3. User/stakeholder :
Pemilik atau admin toko makeup yang butuh mencatat data produk, stok, dan harga tanpa pakai buku catatan manual.

4. Tujuan pembuatan aplikasi :
Mempermudah toko makeup kecil-menengah dalam mengelola data produk: nambah, lihat, ubah, dan hapus data, sekaligus dapat laporan ringkas kondisi stok tanpa cek satu-satu.

5. Penjelasan fitur (bagi menjadi fitur utama (CRUD) dan fitur tambahan)


     a. CRUD

       - Create: tambah produk baru, dengan validasi kode duplikat dan validasi input harus angka
   
       - Read: lihat semua produk dalam tabel, cari produk by kode, cari produk by nama/merek
   
       - Update: ubah data produk (Nama, Merek, Harga, atau Stok)
   
       - Delete: hapus produk dengan konfirmasi dulu sebelum data hilang
   
    b. Peringatan Stok Kritis

       - otomatis menampilkan tanda kalau stok produk sisa 3 unit atau kurang
    c. Laporan Toko
      
       - total jenis produk, total unit stok, total nilai stok, harga rata-rata, produk stok paling sedikit, dan daftar produk yang perlu di-restock

5. Minimum Requirements

Python 3.13, dijalankan di terminal/CLI biasa tanpa library eksternal tambahan.

    1. Limitasi Aplikasi

Aplikasi ini hanya bisa nyimpen data selama program lagi jalan (in-memory). Begitu program ditutup, semua perubahan (tambah/update/hapus produk) tidak disimpan dan bakal balik ke data awal pas dijalankan lagi.

    2. Credits
Copyright Kamila Fazilatunisa. All rights reserved
