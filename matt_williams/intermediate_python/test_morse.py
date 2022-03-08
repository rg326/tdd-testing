#import morse

#message = "hello everyone"

#code = morse.encode(message)
#decoded = morse.decode(code)

#print(message == decoded)

from morse import EnglishMessage, MorseMessage

message_string = 'hello world'
message = EnglishMessage(message_string)

code_string = message.encode()
code = MorseMessage(code_string)
decoded = code.decode()

print(message_string)
print(code)
print(decoded)
print(decoded == message_string)
