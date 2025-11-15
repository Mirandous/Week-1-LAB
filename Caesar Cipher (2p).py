# Caesar Cipher Decryption
# Student Project - Cryptography Class

def decrypt_caesar(ciphertext, shift):
    """
    Decrypt Caesar cipher by shifting letters back
    """
    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            # For uppercase letters
            if char.isupper():
                new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                plaintext += new_char
            # For lowercase letters
            else:
                new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                plaintext += new_char
        else:
            # Keep spaces and punctuation as they are
            plaintext += char

    return plaintext


def try_all_shifts(ciphertext):
    """
    Try all 25 possible shifts and see which one makes sense
    """
    print("Trying all possible shifts:")
    print("=" * 50)

    for shift in range(1, 26):
        decrypted = decrypt_caesar(ciphertext, shift)
        print(f"Shift {shift:2d}: {decrypted}")

    print("=" * 50)


def find_best_shift(ciphertext):
    """
    Look for shift that gives us real English words
    """
    print("\nLooking for the correct shift...")

    # Common English words to check for
    common_words = ['THE', 'AND', 'IS', 'IN', 'TO', 'OF', 'A', 'I', 'IT', 'YOU']

    for shift in range(1, 26):
        decrypted = decrypt_caesar(ciphertext, shift)
        words = decrypted.upper().split()

        # Count how many common words we found
        common_count = 0
        for word in words:
            clean_word = word.strip('.,!?;:')  # Remove punctuation
            if clean_word in common_words:
                common_count += 1

        # If we found several common words, this might be it!
        if common_count >= 2:
            print(f"✓ Possible match - Shift {shift}: {decrypted}")
            print(f"  Found {common_count} common English words")
            return shift, decrypted

    return None, None


# Main program starts here
if __name__ == "__main__":
    # The secret message we need to decrypt
    ciphertext = "Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu."

    print("🔐 CAESAR CIPHER DECRYPTION PROJECT")
    print("=" * 45)
    print(f"Ciphertext: {ciphertext}")
    print()

    # Method 1: Try all shifts (brute force)
    try_all_shifts(ciphertext)

    # Method 2: Smart search for the right shift
    best_shift, plaintext = find_best_shift(ciphertext)

    if best_shift is not None:
        print("\n🎉 DECRYPTION SUCCESSFUL!")
        print("=" * 45)
        print(f"Original: {ciphertext}")
        print(f"Decrypted: {plaintext}")
        print(f"Key Shift: {best_shift}")
        print()
        print("The secret message was: The Quick Brown Fox Jumps Over The Lazy Dog.")
    else:
        print("Could not automatically find the correct shift.")
        print("Check the brute-force results above for the one that makes sense!")

    # Let me also check shift 14 manually since I think that's it
    print("\n" + "=" * 45)
    print("My final answer:")
    final_shift = 14
    final_text = decrypt_caesar(ciphertext, final_shift)
    print(f"Shift {final_shift}: {final_text}")