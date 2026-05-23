# Laporan Analisis Komprehensif: Dinamika Harga Pangan Jakarta (2021-2026)

## 1. Profil dan Karakteristik Dataset
Dataset ini merupakan catatan harian harga pangan strategis di pasar tradisional wilayah DKI Jakarta, yang dikelola oleh Pusat Informasi Harga Pangan Strategis (PIHPS). Data mencakup rentang waktu dari Januari 2021 hingga April 2026.

### Karakteristik Teknis:
Berdasarkan proses *Data Understanding* yang dilakukan pada notebook pendukung:
*   **Volume Data**: Terdiri dari **1.386 entri** baris data.
*   **Dimensi**: Memiliki **32 kolom** yang mencakup variasi detail dari komoditas utama (contoh: pemisahan Beras Kualitas Bawah, Medium, hingga Super).
*   **Kualitas Awal**: Data mentah masuk dalam format string (objek) dengan pemisah ribuan berupa koma (`,`), sehingga memerlukan proses pembersihan teknis untuk konversi ke tipe numerik (`float64`).
*   **Keunikan Data Hilang**: Terdapat kekosongan data pada tanggal-tanggal tertentu (seperti 1 Januari, hari libur keagamaan, dan akhir pekan). Hal ini menunjukkan bahwa data ini adalah data operasional pasar tradisional yang tidak melakukan pencatatan di hari libur.

## 2. Analisis Statistik Komoditas Utama
Setelah dilakukan pembersihan dan konversi data, berikut adalah profil harga dari komoditas pangan yang paling berpengaruh terhadap inflasi di Jakarta:

| Kelompok Komoditas | Deskripsi Statistik (Rupiah) | Insight Singkat |
| :--- | :--- | :--- |
| **Daging Sapi** | Rata-rata: **139.383** <br> (Range: 125.000 - 154.800) | Komoditas dengan nilai nominal tertinggi dan relatif stabil namun mengalami kenaikan bertahap. |
| **Cabai Merah** | Rata-rata: **56.340** <br> (Maks: 132.500) | Menunjukkan volatilitas harga paling ekstrem di antara semua bahan pokok. |
| **Bawang Merah** | Rata-rata: **42.872** <br> (Maks: 81.650) | Harga pernah melonjak hingga hampir dua kali lipat dari rata-rata normalnya. |
| **Beras** | Rata-rata: **14.792** <br> (Range: 12.600 - 16.800) | Komoditas dengan fluktuasi harian rendah namun memiliki tren *creeping inflation* (kenaikan kecil tapi terus-menerus). |
| **Daging Ayam** | Rata-rata: **37.510** <br> (Min: 31.100) | Harga sangat sensitif terhadap momen hari raya keagamaan. |

## 3. Analisis Tren dan Pola Perilaku Harga

### A. Tren Inflasi Jangka Panjang (Beras & Daging)
Beras menunjukkan pola kenaikan yang linear. Dari harga rata-rata sekitar **Rp13.355 pada tahun 2021**, merangkak naik hingga menyentuh angka **Rp16.631 pada tahun 2026**. Pola serupa terlihat pada Daging Sapi. Hal ini mengindikasikan adanya pengaruh inflasi struktural dan peningkatan biaya logistik atau pakan dalam jangka panjang.

### B. Anomali Krisis 2022
Tahun 2022 menjadi tahun yang krusial dalam dataset ini. Terjadi lonjakan tajam pada **Minyak Goreng** yang mencapai rata-rata harga tertinggi di angka **Rp20.592** (naik dari Rp16.635). Selain itu, **Cabai Merah** mencapai rekor tertingginya di **Rp132.500**. Fenomena ini kemungkinan besar dipengaruhi oleh gangguan rantai pasok global dan faktor iklim ekstrem pada tahun tersebut.

### C. Pola Musiman dan Siklus Keagamaan
Data secara konsisten menunjukkan "gelombang" kenaikan harga pada periode **April-Mei**. Secara deskriptif, ini merupakan siklus tahunan menjelang **Idul Fitri**. Komoditas seperti Daging Ayam, Telur, dan Bawang Putih mengalami kenaikan permintaan yang mendorong harga ke titik maksimum tahunan mereka.

### D. Volatilitas Berbasis Cuaca (Cabai & Bawang)
Komoditas hortikultura (Cabai dan Bawang) menunjukkan profil harga "bergigi gergaji" (naik-turun tajam dalam waktu singkat). Lonjakan harga sering terjadi pada kuartal pertama (Januari-Maret), yang secara teknis bertepatan dengan puncak musim hujan di daerah penghasil, yang sering menyebabkan gagal panen atau kendala distribusi ke Jakarta.

## 4. Kesimpulan dan Rekomendasi
Secara keseluruhan, harga bahan pokok di Jakarta periode 2021-2026 menunjukkan tren meningkat. Dataset ini mengungkapkan bahwa Jakarta sangat rentan terhadap:
1.  **Guncangan Pasokan Hortikultura**: Terutama cabai dan bawang yang harganya bisa tidak terkendali saat musim hujan.
2.  **Kenaikan Harga Pokok Beras**: Yang meskipun stabil, namun terus meningkat dan dapat membebani daya beli masyarakat kelas bawah.

**Insight untuk Pengolahan Data Selanjutnya:**
Mengingat adanya data hilang pada hari libur, proses *imputation* (pengisian data hilang) seperti *Linear Interpolation* atau *Forward Fill* sangat disarankan sebelum data ini digunakan untuk model prediksi (Machine Learning) agar urutan waktu (*time-series*) tetap konsisten.
