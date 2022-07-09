## Task - Using SQL Database

1. Create a token when user logged in and token should be valid for 2 minutes.
2. The API's request should only be accepted when the token is valid.
3. User will make request to a particular endpoint like ('/summary') then increase the token expiry time by 3 minutes.
4. For normal endpoint like ('/details) just check the token validity.

## To run the backend server

```
python3 server/server.py
```

## Encrypt and Decrypt Strings in Python [Link!](https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/)

### Encryption:

Encryption is the process of encoding the data. i.e converting plain text into ciphertext. This conversion is done with a key called an encryption key.

### Decryption:

Decryption is the process of decoding the encoded data. Converting the ciphertext into plain text. This process requires a key that we used for encryption.

We require a key for encryption. There are two main types of keys used for encryption and decryption. They are Symmetric-key and Asymmetric-key.

Symmetric-key Encryption:

In symmetric-key encryption, the data is encoded and decoded with the same key. This is the easiest way of encryption, but also less secure. The receiver needs the key for decryption, so a safe way need for transferring keys. Anyone with the key can read the data in the middle.

##  Problem Occured During Token Check
- Token Validation Is Incorrect