# Laporan Hasil Data Cleaning

Laporan ini merangkum proses pembersihan data (*data cleaning*) yang dilakukan pada dua dataset utama: Harga Bahan Pokok (Jakarta) dan Cuaca (Bandung). Tujuan utama dari proses ini adalah untuk memastikan integritas data sebelum dilakukan penggabungan dan analisis lebih lanjut untuk prediksi harga cabai.

## 1. Data Cleaning: Harga Bahan Pokok (Jakarta)

Proses pembersihan data harga dilakukan pada file `PIHPS_Jakarta_Full_2021_2026.csv`. Fokus utama adalah mengubah format data mentah yang mengandung karakter non-numerik menjadi format yang siap diolah.

### Langkah-langkah Pembersihan:
- **Konversi Tanggal:** Kolom `Tanggal` diubah menjadi tipe data `datetime` menggunakan `pd.to_datetime`. Baris dengan tanggal yang tidak valid dihapus.
- **Normalisasi Nama Kolom:** Menghapus spasi di awal dan akhir (*strip*) pada semua nama kolom.
- **Pembersihan Nilai Numerik:**
  - Karakter seperti koma (`,`) dan tanda hubung (`-`) dihapus dari kolom harga.
  - Nilai diubah menjadi tipe data numerik. Nilai yang kosong atau tidak valid diubah menjadi `NaN`.
- **Penanganan Missing Values:**
  - Menggunakan **Interpolasi Linier** untuk mengisi kekosongan data di tengah urutan waktu.
  - Menggunakan **Backward Fill (bfill)** untuk menangani nilai `NaN` yang mungkin muncul di baris awal dataset.
- **Pengurutan:** Data diurutkan berdasarkan `Tanggal` untuk memastikan kontinuitas deret waktu.

### Output:
- `PIHPS_Jakarta_Cleaned_2021_2026.csv`: Dataset lengkap yang telah dibersihkan.
- `dataset_cabe_mb_cleaned.csv`: Dataset khusus yang hanya berisi harga **Cabai Merah Besar**.

---

## 2. Data Cleaning: Cuaca Bandung

Proses pembersihan data cuaca dilakukan pada file `Gabungan_Laporan_Iklim_Harian_Bandung_Mei_2024_April_2026.csv`. Dataset ini memiliki tantangan khusus berupa kode internal untuk data yang hilang.

### Langkah-langkah Pembersihan:
- **Konversi Tanggal:** Kolom `TANGGAL` diubah ke format `datetime` dengan format `%d-%m-%Y`.
- **Penanganan Kode Khusus:**
  - Nilai `8888` (Data tidak terukur) dan `9999` (Tidak ada data) diganti menjadi `NaN`. Ini sangat penting agar statistik deskriptif tidak terdistorsi oleh nilai ekstrem tersebut.
- **Pengecekan Duplikat:** Memastikan tidak ada tanggal yang tercatat lebih dari satu kali untuk menjaga integritas deret waktu.
- **Interpolasi dengan Batasan:**
  - Menggunakan **Interpolasi Linier** dengan parameter `limit=5`. Hal ini dilakukan untuk menghindari pengisian data yang terlalu panjang secara artifisial, yang bisa mengurangi representasi kondisi cuaca yang sebenarnya.
- **Index Set:** Menetapkan `TANGGAL` sebagai index dataset.

### Output:
- `dataset_cuaca_bandung_cleaned.csv`: Dataset cuaca Bandung yang telah siap digunakan.

---

## Kesimpulan

Kedua dataset telah melalui tahap pembersihan yang ketat. Penanganan *missing values* menggunakan interpolasi linier pada kedua dataset memastikan bahwa data deret waktu tetap kontinu, yang sangat krusial untuk model prediksi Machine Learning di tahap selanjutnya. Data sekarang dalam kondisi optimal untuk digabungkan berdasarkan kunci `Tanggal`.
