# Ringkasan Analisis Dataset Iklim Bandung (Mei 2024 - April 2026)

Dataset ini berisi laporan iklim harian untuk wilayah Bandung yang mencakup periode dari Mei 2024 hingga April 2026. Ringkasan ini telah diperbarui berdasarkan proses *Data Understanding* dan *Exploratory Data Analysis (EDA)* yang dilakukan pada notebook proyek.

## Metodologi Data Understanding & Cleaning
- **Penanganan Nilai Anomali**: Nilai khusus `8888` (data tidak terukur/trace) dan `9999` (tidak ada pengamatan) telah diidentifikasi sebagai data hilang dan dikonversi menjadi `NaN`.
- **Imputasi Data**: Menggunakan metode **Interpolasi Linier** untuk mengisi nilai yang hilang. Metode ini dipilih karena sangat cocok untuk data *time series* cuaca guna mempertahankan kontinuitas tren harian.
- **Strukturasi Waktu**: Kolom tanggal telah dikonversi ke format `datetime` dan ditetapkan sebagai indeks utama untuk mempermudah analisis deret waktu.

## Insight Utama (Hasil EDA)

### 1. Profil Suhu & Distribusi
- **Distribusi Normal**: Suhu rata-rata (`TAVG`) dan kelembapan (`RH_AVG`) menunjukkan distribusi yang cenderung terpusat, memudahkan identifikasi batas kondisi cuaca normal di Bandung.
- **Suhu Dingin Khas**: Suhu minimum (`TN`) konsisten di kisaran **16°C - 22°C**. Suhu tertinggi biasanya tercatat pada bulan-bulan kering (seperti Oktober) yang dapat mencapai **35°C**.

### 2. Kelembapan & Korelasi Multivariat
- **Tingkat Kelembapan**: Rata-rata kelembapan berada di atas **70%**, dengan puncak mencapai **95%** pada musim hujan.
- **Hubungan Antar Variabel**: Analisis *heatmap* korelasi menunjukkan hubungan linier yang signifikan antar parameter cuaca. Terdapat korelasi kuat antara tingkat kelembapan (`RH_AVG`) dengan peluang dan intensitas curah hujan harian.

### 3. Pola Curah Hujan & Deteksi Outlier
- **Identifikasi Outlier**: Berdasarkan analisis *boxplot*, ditemukan banyak pencilan (*outliers*) pada variabel curah hujan (`RR`). Ini menunjukkan adanya hari-hari dengan kejadian hujan sangat lebat/ekstrem yang terjadi di luar pola hujan reguler.
- **Karakteristik Hujan**: Banyaknya kejadian hujan rintik (*trace*) yang sebelumnya tercatat sebagai `8888` kini telah tertangani melalui imputasi untuk menjaga integritas data model.

### 4. Analisis Tren Waktu (Time Series)
- **Dinamika Musiman**: Plot deret waktu memperlihatkan fluktuasi harian yang dinamis antara musim kemarau dan musim hujan. Puncak curah hujan biasanya diikuti dengan penurunan suhu rata-rata harian yang cukup terlihat.
- **Angin & Matahari**: Kecepatan angin maksimum berada di kisaran **0-8 m/s**, sementara durasi penyinaran matahari sangat fluktuatif (0-8 jam) tergantung pada tutupan awan harian.

## Kesimpulan & Kesiapan Data
Dataset ini kini dalam kondisi **bersih (cleaned)** dan siap untuk tahap pemodelan *Data Mining*. Melalui teknik interpolasi dan penanganan *outlier*, integritas temporal data tetap terjaga. Dataset ini sangat layak digunakan sebagai fitur prediktor dalam model prediksi harga pangan, mengingat korelasi kuat antara faktor cuaca (seperti kelembapan dan hujan ekstrem) terhadap potensi produktivitas pertanian di wilayah penyokong Jakarta.
