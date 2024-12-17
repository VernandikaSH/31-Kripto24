# Program Game Kriptografi dengan Shift Cipher dan Zigzag Cipher
# Muhammad Wildan Kamil - 140810220009
# Vernandika Stanley Hansen - 140810220031
# Adrian Jeremia Kurniawan - 140810220047

import time
import streamlit as st

# Fungsi Shift Cipher
def encrypt_shift_cipher(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

def decrypt_shift_cipher(text, shift):
    return encrypt_shift_cipher(text, -shift)

# Fungsi Zigzag Cipher
def encrypt_zigzag_cipher(text, depth):
    if depth == 1:
        return text
    rail = [''] * depth
    direction_down = False
    row = 0
    for char in text:
        rail[row] += char
        if row == 0 or row == depth - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1
    return ''.join(rail)

def decrypt_zigzag_cipher(cipher, depth):
    if depth == 1:
        return cipher
    
    n = len(cipher)
    rail = [['\n'] * n for _ in range(depth)]
    direction_down = None
    row, col = 0, 0

    for _ in range(n):
        if row == 0:
            direction_down = True
        if row == depth - 1:
            direction_down = False
        
        rail[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1

    idx = 0
    for i in range(depth):
        for j in range(n):
            if rail[i][j] == '*' and idx < len(cipher):
                rail[i][j] = cipher[idx]
                idx += 1

    result = []
    row, col = 0, 0
    for _ in range(n):
        if row == 0:
            direction_down = True
        if row == depth - 1:
            direction_down = False

        if rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1
        row += 1 if direction_down else -1

    return ''.join(result)

# Data Level
levels = [
    {"cipher": "Shift", "message": encrypt_shift_cipher("HELLO", 6), "key": 6},
    {"cipher": "Shift", "message": encrypt_shift_cipher("MY", 5), "key": 5},
    {"cipher": "Shift", "message": encrypt_shift_cipher("NAME", 9), "key": 9},
    {"cipher": "Shift", "message": encrypt_shift_cipher("IS", 7), "key": 7},
    {"cipher": "Zigzag", "message": encrypt_zigzag_cipher("BUDI", 2), "key": 2},
    {"cipher": "Zigzag", "message": encrypt_zigzag_cipher("WHAT", 3), "key": 3},
    {"cipher": "Zigzag", "message": encrypt_zigzag_cipher("ABOUT", 2), "key": 2},
    {"cipher": "Zigzag", "message": encrypt_zigzag_cipher("YOU", 3), "key": 3},
]

# Streamlit App
st.title("Game Kriptografi")
st.write("Selamat datang di game kriptografi! Pecahkan pesan terenkripsi untuk memenangkan permainan.")

# Inisialisasi State
if "game_started" not in st.session_state:
    st.session_state.game_started = False  # Game belum dimulai
if "level" not in st.session_state:
    st.session_state.level = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = None

# Tombol Start di Tampilan Awal
if not st.session_state.game_started:
    if st.button("Start"):
        st.session_state.game_started = True
        st.session_state.start_time = time.time()  # Mulai pencatatan waktu
        st.experimental_rerun()  # Refresh untuk memulai permainan
else:
    # Main Gameplay
    if st.session_state.level < len(levels):
        current_level = levels[st.session_state.level]
        st.write(f"### Level {st.session_state.level + 1}")
        st.write(f"**Tipe Cipher:** {current_level['cipher']}")
        st.write(f"**Pesan Terenkripsi:** {current_level['message']}")
        st.write(f"**Kunci:** {current_level['key']}")

        # Menggunakan st.form untuk input jawaban dan tombol
        with st.form(key=f"form_level_{st.session_state.level}"):
            user_answer = st.text_input("Masukkan jawaban Anda:", key="user_answer")
            submit_button = st.form_submit_button("Kirim")

        if submit_button:
            if current_level["cipher"] == "Shift":
                decrypted = decrypt_shift_cipher(current_level["message"], current_level["key"])
            elif current_level["cipher"] == "Zigzag":
                decrypted = decrypt_zigzag_cipher(current_level["message"], current_level["key"])

            if user_answer.upper() == decrypted:
                st.success("Jawaban benar!")
                st.session_state.level += 1
                st.experimental_rerun()  # Refresh untuk langsung ke soal berikutnya
            else:
                st.error("Jawaban salah. Coba lagi!")
    else:
        # Hitung waktu selesai
        end_time = time.time()
        total_time = end_time - st.session_state.start_time
        minutes, seconds = divmod(total_time, 60)
        
        st.write("### Selamat! Anda telah menyelesaikan semua level!")
        st.write(f"Total waktu yang dibutuhkan: {int(minutes)} menit {int(seconds)} detik")

        if st.button("Mulai Ulang"):
            st.session_state.game_started = False
            st.session_state.level = 0
            st.session_state.start_time = None
            st.experimental_rerun()  # Refresh untuk kembali ke halaman awal
