# Analisis Business Understanding
**Proyek**: Prediksi Harga Cabai Merah Besar Jakarta Berbasis Iklim Bandung  
**Tim**: [DM210]  
**Metodologi**: CRISP-DM (Fase 1)

## 1. Background (Latar Belakang)
Cabai merah besar merupakan komoditas hortikultura strategis yang sering mengalami fluktuasi harga ekstrem di pasar tradisional Jakarta. Ketidakstabilan harga ini berdampak pada inflasi nasional, kesejahteraan petani, dan operasional UMKM. Mengingat Jakarta sangat bergantung pada pasokan luar daerah, kondisi iklim di wilayah pemasok utama seperti Bandung menjadi faktor krusial yang menentukan volume panen dan harga pasar.

## 2. Problem Statement (Pernyataan Masalah)
- Tingginya volatilitas harga cabai merah besar di Jakarta yang sulit diprediksi secara konvensional.
- Kurangnya sistem peringatan dini (*early warning system*) yang mengintegrasikan faktor eksternal seperti data cuaca daerah pemasok.
- Asimetris informasi pasar yang merugikan rantai pasok dari petani hingga konsumen.

## 3. Business Objectives (Tujuan Bisnis)
- Memberikan estimasi harga cabai merah besar yang akurat untuk membantu pengambilan keputusan proaktif bagi pelaku pasar dan pemerintah.
- Memitigasi risiko kerugian akibat lonjakan atau anjloknya harga melalui pendekatan berbasis data (*data-driven approach*).

## 4. Data Mining Goals (Tujuan Data Mining)
- Membangun model prediksi (*regresi*) menggunakan algoritma Machine Learning (seperti XGBoost atau Random Forest) untuk memprediksi harga harian cabai merah besar.
- Menganalisis korelasi dan pengaruh variabel cuaca (curah hujan, suhu, kelembaban) di Bandung terhadap harga di Jakarta.
- Mengidentifikasi pola musiman dan tren historis harga cabai.

## 5. Success Criteria (Kriteria Keberhasilan)
- **Kriteria Teknis**: Model mencapai tingkat kesalahan yang rendah berdasarkan metrik evaluasi regresi:
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)
  - Mean Absolute Percentage Error (MAPE) < 20% (Target awal).
- **Kriteria Bisnis**: Terciptanya *dashboard* prototype (Streamlit) yang dapat digunakan untuk melihat tren dan prediksi harga secara interaktif.

## 6. Project Scope & Constraints (Cakupan & Batasan)
- **Fokus Komoditas**: Terbatas pada Cabai Merah Besar.
- **Wilayah**: Harga di Pasar Tradisional Jakarta dan cuaca di Stasiun Meteorologi Bandung.
- **Data**: Menggunakan data historis (Januari 2021 - April 2026), bukan data *real-time stream*.

---
*Dokumen ini disusun sebagai bagian dari luaran Fase 1 CRISP-DM oleh Tim DM210.*
