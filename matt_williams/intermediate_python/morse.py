

class EnglishMessage:
	def __init__(self, message,):
			self.message = message
			self.letter_to_morse = {
    'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 
    'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 
    'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
    'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
    '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
    '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', ' ':'/'
}
	

	def encode(self):
		morse = []

		for letter in self.message:
			letter = letter.lower()
			morse_letter = self.letter_to_morse[letter]
			morse.append(morse_letter)

			morse_message = " ".join(morse)
    
			return morse_message


# We need to invert the dictionary. This will create a dictionary
# that can go from the morse back to the letter
class MorseMessage:
	def __init__(self, message):
		self.message = message
		letter_to_morse = {
    'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 
    'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 
    'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
    'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
    '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
    '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', ' ':'/'
}
		self.morse_to_letter = {}
		for letter in letter_to_morse:
			morse = letter_to_morse[letter]
			self.morse_to_letter[morse] = letter



	def decode(self):
		english = []

    # Now we cannot read by letter. We know that morse letters are
    # separated by a space, so we split the morse string by spaces
		morse_letters = self.message.split(" ")

		for letter in morse_letters:
			english_letter = self.morse_to_letter[letter]
			english.append(english_letter)

    # Rejoin, but now we don't need to add any spaces
		english_message = "".join(english)
    
		return english_message
