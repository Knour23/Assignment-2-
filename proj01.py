def decrypt_caesar_cipher():
    # Step 1: Read the ciphertext from file
    words = ""
    try:
        with open("cipherText.txt", 'r') as file:
            for line in file:
                words += line.strip()  # Remove trailing spaces or newlines
    except FileNotFoundError:
        print("Error: 'cipherText.txt' not found.")
        return

    # Step 2: Count occurrences of each letter (ignore spaces)
    letter_counts = [0] * 26  # List to count occurrences of each letter (a-z)
    for char in words:
        if char.isalpha():  # Count only alphabetic characters
            index = ord(char.lower()) - ord('a')
            letter_counts[index] += 1

    # Step 3: Find the most common letter
    most_common_count = max(letter_counts)
    most_common_index = letter_counts.index(most_common_count)
    most_common_letter = chr(most_common_index + ord('a'))

    # Step 4: Calculate the shift assuming the most common letter maps to 'E'
    shift = (most_common_index - (ord('e') - ord('a'))) % 26
    print(f"Most common letter: {most_common_letter.upper()}, Shift: {shift}")

    # Step 6: Decode the message using the shift
    decoded_message = ""
    for char in words:
        if char == ' ':  # Preserve spaces
            decoded_message += char
        elif char.isalpha():  # Decode alphabetic characters
            index = ord(char.lower()) - ord('a')
            shifted_index = (index - shift) % 26
            decoded_char = chr(shifted_index + ord('a'))
            # Preserve the case (upper or lower)
            decoded_message += decoded_char.upper() if char.isupper() else decoded_char

    # Output the decoded message
    print("Decoded message:", decoded_message)


# Call the function
decrypt_caesar_cipher()
