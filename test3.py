from Cryptodome.Cipher import DES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

def encrypt(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text.encode('utf-8'), 8)
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text

def decrypt(encrypted_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(encrypted_text)
    unpadded_text = unpad(decrypted_text, 8)
    return unpadded_text.decode('utf-8')

# Tạo khóa ngẫu nhiên
key = get_random_bytes(8)

# Mã hóa
plain_text = "TRUONG DAI HOC CONG NGHIEP HA NOI"
encrypted_text = encrypt(plain_text, key)
print("Encrypted text:", encrypted_text)

# Giải mã
decrypted_text = decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)