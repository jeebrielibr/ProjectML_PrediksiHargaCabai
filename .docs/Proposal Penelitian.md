**PROPOSAL**  
**PROJECT DATA MINING**

**Tim**: \[DM210\]  
**Tema**: Smart City \-\> Smart Economy & Smart Food Security

| NIM | NAMA |
| :---: | :---: |
| 0110224098 | Muhamad Solihin |
| 0110224002 | Muhammad Jibril Ibrahim |
| 0110224099 | Azkia Amanda |
| 0110224145 | Anisa Fitriyani |

**Judul Proposal:**  
**Pembuatan Model Prediksi Harga Cabai Merah Besar di pasar Tradisional Jakarta berdasarkan Pengaruh Iklim Cuaca di Daerah Pemasok Bandung**

**PROGRAM STUDI TEKNIK INFORMATIKA**  
**SEKOLAH TINGGI TEKNOLOGI TERPADU NURUL FIKRI**  
**DEPOK**  
**2026**

# **DAFTAR ISI** {#daftar-isi}

[DAFTAR ISI	2](#daftar-isi)

[BAGIAN 1	1](#bagian-1)

[1.1	Problem Statement	1](#problem-statement)

[1.2	Perumusan Masalah	2](#perumusan-masalah)

[1.3	Latar Belakang	2](#latar-belakang)

[1.4	Alasan Pemilihan Proyek	4](#alasan-pemilihan-proyek)

[BAGIAN 2 CAKUPAN PROYEK DAN HASIL KERJA	6](#bagian-2-cakupan-proyek-dan-hasil-kerja)

[2.1 Cakupan Proyek	6](#2.1-cakupan-proyek)

[2.2 Kunci Batasan	7](#2.2-kunci-batasan)

[BAGIAN 3	8](#bagian-3)

[3.1 Fase 1 — Business Understanding, Data Understanding & Exploratory Data Analysis	8](#3.1-fase-1-—-business-understanding,-data-understanding-&-exploratory-data-analysis)

[3.2 Fase 2 — Data Cleaning	9](#3.2-fase-2-—-data-cleaning)

[3.3 Fase 3 — Modelling	10](#3.3-fase-3-—-modelling)

[3.4 Fase 4 — Evaluasi / Pengujian	11](#3.4-fase-4-—-evaluasi-/-pengujian)

[3.5 Fase 5 — Deployment	13](#3.5-fase-5-—-deployment)

[3.6 Fase 6 — Finalisasi Dokumen	14](#3.6-fase-6-—-finalisasi-dokumen)

[BAGIAN 4	15](#bagian-4)

[4.1 Bahasa Pemrograman	15](#4.1-bahasa-pemrograman)

[4.2 Framework dan Library	15](#4.2-framework-dan-library)

[4.3 Tools dan Platform Pengembangan	16](#4.3-tools-dan-platform-pengembangan)

[4.4 Dataset	17](#4.4-dataset)

[4.5 Paper / Jurnal / Artikel Referensi	18](#4.5-paper-/-jurnal-/-artikel-referensi)

[DAFTAR PUSTAKA	20](#daftar-pustaka)

# **BAGIAN 1** {#bagian-1}

**RINGKASAN EKSEKUTIF**

1. ## **Problem Statement**  {#problem-statement}

Stabilitas harga komoditas pangan merupakan salah satu aspek penting dalam menjaga ketahanan ekonomi masyarakat. Salah satu komoditas yang sering mengalami fluktuasi harga adalah cabai merah besar. Cabai merah besar termasuk ke dalam komoditas hortikultura strategis di Indonesia, komoditas ini memiliki nilai ekonomi yang tinggi dan permintaan yang konstan. Namun, komoditas ini sangat rentan terhadap fluktuasi harga yang ekstrem. Volatilitas ini berdampak sistemis yang bisa memicu inflasi nasional, merugikan petani yang mengalami penurunan harga anjlok saat panen raya, hingga mengancam keberlangsungan operasional UMKM yang bergantung pada stabilitas biaya bahan baku. Bagi beberapa sektor seperti sektor industri dan UMKM, ke tidak pastian harga ini merusak struktur manajemen biaya dan bertentangan dengan prinsip perbaikan berkelanjutan.  
Penyebab utama fenomena fluktuasi ini sangat kompleks, meliputi kendala hulu ke hilir. Di sisi produksi, ada beberapa faktor yang menentukan berapa banyak volume panen yang akan dihasilkan, bisa karna cuaca ekstrem, fluktuasi curah hujan, kekeringan lahan garapan, serangan hama, serta biaya input pertanian seperti pupuk, pestisida dan lainnya. Sebagai bukti empiris, sebuah jurnal menyebutkan bahwa harga cabai di Indonesia mengalami fluktuasi harga setiap tahunnya. Pada tahun 2018 hasil produksi cabai merah mencapai Rp6.279.896 dengan volume hasil panen 2.542.333 ton, namun mengalami penurunan pada 2019 menjadi Rp5.244.018 dengan hasil produksi yang justru naik dari tahun sebelumnya yaitu sebanyak 2.588.633 ton. Tahun berikutnya 2020, pendapatan petani kembali menurun menjadi Rp3.120.489 dengan jumlah hasil produksi yang kembali meningkat sebanyak 2.772.594 ton \[1\].Di sisi distribusi, panjangnya rantai pasok pemasaran menyebabkan disparitas harga yang jauh antara tingkat petani dan konsumen. Masalah ini menjadi serius dengan adanya asimetris informasi dan keterlambatan penyajian data pasar, sehingga pemerintah maupun pelaku pasar kehilangan momentum untuk mengambil keputusan yang proaktif.  
Dalam kondisi tersebut, pendekatan konvensional yang bersifat reaktif dinilai kurang efektif. Oleh karena itu, diperlukan suatu pendekatan berbasis data yang mampu memprediksi harga cabai secara lebih akurat. Pemanfaatan teknologi machine learning dan data mining memungkinkan pembangunan model prediktif berdasarkan data historis harga dan faktor eksternal seperti kondisi cuaca.  
Melalui pengembangan model prediksi harga cabai merah besar berbasis machine learning, diharapkan dapat dihasilkan sistem yang mampu memberikan estimasi harga dengan tingkat kesalahan yang rendah. Hasil prediksi ini dapat dimanfaatkan oleh berbagai pihak, seperti petani dalam menentukan strategi panen, pelaku usaha dalam perencanaan biaya, serta pemerintah dalam merumuskan kebijakan stabilisasi harga yang lebih tepat dan berbasis data.

2. ## **Perumusan Masalah** {#perumusan-masalah}

Berdasarkan permasalahan yang ditemukan, berikut adalah perumusan masalah dalam penelitian ini.

1. Bagaimana pola fluktuasi harga cabai merah besar di pasar tradisional wilayah Jakarta berdasarkan data historis yang tersedia?  
2. Bagaimana karakteristik variabel cuaca di daerah pemasok (Bandung), seperti curah hujan, suhu, dan kelembaban, dalam periode waktu yang sama?  
3. Apakah terdapat hubungan yang signifikan antara variabel curah hujan di daerah pemasok dengan perubahan harga cabai merah besar di daerah Jakarta?  
4. Bagaimana membangun model prediksi harga cabai merah besar berbasis machine learning dengan memanfaatkan variabel cuaca sebagai faktor independen?  
5. Seberapa baik performa model prediksi yang dihasilkan berdasarkan metrik evaluasi seperti MAE, RMSE, dan MAPE?

   3. ## **Latar Belakang** {#latar-belakang}

Cabai merah besar merupakan salah satu komoditas hortikultura strategis di Indonesia yang memiliki peran penting dalam menjaga stabilitas ekonomi pangan nasional. Tingginya tingkat konsumsi masyarakat terhadap cabai menjadikan komoditas ini memiliki permintaan yang relatif stabil sepanjang tahun. Namun demikian, harga cabai merah besar di pasar tradisional, khususnya di wilayah DKI Jakarta, sering mengalami fluktuasi yang cukup tinggi dan sulit diprediksi. Kondisi ini berdampak langsung terhadap konsumen, pedagang, hingga petani karena perubahan harga yang tidak stabil dapat mengganggu keseimbangan rantai pasok pangan. Fluktuasi harga cabai merah besar dipengaruhi oleh berbagai faktor, salah satunya adalah kondisi iklim dan cuaca di daerah pemasok utama seperti Bandung. Perubahan curah hujan, suhu udara, serta kondisi cuaca ekstrem dapat memengaruhi hasil panen cabai, baik dari segi kuantitas maupun kualitas. Ketika produksi menurun akibat kondisi cuaca yang tidak stabil, maka pasokan ke wilayah DKI Jakarta juga ikut berkurang sehingga menyebabkan kenaikan harga di pasar tradisional.  
Selain faktor cuaca, distribusi dan ketergantungan pasokan juga menjadi faktor penting dalam pembentukan harga. Wilayah DKI Jakarta sebagai pusat konsumsi tidak memiliki produksi cabai yang cukup sehingga sangat bergantung pada daerah pemasok seperti Bandung dan sekitarnya. Gangguan dalam proses distribusi, jarak pengiriman, serta biaya logistik turut memperkuat ketidakstabilan harga di pasar. Hal ini menunjukkan bahwa harga cabai tidak hanya dipengaruhi oleh permintaan dan penawaran, tetapi juga oleh faktor eksternal yang saling berkaitan.  
Dalam beberapa tahun terakhir, perkembangan teknologi digital dan kecerdasan buatan telah memberikan dampak besar dalam berbagai sektor, termasuk sektor pertanian dan ekonomi pangan. Pemanfaatan data dalam jumlah besar mulai digunakan untuk membantu memahami pola perubahan harga komoditas yang bersifat fluktuatif. Hal ini membuka peluang untuk melakukan analisis yang lebih sistematis dalam memprediksi harga berdasarkan data historis dan faktor eksternal yang memengaruhinya.  
Selain itu, industri pertanian modern saat ini mulai mengarah pada konsep pemanfaatan data dalam pengambilan keputusan. Pendekatan berbasis data tersebut memungkinkan pelaku pasar untuk memahami pola perubahan harga dan melakukan perencanaan yang lebih baik dalam distribusi maupun pengelolaan stok. Di sisi lain, kondisi sosial ekonomi masyarakat juga sangat dipengaruhi oleh perubahan harga cabai, karena komoditas ini termasuk kebutuhan pokok yang berdampak pada inflasi pangan nasional.  
Berdasarkan data produksi nasional, Provinsi Jawa Barat merupakan salah satu daerah penghasil cabai terbesar di Indonesia. Tingginya kontribusi produksi dari wilayah ini menjadikan Bandung sebagai salah satu daerah pemasok utama cabai ke DKI Jakarta. Oleh karena itu, perubahan kondisi cuaca di Bandung memiliki potensi besar dalam memengaruhi harga cabai di pasar tradisional Jakarta \[2\].   
Beberapa penelitian sebelumnya menunjukkan bahwa pendekatan berbasis data dapat digunakan untuk memahami pola perubahan harga komoditas pertanian. Namun, sebagian besar penelitian masih berfokus pada data harga historis tanpa mempertimbangkan faktor eksternal secara spesifik seperti kondisi cuaca di daerah pemasok utama \[3\].  
Berdasarkan hal tersebut, diperlukan suatu pendekatan analisis yang mampu menghubungkan faktor harga di pasar Jakarta dengan kondisi cuaca di daerah pemasok seperti Bandung. Penelitian ini menjadi penting untuk memberikan gambaran yang lebih komprehensif mengenai faktor-faktor yang memengaruhi perubahan harga cabai di pasar tradisional.  
Dengan demikian, penelitian ini diharapkan dapat memberikan kontribusi dalam pengembangan analisis data di sektor pertanian serta membantu dalam memahami pola fluktuasi harga cabai secara lebih akurat dan terstruktur.

4. ## **Alasan Pemilihan Proyek** {#alasan-pemilihan-proyek}

1. **Kompentensi yang ingin di kembangkan**

Pemilihan proyek prediksi harga cabai merah dilakukan karena komoditas ini memiliki tingkat perubahan harga yang cukup tinggi dan sering menjadi perhatian masyarakat. Harga cabai dapat berubah dalam waktu singkat akibat berbagai faktor seperti kondisi cuaca, musim panen, distribusi barang, permintaan pasar, hingga inflasi. Perubahan harga yang tidak stabil sering menimbulkan dampak terhadap pedagang, petani, pelaku usaha kuliner, maupun konsumen. Oleh karena itu, diperlukan suatu sistem yang mampu membantu memperkirakan harga cabai pada periode mendatang agar pihak terkait dapat mengambil keputusan yang lebih tepat. Proyek ini dipilih karena prediksi harga cabai memiliki manfaat nyata dalam kehidupan sehari-hari. Dengan adanya prediksi harga, pedagang dapat memperkirakan kapan waktu terbaik untuk membeli stok dalam jumlah besar, petani dapat menentukan strategi penjualan hasil panen, dan konsumen dapat memahami tren kenaikan maupun penurunan harga. Selain itu, pemerintah juga dapat memanfaatkan hasil prediksi sebagai bahan evaluasi dalam menjaga stabilitas harga pangan.

2. **Relevansi dengan learning path masing-masing anggota**

Proyek ini relevan dengan learning path masing-masing anggota tim yang berfokus pada bidang data science, machine learning, dan data analysis. Melalui proyek ini, anggota tim dapat menerapkan berbagai kompetensi yang telah dipelajari, seperti pengolahan data, data preprocessing, eksplorasi data (EDA), serta penerapan algoritma machine learning untuk kasus prediksi berbasis data historis. Selain itu, proyek ini juga mendukung pengembangan kemampuan dalam penggunaan Python, library machine learning seperti scikit-learn, serta pemahaman proses end-to-end machine learning yang mencakup pengumpulan data, pembersihan data, pemodelan, hingga evaluasi model menggunakan metrik seperti accuracy, precision, recall, dan f1-score. Dengan demikian, proyek ini membantu anggota tim dalam menghubungkan teori yang telah dipelajari dengan implementasi pada kasus nyata.  
Selain itu, penelitian dalam jurnal Model Prediksi Harga Cabai Merah Besar di Tingkat Pasar Tradisional Tahun 2017–2024: Pendekatan Supervised Learning Berbasis Orange Data Mining menjelaskan bahwa prediksi harga dapat berfungsi sebagai sistem peringatan dini untuk mengantisipasi lonjakan harga pangan. Dengan model prediksi, perubahan harga dapat dipantau lebih awal sehingga langkah pengendalian dapat dilakukan sebelum terjadi kenaikan harga yang signifikan \[2\].

3. **Nilai tambah yang bisa diberikan proyek ini**

Pemilihan proyek prediksi harga cabai merah dilakukan karena komoditas ini memiliki tingkat perubahan harga yang cukup tinggi dan sering menjadi perhatian masyarakat. Harga cabai dapat berubah dalam waktu singkat akibat berbagai faktor seperti kondisi cuaca, musim panen, distribusi barang, permintaan pasar, hingga inflasi. Perubahan harga yang tidak stabil sering menimbulkan dampak terhadap pedagang, petani, pelaku usaha kuliner, maupun konsumen. Oleh karena itu, diperlukan suatu sistem yang mampu membantu memperkirakan harga cabai pada periode mendatang agar pihak terkait dapat mengambil keputusan yang lebih tepat.  
Proyek ini dipilih karena prediksi harga cabai memiliki manfaat nyata dalam kehidupan sehari-hari. Dengan adanya prediksi harga, pedagang dapat memperkirakan kapan waktu terbaik untuk membeli stok dalam jumlah besar, petani dapat menentukan strategi penjualan hasil panen, dan konsumen dapat memahami tren kenaikan maupun penurunan harga. Selain itu, pemerintah juga dapat memanfaatkan hasil prediksi sebagai bahan evaluasi dalam menjaga stabilitas harga pangan.  
Dengan demikian, proyek prediksi harga cabai dipilih karena memiliki nilai manfaat yang tinggi, relevan dengan kondisi nyata, dapat membantu proses pengambilan keputusan, serta mendukung pemanfaatan teknologi data mining dan machine learning dalam menyelesaikan permasalahan ekonomi dan pangan.

# **BAGIAN 2** **CAKUPAN PROYEK DAN HASIL KERJA** {#bagian-2-cakupan-proyek-dan-hasil-kerja}

## **2.1 Cakupan Proyek** {#2.1-cakupan-proyek}

Proyek ini akan difokuskan pada pengembangan model prediktif berbasis *Machine Learning* untuk memprediksi harga cabai merah besar serta implementasinya dalam bentuk *dashboard* sederhana yang interaktif. Ruang lingkup pengerjaan proyek ini meliputi:

1. Pengumpulan dan Preprocessing Data, Mengumpulkan dataset historis harga cabai merah besar di pasar tradisional DKI Jakarta dan data historis curah hujan di daerah pemasok utama yaitu Bandung. Data yang dikumpulkan diharapkan dapat terkumpul setidaknya 700 lebih baris data. Pada tahap prepocessing data akan dilakukan :  
   * Data cleaning  
   * Penanganan nilai kosong (missing value),  
   * Sinkronisasi dan penggabungan data berdasarkan waktu  
   * Transformasi data menggunakan library seperti Pandas dan NumPy  
2. Exploratory Data Analysis (EDA), Melakukan eksplorasi data untuk memahami karakteristik dataset, seperti:   
* Analisis tren harga cabai  
* Pola musiman  
* Analisis hubungan antara variabel cuaca dan harga  
* Visualisasi data menggunakan grafik (line chart, histogram, heatmap)  
3. Pemodelan Prediktif, Membangun dan melatih model prediksi harga cabai menggunakan algoritma Machine Learning Time Series, seperti Random Forest Regressor (baseline), Gradient Boosting Regressor, XGBoost Regressor (model utama).  
4. Evaluasi dan Analisis Model, Melakukan evaluasi performa model serta analisis hasil prediksi, termasuk Perbandingan nilai prediksi dan aktual, Analisis error (residual), Identifikasi faktor yang paling berpengaruh terhadap harga cabai.  
5. Deployment dan Implementasi Sistem, Mengimplementasikan model ke dalam bentuk aplikasi sederhana berbasis web menggunakan tools seperti Streamlit.  
   

## **2.2 Kunci Batasan** {#2.2-kunci-batasan}

Proyek ini memiliki beberapa batasan untuk menjaga fokus dan kesesuaian dengan ruang lingkup yang telah ditentukan, yaitu:

1. Sistem hanya digunakan untuk memprediksi harga cabai merah besar, dan tidak mencakup komoditas lain.  
2. Data yang digunakan bersifat historis dan tidak mengambil data secara real-time.  
3. Variabel yang digunakan terbatas pada data harga dan faktor cuaca, tanpa mempertimbangkan faktor lain seperti distribusi, kebijakan pemerintah, atau kondisi pasar secara langsung.  
4. Proyek tidak mencakup integrasi dengan database online, API eksternal secara real-time, maupun sistem pasar secara langsung.  
5. Dashboard yang dikembangkan bersifat sederhana (prototype) dan hanya digunakan untuk demonstrasi, bukan aplikasi komersial.  
6. Sistem tidak mencakup fitur lanjutan seperti login pengguna, manajemen akun, transaksi, atau sistem distribusi.  
7. Deployment dilakukan sebatas simulasi/prototype, bukan implementasi pada lingkungan production yang kompleks.  
8. Model yang digunakan terbatas pada beberapa algoritma yang telah ditentukan dan tidak mencakup seluruh metode machine learning yang ada.

# 

# **BAGIAN 3** {#bagian-3}

**URAIAN RENCANA PENUGASAN**

## **3.1 Fase 1 — Business Understanding, Data Understanding & Exploratory Data Analysis** {#3.1-fase-1-—-business-understanding,-data-understanding-&-exploratory-data-analysis}

Fase awal: pahami masalah bisnis secara mendalam, identifikasi sumber data yang tersedia, dan lakukan eksplorasi awal untuk memahami karakteristik data sebelum masuk ke preprocessing

| Fase 1 — Business Understanding, Data Understanding & EDA |  |
| ----- | :---- |
| **Durasi** | Week 1 |
| **PIC** | Azkia Amanda |
| **Tugas & Aktivitas** | Tugas 1: Mendefinisikan tujuan bisnis dan problem yang ingin diselesaikan dengan data mining. Tugas 2: Mengidentifikasi dan mengumpulkan data dari sumber data yang relevan seperti website BMKG untuk data historis curah hujan, dan website Pusat Informasi Harga Pangan Strategis Nasional (PIHPS) Bank Indonesia untuk data historis harga cabai di Jakarta. Tugas 3: Melakukan Exploratory Data Analysis (EDA) seperti melihat tren harga, pola musiman curah hujan, dan uji korelasi awal antara harga cabai dengan cuaca. Tugas 4: Menyusun hipotesis awal berdasarkan hasil EDA |
| **Deliverables** | Deliverable 1: Dokumen Business Understanding (tujuan proyek, success criteria) Deliverable 2: Laporan EDA lengkap dengan visualisasi (histogram, heatmap korelasi, dsb.) Deliverable 3: Upload daftar dataset mentah yang telah terkumpul ke dalam Google Drive. Deliverable 4: Daftar hipotesis awal dan insight yang diperoleh dari analisis data |
| **Milestone** | Tim memahami permasalahan bisnis dan tujuan analisis secara menyeluruh, serta memperoleh insight awal mengenai pola harga cabai dan hubungan dengan faktor cuaca, sehingga siap untuk masuk ke tahap data cleaning dan preprocessing. |

## **3.2 Fase 2 — Data Cleaning** {#3.2-fase-2-—-data-cleaning}

Fase pembersihan data: tangani semua masalah kualitas data yang ditemukan di fase EDA. Data yang bersih adalah syarat utama model yang akurat.

| Fase 2 — Data Cleaning |  |
| ----- | :---- |
| **Durasi** | Week 2 – Week 3 |
| **PIC** | Muhamad Solihin |
| **Tugas & Aktivitas** | Tugas 1: Menangani missing values dengan melakukan identifikasi pada data harga cabai dan data cuaca dengan metode imputasi, penghapusan, atau pemberian penanganan sesuai karakteristik data time series. Tugas 2: Melakukan sinkronisasi dan integrasi data hargai cabai dengan cuaca berdasarkan tanggal, serta penggabungan menjadi satu data yang konsisten Tugas 3 : Mendeteksi dan menangani outlier dengan menentukan strategi penanganan yang terbaik seperti menghapus atau mempertahan jika outlier itu memiliki alasan logis. Tugas 4 : Melakukan standarisasi atau normalisasi pada fitur numerik jika diperlukan, terutama untuk meningkatkan performa model machine learning Tugas 5 : Mengubah fitur kategorial seperti bulan atau musim menjadi format numerik menggunakan teknik encoding (One-Hot Encoding atau Label Encoding). Tugas 7: Melakukan feature selection dengan emilih fitur yang relevan berdasarkan analisis korelasi atau importance untuk meningkatkan performa model. (Jika diperlukan) |
| **Deliverables** | Deliverable 1: Dataset hasil integrasi (harga cabai \+ data cuaca) yang telah dibersihkan Deliverable 2: Dataset final yang telah melalui proses feature engineering dan siap digunakan untuk modeling Deliverable 3: Dokumentasi lengkap setiap tahap data cleaning dan preprocessing beserta alasan pemilihan metode Deliverable 4: Script atau notebook preprocessing yang dapat direproduksi (reproducible) |
| **Milestone** | Dataset terintegrasi, bersih, telah melalui proses feature engineering, serta siap digunakan pada tahap pemodelan dan evaluasi model prediksi. |

## **3.3 Fase 3 — Modelling** {#3.3-fase-3-—-modelling}

Fase pemodelan: bangun dan latih model machine learning sesuai pendekatan yang dipilih. Mulai dari model sederhana (baseline) lalu kembangkan ke model yang lebih kompleks.

| Fase 3 — Modelling |  |
| ----- | :---- |
| **Durasi** | Week 3 – Week 5 |
| **PIC** | Anisa Fitriyani |
| **Tugas & Aktivitas** | Tugas 1: Memilih algoritma/pendekatan yang sesuai dengan tipe masalah prediksi hargai cabai merah besar. Tugas 2: Membagi dataset menjadi train, validation, dan test set berdasarkan urutan waktu (bukan random split) untuk menjaga validitas prediksi time series. Tugas 3: Membangun dan melatih model baseline menggunakan algoritma sederhana (misalnya Random Forest) sebagai pembanding performa model lanjutan. Tugas 4: Melakukan hyperparameter tuning dengan melakukan optimasi parameter model menggunakan metode seperti Grid Search atau Random Search untuk meningkatkan performa model. Tugas 5: Eksperimen dengan beberapa algoritma seperti Random Forest, Gradient Boosting, XGBoost dan membandingkan performanya menggunakan metrik evaluasi regresi. Tugas 6: Melakukan evaluasi model evaluasi model menggunakan metrik: MAE (Mean Absolute Error) RMSE (Root Mean Squared Error) MAPE (Mean Absolute Percentage Error) Serta visualisasi hasil prediksi vs data aktual menggunakan grafik time series Tugas 7 : Menganalisis hasil prediksi serta mengidentifikasi fitur yang paling berpengaruh (feature importance), khususnya variabel cuaca terhadap harga cabai. Tugas 8: Membuat kesimpulan dengan menentukan model terbaik berdasarkan hasil evaluasi dan kesesuaian dengan tujuan penelitian. |
| **Deliverables** | Deliverable 1: Model baseline yang telah dilatih dan dievaluasi Deliverable 2: Model final hasil tuning dengan performa terbaik Deliverable 3: Hasil evaluasi model (MAE, RMSE, MAPE) beserta visualisasi perbandingan prediksi dan data aktual Deliverable 4: Notebook eksperimen yang terdokumentasi dan dapat direproduksi  |
| **Milestone** | Model terbaik telah teridentifikasi berdasarkan hasil evaluasi metrik regresi dan mampu memberikan prediksi harga cabai dengan tingkat error yang memenuhi success criteria yang telah ditetapkan. |

## **3.4 Fase 4 — Evaluasi / Pengujian** {#3.4-fase-4-—-evaluasi-/-pengujian}

Fase evaluasi: uji model secara menyeluruh menggunakan data yang belum pernah dilihat model (test set), lakukan analisis error, dan pastikan model menjawab Research Questions yang sudah ditetapkan.

| Fase 4 — Evaluasi / Pengujian |  |
| ----- | :---- |
| **Durasi** | Week 5 – Week 6 |
| **PIC** | Semua anggota tim |
| **Tugas & Aktivitas** | Tugas 1: Mengevaluasi model menggunakan metrik regresi, seperti: MAE (Mean Absolute Error) RMSE (Root Mean Squared Error) MAPE (Mean Absolute Percentage Error) Tugas 2: Menganalisis selisih antara nilai aktual dan prediksi untuk memahami pola kesalahan model Tugas 3: Melakukan visualisasi performa model dengan membandingkan hasil prediksi dengan data aktual menggunakan grafik time series untuk melihat kemampuan model dalam mengikuti tren harga cabai. Tugas 4: Uji robustness model terhadap data edge case kondisi ekstrim atau data baru Tugas 5: Menjawab Research Questions berdasarkan hasil evaluasi Tugas 6: Meidentifikasi potensi bias atau kelemahan model |
| **Deliverables** | Deliverable 1: Laporan evaluasi model lengkap dengan metrik (MAE, RMSE, MAPE) dan visualisasi hasil prediksi vs aktual Deliverable 2: Analisis error dan interpretasi hasil model Deliverable 3: Jawaban terhadap Research Questions berdasarkan hasil evaluasi Deliverable 4: Dokumentasi kelemahan model dan rekomendasi pengembangan ke depan |
| **Milestone** | Model telah dievaluasi secara menyeluruh menggunakan metrik regresi dan analisis visual, serta mampu memberikan insight yang menjawab Research Questions terkait pengaruh cuaca terhadap harga cabai. |

## **3.5 Fase 5 — Deployment** {#3.5-fase-5-—-deployment}

Fase deployment: kemas model ke dalam aplikasi atau layanan yang dapat digunakan oleh end-user. Pastikan sistem dapat diakses dan berjalan dengan baik di lingkungan produksi/demo.

| Fase 5 — Deployment |  |
| ----- | :---- |
| **Durasi** | Week 6 – Week 7 |
| **PIC** | Muhammad Jibril Ibrahim |
| **Tugas & Aktivitas** | Tugas 1: Menyiapkan model untuk deployment dengan melakukan serialisasi model terbaik hasil tahap modeling menggunakan format seperti .pkl atau .joblip, serta memastikan pipeline preprocessing (scaling, feature engineering) ikut disimpan agar konsisten saat digunakan. Tugas 2: Membangun pipeline prediksi dengan menyusun alur input-proses-output Tugas 2: Membangun antarmuka pengguna/API untuk mengakses model dengan Streamlit untuk dashboard interaktifatau  Flask/FastAPI untuk layanan berbasis API Tugas 3: Melakukan deployment ke platform cloud atau hosting seperti Streamlit Cloud atau layanan hosting lainnya Tugas 5: Melakukan pengujian pada sistem yang telah di-deploy, meliputi Functional testing, Smoke testing, dan pengujian lainnya. |
| **Deliverables** | Deliverable 1: Model yang telah di-deploy dan dapat diakses melalui URL atau API Deliverable 2: Aplikasi/demo interaktif untuk prediksi harga cabai berbasis input data cuaca Deliverable 3: Dokumentasi penggunaan sistem (cara input data dan interpretasi output) Deliverable 4: Dokumentasi teknis deployment (arsitektur sederhana dan alur sistem) |
| **Milestone** | Sistem prediksi harga cabai berbasis model machine learning berhasil di-deploy dan dapat diakses secara online, serta siap untuk didemonstrasikan kepada reviewer. |

## **3.6 Fase 6 — Finalisasi Dokumen** {#3.6-fase-6-—-finalisasi-dokumen}

Fase penutup: rapikan semua dokumentasi proyek, bersihkan repository, dan siapkan materi presentasi final. Ini yang akan dinilai oleh mentor dan reviewer Capstone.

| Fase 6 — Finalisasi Dokumen |  |
| ----- | :---- |
| **Durasi** | Week 7 – Week 8 |
| **PIC** | Semua anggota tim |
| **Tugas & Aktivitas** | Tugas 1: Menyusun laporan teknis final (project brief) secara lengkap Tugas 2: Membuat slide presentasi yang rapi dan informatif Tugas 3: Membersihkan dan menstrukturkan repository (README, folder structure, komentar kode) Tugas 4: Menyiapkan panduan penggunaan sistem (user guide / technical documentation) |
| **Deliverables** | Deliverable 1: Laporan teknis final proyek (project brief) Deliverable 2: Slide presentasi siap untuk Final Presentation Deliverable 3: Repository bersih, terdokumentasi, dan publik/siap dikumpulkan Deliverable 4: Panduan penggunaan sistem (README atau dokumen terpisah) |
| **Milestone** | Milestone: Semua artefak proyek lengkap, terdokumentasi, dan siap untuk Final Presentation Data Mining |

# **BAGIAN 4** {#bagian-4}

**SUMBER DAYA PROJECT**

## **4.1 Bahasa Pemrograman** {#4.1-bahasa-pemrograman}

Bahasa yang digunakan dalam proyek ini yaitu Python. Python merupakan bahasa pemrograman yang paling luas digunakan saat ini. Dalam konteks penyelesaian tugas dan tantangan pada bidang data science, Python senantiasa memberikan kemudahan dan fleksibilitas bagi penggunanya. Python dilengkapi dengan pustaka-pustaka unggulan yang digunakan secara luas dalam pemecahan permasalahan komputasi \[4\].  
Python dipilih karena merupakan bahasa pemrograman tingkat tinggi yang bersifat open-source dengan ekosistem sains data paling matang di dunia. Dalam konteks prediksi harga cabai merah besar, Python unggul dalam menangani data unstructured (seperti scraping data cuaca) maupun structured (data harga pasar). Selain itu, Python menyediakan berbagai library yang mendukung proses analisis data, mulai dari preprocessing, eksplorasi data, hingga pemodelan machine learning \[4\].  
Keunggulan lain dari Python adalah kemampuannya dalam melakukan komputasi numerik dan pengolahan data multidimensi secara efisien, yang sangat dibutuhkan dalam menganalisis hubungan antara variabel cuaca di daerah pemasok dan harga cabai di pasar tujuan. Selain itu, Python juga mendukung integrasi dengan berbagai sumber data eksternal seperti API cuaca, sehingga mempermudah proses pengumpulan data dalam penelitian ini. 

## **4.2 Framework dan Library** {#4.2-framework-dan-library}

Library yang kami gunakan dalam proyek ini yaitu: 

1. Data Processing  
* Pandas, Pandas merupakan library utama dalam proses data science yang digunakan untuk manipulasi dan analisis data terstruktur. Pandas menyediakan struktur data seperti DataFrame yang memungkinkan pengolahan data dalam bentuk tabel secara efisien dan intuitif \[4\]. Dalam proyek ini, Pandas digunakan pada tahap preprocessing, seperti pembersihan data, penanganan missing value, transformasi data, serta penggabungan data harga cabai dan data cuaca menjadi satu dataset terintegrasi.   
* NumPy, NumPy (Numerical Python) merupakan library fundamental dalam komputasi numerik di Python yang menyediakan struktur array multidimensi serta operasi matematika berperforma tinggi \[4\]. Dalam proyek ini, NumPy digunakan untuk mendukung perhitungan numerik seperti normalisasi data, perhitungan statistik, serta transformasi fitur yang dibutuhkan dalam proses modeling.   
2. Data Mining & Modeling  
* Scikit-Learn, Scikit-Learn merupakan library machine learning berbasis Python yang menyediakan berbagai algoritma seperti clustering, klasifikasi, regresi, serta tools untuk preprocessing dan evaluasi model. Dalam proyek ini, Scikit-Learn digunakan untuk:  
  * Implementasi model Random Forest Regressor  
  * Implementasi Gradient Boosting Regressor  
  * Preprocessing data (scaling, splitting dataset)  
  * Evaluasi model menggunakan metrik seperti MAE, RMSE, dan R²  
    Library ini dipilih karena memiliki antarmuka yang konsisten serta mempermudah proses eksperimen model \[5\].  
3. Visualisasi Data  
* Matplotlib, Matplotlib merupakan library visualisasi data yang digunakan untuk membuat grafik seperti line chart, scatter plot, dan histogram \[4\].  
* Seaborn, Seaborn adalah library yang dibangun di atas Matplotlib dan digunakan khusus untuk visualisasi data statistik. Seaborn menyediakan fungsi dan tampilan yang lebih kaya untuk membuat visualisasi yang menarik dan informatif \[6\].


## **4.3 Tools dan Platform Pengembangan** {#4.3-tools-dan-platform-pengembangan}

Tools yang kami gunakan dalam proyek ini yaitu: 

* Google Colab, Google Colab merupakan platform berbasis cloud yang digunakan untuk menjalankan kode Python tanpa perlu instalasi di perangkat lokal. Platform ini sangat membantu dalam pengolahan data mining karena menyediakan resource komputasi yang cukup besar serta mendukung integrasi dengan library data science. Dalam proyek ini, Google Colab digunakan untuk eksplorasi data, preprocessing, serta implementasi model clustering \[7\].  
* VS Code Jupyter, VS Code merupakan code editor yang digunakan untuk pengembangan program secara lokal. Editor ini mendukung berbagai ekstensi Python yang memudahkan debugging, manajemen file, serta mempercepat modeling karana menggunakan gpu lokal \[8\].  
* Notion, Notion digunakan sebagai tools manajemen proyek dan kolaborasi kelompok untuk mencatat progres pengerjaan, membagi tugas, serta mendokumentasikan hasil analisis dan diskusi selama proses pengembangan proyek.  
* Google Meet, Google Meet digunakan sebagai media komunikasi dan koordinasi kelompok secara online, seperti diskusi progres, pembagian tugas, serta evaluasi hasil pengembangan proyek.  
* Streamlit, Streamlit merupakan sebuah framework opensource berbasis Python yang memungkinkan pengembangan aplikasi web secara cepat dan interaktif. Dalam proyek ini, Streamlit digunakan untuk mengembangkan dan menampilkan aplikasi prediksi harga beras berbasis web, sehingga hasil analisis dapat diakses dengan mudah oleh pengguna non-teknis \[9\].


## **4.4 Dataset** {#4.4-dataset}

Dataset yang digunakan dalam penelitian ini merupakan hasil integrasi dari dua sumber data utama yang berbeda untuk mencakup variabel target (harga) dan variabel prediktor (iklim). Berikut adalah rincian mengenai dataset tersebut:

1. Sumber Data Harga Pangan (Variabel Target) Data harga diperoleh dari Pusat Informasi Harga Pangan Strategis (PIHPS) Nasional untuk wilayah DKI Jakarta (Pasar Tradisional).  
* Komoditas: Cabai Merah Besar.  
* Rentang Waktu: Januari 2021 hingga April 2026\.  
* Jumlah Data: Kurang lebih 1.386 baris data harian.  
* Fitur Utama: Harga rata-rata harian dalam satuan Rupiah (IDR).  
2. Sumber Data Iklim/Cuaca (Variabel Prediktor) Data iklim diperoleh dari stasiun pengamatan meteorologi di wilayah Bandung, yang diidentifikasi sebagai salah satu daerah pemasok utama cabai untuk Jakarta. Data ini berasal dari catatan historis BMKG.  
* Rentang Waktu: Mei 2024 hingga April 2026 (disinkronkan dengan data harga).  
* Atribut Cuaca:  
  * TAVG: Temperatur rata-rata harian (°C).  
  * RH\_AVG: Kelembapan rata-rata harian (%).  
  * RR: Curah hujan harian (mm).  
  * TN / TX: Temperatur minimum dan maksimum harian (°C).  
  * SS: Durasi penyinaran matahari (jam).  
  * ff\_avg: Kecepatan angin rata-rata (m/s).  
3. Integrasi dan Kondisi Data Kedua sumber data tersebut digabungkan berdasarkan kunci format waktu (*timestamp*). Mengingat karakteristik data *time series*, dilakukan beberapa perlakuan khusus sebelum masuk ke tahap pemodelan:  
* Penanganan Missing Values: Menggunakan metode *Linear Interpolation* untuk mengisi kekosongan data pada hari libur nasional atau akhir pekan (khusus data harga) dan penanganan nilai anomali (kode 8888/9999) pada data cuaca.  
* Sinkronisasi Waktu: Data diformat ke dalam indeks harian untuk memastikan hubungan kausalitas antara cuaca di hari dan harga di hari yang sama dapat dianalisis melalui teknik *lagging features*.  
* Karakteristik Data: Dataset ini bersifat multivariat, di mana fluktuasi harga cabai merah besar menunjukkan pola musiman yang dipengaruhi secara signifikan oleh fenomena anomali cuaca (hujan ekstrem) di daerah produksi.

## **4.5 Paper / Jurnal / Artikel Referensi** {#4.5-paper-/-jurnal-/-artikel-referensi}

**Referensi 1**  
Hamizan Gholib, Muhinda Yasa Arindra Barana Dya, Sarah Anami Girsang, Sartika Almirah Sobri. (2025). Model Prediksi Harga Cabai Merah Besar di Tingkat Pasar Tradisional Tahun 2017–2024: Pendekatan Supervised Learning Berbasis Orange Data Mining.  Integrative Perspectives of Social and Science Journal (IPSSJ), Volume 2 No.3. Link: [https://ipssj.com/index.php/ojs/article/view/792](https://ipssj.com/index.php/ojs/article/view/792)	

Relevansi:   
Jurnal ini sangat relevan dengan proyek yang dikembangkan karena memiliki tujuan yang sama, yaitu memprediksi harga cabai merah besar menggunakan pendekatan machine learning. Penelitian tersebut menggunakan metode supervised learning dengan membandingkan beberapa algoritma regresi seperti Linear Regression, SVM, Decision Tree, Random Forest, Gradient Boosting, hingga AdaBoost untuk menentukan model terbaik.  
Selain itu, penelitian ini juga menggunakan data multivariat berbasis time series yang mencakup harga cabai di beberapa wilayah pemasok seperti Bandung serta variabel pendukung seperti inflasi . Hal ini sejalan dengan proyek yang dikembangkan, yang juga memanfaatkan data historis harga dan faktor eksternal (dalam hal ini variabel cuaca) untuk melakukan prediksi.  
Dari sisi metodologi, penelitian ini mengacu pada framework CRISP-DM yang mencakup tahapan business understanding, data understanding, data preparation, modeling, evaluation, hingga deployment . Pendekatan ini menjadi dasar dalam perancangan alur pengerjaan proyek sehingga proses data mining dapat dilakukan secara sistematis dan terstruktur.   
Hasil penelitian menunjukkan bahwa algoritma berbasis ensemble seperti AdaBoost mampu memberikan performa prediksi yang tinggi dengan tingkat error yang rendah . Hal ini menjadi inspirasi dalam pemilihan algoritma pada proyek, khususnya penggunaan model berbasis boosting seperti XGBoost sebagai salah satu pendekatan utama.

# **DAFTAR PUSTAKA** {#daftar-pustaka}

\[1\]	Winda Andini, Siti Kumala Zahra, Muhammad Abdurrahman, and Veralianta Br Sebayang, “Analisis Fluktuasi Harga Terhadap Faktor-Faktor Yang Mempengaruhi Produktivitas Usaha Tani Cabai Merah di Indonesia,” *Jurnal Riset dan Inovasi Manajemen*, vol. 2, no. 2, pp. 162–172, 2024, doi: 10.59581/jrim-widyakarya.v2i2.3526.  
\[2\]	H. Gholib, M. Yasa, A. Barana, S. A. Girsang, and S. A. Sobri, “Model Prediksi Harga Cabai Merah Besar Di Tingkat Pasar Tradisional Tahun 2017 \- 2024: Pendekatan Supervised Learning Berbasis Orange Data Mining,” *Integrative Perspectives of Social and Science Journal*, vol. 2, no. 03 Agustus, pp. 6823–6839, 2025, \[Online\]. Available: https://ipssj.com/index.php/ojs/article/view/792  
\[3\]	D. Montreano, Redian Wahyu Elanda, and Harditriyono Putra, “Model Prediksi Harga Cabai Merah Besar Di Tingkat Produsen Periode 2022-2024 Dengan Metode Supervised Learning Menggunakan Orange Data Mining,” *Venus: Jurnal Publikasi Rumpun Ilmu Teknik *, vol. 3, no. 1, pp. 19–29, 2025, doi: 10.61132/venus.v3i1.697.  
\[4\]	A. S. Saabith, T. Vinothraj, and M. Fareez, “A Review on Python Libraries and Ides for Data Science,” *International Journal of Research in Engineering and Science (IJRES) ISSN*, vol. 09, no. 11, pp. 36–53, 2021, \[Online\]. Available: www.ijres.org  
\[5\]	M. F. El-Amin, B. Alwated, and H. A. Hoteit, “Machine Learning Prediction of Nanoparticle Transport with Two-Phase Flow in Porous Media,” *Energies (Basel).*, vol. 16, no. 2, 2023, doi: 10.3390/en16020678.  
\[6\]	K. Hermanto, D. Salim, B. Wu, O. R. Alim, and R. B. Gunadi, “Penggunaan Python Untuk Menganalisis Pola Penyebaran Covid-19 Di Masa,” vol. 2, pp. 120–133, 2022, doi: https://doi.org/10.36987/josdis.v3i2.4548.  
\[7\]	R. A. A. Yanuar, “Sentimen Analisis Aplikasi Posaja Pada Google Playstore Untuk Peningkatan Pospay Superapp Menggunakan Support Vector Meachine" Jurnal Teknik Informatika, Vol. 16, No. 2, April 2024,” *Jurnal Teknik Informatika*, vol. 16, no. 2, pp. 1–7, 2024\.  
\[8\]	K. S. Ningsih, N. J. Aruan, and A. T. A. A. Siahaan, “Aplikasi Buku Tamu Menggunakan Fitur Kamera Dan Ajax Berbasis Website Pada Kantor Dispora Kota Medan,” *SITek: Jurnal Sains, Informatika, dan Tekonologi*, vol. 1, pp. 94–99, 2022\.  
\[9\]	D. Devalio, A. Anisya, A. Syahrani, I. Warman, and B. Busran, “Perancangan Website Untuk Prediksi Jumlah Pengeluaran Mahasiswa Berbasis Framework Streamlit,” *Jurnal Informatika dan Teknik Elektro Terapan*, vol. 13, no. 2, 2025, doi: 10.23960/jitet.v13i2.6451.  
 

**LAMPIRAN**

1. Video Presentasi Data Mining Kelompok 10: [Link](https://drive.google.com/file/d/1PVnHAmHIlMq7k9hpmXrKOtTeOscZn51H/view?usp=sharing)