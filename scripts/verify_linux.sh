#!/usr/bin/env bash
# ==============================================================================
# Script Verifikasi Integrasi Linux Fundamental — Cyber Hygiene Scorecard
# Penanggung Jawab: Ryamizard Novriyanto (4332611008)
#
# Fungsi:
# Membantu demonstrasi & pengecekan direktori laporan (`mkdir`), daftar file &
# permission (`ls -l`), pengaturan hak akses terbatas (`chmod 600`), serta
# pembacaan isi laporan (`cat`) di terminal Linux.
# ==============================================================================

set -e

REPORTS_DIR="reports"

echo "=== [1/3] Memastikan direktori '$REPORTS_DIR' tersedia ==="
mkdir -p "$REPORTS_DIR"

echo "=== [2/3] Memeriksa daftar file dan permission di '$REPORTS_DIR' (ls -l) ==="
ls -l "$REPORTS_DIR"

echo "=== [3/3] Panduan cek isi laporan ==="
echo "Gunakan perintah: cat $REPORTS_DIR/<nama_file_laporan>.txt"
echo "Pastikan kolom permission di atas tertulis '-rw-------' (chmod 600)."
