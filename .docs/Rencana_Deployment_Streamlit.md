# Rencana Deployment dengan Streamlit: Prediksi Harga Cabai Merah Besar

Rencana ini disusun oleh **AI Team Member (Informatics Engineering Student)** untuk menjembatani tahap pemodelan (*modeling*) dan tahap deployment (*deployment*) dalam metodologi **CRISP-DM**.

Deployment ini menggunakan **Streamlit**, sebuah pustaka open-source Python yang dirancang untuk membangun aplikasi web data science secara cepat, interaktif, dan dengan kode minimal. Streamlit unggul dalam rendering otomatis, layout berbasis kolom, dan integrasi langsung dengan model machine learning tanpa memerlukan keahlian frontend web.

---

## 1. Tujuan Deployment

1. **Aksesibilitas Model**: Memungkinkan pengguna non-teknis (petani, pedagang pasar, atau dinas terkait) melakukan prediksi harga cabai secara real-time melalui antarmuka web.
2. **Validasi Peer-to-Peer**: Memudahkan sesama anggota tim penelitian atau dosen penguji untuk menguji ketahanan model dengan berbagai skenario data masukan tanpa harus membuka kode Jupyter Notebook.
3. **Prototyping Cepat**: Menyediakan produk minimum yang layak (*Minimum Viable Product* - MVP) untuk dipresentasikan dalam ujian akhir projek Data Mining.
4. **Alternatif Deployment**: Menyediakan opsi deployment selain Gradio, dengan keunggulan layout yang lebih fleksibel dan kemampuan deployment permanen di **Streamlit Community Cloud** secara gratis.

---

## 2. Struktur Proyek Deployment

```text
ProjectML_PrediksiHargaCabai/
├── models/
│   └── model_cabai_lr.pkl             # File binary model Linear Regression terbaik
├── scripts/
│   └── app_streamlit.py               # Skrip utama aplikasi web Streamlit
├── notebook/
│   └── Deployment_Streamlit.ipynb     # Notebook deployment (generate + run script)
└── .docs/
    └── Rencana_Deployment_Streamlit.md # Dokumen rencana deployment (file ini)
```

> **Catatan**: File `scripts/app_streamlit.py` di-generate oleh notebook `Deployment_Streamlit.ipynb` pada cell akhir. Streamlit tidak dapat dijalankan secara *inline* di notebook seperti Gradio — ia membutuhkan file script terpisah yang dijalankan via `streamlit run`.

---

## 3. Variabel Input, Output, dan Komponen Streamlit

Untuk menghasilkan prediksi yang valid, aplikasi Streamlit mengumpulkan **6 variabel input** yang persis sama dengan fitur yang digunakan saat pelatihan model Linear Regression.

### Variabel Input (Prediktor):

| Nama Fitur di Model | Jenis Data | Komponen Streamlit | Label UI | min | max | step | Default |
| :--- | :---: | :---: | :--- | :---: | :---: | :---: | :--- |
| `Cabai_lag_1` | Float / Int | `st.number_input` | Harga Cabai Kemarin (Rp/Kg) | 0 | — | 100 | 64600 |
| `Cabai_lag_7` | Float / Int | `st.number_input` | Harga Cabai Seminggu Lalu (Rp/Kg) | 0 | — | 100 | 57000 |
| `bulan` | Integer (1–12) | `st.selectbox` | Bulan Prediksi | — | — | — | April |
| `RR_lag_45` | Float | `st.number_input` | Curah Hujan Lag-45 Hari (mm) | 0.0 | — | 0.1 | 0.0 |
| `RH_lag_30` | Float | `st.slider` | Kelembapan Lag-30 Hari (%) | 0 | 100 | 1 | 78 |
| `RR_rolling_mean_14` | Float | `st.number_input` | Rerata Curah Hujan 14 Hari (mm) | 0.0 | — | 0.01 | 11.36 |

### Variabel Output:
*   `harga_prediksi`: Ditampilkan dalam komponen `st.success()` box dengan format Rupiah (misal: `Rp 64,890.85`).

---

## 4. Alur Kerja Aplikasi (Workflow)

```text
[ Pengguna menginput data di UI Streamlit ]
                    │
                    ▼
[ Pengguna klik tombol preset (opsional) ]
                    │
                    ▼
[ Preset handler: set st.session_state flag → st.rerun() ]
                    │
                    ▼
[ Flag detected: inject preset values to session_state → pop flag ]
                    │
                    ▼
[ Widget render dengan value dari session_state ]
                    │
                    ▼
[ Pengguna klik "Hitung Estimasi Harga" ]
                    │
                    ▼
[ Konversi "Nama Bulan" menjadi "Integer" (1-12) ]
                    │
                    ▼
[ Susun input menjadi Pandas DataFrame ]
                    │
                    ▼
[ Load model via st.cache_resource → model.predict(df) ]
                    │
                    ▼
[ Format hasil → st.success("Rp xxx,xxx.xx") ]
```

### Pola Manajemen State untuk Tombol Preset

Streamlit bersifat *stateless* — setiap interaksi memicu rerun penuh. Untuk mengisi field input secara otomatis ketika tombol preset diklik, digunakan pola `st.session_state`:

1. Tombol preset diklik → set flag di `st.session_state` (misal: `st.session_state["preset_harga"] = "📉 Harga Rendah"`)
2. `st.rerun()` dipanggil untuk memicu rerun penuh
3. Di awal rerun, script mendeteksi flag → inject nilai preset ke `st.session_state` key per-widget → pop flag
4. Widget render membaca default value dari `st.session_state` → menampilkan nilai preset

Pola ini memastikan bahwa setiap klik preset mengisi seluruh field input yang relevan secara otomatis, mirip dengan perilaku tombol preset pada Gradio.

---

## 5. Preset Skenario

### Preset Iklim Bandung (5 skenario):

| Skenario | RR_lag_45 | RH_lag_30 | RR_rolling_mean_14 | Bulan |
| :--- | :---: | :---: | :---: | :--- |
| ☀️ Kemarau Panas | 0.0 | 65 | 0.0 | September |
| 🌤️ Kemarau Sejuk | 0.0 | 72 | 1.5 | Agustus |
| 🌥️ Musim Transisi | 3.0 | 78 | 5.0 | Oktober |
| 🌧️ Hujan Ringan | 8.0 | 82 | 7.5 | November |
| ⛈️ Hujan Lebat | 35.0 | 88 | 15.0 | Januari |

### Preset Harga Cabai Historis (4 skenario):

| Skenario | Cabai_lag_1 | Cabai_lag_7 | Bulan |
| :--- | :---: | :---: | :--- |
| 📉 Rendah (Q10) | 42500 | 42500 | November |
| 📊 Normal (Median) | 53500 | 53500 | September |
| 📈 Tinggi (Q75) | 65500 | 65550 | Juni |
| 🔥 Sangat Tinggi (Q90) | 71400 | 71400 | Maret |

---

## 6. Implementasi Kode Aplikasi (`scripts/app_streamlit.py`)

Script ini di-generate oleh notebook `Deployment_Streamlit.ipynb` dan berisi seluruh logic secara *standalone*:

1. **`st.set_page_config()`** — Konfigurasi halaman (title, icon 🌶️, layout wide)
2. **`@st.cache_resource`** — Model loading dengan caching otomatis
3. **BULAN_MAP + `prediksi_harga_cabai()`** — Identik dengan versi Gradio
4. **PRESET dictionaries** — Identik dengan versi Gradio
5. **`st.session_state` handling** — Pola preset flag inject/pop
6. **UI Layout** — 2 kolom input, baris preset buttons, output box
7. **Footer** — Divider + credit markdown

---

## 7. Panduan Instalasi dan Eksekusi

### A. Penginstalan Dependency

```text
streamlit>=1.20.0
scikit-learn
joblib
pandas
numpy
```

Instalasi:
```bash
pip install streamlit scikit-learn joblib pandas numpy
```

### B. Menjalankan Aplikasi dari Notebook

Jalankan notebook `Deployment_Streamlit.ipynb` cell per cell. Cell akhir akan:
1. Generate `scripts/app_streamlit.py`
2. Launch Streamlit sebagai background process via `subprocess.Popen`
3. Print URL: `http://localhost:8501`

### C. Menjalankan Aplikasi dari Terminal

```bash
streamlit run scripts/app_streamlit.py
```

Buka browser dan akses: **`http://localhost:8501`**

### D. Berbagi Aplikasi secara Publik (*Public Sharing*)

Streamlit menyediakan **Streamlit Community Cloud** untuk deployment permanen secara gratis:

1. Push repository ke GitHub
2. Login di [share.streamlit.io](https://share.streamlit.io)
3. Deploy langsung dari repo — aplikasi aktif 24/7 tanpa batasan waktu

Ini merupakan keunggulan signifikan dibandingkan Gradio share link yang hanya aktif 72 jam.

---

## 8. Perbandingan Gradio vs Streamlit

| Aspek | Gradio | Streamlit |
| :--- | :--- | :--- |
| Eksekusi di Notebook | Inline (langsung di cell) | Generate script + subprocess.Popen |
| State Management | Component-based (langsung set value) | session_state + rerun pattern |
| Layout | `gr.Blocks`, `gr.Row`, `gr.Column` | `st.columns`, sidebar, tabs |
| Public Sharing | `share=True` (72 jam) | Community Cloud (permanen, gratis) |
| Theme | `gr.themes.Soft()` | `st.set_page_config` + CSS custom |
| Caching | Manual | `@st.cache_resource` (automatic) |
| Hot Reload | Manual restart | Auto-detect file change |

---

## 9. Keunggulan dan Batasan

### Keunggulan:
* **Layout Fleksibel**: Streamlit menyediakan `st.columns`, `st.tabs`, sidebar, dan container yang lebih fleksibel dibandingkan Gradio.
* **Caching Otomatis**: `@st.cache_resource` menghindari reload model setiap rerun.
* **Deployment Permanen**: Community Cloud gratis dan tanpa batasan waktu (vs Gradio 72 jam).
* **Hot Reload**: Edit script → browser auto-refresh tanpa restart manual.

### Batasan:
* **Tidak Inline**: Harus generate script terpisah, tidak bisa dijalankan langsung di notebook cell.
* **Stateless**: Setiap interaksi memicu rerun penuh — preset buttons membutuhkan session_state pattern yang lebih kompleks.
* **Input Manual**: Sama seperti Gradio — pengguna harus memasukkan data cuaca dan harga historis sendiri.
