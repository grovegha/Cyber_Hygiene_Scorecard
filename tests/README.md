# Folder Pengujian (`tests/`)

> **Penanggung Jawab:** Wahyu Iqbal Apriliansyah (`4332611019`)

Folder ini disiapkan untuk menyimpan script pengujian otomatis (misalnya menggunakan modul bawaan `unittest` Python) maupun data simulasi untuk memverifikasi ke-6 skenario teknis pada proposal:

1. Semua jawaban bernilai `2` -> Skor `100` (*Baik*).
2. Semua jawaban bernilai `0` -> Skor `0` (*Perlu Ditingkatkan*).
3. Kombinasi jawaban -> Skor per kategori dan skor total sesuai rumus.
4. Input tidak valid -> Ditolak dan diminta ulang.
5. Rekomendasi prioritas -> Tepat pada kategori terendah (termasuk saat seri).
6. Penyimpanan laporan Linux -> File terbuat di `reports/` dengan permission `600`.
