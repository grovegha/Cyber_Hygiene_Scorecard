"""
Modul Penyimpanan Laporan & Integrasi Permission Linux
Penanggung Jawab: Ryamizard Novriyanto (Linux Integration) & Galang Rovegha Putera

Aturan sesuai Proposal Mini PBL:
- Membuat direktori `reports/` jika belum tersedia.
- Menyimpan ringkasan hasil penilaian ke file `.txt` TANPA identitas/jawaban sensitif.
- Mengatur hak akses file laporan menjadi terbatas (`chmod 600` / `0o600` di Linux)
  agar pengguna lain di sistem tidak dapat membaca laporan secara sembarangan.
"""

import os


def save_assessment_report(report_content: str, reports_dir: str = "reports") -> str:
    """Menyimpan ringkasan penilaian ke file TXT dan menerapkan permission 600 di Linux."""
    # TODO (Ryamizard & Galang):
    # 1. Pastikan direktori `reports/` tersedia (os.makedirs)
    # 2. Buat nama file unik berbasis timestamp (misal: scorecard_YYYYMMDD_HHMMSS.txt)
    # 3. Tulis `report_content` ke file
    # 4. Atur permission file dengan os.chmod(filepath, 0o600) saat berjalan di Linux
    pass
