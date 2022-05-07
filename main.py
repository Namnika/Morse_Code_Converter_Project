MORSE_CODE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
    "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "--.", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.-.", "Z": "--..",
}


code_converter = input("Enter text to convert into Morse Code: ")

texts = []

def text():
    for letter in code_converter:
        letter = letter.upper()
        texts.append(MORSE_CODE[letter])  # add each value in a list

    # print(texts)

text()

resultant_text = " ".join(texts)
print(f"The Morse Code of '{code_converter}' is '{resultant_text}'")



