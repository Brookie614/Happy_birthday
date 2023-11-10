def encode_decode(message, key, mode='encode'):
    if not message:  # Checks if the message is None or empty
        return ""

    result = ""
    for i in range(len(message)):
        char = message[i]
        # Encrypt or decrypt the character based on mode
        if char.isupper():
            if mode == 'encode':
                result += chr((ord(char) + key - 65) % 26 + 65)
            else:
                result += chr((ord(char) - key - 65) % 26 + 65)
        elif char.islower():
            if mode == 'encode':
                result += chr((ord(char) + key - 97) % 26 + 97)
            else:
                result += chr((ord(char) - key - 97) % 26 + 97)
        else:
            result += char

    return result
# Secret message
secret_message = "నా ప్రియతమా, నీ పుట్టిన రోజున అభినందనలు! నీకు ఎంతో ప్రత్యేకమైన ఈ రోజున, నా జీవితంలో నీ స్థానం ఎంతో గొప్పది అని నీకు తెలియజేయాలని ఉంది. నా చీకటి రోజులను నీ నవ్వు వెలుగులో ముంచెత్తింది, నీ ప్రేమ నా హృదయపు తాళం తో సరిపోల్చుకుంది. నీవు నా ప్రేమికుడు మాత్రమే కాదు, నా ఉత్తమ మిత్రుడు, నా రహస్యాల భాగస్వామి, మరియు నా అతిపెద్ద సాహసం. ఈ రోజు, నేను నిన్ను, మనం పంచుకున్న ప్రేమను, మరియు మనం కలిసి సృష్టించిన అందమైన క్షణాలను జరుపుకుంటున్నాను. ఇంకా చాలా సంవత్సరాలు ప్రేమ, నవ్వులు, మరియు జ్ఞాపకాలు సృష్టించడానికి ఇది ఒక ప్రారంభం. జన్మదినం శుభాకాంక్షలు, నా ప్రియతమా!"

# Convert
date_key = '9172022' 
key = sum([int(digit) for digit in date_key])

# Encode the message
encoded_message = encode_decode(secret_message, key)

# Loop until the correct key is entered
while True:
    try:
        input_key = int(input("Enter the key to decode the message: "))
        if input_key == key:
            decoded_message = encode_decode(encoded_message, input_key, mode='decode')
            print("Decoded Message: ", decoded_message)
            break  # Exit the loop if the key is correct
        else:
            print("Incorrect key. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numerical key.")