# Cäser-Verschiebung // Cäsar-Algorhythmus / Cäser-Chiffre

msg = 'PYTHONIC'
key = 1
secret_msg = ''

# Nachricht Verschlüsseln
for char in msg:
    if not char.isalpha(): # Prüfung ob Buchstabe
            continue
    char = char.upper() # covert in upper case
    code = ord(char) + key #Zahl zum Zeichen zurückgeben
    if code > ord('Z'): # wenn größer als Z
        code = ord('A') # Dann A draus machen

    secret_msg += chr(code)
print(secret_msg)


# Nachricht entschlüsseln
msg = ''
for char in secret_msg:
    if not char.isalpha(): # Prüfung ob Buchstabe
            continue
    char = char.upper() # covert in upper case
    code = ord(char) - key #Zahl zum Zeichen zurückgeben
    if code < ord('A'): # wenn kleiner als A
        code = ord('Z') # Dann Z draus machen

    msg += chr(code)
print(msg)
