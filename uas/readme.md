# Game Kriptografi

## Deskripsi
Game Kriptografi adalah aplikasi interaktif berbasis web yang menguji kemampuan pemain dalam memecahkan pesan terenkripsi menggunakan dua metode kriptografi:
1. **Shift Cipher**
2. **Zigzag Cipher**

Pemain harus memecahkan setiap pesan untuk naik ke level berikutnya hingga semua level selesai. Aplikasi ini dibuat menggunakan Python dan framework **Streamlit**.

## Fitur Utama
- **Shift Cipher**: Metode substitusi sederhana di mana setiap huruf digeser sejauh kunci tertentu.
- **Zigzag Cipher**: Metode transposisi yang menyusun teks dalam pola zigzag sesuai dengan kedalaman tertentu.
- Antarmuka pengguna berbasis web untuk interaksi yang mudah.
- Pencatatan waktu penyelesaian game.

## Cara Bermain
1. Jalankan aplikasi.
2. Klik tombol **Start** untuk memulai permainan.
3. Pada setiap level, baca tipe cipher, pesan terenkripsi, dan kunci.
4. Masukkan jawaban Anda di kolom yang tersedia.
5. Klik **Kirim** untuk memeriksa jawaban Anda.
6. Jika jawaban benar, Anda akan naik ke level berikutnya. Jika salah, Anda bisa mencoba lagi.
7. Setelah menyelesaikan semua level, total waktu penyelesaian Anda akan ditampilkan.

## Instalasi
Ikuti langkah-langkah berikut untuk menjalankan aplikasi di lokal:

1. **Clone Repository**
   ```bash
   git clone https://github.com/username/repository-name.git
   cd repository-name
   ```

2. **Buat dan Aktifkan Virtual Environment** (Opsional)
   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk macOS/Linux
   venv\Scripts\activate   # Untuk Windows
   ```

3. **Jalankan Aplikasi**
   ```bash
   streamlit run game.py
   ```

4. **Akses di Browser**
   Aplikasi dapat diakses melalui URL yang diberikan oleh Streamlit, biasanya `http://localhost:8501`.

## Struktur Proyek
```
project-folder/
├── game.py              # File utama aplikasi
├── README.md            # Dokumentasi proyek
```

## Dependensi
- **Python**: Versi 3.7 atau lebih baru
- **Streamlit**: Framework untuk antarmuka web
- **time**: Modul Python standar untuk pencatatan waktu

## Kontribusi
Kontribusi terbuka untuk pengembangan lebih lanjut. Jika ingin menambahkan fitur baru atau memperbaiki bug, silakan buat pull request di repository ini.

## Lisensi
Proyek ini dilisensikan di bawah [MIT License](LICENSE).

## Pembuat
- Muhammad Wildan Kamil - 140810220009
- Vernandika Stanley Hansen - 140810220031
- Adrian Jeremia Kurniawan - 140810220047

---
Selamat bermain dan semoga sukses memecahkan semua pesan terenkripsi!

