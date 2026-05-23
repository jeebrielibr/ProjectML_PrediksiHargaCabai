# Laporan Analisis: Penggabungan Dataset Harga Cabai dan Cuaca

Laporan ini merangkum proses dan hasil dari penggabungan dataset harga cabai merah besar di Jakarta dengan dataset iklim/cuaca di Bandung untuk keperluan pemodelan prediksi berbasis CRISP-DM.

## 1. Tujuan Penggabungan
Tujuan utama dari tahap ini adalah untuk mengintegrasikan data target (harga cabai) dengan fitur-fitur prediktor (iklim) ke dalam satu dataset tunggal. Hal ini diperlukan agar model machine learning dapat mempelajari hubungan antara variabel cuaca di Bandung dengan fluktuasi harga cabai merah besar di Jakarta.

## 2. Sumber Data
Dua dataset utama yang digunakan dalam proses ini adalah:
*   **Dataset Harga**: `dataset/dataset_cabe_mb_cleaned.csv`
    *   Berisi harga harian Cabai Merah Besar (2021-2026).
*   **Dataset Cuaca**: `dataset/Cuaca_Bandung_Cleaned.csv`
    *   Berisi data meteorologi harian dari BMKG Bandung (2024-2026).

## 3. Metodologi Penggabungan
Proses penggabungan dilakukan melalui skrip Python dengan langkah-langkah sebagai berikut:
1.  **Standardisasi Tanggal**: Mengonversi kolom tanggal di kedua dataset ke tipe data `datetime` dan menyeragamkan nama kolom menjadi `tanggal`.
2.  **Inner Join**: Melakukan penggabungan berbasis irisan tanggal. Hanya tanggal yang memiliki data harga dan data cuaca yang dipertahankan.
3.  **Pembersihan**: Menghapus baris yang tidak lengkap untuk menjaga kualitas input model.

## 4. Hasil Analisis Dataset Tergabung (`dataset_merged.csv`)

### Karakteristik Dataset
*   **Jumlah Baris**: 518 baris.
*   **Rentang Waktu**: 1 Mei 2024 hingga 24 April 2026.
*   **Kolom Terpilih**:
    *   `tanggal`: Indeks waktu.
    *   `Cabai Merah Besar`: Variabel target (Harga).
    *   `TN`, `TX`, `TAVG`: Suhu (Minimum, Maksimum, Rata-rata).
    *   `RH_AVG`: Kelembapan rata-rata.
    *   `RR`: Curah hujan.
    *   `SS`: Lamanya penyinaran matahari.
    *   `FF_X`, `DDD_X`: Kecepatan dan arah angin.

### Validasi Kualitas
Berdasarkan hasil pengecekan kualitas data setelah penggabungan:
*   **Missing Values**: 0 (Tidak ada nilai kosong di seluruh kolom).
*   **Duplikasi**: 0 (Tidak ada tanggal yang berulang).
*   **Integritas**: Seluruh kolom numerik memiliki tipe data yang sesuai untuk analisis statistik.

## 5. Kesimpulan dan Langkah Selanjutnya
Proses integrasi data telah berhasil diselesaikan dengan hasil yang bersih dan valid. Dataset `dataset_merged.csv` kini siap untuk digunakan dalam tahap selanjutnya:
1.  **Exploratory Data Analysis (EDA)**: Menganalisis korelasi antara variabel cuaca dan harga.
2.  **Feature Engineering**: Membuat fitur tambahan seperti *lagged features* atau *rolling averages* jika diperlukan.
3.  **Modeling**: Pelatihan model prediksi harga.

---
*Laporan ini disusun oleh AI Team Member sebagai bagian dari dokumentasi teknis proyek DM210.*
