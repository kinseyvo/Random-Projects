# Message Decoder
def decode(message_file):
    # Reading the file
    f = open(message_file, "r")
    lines = f.readlines()

    # A dictionary to store words with their associated numbers
    words_dictionary = {}
    for line in lines:
        # Used split() to seperate ['1', 'opposite']
        parts = line.split()
        if len(parts) == 2:
            number, word = int(parts[0]), parts[1]
            words_dictionary[number] = word

    # Get the maximum number in the pyramid
    total = max(words_dictionary.keys())

    # Get and put all the words together
    decoded_string = ""
    for i in range(1, total + 1):
        decoded_string = decoded_string + ' ' + words_dictionary[i]

    # Remove leading space
    decoded_string = decoded_string.lstrip()

    return decoded_string

message_file = 'pyramid.txt'
decoded_message = decode(message_file)
print(decoded_message)