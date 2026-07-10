# Buku Panduan Penggunaan: Sistem Pemantauan Aktivitas Kelas (AI Classroom Monitoring)

Buku panduan ini dirancang untuk menjelaskan cara menggunakan sistem pemantauan kelas berbasis website secara praktis langkah demi langkah bagi Guru dan Kepala Sekolah.

**Link Google Drive Resmi:** [Unduh Berkas Buku Panduan PDF](https://drive.google.com/drive/folders/1ctk4lhtUS3Ki5RdJZ5mAR3rMVt35J1rc?usp=sharing)

---

## 1. PANDUAN PENGGUNAAN BAGI GURU (TEACHER)

Guru menggunakan sistem ini untuk mengunggah video sesi belajar kelas dan melihat hasil analisis ekspresi emosi siswa di kelasnya masing-masing secara berkala.

### Langkah 1: Login ke Akun Guru
Buka halaman utama website. Masukkan kredensial Guru Anda:
*   **Username:** `guru` (untuk Guru utama) atau `guru2` (untuk Guru muda).
*   **Password:** `guru123` (atau `guru2123`).
Setelah data terisi, klik tombol **Login**. Sistem akan memverifikasi peran Anda dan mengarahkan ke **Teacher Dashboard** secara otomatis.

### Langkah 2: Memahami Dashboard Guru
Setelah berhasil login, Anda berada di halaman dashboard Guru yang menyajikan:
1.  **Kotak Metrik Ringkasan:** 
    *   **Total Upload:** Jumlah keseluruhan video pembelajaran yang pernah Anda unggah.
    *   **Selesai Diproses:** Jumlah video pembelajaran yang telah selesai dianalisis oleh sistem AI.
    *   **Sedang Diproses:** Jumlah video yang saat ini sedang dalam proses analisis.
2.  **Tabel Riwayat Video (Riwayat Upload Video):** Daftar seluruh rekaman video yang pernah Anda unggah lengkap dengan informasi Mata Pelajaran (*Subject*), Kelas (*Class*), Hari (*Day*), Jam (*Time*), Status Analisis (*Status*), dan tautan aksi untuk melihat detail (*View*).

![Dashboard Guru dan Riwayat Upload](/Users/reynaldabner/.gemini/antigravity-ide/brain/c06692c6-ca5e-4e3b-bddc-a5fb11b8e2e5/media__1782967424619.png)

### Langkah 3: Mengisi Formulir & Mengunggah Video Baru
Untuk mengunggah video baru, klik tombol **Upload New Video** (atau **Upload Video Baru**) di dashboard (kanan atas) atau navigasi atas. Isi formulir metadata dengan lengkap:
*   **Subject (Mata Pelajaran):** Pilih opsi pelajaran (English, Bahasa Indonesia, Science, Math).
*   **Class Name (Nama Kelas):** Masukkan nama kelas secara manual (contoh: *Class 10-A* atau *11-MIPA-3*).
*   **Learning Date (Tanggal Belajar):** Pilih tanggal pelaksanaan kelas menggunakan pemilih kalender. Kolom Hari (*Day*) akan terisi otomatis setelah tanggal ditentukan.
*   **Start & End Time (Jam Mulai/Selesai):** Tentukan jam pelajaran dimulai dan selesai (misalnya: *10:00 AM* dan *12:00 PM*).
*   **Notes (Catatan):** Masukkan catatan tambahan opsional mengenai jalannya kelas.
*   **Video File:** Pilih berkas rekaman video pembelajaran (.mp4, .mts).
Setelah itu, klik tombol **Upload and Process** di bagian bawah form.

![Halaman Upload Video](/Users/reynaldabner/.gemini/antigravity-ide/brain/c06692c6-ca5e-4e3b-bddc-a5fb11b8e2e5/teacher_upload_clean_1782967233753.png)

### Langkah 4: Memantau Proses Pipeline AI
Setelah tombol ditekan, modal **Memproses Video** akan muncul di layar. Modal ini memperlihatkan empat tahapan yang berjalan berturut-turut:
1.  *Upload File:* Berkas video Anda berhasil diunggah ke server.
2.  *Preprocessing:* AI mengekstrak wajah siswa menggunakan model *YOLOv8-Face*.
3.  *Model Inference:* AI melakukan klasifikasi ekspresi wajah menggunakan model *EfficientNet-B2*.
4.  *Selesai:* Sistem menyimpan log dan hasil analisis ke database.
**PENTING:** Jangan menutup atau merefresh halaman web selama modal pemrosesan berjalan. Begitu mencapai 100% (Completed), Anda akan langsung dialihkan ke halaman detail secara otomatis.

![Modal Proses Video](/Users/reynaldabner/.gemini/antigravity-ide/brain/c06692c6-ca5e-4e3b-bddc-a5fb11b8e2e5/media__1782967415152.png)

### Langkah 5: Meninjau Detail Hasil Analisis Kelas
Halaman **Detail Upload Guru** menampilkan hasil analisis kelas yang lengkap:
*   **Metadata Kelas:** Rincian jadwal, mata pelajaran, nama kelas, tanggal upload, status, waktu selesai proses, jumlah wajah, skor model, prediksi dominan, dan berkas video.
*   **📊 Breakdown Ekspresi:** Menampilkan jumlah wajah terdeteksi dan persentase kemunculan dari masing-masing 6 ekspresi emosi siswa (Happy, Sad, Angry, Surprised, Neutral, Tired) secara visual untuk memantau keterlibatan siswa.
*   **Aksi Cepat:** Guru dapat kembali ke dashboard atau menghapus berkas data video (serta data wajah yang diekstrak) secara permanen dari server dengan menekan tombol **Hapus video**.

![Detail Upload Guru](/Users/reynaldabner/.gemini/antigravity-ide/brain/c06692c6-ca5e-4e3b-bddc-a5fb11b8e2e5/media__1782967403695.png)

---

## 2. PANDUAN PENGGUNAAN BAGI KEPALA SEKOLAH (PRINCIPAL)

Kepala Sekolah menggunakan sistem ini untuk pengawasan umum, memantau data analitik agregat tingkat sekolah, serta memvalidasi keakuratan prediksi model AI.

### Langkah 1: Login ke Akun Kepala Sekolah
Masukkan kredensial Kepala Sekolah Anda:
*   **Username:** `kepsek`
*   **Password:** `kepsek123`
Setelah login, Anda langsung diarahkan ke Dashboard Kepala Sekolah.

### Langkah 2: Memantau Dashboard Analitik Utama
Pada Dashboard Kepala Sekolah, Anda disajikan data visualisasi pemantauan tingkat sekolah secara real-time:
*   **Statistik Total Submisi:** Jumlah total video kelas terkumpul dan rincian status keberhasilan proses (selesai, sedang proses, gagal).
*   **Filter Tanggal (Filter Uploads by Date):** Masukkan rentang tanggal *From Date* dan *To Date*, lalu klik *Apply Filter* untuk membatasi laporan daftar pembelajaran di bawahnya secara instan.
*   **Weekly Activity Pattern:** Grafik batang dinamis jumlah video yang diunggah dalam 7 hari terakhir.
*   **Subject-wise Analytics (Analisis Pelajaran):** Menampilkan tingkat keberhasilan analisis dan tiga ekspresi dominan (*Top 3 Expressions*) siswa untuk setiap mata pelajaran (contoh: Math dominan Tired, English dominan Happy).
*   **Teacher Contribution Board (Performa Guru):** Papan peringkat guru yang paling aktif mengunggah video sesi belajar beserta persentase keberhasilan kinerjanya.
*   **Top Expressions in School (Ekspresi Dominan):** Diagram batang akumulasi sebaran emosi siswa di tingkat sekolah.
*   **Latest Uploads:** Tabel 20 rekaman video terbaru dari seluruh guru.

![Dashboard Kepala Sekolah](/Users/reynaldabner/.gemini/antigravity-ide/brain/c06692c6-ca5e-4e3b-bddc-a5fb11b8e2e5/principal_dashboard_clean_1782966793657.png)

### Langkah 3: Validasi Keakuratan Sistem AI
Untuk menguji keandalan sistem AI, klik menu **Model Validation** di navigasi atas. Di halaman ini, Kepala Sekolah dapat melihat perbandingan data prediksi website dengan Ground Truth (GT) asli dari observasi pengamat:
*   **Akurasi & Kemiripan:** Persentase kecocokan prediksi label dominan model website dengan Ground Truth (Akurasi) dan persentase kemiripan sebaran emosi (Average Similarity).
*   **Bagan Komparasi (Comparison Chart):** Klik baris submisi untuk menampilkan grafik komparatif yang membandingkan persentase emosi prediksi website (merah) dan Ground Truth (biru) secara berdampingan untuk 6 ekspresi wajah (Angry, Happy, Neutral, Sad, Surprised, Tired). Status kecocokan akan ditandai dengan **CORRECT** atau **INCORRECT**.

![Halaman Validasi Model AI](/Users/reynaldabner/.gemini/antigravity-ide/brain/c06692c6-ca5e-4e3b-bddc-a5fb11b8e2e5/principal_validation_clean_1782966854037.png)

---

## 3. TIPS PENGOPERASIAN VIDEO YANG BAIK

*   **Posisi Kamera:** Letakkan kamera di sudut kelas yang dapat menangkap wajah siswa secara frontal (hadap depan) dengan jelas agar mempermudah deteksi wajah oleh YOLOv8.
*   **Pencahayaan:** Pastikan pencahayaan kelas cukup terang untuk membantu model AI mengenali ekspresi wajah siswa secara akurat.
*   **Menghapus Data:** Guru dapat menghapus berkas video yang salah atau tidak terpakai secara permanen dengan mengeklik tombol **Hapus video** di halaman detail riwayat Guru.
