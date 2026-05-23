# Prediksi Harga Cabai Merah Besar Jakarta Berbasis Iklim Bandung

[![Project Status: Active](https://img.shields.io/badge/Project%20Status-Active-green.svg)](https://github.com/your-username/ProjectML_PrediksiHargaCabai)
[![Methodology: CRISP-DM](https://img.shields.io/badge/Methodology-CRISP--DM-blue.svg)](#metodologi-penelitian)

Proyek ini bertujuan untuk membangun model prediksi harga Cabai Merah Besar di pasar tradisional wilayah DKI Jakarta dengan mempertimbangkan faktor kondisi iklim/cuaca di wilayah pemasok utama, yaitu Bandung. Proyek ini merupakan bagian dari tugas akhir mata kuliah Data Mining yang berfokus pada tema **Smart Economy & Smart Food Security**.

## 📌 Latar Belakang
Stabilitas harga pangan, khususnya cabai, sangat dipengaruhi oleh keberhasilan panen di daerah pemasok. Dengan memanfaatkan teknik Data Mining dan Machine Learning, kami berupaya memprediksi fluktuasi harga untuk membantu pemangku kepentingan dalam pengambilan keputusan yang lebih proaktif.

## 📊 Dataset
Dataset yang digunakan merupakan integrasi dari dua sumber utama:
1. **Harga Pangan (Variabel Target)**: Data historis harga Cabai Merah Besar dari **Pusat Informasi Harga Pangan Strategis (PIHPS) Nasional** untuk wilayah Jakarta (2021 - 2026).
2. **Iklim/Cuaca (Variabel Prediktor)**: Data meteorologi dari **BMKG** untuk wilayah Bandung (2024 - 2026), meliputi:
   - `TAVG`: Temperatur rata-rata (°C)
   - `RH_AVG`: Kelembapan rata-rata (%)
   - `RR`: Curah hujan (mm)
   - `SS`: Penyinaran matahari (jam)
   - `FF_AVG`: Kecepatan angin rata-rata (m/s)

## 📁 Struktur Proyek
```text
├── .docs/              # Dokumen proposal dan format laporan
├── dataset/            # Dataset mentah dan hasil pembersihan (CSV/MD)
├── model/              # Serialisasi model (pkl/joblib) - [Upcoming]
├── notebook/           # Jupyter Notebooks untuk EDA dan Preprocessing
└── readme.md           # Dokumentasi utama proyek
```

## 🛠️ Tech Stack
- **Bahasa Pemrograman**: Python 3.x
- **Analisis Data**: Pandas, NumPy
- **Visualisasi**: Matplotlib, Seaborn
- **Machine Learning**: Scikit-Learn, XGBoost, LSTM (Planned)
- **Deployment**: Streamlit (Planned)

## 📈 Metodologi Penelitian (CRISP-DM Progress)
| Fase | Status | Deskripsi |
| :--- | :---: | :--- |
| **1. Business Understanding** | ✅ | Identifikasi masalah dan penentuan tujuan penelitian. |
| **2. Data Understanding** | ✅ | Eksplorasi data (EDA) pada harga pangan dan cuaca. |
| **3. Data Preparation** | ✅ | Pembersihan data, sinkronisasi waktu, dan penanganan *missing values*. |
| **4. Modeling** | 🟡 | Pemilihan algoritma dan pelatihan model prediksi. |
| **5. Evaluation** | ⏳ | Validasi model menggunakan metrik MAE, RMSE, dan MAPE. |
| **6. Deployment** | ⏳ | Implementasi model ke dashboard interaktif (Streamlit). |

## 👥 Anggota Tim [DM210]
- **Muhamad Solihin** (0110224098)
- **Muhammad Jibril Ibrahim** (0110224002)
- **Azkia Amanda** (0110224099)
- **Anisa Fitriyani** (0110224145)

---
*Proyek ini dikembangkan untuk program studi Teknik Informatika, STT Terpadu Nurul Fikri (2026).*
