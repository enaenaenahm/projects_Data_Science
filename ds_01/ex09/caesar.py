import sys

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encode' else -shift
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char
    return result

def main():
    if len(sys.argv) != 4:
        raise ValueError("Invalid number of arguments. Usage: python script.py <encode/decode> <text> <shift>")
    mode = sys.argv[1]
    text = sys.argv[2]
    try:
        shift = int(sys.argv[3])
    except ValueError:
        raise ValueError("Shift must be an integer")
    if mode not in ['encode', 'decode']:
        raise ValueError("Invalid mode. Use 'encode' or 'decode'")
    try:
        output = caesar_cipher(text, shift, mode)
        print(output)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()