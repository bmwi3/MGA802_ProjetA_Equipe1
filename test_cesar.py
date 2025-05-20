if __name__=="__main__":
   
def cesar_encode(text, shift):
    """
    Encrypts the given text using Caesar cipher with the specified shift.
    
    Parameters:
    text (str): The text to be encrypted.
    shift (int): The number of positions to shift each letter.
    
    Returns:
    str: The encrypted text.
    """
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            # Shift character and wrap around the alphabet
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            # Non-alphabetic characters remain unchanged
            encrypted_text += char
    
    return encrypted_text

def cesar_decode(text, shift):
    """
    Decrypts the given text using Caesar cipher with the specified shift.
    
    Parameters:
    text (str): The text to be decrypted.
    shift (int): The number of positions to shift each letter.
    
    Returns:
    str: The decrypted text.
    """
    return cesar_encode(text, -shift)  # Decrypting is just encoding with negative shift