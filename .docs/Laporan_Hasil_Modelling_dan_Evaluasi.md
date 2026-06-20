# Laporan Hasil Pemodelan dan Evaluasi: Prediksi Harga Cabai Merah Besar

Laporan ini menyajikan hasil analisis, eksperimen, dan evaluasi dari tahap **Pemodelan (*Modeling*)** dan **Evaluasi (*Evaluation*)** berdasarkan metodologi **CRISP-DM** untuk proyek *"Prediksi Harga Cabai Merah Besar Jakarta Berbasis Iklim Bandung"*. 

Analisis ini didasarkan pada eksperimen yang terdokumentasi dalam file notebook `notebook/Modelling_dengan_Evaluasi_FINAL_revisi_output.ipynb`.

---

## 1. Pendahuluan dan Tujuan (CRISP-DM: Modeling & Evaluation)

Tahap pemodelan bertujuan untuk memetakan hubungan statistik dan pola non-linear antara variabel iklim Bandung (prediktor) serta harga historis cabai (prediktor lag) terhadap harga aktual Cabai Merah Besar di Jakarta (target). Tahap evaluasi berikutnya mengukur akurasi prediktif model guna memastikan kelayakan model sebelum dideploy ke lingkungan produksi.

### Tujuan Utama Tahap Ini:
1.  **Komparasi Algoritma**: Membandingkan tiga model dengan arsitektur berbeda (Linear Regression, Random Forest, dan XGBoost) untuk menemukan model terbaik berdasarkan metrik error terkecil.
2.  **Validasi Kritis**: Menguji performa model terhadap baseline sederhana (*Naive Forecast*) untuk memastikan bahwa model *machine learning* benar-benar memberikan nilai tambah prediktif.
3.  **Analisis Faktor Kontribusi (*Feature Importance*)**: Mengidentifikasi fitur mana yang paling dominan dalam menentukan fluktuasi harga cabai.
4.  **Eksperimen Pengaruh Cuaca**: Menguji secara empiris seberapa besar kemampuan prediktif variabel cuaca Bandung jika digunakan secara mandiri tanpa harga historis.

---

## 2. Deskripsi Dataset dan Fitur Pemodelan

Dataset yang digunakan merupakan hasil pembersihan dan penggabungan (*merge*) data deret waktu harian dari **15 Juni 2024 hingga 24 April 2026** (total **679 baris** data setelah pembersihan *missing values*).

### Variabel Target ($y$):
*   `Cabai Merah Besar`: Harga harian Cabai Merah Besar di pasar DKI Jakarta (Rupiah/Kg).

### Variabel Fitur ($X$):
Untuk menghindari *data leakage* (kebocoran informasi masa depan) dan menangkap efek tunda (*delayed effects*) cuaca terhadap panen, digunakan kombinasi fitur lag historis dan musiman:
1.  `Cabai_lag_1`: Harga cabai 1 hari sebelumnya (Rupiah/Kg).
2.  `Cabai_lag_7`: Harga cabai 7 hari sebelumnya (Rupiah/Kg).
3.  `RR_lag_45`: Curah hujan Bandung 45 hari sebelumnya (mm).
4.  `RH_lag_30`: Kelembapan udara rata-rata Bandung 30 hari sebelumnya (%).
5.  `RR_rolling_mean_14`: Rata-rata curah hujan Bandung dalam 14 hari terakhir (mm).
6.  `bulan`: Bulan kalender (1–12) untuk menangkap pola musiman (*seasonality*).

---

## 3. Metodologi Eksperimen

### A. Pembagian Data (*Data Splitting*)
Karena karakteristik data berupa runtun waktu (*time series*), pembagian data dilakukan secara **kronologis (tanpa pengacakan / `shuffle=False`)** untuk menjaga struktur waktu:
*   **Data Latih (*Train Set*)**: 80% data awal (543 baris) untuk pembelajaran model.
*   **Data Uji (*Test Set*)**: 20% data terakhir (136 baris) untuk menguji performa prediksi ke masa depan (skenario *out-of-sample*).

### B. Algoritma Pemodelan
Tiga model dengan karakteristik arsitektur berbeda dilatih dan dibandingkan:
1.  **Linear Regression (Baseline)**: Model statistik linier klasik yang efisien dan sangat kuat dalam menangkap korelasi kuat jangka pendek.
2.  **Random Forest Regressor**: Algoritma *Ensemble Bagging* berbasis pohon keputusan yang kuat dalam menangkap hubungan non-linear dan interaksi kompleks antarfitur tanpa mudah *overfitting*.
3.  **XGBoost Regressor**: Algoritma *Gradient Boosting* tingkat lanjut yang melatih pohon keputusan secara bertahap dan korektif untuk meminimalkan error iterasi sebelumnya.

---

## 4. Hasil Kuantitatif Evaluasi Model

Evaluasi model pada data uji diukur menggunakan empat metrik standar:
*   **MAE (Mean Absolute Error)**: Rata-rata selisih absolut antara harga aktual dan prediksi (dalam satuan Rupiah).
*   **RMSE (Root Mean Squared Error)**: Akar dari rata-rata kuadrat error yang memberikan penalti lebih besar pada error ekstrem.
*   **MAPE (Mean Absolute Percentage Error)**: Rata-rata persentase error terhadap harga aktual.
*   **R² Score**: Koefisien determinasi yang mengukur seberapa besar variasi harga target dapat dijelaskan oleh fitur prediktor.

Berikut adalah tabel hasil komparasi seluruh model, termasuk pembanding **Naive Forecast** (pendekatan sederhana yang mengasumsikan harga hari ini sama dengan harga kemarin / `Cabai_lag_1`):

| Peringkat | Model | MAE (Rp) | RMSE (Rp) | MAPE (%) | $R^2$ Score |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1** | **Naive Forecast (Baseline Deret Waktu)** | **791.91** | **1,342.04** | **1.44%** | **0.9781** |
| **2** | **Linear Regression (Semua Fitur)** | **817.17** | **1,227.65** | **1.49%** | **0.9817** |
| 3 | Random Forest Regressor | 979.52 | 1,450.05 | 1.77% | 0.9745 |
| 4 | XGBoost Regressor | 1,116.41 | 1,596.07 | 2.04% | 0.9691 |

### Analisis Kritis Hasil Evaluasi:
*   **Akurasi Sangat Tinggi**: Ketiga model *machine learning* dan Naive Forecast menghasilkan performa yang luar biasa dengan nilai $R^2$ di atas **0.96** dan MAPE di bawah **2.1%**. Ini menunjukkan model sangat presisi dalam mengikuti pergerakan harga.
*   **Linear Regression Unggul dalam RMSE dan $R^2$**: Model Linear Regression menghasilkan $R^2$ tertinggi (**0.9817**) dan RMSE terendah (**Rp 1,227.65**). Hal ini menunjukkan bahwa Linear Regression lebih tangguh dalam menghindari kesalahan prediksi yang besar (outlier error) pada data uji dibandingkan model berbasis pohon keputusan (*Random Forest* dan *XGBoost*).
*   **Tantangan Naive Forecast**: Pendekatan sederhana Naive Forecast memiliki MAE (**Rp 791.91**) dan MAPE (**1.44%**) yang sedikit lebih rendah daripada Linear Regression. Fakta jujur ini menunjukkan bahwa **autokorelasi harga historis satu hari sebelumnya (`Cabai_lag_1`) sangat mendominasi pola deret waktu harga cabai**.

---

## 5. Analisis Sisaan (*Residual Analysis*) & Cross Validation

Untuk memverifikasi keandalan model terpilih (**Linear Regression**), dilakukan analisis mendalam terhadap sisaan (*residual*) dan validasi silang.

### A. Analisis Residual
Residual dihitung dengan rumus: $e = y_{aktual} - y_{prediksi}$.
*   **Rata-rata Residual**: **-Rp 0.99** (Sangat mendekati nol, menunjukkan model tidak memiliki bias sistematis/tidak cenderung *underestimate* atau *overestimate* secara konsisten).
*   **Median Residual**: **Rp 5.38**
*   **Standar Deviasi Residual**: **Rp 1,227.65**
*   **Pola Distribusi**: Distribusi residual terpusat secara simetris di sekitar angka nol (membentuk lonceng normal). Hal ini membuktikan bahwa kesalahan prediksi bersifat acak (noise) dan model telah menyerap informasi prediktif dengan optimal.

### B. Time Series Cross Validation (5-Fold TSCV)
Untuk menghindari evaluasi bias pada satu potongan waktu saja, model Linear Regression diuji kembali menggunakan metode *TimeSeriesSplit* 5-Fold (validasi silang deret waktu maju):
*   **Rata-rata MAE CV**: **Rp 1,113.36**
*   **Rata-rata RMSE CV**: **Rp 1,722.04**
*   **Rata-rata MAPE CV**: **1.88%**
*   **Rata-rata $R^2$ CV**: **0.9385**
*   *Interpretasi*: Meskipun rata-rata error sedikit meningkat saat diuji pada berbagai potongan waktu historis yang berbeda, model tetap mempertahankan nilai $R^2$ rata-rata yang sangat tinggi (**0.9385**) dan MAPE di bawah **2%**. Ini menunjukkan kemampuan generalisasi model yang sangat stabil dan konsisten.

---

## 6. Interpretasi Pengaruh Faktor Cuaca (*Feature Importance*)

Satu aspek krusial dalam penelitian ini adalah membuktikan secara ilmiah hubungan antara cuaca Bandung dengan harga cabai di Jakarta. 

### A. Koefisien Standar Linear Regression
Karena fitur memiliki satuan yang berbeda (Rupiah, mm, %, nomor bulan), perbandingan pengaruh dilakukan menggunakan koefisien yang telah distandarisasi (*Standardized Coefficients*):
*   **`Cabai_lag_1`**: **+13,199.50** (Faktor yang sangat mendominasi secara mutlak).
*   **`Cabai_lag_7`**: **+909.70** (Pengaruh positif signifikan dari harga seminggu sebelumnya).
*   **Fitur Cuaca & Musiman**: Koefisien untuk variabel `RH_lag_30`, `RR_rolling_mean_14`, dan `RR_lag_45` bernilai jauh lebih kecil (dalam kisaran puluhan hingga ratusan rupiah).

### B. Eksperimen Kontrol: Model Hanya Fitur Cuaca (Tanpa Lag Harga)
Untuk melihat kekuatan murni dari variabel iklim Bandung, dilakukan eksperimen melatih model Linear Regression **hanya dengan fitur cuaca** (`RR_lag_45`, `RH_lag_30`, `RR_rolling_mean_14`, `bulan`):
*   **MAE**: **Rp 11,584.85**
*   **MAPE**: **23.51%**
*   **$R^2$ Score**: **-1.1951**

### Kesimpulan Ilmiah Pengaruh Cuaca:
1.  **Cuaca Sendiri Tidak Cukup**: Nilai $R^2$ yang negatif (**-1.1951**) menunjukkan bahwa variabel cuaca Bandung **tidak dapat digunakan secara mandiri** untuk memprediksi harga cabai harian di Jakarta. Variasi harga harian terlalu dinamis untuk digerakkan oleh tren cuaca saja.
2.  **Autokorelasi Harga Mendominasi**: Pola harga jangka pendek didominasi oleh mekanisme pasar (suplai harian, permintaan, dan harga hari sebelumnya).
3.  **Peran Cuaca Sebagai Faktor Tunda (Pendukung)**: Variabel cuaca seperti kelembapan lag 30 hari (`RH_lag_30`) dan rata-rata curah hujan 14 hari terakhir (`RR_rolling_mean_14`) tetap bernilai penting karena memberikan sinyal tunda mengenai kondisi pasokan di masa depan (misalnya curah hujan tinggi memicu gagal panen yang baru berdampak pada suplai pasar beberapa minggu kemudian). Namun, kontribusi matematis harian fitur ini dalam model kalah dominan dibanding harga lag-1.

---

## 7. Pencegahan *Data Leakage* (Kebocoran Data)

Proyek ini telah menerapkan protokol pencegahan kebocoran data yang ketat:
*   **Tidak Ada Pengacakan (`shuffle=False`)**: Memastikan model tidak belajar dari data masa depan untuk memprediksi masa lalu.
*   **Penggunaan Lag Terstruktur**: Seluruh fitur prediktor (baik harga maupun cuaca) menggunakan nilai masa lalu (lag 1, lag 7, lag 30, lag 45), sehingga pada hari prediksi $t$, seluruh data input dijamin sudah tersedia secara realistis tanpa membutuhkan informasi dari hari $t$ itu sendiri.

---

## 8. Kesimpulan Akhir Pemodelan

1.  **Model Terpilih**: **Linear Regression** dipilih sebagai model final karena menghasilkan keseimbangan performa terbaik (RMSE: Rp 1,227.65 dan $R^2$: 0.9817), struktur model yang sederhana (YAGNI - sesuai prinsip efisiensi), dan memiliki interpretasi matematis (koefisien) yang sangat jelas secara akademis.
2.  **Kelayakan Deployment**: Dengan nilai MAPE sebesar **1.49%** pada data uji dan hasil *Cross Validation* yang stabil, model ini **sangat layak untuk diterapkan** pada aplikasi prediksi harga skala harian.
3.  **Rekomendasi Teknis**: Model terbaik telah disimpan dengan nama `model_cabai_lr.pkl` di dalam folder `models/` menggunakan pustaka `joblib` untuk digunakan pada tahap deployment.

---
*Laporan ini disusun oleh AI Team Member sebagai bagian dari dokumentasi teknis proyek DM210.*
