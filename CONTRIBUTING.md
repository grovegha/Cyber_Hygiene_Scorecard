# 🤝 Panduan Kolaborasi Tim WARRGA BULAN (`CONTRIBUTING.md`)

Halo tim **WARRGA BULAN**! Dokumen ini dibuat supaya kita berlima bisa ngerjain **Cyber Hygiene Scorecard** bareng-bareng di GitHub dengan rapi, nggak saling menimpa kerjaan teman lain, dan kontribusi (*commit*) tiap anggota tercatat jelas saat dinilai dosen.

---

## 1. Pembagian "Kavling" File per Anggota

Supaya nggak rebutan mengedit file yang sama di waktu bersamaan, fokuskan pengerjaan di folder/file sesuai peran masing-masing:

| Anggota | Fokus File yang Dikerjakan |
| :--- | :--- |
| **Galang** (*Python App Dev*) | `src/main.py` & integrasi antar file di `src/` |
| **Firembulan** (*Security Research*) | `src/questions_data.py` & `docs/security_assessment_design.md` |
| **Rizal** (*System & Algorithm*) | `docs/algorithm_and_scoring.md` & logika rumus di `src/scoring.py` |
| **Ryamizard** (*Linux Integration*) | `src/report_linux.py`, `scripts/verify_linux.sh`, & `docs/linux_integration_proof.md` |
| **Wahyu** (*Testing & Docs*) | `tests/` & `docs/testing_and_feedback.md` |

> *Catatan: Kalau butuh mengubah file di luar kavlingmu, kabari dulu di grup tim ya!*

---

## 2. Langkah Awal (Cuma Dilakukan Sekali di Laptop Masing-Masing)

1. Pastikan sudah klik **Accept Invitation** dari link undangan repo GitHub yang dikirim Galang.
2. Buka Terminal (Linux / Git Bash / PowerShell), lalu jalankan:
   ```bash
   git clone https://github.com/grovegha/Cyber_Hygiene_Scorecard.git
   cd Cyber_Hygiene_Scorecard
   ```

---

## 3. Alur Kerja Harian (Jangan Langsung Push ke `main`!)

Branch **`main`** kita jaga khusus untuk versi yang sudah rapi dan jalan. Setiap kali mau ngerjain tugasmu, ikuti 5 langkah gampang ini:

### Langkah 1: Ambil update terbaru dari `main`
```bash
git checkout main
git pull origin main
```

### Langkah 2: Buat atau pindah ke *branch* kerjamu sendiri
Gunakan format nama branch yang jelas (contoh per anggota):
* `feat/firembulan-pertanyaan`
* `feat/rizal-algoritma`
* `feat/galang-cli`
* `feat/ryamizard-linux`
* `docs/wahyu-pengujian`

Cara membuatnya:
```bash
git checkout -b nama-branch-kamu
```
*(Kalau branch-nya sudah pernah dibuat sebelumnya, cukup `git checkout nama-branch-kamu`).*

### Langkah 3: Kerjakan tugasmu & cek perubahan
Setelah selesai mengedit dan mengetes file:
```bash
git status
```

### Langkah 4: Simpan (*Commit*) dan unggah (*Push*) ke GitHub
```bash
git add .
git commit -m "Menambahkan daftar 10 pertanyaan dan rekomendasi keamanan"
git push -u origin nama-branch-kamu
```

### Langkah 5: Buat *Pull Request (PR)* di Web GitHub
1. Buka halaman repo GitHub `grovegha/Cyber_Hygiene_Scorecard`.
2. Klik tombol kuning/hijau **Compare & pull request** yang muncul di atas.
3. Isi deskripsi singkat apa yang kamu kerjakan, lalu klik **Create pull request**.
4. Kabari di grup supaya dicek bareng sebelum di-*Merge* ke `main`!

---

## 4. Aturan Keamanan & Kerapian (Wajib Anak RKS!)
* **Jangan pernah** mengunggah password asli, token, API key, atau data pribadi responden pengujian ke dalam repositori.
* File hasil percobaan laporan (`reports/*.txt`) sudah otomatis diabaikan oleh `.gitignore` supaya tidak mengotori GitHub. Kalau butuh melampirkan contoh hasil di dokumentasi, pastikan isinya murni data simulasi anonim.
* Gunakan hanya **Python 3 Standard Library** (bawaan Python) tanpa library eksternal tambahan agar aplikasi langsung berjalan mulus di semua komputer Linux tanpa kendala instalasi.
