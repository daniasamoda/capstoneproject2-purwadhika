# capstoneproject2-purwadhika
This is the submission of Dania Samoda Renda capstone project 2 regarding the warehouse datastock flow and the python inside.

**Warehouse Stock System 📦**
Purwadhika Capstone Project Module 2 - Python for Data Analysis

1. Tentang Program Ini:

Warehouse Stock System adalah sebuah aplikasi berbasis Command Line Interface (CLI) yang ditulis menggunakan bahasa pemrograman Python. Program ini dirancang untuk mensimulasikan sistem manajemen basis data sederhana pada sebuah gudang. Pengguna dapat berinteraksi dengan sistem melalui terminal untuk mengelola data inventaris barang secara terpusat tanpa memerlukan antarmuka grafis (GUI).

2. Manfaat dan Kegunaan Program (Benefit)
Aplikasi ini memberikan kemudahan dalam pengelolaan stok gudang melalui fitur-fitur berikut:

- Pencatatan Sistematis: Memudahkan pengguna untuk melihat seluruh daftar barang yang tersedia di gudang beserta rincian lengkapnya.
- Akurasi Data (Validasi Input): Mencegah terjadinya duplikasi data dengan sistem penolakan otomatis jika pengguna memasukkan item_id yang sudah ada. Sistem juga memastikan tipe data jumlah stok dan harga hanya bisa diisi dengan angka (numeric).
- Efisiensi Pembaruan: Pengguna dapat memperbarui (update) satu spesifikasi atribut saja (misalnya hanya mengubah harga) tanpa harus menghapus dan menulis ulang seluruh data barang.
- Keamanan Data: Terdapat lapis konfirmasi (Yes/No) sebelum data disimpan atau dihapus secara permanen untuk mencegah kesalahan input pengguna.

3. Struktur Data (Keys)
Data inventaris disimpan menggunakan struktur List of Dictionaries di dalam Python. Setiap barang (item) memiliki 6 kunci (keys) spesifik sebagai berikut:

- item_id : Identitas unik barang (Bertindak sebagai Primary Key / tidak boleh sama).

- item_name : Nama produk atau barang.

- category : Kategori jenis barang (contoh: Food, Drink).

- stock : Jumlah ketersediaan barang di gudang (Tipe data: Integer).

- price : Harga satuan barang (Tipe data: Integer).

- supplier : Nama pemasok atau distributor barang tersebut.

4. Evaluasi Checklist Guideline Capstone Project
Berdasarkan dokumen instruksi JC BDA - Capstone Project Module 2 Guideline, syarat minimum kelulusan proyek:

[✓] Tipe Data Collection: Program menampung data dummy menggunakan tipe data collection bawaan Python, yaitu List berisi sekumpulan Dictionary.

[✓] Syarat Field & Kolom Unik: Program memiliki lebih dari batas minimum kolom (memiliki 6 kolom atribut) dengan 1 kolom bertindak sebagai nilai unik, yaitu item_id.

[✓] Fitur Utama CRUD: Program mengeksekusi 4 fitur utama secara lengkap:
- Create (Menu Add Data)
- Read (Menu Display Data)
- Update (Menu Update Data)
- Delete (Menu Delete Data)

[✓] Regular Function: Seluruh fitur menu utama dibungkus dan dijalankan menggunakan format regular function pada Python (def read_data(), def create_data(), dst).

[✓] Data Dummy: Program sudah memiliki inisiasi data awal (Indomie dan Aqua) sebelum pengguna mulai menginput data baru.



