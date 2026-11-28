# Cyber Hygiene Scorecard
> **Mini PBL — Build Cybersecurity for Humans**  
> **Kelompok:** WARRGA BULAN | **Kelas:** Malam 1A  
> **Program Studi:** Rekayasa Keamanan Siber — Politeknik Negeri Batam (2026)

---

## Tentang Proyek
**Cyber Hygiene Scorecard** adalah aplikasi interaktif berbasis **Python CLI (Command Line Interface)** yang dijalankan melalui terminal Linux untuk membantu mahasiswa dan pengguna digital pemula mengevaluasi kebiasaan keamanan siber sehari-hari secara mandiri.

Pengguna menjawab **10 pertanyaan kebiasaan digital** yang terbagi ke dalam **5 kategori keamanan**, lalu program menghitung skor keseluruhan maupun skor per aspek, mengklasifikasikan tingkat keamanan, memberikan rekomendasi perbaikan paling prioritas, serta menyimpan laporan ringkasan lokal dengan izin akses terbatas (`chmod 600`) di Linux.

> **Prinsip Privasi & Keamanan:**  
> Aplikasi ini bersifat murni edukatif. Program **tidak pernah** meminta password asli, kode OTP, token, maupun identitas/data pribadi sensitif pengguna.

---

## 👥 Anggota Kelompok (WARRGA BULAN)

| No. | Nama Anggota | NIM | Peran (*Role*) | Fokus Tanggung Jawab |
| :-: | :--- | :---: | :--- | :--- |
| 1 | **Wahyu Iqbal Apriliansyah** | `4332611019` | *Testing & Documentation* | Pengujian 6 skenario teknis, uji coba >=10 pengguna, & dokumentasi |
| 2 | **Galang Rovegha Putera** | `4332611004` | *Python Application Developer* | Membangun program utama Python CLI, validasi input, & integrasi modul |
| 3 | **Firembulan Nurhaniza** | `4332611024` | *Security Research & Assessment* | Menyusun 10 pertanyaan di 5 kategori, bobot jawaban, & teks rekomendasi |
| 4 | **Rizal Oky Alghifari** | `4332611027` | *System & Algorithm Designer* | Merancang flowchart, pseudocode, & logika perhitungan/klasifikasi skor |
| 5 | **Ryamizard Novriyanto** | `4332611008` | *Linux Integration* | Manajemen direktori `reports/`, penyimpanan laporan, & permission Linux (`chmod 600`) |

---

## Integrasi Mata Kuliah

| Mata Kuliah | Penerapan dalam Proyek |
| :--- | :--- |
| **Dasar Keamanan Siber** | Penerapan konsep *cyber hygiene* pada 5 aspek utama: *Password Security*, *Multi-Factor Authentication (MFA)*, *Software Update*, *Data Backup*, dan *Message Security*. |
| **Algoritma dan Pemrograman** | Penggunaan Python standar untuk struktur data (`list`/`dict`), perulangan, validasi input interaktif, percabangan (`if-elif-else`), kalkulasi skor, dan penulisan file. |
| **Linux Fundamental** | Eksekusi aplikasi via terminal Linux, pembuatan direktori laporan (`mkdir`), pembatasan hak akses file laporan (`chmod 600`), serta verifikasi file (`ls -l` dan `cat`). |

---

## Rancangan Penilaian (*Scoring Rules*)

* **Jumlah Pertanyaan:** 10 pertanyaan (5 kategori × 2 pertanyaan).
* **Poin Jawaban:**
  * Kebiasaan Aman = **`2` poin**
  * Kadang-kadang = **`1` poin**
  * Kurang Aman = **`0` poin**
* **Rumus Perhitungan:**
  * **Skor Kategori** = `(Poin Kategori / 4) × 100` *(rentang 0–100)*
  * **Skor Akhir** = `(Total Poin / 20) × 100` *(rentang 0–100)*
* **Klasifikasi Hasil Akhir:**
  * `80 – 100` : **Baik**
  * `60 – 79`  : **Cukup**
  * `0 – 59`   : **Perlu Ditingkatkan**
* **Aturan Rekomendasi:** Memprioritaskan kategori dengan **skor paling rendah**. Apabila terdapat skor terendah yang seri (*tie*), seluruh kategori terendah tersebut ditampilkan rekomendasinya.

---

## Struktur Repositori

Setiap anggota tim memiliki ruang kerja yang terorganisir agar pengembangan berjalan rapi dan minim konflik kode:

```text
Cyber_Hygiene_Scorecard/
├── .github/                        # Template Issue & Pull Request untuk kolaborasi tim
├── docs/                           # Dokumentasi per bidang tugas Mini PBL
│   ├── algorithm_and_scoring.md    # Flowchart, pseudocode, & aturan hitung (Rizal)
│   ├── security_assessment_design.md # Riset 5 kategori, kuesioner, & saran (Firembulan)
│   ├── linux_integration_proof.md  # Panduan & bukti eksekusi di Linux (Ryamizard)
│   └── testing_and_feedback.md     # Hasil uji 6 skenario & feedback >=10 user (Wahyu)
├── reports/                        # Direktori output laporan TXT lokal (di-ignore dari Git)
├── scripts/
│   └── verify_linux.sh             # Script bantu cek direktori & permission di Linux (Ryamizard)
├── src/                            # Kode sumber aplikasi Python CLI
│   ├── __init__.py
│   ├── main.py                     # Entry point aplikasi & interaksi CLI (Galang)
│   ├── questions_data.py           # Bank 10 pertanyaan & daftar rekomendasi (Firembulan)
│   ├── scoring.py                  # Fungsi kalkulasi skor & penentuan kategori (Rizal & Galang)
│   └── report_linux.py             # Penyimpanan file TXT & pengaturan chmod 600 (Ryamizard & Galang)
├── tests/                          # Skenario pengujian teknis aplikasi (Wahyu)
│   └── README.md
├── .gitattributes
├── .gitignore
├── CONTRIBUTING.md                 # Panduan cara kerja bareng di GitHub untuk anggota tim
└── README.md
```

---

## Cara Menjalankan (Terminal Linux)

Pastikan **Python 3** sudah terpasang di lingkungan Linux kamu (`python3 --version`).

```bash
# 1. Clone repositori ini
git clone https://github.com/grovegha/Cyber_Hygiene_Scorecard.git
cd Cyber_Hygiene_Scorecard

# 2. Jalankan aplikasi Cyber Hygiene Scorecard
python3 src/main.py

# 3. Periksa file laporan dan permission-nya di Linux (harus -rw------- / 600)
ls -l reports/

# 4. Baca isi laporan hasil penilaian
cat reports/<nama_file_laporan>.txt
```

---

## Rencana Pengujian Utama
1. Seluruh jawaban bernilai `2` menghasilkan skor akhir **`100`** (*Baik*).
2. Seluruh jawaban bernilai `0` menghasilkan skor akhir **`0`** (*Perlu Ditingkatkan*).
3. Kombinasi jawaban menghasilkan perhitungan skor per kategori dan total yang akurat.
4. Input di luar opsi yang valid ditolak dan pengguna diminta mengisi ulang tanpa membuat program berhenti (*crash*).
5. Rekomendasi tampil akurat sesuai kategori skor terendah (termasuk saat terjadi nilai terendah seri).
6. Laporan `.txt` berhasil dibuat di folder `reports/`, dapat dibaca dengan `cat`, dan terkonfirmasi memiliki izin terbatas `chmod 600` (`-rw-------`).
