import base64


# --- Step 1: Caesar Cipher Brute-Force ---

def caesar_brute_force(ciphertext):
    """
    Performs a brute-force attack on a Caesar cipher by trying all possible shifts.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    print("--- Starting Caesar Cipher Brute-Force ---")
    print(f"Ciphertext: {ciphertext}\n")

    for shift in range(26):
        decrypted_text = ''
        for char in ciphertext:
            if char in alphabet:
                position = alphabet.find(char)
                new_position = (position - shift) % 26
                decrypted_text += alphabet[new_position]
            else:
                decrypted_text += char

        print(f"Shift {shift:2}: {decrypted_text}")
    print("\nCORRECT DECRYPTION FOUND AT SHIFT 21: 'rescue'")
    print("------------------------------------------\n")


# The ciphertext from the challenge
caesar_ciphertext = "mznxpz"
caesar_brute_force(caesar_ciphertext)

# --- Step 2: Solve the Anagram ---

# The anagram of "rescue" is "secure", a fundamental concept in cryptography.
passphrase = "secure"  # <--- THIS IS THE CORRECTED PASSPHRASE
print(f"--- Anagram Solution ---\nRecovered Passphrase: {passphrase}\n------------------------\n")


# --- Step 3: XOR Decryption ---

def xor_decrypt(ciphertext_bytes, key):
    """
    Decrypts a byte string using a repeating XOR key.
    """
    decrypted_bytes = bytearray()
    key_length = len(key)

    for i in range(len(ciphertext_bytes)):
        key_char = key[i % key_length]
        decrypted_byte = ciphertext_bytes[i] ^ ord(key_char)
        decrypted_bytes.append(decrypted_byte)

    return decrypted_bytes


# The Base64 encoded ciphertext from the challenge
base64_ciphertext = "Jw0KBlIMAEUXHRdFKyoxVRENEgkPEBwCFkQ="

print("--- Starting XOR Decryption ---")
print(f"Base64 Ciphertext: {base64_ciphertext}")
print(f"Using Passphrase: {passphrase}\n")

try:
    # 1. Decode the Base64 string into bytes
    decoded_ciphertext = base64.b64decode(base64_ciphertext)
    print(f"Decoded (bytes): {decoded_ciphertext}")

    # 2. Perform XOR decryption with the passphrase
    final_decrypted_message_bytes = xor_decrypt(decoded_ciphertext, passphrase)

    # Attempt to decode the final result as a UTF-8 string.
    final_message = final_decrypted_message_bytes.decode('utf-8', errors='replace')

    print(f"\nFinal Decrypted Message (bytes): {final_decrypted_message_bytes}")
    print(f"Final Decrypted Message (string): {final_message}")

except Exception as e:
    print(f"An error occurred: {e}")

print("-----------------------------\n")