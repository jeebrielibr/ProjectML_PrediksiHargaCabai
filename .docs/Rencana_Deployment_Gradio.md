# Rencana Deployment Sederhana dengan Gradio: Prediksi Harga Cabai Merah Besar

Rencana ini disusun oleh **AI Team Member (Informatics Engineering Student)** untuk menjembatani tahap pemodelan (*modeling*) dan tahap deployment (*deployment*) dalam metodologi **CRISP-DM**. 

Deployment ini menggunakan **Gradio**, sebuah pustaka open-source Python yang dirancang untuk membangun antarmuka web interaktif (UI) secara cepat, bersih, dan hemat kode (sesuai prinsip *lazy senior dev* dari Ponytail), tanpa memerlukan keahlian frontend web yang mendalam.

---

## 1. Tujuan Deployment
1.  **Aksesibilitas Model**: Memungkinkan pengguna non-teknis (petani, pedagang pasar, atau dinas terkait) melakukan prediksi harga cabai secara real-time melalui antarmuka web.
2.  **Validasi Peer-to-Peer**: Memudahkan sesama anggota tim penelitian atau dosen penguji untuk menguji ketahanan model dengan berbagai skenario data masukan tanpa harus membuka kode Jupyter Notebook.
3.  **Prototyping Cepat**: Menyediakan produk minimum yang layak (*Minimum Viable Product* - MVP) untuk dipresentasikan dalam ujian akhir projek Data Mining.

---

## 2. Struktur Proyek Deployment

Struktur folder proyek diatur secara rapi dan modular untuk memisahkan model, skrip deployment, dan dokumentasi:

```text
ProjectML_PrediksiHargaCabai/
├── models/
│   └── model_cabai_lr.pkl             # File binary model Linear Regression terbaik
├── scripts/
│   └── app_gradio.py                  # Skrip utama aplikasi web Gradio
├── requirements_deploy.txt            # Daftar pustaka Python yang dibutuhkan
└── .docs/
    └── Rencana_Deployment_Gradio.md   # Dokumen rencana deployment (file ini)
```

---

## 3. Variabel Input, Output, dan Komponen Gradio

Untuk menghasilkan prediksi yang valid, aplikasi Gradio harus mengumpulkan **6 variabel input** yang persis sama dengan fitur yang digunakan saat pelatihan model Linear Regression.

### Variabel Input (Prediktor):

| Nama Fitur di Model | Jenis Data | Komponen Gradio | Label UI | Deskripsi & Nilai Default |
| :--- | :---: | :---: | :--- | :--- |
| `Cabai_lag_1` | Float / Int | `gr.Number` | Harga Kemarin (Rp/Kg) | Harga cabai harian di pasar Jakarta 1 hari sebelum prediksi. *Default: 64,600* |
| `Cabai_lag_7` | Float / Int | `gr.Number` | Harga Seminggu Lalu (Rp/Kg) | Harga cabai harian di pasar Jakarta 7 hari sebelum prediksi. *Default: 57,000* |
| `RR_lag_45` | Float | `gr.Number` | Curah Hujan Lag-45 Hari (mm) | Curah hujan harian di Bandung 45 hari lalu. *Default: 0.0* |
| `RH_lag_30` | Float | `gr.Slider` | Kelembapan Lag-30 Hari (%) | Kelembapan rata-rata Bandung 30 hari lalu. Rentang: 0-100. *Default: 78* |
| `RR_rolling_mean_14` | Float | `gr.Number` | Rerata Curah Hujan 14 Hari (mm) | Rata-rata curah hujan Bandung dalam 14 hari terakhir. *Default: 11.36* |
| `bulan` | Integer (1–12) | `gr.Dropdown` | Bulan Prediksi | Bulan dilakukannya prediksi. Di UI direpresentasikan sebagai nama bulan (Jan-Des), lalu dikonversi ke integer. *Default: April* |

### Variabel Output:
*   `harga_prediksi`: String yang menampilkan estimasi harga dalam format Rupiah terformat (misal: `Rp 64,890.85`), ditampilkan dalam komponen `gr.Textbox(label="Hasil Prediksi Harga Cabai (Rupiah/Kg)")`.

---

## 4. Alur Kerja Aplikasi (Workflow)

```text
[ Pengguna menginput data di UI Gradio ]
                    │
                    ▼
[ Skrip app_gradio.py membaca masukan ]
                    │
                    ▼
[ Konversi "Nama Bulan" menjadi "Integer" (1-12) ]
                    │
                    ▼
[ Menyusun input menjadi Pandas DataFrame dengan nama kolom yang sesuai ]
                    │
                    ▼
[ Memuat model_cabai_lr.pkl menggunakan joblib ]
                    │
                    ▼
[ Melakukan prediksi: model.predict(df) ]
                    │
                    ▼
[ Memformat hasil angka menjadi string Rupiah (Rp xxx,xxx.xx) ]
                    │
                    ▼
[ Menampilkan hasil di Textbox Output UI Gradio ]
```

---

## 5. Implementasi Kode Aplikasi (`scripts/app_gradio.py`)

Berikut adalah kode bersih, ringkas, dan aman yang siap dijalankan. Skrip ini dilengkapi dengan penanganan error jika file model tidak ditemukan:

```python
import os
import joblib
import pandas as pd
import numpy as np
import gradio as gr

# 1. Tentukan path model
# Menggunakan path relatif agar fleksibel dijalankan dari mana saja
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'model_cabai_lr.pkl')

# 2. Fungsi memuat model secara aman
def load_prediction_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model pkl tidak ditemukan di path: {MODEL_PATH}. Pastikan Anda telah menjalankan tahap evaluasi dan menyimpan model.")
    return joblib.load(MODEL_PATH)

try:
    model = load_prediction_model()
    model_loaded = True
except Exception as e:
    print(f"Error memuat model: {e}")
    model_loaded = False
    model = None

# 3. Pemetaan Bulan (UI String -> Model Integer)
BULAN_MAP = {
    "Januari": 1, "Februari": 2, "Maret": 3, "April": 4, "Mei": 5, "Juni": 6,
    "Juli": 7, "Agustus": 8, "September": 9, "Oktober": 10, "November": 11, "Desember": 12
}

# 4. Fungsi Prediksi Utama
def prediksi_harga_cabai(cabai_lag_1, cabai_lag_7, rr_lag_45, rh_lag_30, rr_rolling_mean_14, nama_bulan):
    if not model_loaded:
        return "Error: File model_cabai_lr.pkl gagal dimuat. Periksa log konsol."
    
    try:
        # Konversi bulan string ke integer
        bulan_val = BULAN_MAP.get(nama_bulan, 1)
        
        # Susun data baru ke dalam DataFrame dengan susunan kolom yang persis sama dengan X_train
        input_data = pd.DataFrame({
            'Cabai_lag_1': [float(cabai_lag_1)],
            'Cabai_lag_7': [float(cabai_lag_7)],
            'RR_lag_45': [float(rr_lag_45)],
            'RH_lag_30': [float(rh_lag_30)],
            'RR_rolling_mean_14': [float(rr_rolling_mean_14)],
            'bulan': [int(bulan_val)]
        })
        
        # Prediksi menggunakan model terpilih (Linear Regression)
        predicted_value = model.predict(input_data)[0]
        
        # Batasi agar harga tidak bernilai negatif (safety guard)
        predicted_value = max(0.0, predicted_value)
        
        # Format output ke Rupiah
        return f"Rp {predicted_value:,.2f}"
        
    except Exception as err:
        return f"Terjadi kesalahan saat memproses data: {str(err)}"

# 5. Desain Antarmuka Gradio (Theme & Layout)
with gr.Blocks(theme=gr.themes.Soft(), title="Prediksi Harga Cabai DKI Jakarta") as demo:
    gr.Markdown(
        """
        # 🌶️ Aplikasi Prediksi Harga Cabai Merah Besar Jakarta
        **Proyek Akhir Data Mining (DM210) - STT Terpadu Nurul Fikri**
        
        Aplikasi ini memprediksi harga harian Cabai Merah Besar di DKI Jakarta menggunakan model **Linear Regression** terbaik yang telah dilatih menggunakan data historis harga cabai dan data iklim/cuaca BMKG Bandung.
        """
    )
    
    with gr.Row():
        # Kolom Input Kiri (Harga Historis)
        with gr.Column():
            gr.Markdown("### 💵 Parameter Harga Cabai Historis")
            cabai_lag_1 = gr.Number(label="Harga Cabai Kemarin (Rp/Kg)", value=64600)
            cabai_lag_7 = gr.Number(label="Harga Cabai Seminggu Lalu (Rp/Kg)", value=57000)
            nama_bulan = gr.Dropdown(
                label="Bulan Prediksi", 
                choices=list(BULAN_MAP.keys()), 
                value="April"
            )
            
        # Kolom Input Kanan (Variabel Cuaca Bandung)
        with gr.Column():
            gr.Markdown("### 🌦️ Parameter Iklim Bandung")
            rr_lag_45 = gr.Number(label="Curah Hujan Bandung Lag-45 Hari (mm)", value=0.0)
            rh_lag_30 = gr.Slider(label="Kelembapan Bandung Lag-30 Hari (%)", minimum=0, maximum=100, step=1, value=78)
            rr_rolling_mean_14 = gr.Number(label="Rata-rata Curah Hujan Bandung 14 Hari Terakhir (mm)", value=11.36)

    # Output & Tombol Prediksi
    with gr.Row():
        with gr.Column(scale=1):
            btn_predict = gr.Button("🔮 Hitung Estimasi Harga", variant="primary")
        with gr.Column(scale=2):
            output_text = gr.Textbox(
                label="Hasil Prediksi Harga Cabai Merah Besar (Rupiah/Kg)", 
                interactive=False, 
                placeholder="Hasil prediksi akan muncul di sini..."
            )
            
    # Hubungkan tombol dengan fungsi prediksi
    btn_predict.click(
        fn=prediksi_harga_cabai,
        inputs=[cabai_lag_1, cabai_lag_7, rr_lag_45, rh_lag_30, rr_rolling_mean_14, nama_bulan],
        outputs=output_text
    )
    
    gr.Markdown(
        """
        ---
        *Aplikasi dikembangkan oleh AI Team Member sebagai bagian dari rencana deployment final projek data mining.*
        """
    )

# 6. Jalankan Aplikasi
if __name__ == "__main__":
    # Menjalankan aplikasi secara lokal. Atur share=True jika ingin membagikan link publik sementara (berlaku 72 jam).
    demo.launch(server_name="127.0.0.1", server_port=7860, share=False)
```

---

## 6. Panduan Instalasi dan Eksekusi

### A. Penginstalan Dependency
Sebelum menjalankan skrip, instal paket-paket Python yang diperlukan. Buat file `requirements_deploy.txt` yang berisi:

```text
gradio>=4.0.0
scikit-learn
joblib
pandas
numpy
```

Lalu jalankan perintah instalasi di terminal PowerShell / Command Prompt Anda:
```bash
pip install -r requirements_deploy.txt
```

### B. Menjalankan Aplikasi Web
Setelah dependency terinstal, Anda dapat langsung menjalankan skrip Gradio dengan perintah:
```bash
python scripts/app_gradio.py
```

Setelah aplikasi berjalan, buka peramban (*web browser*) Anda dan akses alamat berikut:
*   Lokal: **`http://127.0.0.1:7860`**

### C. Berbagi Aplikasi secara Publik (*Public Sharing*)
Jika Anda ingin membagikan antarmuka ini kepada dosen pembimbing atau rekan tim di luar jaringan lokal, Anda cukup mengubah parameter peluncuran di baris terakhir skrip:
```python
demo.launch(share=True)
```
Gradio secara otomatis akan menghasilkan URL publik sementara (misal: `https://xxxx.gradio.live`) yang aktif selama **72 jam** tanpa memerlukan konfigurasi port-forwarding atau hosting VPS tambahan.

---

## 7. Keunggulan dan Batasan Rencana Deployment Ini

### Keunggulan:
*   **Sangat Cepat**: Antarmuka web fungsional berhasil dibuat dengan kurang dari 100 baris kode Python.
*   **Mudah Dipahami**: Input terstruktur dengan slider dan dropdown memperkecil potensi kesalahan input pengguna (*user error*).
*   **Kolaboratif**: Fitur `share=True` sangat ideal untuk demonstrasi tugas atau presentasi di depan dosen penguji.

### Batasan:
*   **Input Manual**: Pengguna harus memasukkan sendiri data cuaca Bandung dan harga historis. Pada deployment tingkat lanjut (*production*), data cuaca dan harga historis harian harus ditarik secara otomatis menggunakan API BMKG dan PIHPS.
*   **Hosting Sementara**: Link `gradio.live` hanya aktif saat laptop atau komputer lokal yang menjalankan skrip dalam keadaan menyala dan terkoneksi internet. Untuk deployment permanen, disarankan menggunakan platform cloud gratis seperti **Hugging Face Spaces**.

---
*Rencana deployment ini disusun oleh AI Team Member sebagai usulan tindak lanjut dari selesainya tahap pemodelan projek DM210.*
