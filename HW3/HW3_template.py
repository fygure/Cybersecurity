"""
Program written by Max Chalitsios for COSC3371 HW3
PSID: 1808500
"""
import rsa
key_size = 2048

class Sender:
    #BEGIN SOLUTION
    def __init__(self, message):
        self.message = message
        self.keys = rsa.newkeys(2048)
        self.digest = None
        self.signature = None
        self.ciphertext = None
        
    def encrypt(self, receiver_pub_key):
        self.ciphertext = rsa.encrypt(self.message, receiver_pub_key)

    def sign(self):
        self.digest = rsa.compute_hash(self.message, 'SHA-1')
        self.signature = rsa.sign_hash(self.digest, self.keys[1], 'SHA-1')
    #END SOLUTION

class Receiver:
    #BEGIN SOLUTION
    def __init__(self):
        self.message = None
        self.keys = rsa.newkeys(2048)
        self.signature = None
        self.ciphertext = None

    def decrypt(self, ciphertext):
        self.message = rsa.decrypt(ciphertext, self.keys[1])

    def verify(self, signature, message, sender_pub_key):
        rsa.verify(message, signature, sender_pub_key)
    #END SOLUTION


if __name__ == "__main__":
    with open('message1.txt', 'rb') as file:
        plaintext = file.read()

    # =================PROBLEM 1=================
    # # Sender Side
    # # BEGIN SOLUTION
    receiver = Receiver()
    sender = Sender(plaintext)
    sender.encrypt(receiver.keys[0])
    print("Encrypted message: ", sender.ciphertext)
    sender.sign()
    print("Signature: ", sender.signature)
    # END SOLUTION

    # Receiver Side
    # BEGIN SOLUTION
    receiver.decrypt(sender.ciphertext)
    print("Decrypted message: ", receiver.message.decode())
    receiver.verify(sender.signature, receiver.message, sender.keys[0])
    print("Signature verified: ", receiver.message == sender.message)
    # # END SOLUTION
    
    # =================PROBLEM 2=================
    # position1 = 1 
    # position2 = 2  
    # switched_bytes = plaintext[:position1] + bytes([plaintext[position2]]) + plaintext[position1+1:position2] + bytes([plaintext[position1]]) + plaintext[position2+1:]
    # # Sender Side
    # receiver = Receiver()
    # # Generate the signature with the original plaintext
    # sender = Sender(plaintext)
    # sender.sign()
    # print("Signature: ", sender.signature)
    # # Change the message after it has been signed
    # sender.message = switched_bytes  
    # sender.encrypt(receiver.keys[0])
    # print("Encrypted message: ", sender.ciphertext)

    # # Receiver Side
    # receiver.decrypt(sender.ciphertext)
    # print("Decrypted message: ", receiver.message.decode())
    # try:
    #     receiver.verify(sender.signature, receiver.message, sender.keys[0])
    #     print("Signature verified: ", receiver.message == sender.message)
    # except rsa.VerificationError:
    #     print("Signature verification failed!")
        
        
    # =================PROBLEM 3=================
    # # Sender Side
    # sender = Sender(plaintext)
    # receiver = Receiver()  # Create an instance of Receiver
    # sender.encrypt(receiver.keys[0])  # Pass the public key of the receiver
    # sender.sign()

    # # Attack: Alter the signature by flipping a bit
    # modified_signature = sender.signature
    # modified_signature = modified_signature[:1] + bytes([modified_signature[1] ^ 1]) + modified_signature[2:]
    # print("Altered Signature: ", modified_signature)

    # # Receiver Side
    # receiver.decrypt(sender.ciphertext)
    # try:
    #     receiver.verify(sender.message, modified_signature, sender.keys[0])
    #     print("Signature verified: ", receiver.message == sender.message)
    # except rsa.VerificationError:
    #     print("Signature verification failed for altered signature!")
