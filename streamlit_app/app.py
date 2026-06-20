"""
Aplikasi Prediksi Harga Cabai Merah Besar Jakarta - Streamlit Cloud
Proyek Akhir Data Mining (DM210) - STT Terpadu Nurul Fikri
"""

import os
import joblib
import pandas as pd
import numpy as np
import streamlit as st
from pathlib import Path

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Prediksi Harga Cabai DKI Jakarta",
    page_icon="🌶️",
    layout="wide",
)

# --- MODEL LOADING (cached) ---
@st.cache_resource
def load_model():
    # Self-contained deployment: model is in the same directory as app.py
    model_file = Path(__file__).parent / "model_cabai_lr.pkl"
    if model_file.exists():
        return joblib.load(model_file)
    # Fallback for local development
    for p in [Path("../models/model_cabai_lr.pkl"), Path("models/model_cabai_lr.pkl")]:
        if p.exists():
            return joblib.load(p)
    raise FileNotFoundError("model_cabai_lr.pkl tidak ditemukan.")

model = load_model()

# --- BULAN MAP ---
BULAN_MAP = {
    "Januari": 1, "Februari": 2, "Maret": 3, "April": 4, "Mei": 5, "Juni": 6,
    "Juli": 7, "Agustus": 8, "September": 9, "Oktober": 10, "November": 11, "Desember": 12
}

# --- PRESET DATA ---
PRESET_CUACA = {
    "☀️ Kemarau Panas": {
        "rr_lag_45": 0.0, "rh_lag_30": 65, "rr_rolling_mean_14": 0.0, "nama_bulan": "September",
    },
    "🌤️ Kemarau Sejuk": {
        "rr_lag_45": 0.0, "rh_lag_30": 72, "rr_rolling_mean_14": 1.5, "nama_bulan": "Agustus",
    },
    "🌥️ Musim Transisi": {
        "rr_lag_45": 3.0, "rh_lag_30": 78, "rr_rolling_mean_14": 5.0, "nama_bulan": "Oktober",
    },
    "🌧️ Hujan Ringan": {
        "rr_lag_45": 8.0, "rh_lag_30": 82, "rr_rolling_mean_14": 7.5, "nama_bulan": "November",
    },
    "⛈️ Hujan Lebat": {
        "rr_lag_45": 35.0, "rh_lag_30": 88, "rr_rolling_mean_14": 15.0, "nama_bulan": "Januari",
    },
}

PRESET_HARGA = {
    "📉 Harga Rendah": {
        "cabai_lag_1": 42500, "cabai_lag_7": 42500, "nama_bulan": "November",
    },
    "📊 Harga Normal": {
        "cabai_lag_1": 53500, "cabai_lag_7": 53500, "nama_bulan": "September",
    },
    "📈 Harga Tinggi": {
        "cabai_lag_1": 65500, "cabai_lag_7": 65550, "nama_bulan": "Juni",
    },
    "🔥 Harga Sangat Tinggi": {
        "cabai_lag_1": 71400, "cabai_lag_7": 71400, "nama_bulan": "Maret",
    },
}

# --- SESSION STATE: PRESET HANDLING ---
if "preset_harga" in st.session_state:
    preset_key = st.session_state.pop("preset_harga")
    preset = PRESET_HARGA[preset_key]
    st.session_state["cabai_lag_1"] = preset["cabai_lag_1"]
    st.session_state["cabai_lag_7"] = preset["cabai_lag_7"]
    st.session_state["nama_bulan"] = preset["nama_bulan"]

if "preset_cuaca" in st.session_state:
    preset_key = st.session_state.pop("preset_cuaca")
    preset = PRESET_CUACA[preset_key]
    st.session_state["rr_lag_45"] = preset["rr_lag_45"]
    st.session_state["rh_lag_30"] = preset["rh_lag_30"]
    st.session_state["rr_rolling_mean_14"] = preset["rr_rolling_mean_14"]
    st.session_state["nama_bulan"] = preset["nama_bulan"]

# --- PREDICTION FUNCTION ---
def prediksi_harga_cabai(cabai_lag_1, cabai_lag_7, rr_lag_45, rh_lag_30, rr_rolling_mean_14, nama_bulan):
    try:
        bulan_val = BULAN_MAP.get(nama_bulan, 1)
        input_data = pd.DataFrame({
            "Cabai_lag_1": [float(cabai_lag_1)],
            "Cabai_lag_7": [float(cabai_lag_7)],
            "RR_lag_45": [float(rr_lag_45)],
            "RH_lag_30": [float(rh_lag_30)],
            "RR_rolling_mean_14": [float(rr_rolling_mean_14)],
            "bulan": [int(bulan_val)],
        })
        predicted_value = model.predict(input_data)[0]
        predicted_value = max(0.0, predicted_value)
        return f"Rp {predicted_value:,.2f}"
    except Exception as err:
        return f"Terjadi kesalahan saat memproses data: {str(err)}"

# --- UI: HEADER ---
st.title("🌶️ Prediksi Harga Cabai Merah Besar Jakarta")
st.caption("**Proyek Akhir Data Mining (DM210) - STT Terpadu Nurul Fikri**")
st.markdown(
    "Aplikasi ini memprediksi harga harian Cabai Merah Besar di DKI Jakarta "
    "menggunakan model **Linear Regression** terbaik yang telah dilatih "
    "menggunakan data historis harga cabai dan data iklim/cuaca BMKG Bandung."
)

# --- UI: PRESET HARGA ---
st.markdown("### 💰 Preset Skenario Harga Historis")
st.markdown("*Klik salah satu tombol untuk mengisi harga cabai historis dan bulan secara otomatis.*")
harga_cols = st.columns(4)
preset_harga_keys = list(PRESET_HARGA.keys())
for i, key in enumerate(preset_harga_keys):
    if harga_cols[i].button(key, key=f"btn_harga_{i}", use_container_width=True):
        st.session_state["preset_harga"] = key
        st.rerun()

# --- UI: PRESET CUACA ---
st.markdown("### 🌦️ Preset Skenario Iklim Bandung")
st.markdown("*Klik salah satu tombol untuk mengisi variabel cuaca Bandung dan bulan secara otomatis.*")
cuaca_cols = st.columns(5)
preset_cuaca_keys = list(PRESET_CUACA.keys())
for i, key in enumerate(preset_cuaca_keys):
    if cuaca_cols[i].button(key, key=f"btn_cuaca_{i}", use_container_width=True):
        st.session_state["preset_cuaca"] = key
        st.rerun()

# --- UI: INPUT FORM ---
input_cols = st.columns(2)

with input_cols[0]:
    st.markdown("### 💵 Parameter Harga Cabai Historis")
    cabai_lag_1 = st.number_input(
        label="Harga Cabai Kemarin (Rp/Kg)",
        min_value=0, step=100,
        value=st.session_state.get("cabai_lag_1", 64600),
        key="cabai_lag_1",
    )
    cabai_lag_7 = st.number_input(
        label="Harga Cabai Seminggu Lalu (Rp/Kg)",
        min_value=0, step=100,
        value=st.session_state.get("cabai_lag_7", 57000),
        key="cabai_lag_7",
    )
    nama_bulan = st.selectbox(
        label="Bulan Prediksi",
        options=list(BULAN_MAP.keys()),
        index=list(BULAN_MAP.keys()).index(st.session_state.get("nama_bulan", "April")),
        key="nama_bulan",
    )

with input_cols[1]:
    st.markdown("### 🌦️ Parameter Iklim Bandung")
    rr_lag_45 = st.number_input(
        label="Curah Hujan Bandung Lag-45 Hari (mm)",
        min_value=0.0, step=0.1, format="%.1f",
        value=st.session_state.get("rr_lag_45", 0.0),
        key="rr_lag_45",
    )
    rh_lag_30 = st.slider(
        label="Kelembapan Bandung Lag-30 Hari (%)",
        min_value=0, max_value=100, step=1,
        value=int(st.session_state.get("rh_lag_30", 78)),
        key="rh_lag_30",
    )
    rr_rolling_mean_14 = st.number_input(
        label="Rata-rata Curah Hujan Bandung 14 Hari Terakhir (mm)",
        min_value=0.0, step=0.01, format="%.2f",
        value=st.session_state.get("rr_rolling_mean_14", 11.36),
        key="rr_rolling_mean_14",
    )

# --- UI: PREDICT BUTTON ---
st.markdown("---")
if st.button("🔮 Hitung Estimasi Harga", use_container_width=True, type="primary"):
    result = prediksi_harga_cabai(cabai_lag_1, cabai_lag_7, rr_lag_45, rh_lag_30, rr_rolling_mean_14, nama_bulan)
    st.success(result)

# --- FOOTER ---
st.markdown("---")
st.caption("Aplikasi dikembangkan sebagai bagian dari rencana deployment final projek data mining.")
