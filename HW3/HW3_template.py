# This is the template for Problem 1 only.
# For problems 2 and 3, keep the class definitions
# the same and rewrite the main program
import rsa
# import sys
# print(sys.executable)
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
    # initialize sender and receiver objects with 2048 key_size

    # Sender Side
    # BEGIN SOLUTION
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
    # END SOLUTION

