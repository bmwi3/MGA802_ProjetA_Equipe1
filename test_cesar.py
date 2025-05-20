def encode_cesar(text, shift):
    encoded_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encoded_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encoded_text += char
    return encoded_text


def decode_cesar(text, shift):
    return encode_cesar(text, -shift)

def brute_force_cesar(text):
    best_guess = ""
    best_score = 0
    for shift in range(26):
        decoded_text = decode_cesar(text, shift)
        score = sum(1 for char in decoded_text if char.isalpha())
        if score > best_score:
            best_score = score
            best_guess = decoded_text
    return best_guess