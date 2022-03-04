import morse

message = "SOS We have hit an iceberg and need help quickly"

encoded_message = morse.encode(message)

print(f"Incoming message: {message}")
print(f"   Morse encoded: {encoded_message}")
