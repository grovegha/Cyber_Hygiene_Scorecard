"""
Modul Perhitungan Skor, Klasifikasi, & Penentuan Rekomendasi
Penanggung Jawab: Rizal Oky Alghifari (System & Algorithm Designer) & Galang Rovegha Putera

Aturan Perhitungan sesuai Proposal Mini PBL:
- Skor Kategori = (Poin Kategori / 4) * 100   [Rentang 0 - 100]
- Skor Akhir    = (Total Poin / 20) * 100     [Rentang 0 - 100]
- Kategori Hasil:
  * 80 - 100 : "Baik"
  * 60 - 79  : "Cukup"
  * 0  - 59  : "Perlu Ditingkatkan"
- Rekomendasi Prioritas:
  * Ambil kategori dengan skor paling rendah.
  * Jika terdapat skor terendah yang seri (tie), kembalikan seluruh kategori terendah tersebut.
"""


def calculate_category_scores(category_points: dict) -> dict:
    """Menghitung skor (0-100) untuk masing-masing dari 5 kategori."""
    # TODO (Rizal & Galang): Implementasikan rumus (poin_kategori / 4) * 100
    pass


def calculate_final_score(total_points: int) -> float:
    """Menghitung skor akhir (0-100) dari total poin maksimum 20."""
    # TODO (Rizal & Galang): Implementasikan rumus (total_points / 20) * 100
    pass


def classify_score(final_score: float) -> str:
    """Mengembalikan label 'Baik', 'Cukup', atau 'Perlu Ditingkatkan'."""
    # TODO (Rizal & Galang): Implementasikan percabangan kategori hasil
    pass


def get_lowest_categories(category_scores: dict) -> list:
    """Mengembalikan daftar kategori dengan skor terendah (mendukung kondisi seri)."""
    # TODO (Rizal & Galang): Cari nilai minimum dan kumpulkan semua kategori yang bernilai minimum
    pass
