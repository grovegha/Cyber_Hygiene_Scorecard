# 🐧 Dokumentasi & Bukti Integrasi Linux Fundamental

> **Penanggung Jawab:** Ryamizard Novriyanto (`4332611008`) — *Linux Integration*

---

## 1. Daftar Perintah Linux yang Diterapkan

| Kebutuhan | Perintah Linux | Tujuan Keamanan / Operasional |
| :--- | :--- | :--- |
| Menjalankan aplikasi | `python3 src/main.py` | Mengeksekusi aplikasi interaktif melalui terminal Linux |
| Membuat direktori laporan | `mkdir -p reports` | Menyiapkan folder khusus penyimpanan hasil assessment |
| Membatasi izin akses laporan | `chmod 600 reports/<file>.txt` | Hanya pemilik file (*owner*) yang dapat membaca & menulis (`-rw-------`) |
| Memeriksa hak akses file | `ls -l reports/` | Memastikan permission `600` sudah aktif |
| Membaca isi laporan | `cat reports/<file>.txt` | Menampilkan ringkasan hasil penilaian di terminal |

---

## 2. Bukti Eksekusi di Lingkungan Linux
*(TODO Ryamizard: Lampirkan log terminal atau screenshot bukti eksekusi di Linux pada bagian ini saat tahap pengujian/demo).*

1. **Bukti menjalankan program (`python3 src/main.py`):**
   * *(Lampirkan di sini)*
2. **Bukti pemeriksaan permission `chmod 600` (`ls -l reports/`):**
   * *(Lampirkan di sini)*
3. **Bukti pembacaan laporan (`cat reports/...`):**
   * *(Lampirkan di sini)*
