# Prediksi Harga Cabai Merah Besar Jakarta Berbasis Iklim Bandung

[![Project Status: Completed](https://img.shields.io/badge/Project%20Status-Completed-green.svg)](https://modelprediksicabai.streamlit.app/)
[![Deployment: Streamlit](https://img.shields.io/badge/Deployment-Streamlit-orange.svg)](https://modelprediksicabai.streamlit.app/)
[![Methodology: CRISP-DM](https://img.shields.io/badge/Methodology-CRISP--DM-blue.svg)](#metodologi-penelitian)

Proyek ini bertujuan untuk membangun model prediksi harga Cabai Merah Besar di pasar tradisional wilayah DKI Jakarta dengan mempertimbangkan faktor kondisi iklim/cuaca di wilayah pemasok utama, yaitu Bandung. Proyek ini merupakan bagian dari tugas akhir mata kuliah Data Mining yang berfokus pada tema **Smart Economy & Smart Food Security**.

🌐 **Dashboard Interaktif**: [modelprediksicabai.streamlit.app](https://modelprediksicabai.streamlit.app/)

## 📌 Latar Belakang
Stabilitas harga pangan, khususnya cabai, sangat dipengaruhi oleh keberhasilan panen di daerah pemasok. Dengan memanfaatkan teknik Data Mining dan Machine Learning, kami berupaya memprediksi fluktuasi harga untuk membantu pemangku kepentingan dalam pengambilan keputusan yang lebih proaktif.

## 📊 Dataset
Dataset yang digunakan merupakan integrasi dari dua sumber utama:
1. **Harga Pangan (Variabel Target)**: Data historis harga Cabai Merah Besar dari **Pusat Informasi Harga Pangan Strategis (PIHPS) Nasional** untuk wilayah Jakarta (2021–2026), 1.386 baris.
2. **Iklim/Cuaca (Variabel Prediktor)**: Data meteorologi dari **BMKG** untuk wilayah Bandung (2024–2026), 727 baris, meliputi:
   - `TAVG`: Temperatur rata-rata (°C)
   - `RH_AVG`: Kelembapan rata-rata (%)
   - `RR`: Curah hujan (mm)
   - `SS`: Penyinaran matahari (jam)
   - `FF_AVG`: Kecepatan angin rata-rata (m/s)

## 🏆 Hasil Modelling
Model terbaik yang dipilih adalah **Linear Regression** dengan performa:

| Model | MAE (Rp) | RMSE (Rp) | MAPE (%) | R² |
| :--- | :---: | :---: | :---: | :---: |
| **Linear Regression** ✅ | **817** | **1.228** | **1,49** | **0,9817** |
| Random Forest | 980 | 1.450 | 1,77 | 0,9745 |
| XGBoost | 1.116 | 1.596 | 2,04 | 0,9691 |
| Naive Forecast (baseline) | 792 | 1.342 | 1,44 | 0,9781 |
| Weather-only LR | 11.585 | 13.443 | 23,51 | -1,20 |

**Fitur yang digunakan**: `Cabai_lag_1`, `Cabai_lag_7`, `RR_lag_45`, `RH_lag_30`, `RR_rolling_mean_14`, `Bulan`

**Temuan kunci**: Kelembapan Bandung (`RH_AVG`) berkorelasi paling kuat dengan harga cabai Jakarta pada lag 30 hari (+0,24), dan curah hujan (`RR`) pada lag 45 hari (+0,10) — mengkonfirmasi bahwa cuaca Bandung memengaruhi harga cabai Jakarta 1–1,5 bulan kemudian.

## 📁 Struktur Proyek
```text
├── .docs/                # Dokumen proposal, analisis, dan laporan CRISP-DM
├── dataset/              # Dataset mentah dan hasil pembersihan (CSV)
│   ├── PIHPS_Jakarta_Full_2021_2026.csv          # Data harga mentah
│   ├── Gabungan_Laporan_Iklim_Harian_Bandung_Mei_2024_April_2026.csv  # Data cuaca mentah
│   ├── PIHPS_Jakarta_Cleaned_2021_2026.csv       # Data harga bersih
│   ├── dataset_cuaca_bandung_cleaned.csv          # Data cuaca bersih
│   ├── dataset_cabe_mb_cleaned.csv               # Data harga cabai saja
│   ├── dataset_merged.csv                         # Data merged (cuaca + harga)
│   ├── dataset_merge_cleaning.csv                 # Data merged + cleaning
│   └── dataset_featured.csv                       # Data fitur final
├── img/                  # Visualisasi hasil EDA
├── models/               # Serialisasi model (pkl)
│   ├── model_cabai_lr.pkl     # Model terbaik (Linear Regression)
│   ├── model_rf.pkl           # Random Forest
│   ├── model_ridge.pkl        # Ridge Regression
│   ├── model_lasso.pkl        # Lasso Regression
│   ├── model_nn.pkl           # Neural Network
│   ├── model_linear.pkl       # Linear Regression (varian awal)
│   └── model_harga.pkl        # Model harga (iterasi awal)
├── notebook/             # Jupyter Notebooks (pipeline CRISP-DM)
│   ├── Data Understanding - Dataset Cuaca Bandung.ipynb
│   ├── Data Understanding - Dataset Harga Bahan Pokok.ipynb
│   ├── Data Cleaning - Cuaca Bandung.ipynb
│   ├── Data Cleaning - Harga Bahan Pokok.ipynb
│   ├── Data Merge - Cuaca dan Harga.ipynb
│   ├── DataCleaning-DatasetMerge.ipynb
│   ├── EDA-DatasetMerge.ipynb
│   ├── Features Engineering.ipynb
│   ├── Modelling_dengan_Evaluasi_FINAL_revisi_output.ipynb
│   ├── Deployment_Streamlit.ipynb
│   ├── Deployment_Gradio.ipynb
│   └── archive/                                  # Notebook eksperimen awal
│       ├── AutoML_pyCaretFeatured.ipynb
│       ├── AutoML_pyCaretRaw.ipynb
│       ├── Model Classic ARIMA.ipynb
│       ├── Model Regression.ipynb
│       └── Modelling.ipynb
├── streamlit_app/        # Package deployment Streamlit Cloud
│   ├── app.py                  # Aplikasi Streamlit
│   ├── model_cabai_lr.pkl      # Model untuk deployment
│   └── requirements.txt        # Dependencies
└── readme.md             # Dokumentasi utama proyek
```

## 🛠️ Tech Stack
- **Bahasa Pemrograman**: Python 3.x
- **Analisis Data**: Pandas, NumPy
- **Visualisasi**: Matplotlib, Seaborn
- **Machine Learning**: Scikit-Learn (Linear Regression, Random Forest), XGBoost
- **Deployment**: Streamlit Community Cloud

## 📈 Metodologi Penelitian (CRISP-DM)
| Fase | Status | Deskripsi |
| :--- | :---: | :--- |
| **1. Business Understanding** | ✅ | Identifikasi masalah dan penentuan tujuan penelitian. |
| **2. Data Understanding** | ✅ | Eksplorasi data (EDA) pada harga pangan dan cuaca. |
| **3. Data Preparation** | ✅ | Pembersihan data, merge dataset, feature engineering (lag & rolling). |
| **4. Modeling** | ✅ | Pelatihan 3 model ML (LR, RF, XGBoost) + baseline Naive Forecast. |
| **5. Evaluation** | ✅ | Validasi model menggunakan MAE, RMSE, MAPE, dan R²; cross-validation TimeSeriesSplit. |
| **6. Deployment** | ✅ | Dashboard interaktif di [Streamlit Community Cloud](https://modelprediksicabai.streamlit.app/). |

## 👥 Anggota Tim [DM210]
- **Muhamad Solihin** (0110224098)
- **Muhammad Jibril Ibrahim** (0110224002)
- **Azkia Amanda** (0110224099)
- **Anisa Fitriyani** (0110224145)

---
*Proyek ini dikembangkan sebagai tugas akhir untuk Matkul Data Mining, STT Terpadu Nurul Fikri (2026).*
