import re

def problem1():
    cipher_text = "ROYQWH KQXXJYQ: N LQGNQAQ HDJH FO. VW NX J KQKLQO VZ J XQMOQH MONKQ VOYJWNSJHNVW MJGGQF U.D.J.W.H.V.K., IDVXQ YVJG NX HVHJG IVOGF FVKNWJHNVW. HDQNO UGJW NX HV JMBRNOQ J XRUQOIQJUVW JWF HV DVGF HDQ IVOGF OJWXVK. N JK JZOJNF HDJH IQ FV WVH DJAQ KRMD HNKQ LQZVOQ HDQT XRMMQQF.\nN DJAQ OQMQWHGT NWHQOMQUHQF JW QWMOTUHQF KQXXJYQ (JHHJMDKQWH MNUDQO2.HCH) HDJH IJX XQWH LT FO. VW HV VWQ VZ DNX MVWXUNOJHVOX, HDQ NWZJKVRX KO. LGVIZNQGF. N KJWJYQF HV FNXMVAQO HDJH HDQ KQXXJYQ IJX QWMOTUHQF RXNWY HDQ PJMEJG MNUDQO (XQQ XVROMQ MVFQ), LRH N IJX WVH JLGQ FNXMVAQO HDQ XQMOQH EQT, JWF HDQ MNUDQO XQQKX HV LQ RWLOQJEJLGQ. N JK JZOJNF HDJH FQMOTUHNWY HDNX KQXXJYQ NX HDQ VWGT IJT HV XHVU FO. VW'X VOYJWNSJHNVW.\nUGQJXQ XQWF OQNWZVOMQKQWHX NKKQFNJHQGT! N HONQF HV JMH MJRHNVRXGT, LRH N DJAQ J ZQQGNWY HDJH FO. VW'X DQWMDKQW JOQ VWHV KQ. N FVW'H EWVI DVI GVWY N DJAQ LQZVOQ HDQT FNXMVAQO KT OQJG NFQWHNHT JWF KT XQMOQH DNFNWY UGJ"
    # BEGIN SOLUTION
    sorted_frequency = {}
    
    def display_message_frequency(cipher_text):
        nonlocal sorted_frequency
        try:
            letter_frequency = {}
            for char in cipher_text:
                if char.isalpha():
                    if char in letter_frequency:
                        letter_frequency[char] += 1
                    else:
                        letter_frequency[char] = 1

            #print(letter_frequency)
            #print()
            #print(len(cipher_text))

            total_characters = len(cipher_text)

            #descending order
            sorted_frequency = sorted(letter_frequency.items(), key=lambda x: x[1], reverse=True)

            #displaying
            for letter, count in sorted_frequency:
                percentage = (count / total_characters) * 100
                print(f"{letter}: {count} ({percentage:.2f}%)")

        except FileNotFoundError:
            print(f"Error.")
        
    def save_decrypted_message(decrypted_message, file_path):
        nonlocal sorted_frequency
        with open(file_path, 'w') as file:
            file.write("Letter Frequency in Cipher Text:\n")
            file.write("-----------------------------\n")
            for letter, count in sorted_frequency:
                file.write(f"{letter}: {count}\n")
            file.write("-----------------------------\n")
            file.write("Decrypted message:\n")
            file.write("-----------------------------\n")
            file.write(decrypted_message)

    def display_message(encrypted_message, decrypted_message):
        print("Encrypted Message:")
        print(encrypted_message)
        print("\nDecrypted Message:")
        print(decrypted_message)
    
    def decrypt(message, decryption_mapping):
        decrypted_message = ''.join(decryption_mapping.get(char, char) for char in message)
        return decrypted_message
    
    display_message_frequency(cipher_text)
    decryption_mapping = {}
    while True:
        decrypted_message = decrypt(cipher_text, decryption_mapping)
        display_message(cipher_text, decrypted_message)

        user_input = input("\nEnter a substitution (e.g., 'a=b', 'x=y') or type 'exit' to finish: ").strip()

        if user_input.lower() == 'exit':
            break

        try:
            substitution_pair = user_input.split('=')
            encrypted_char, decrypted_char = substitution_pair[0].strip(), substitution_pair[1].strip()
            decryption_mapping[encrypted_char] = decrypted_char
        except (ValueError, IndexError):
            print("Invalid input. Please provide a valid substitution pair.")
    
    save_decrypted_message(decrypted_message, 'decrypted.txt')
    print("Decrypted message saved to 'decrypted.txt'.")

    # END SOLUTION


def JACKAL_Decrypt(firstKeyByte, secondKeyByte, cipherText):
# returns a plaintext bytearray 
    x = (firstKeyByte + 31)
    y = (secondKeyByte * 3)
    p = []
    for z in range(len(cipherText)):
        x = (x + 29) & 0xFF
        y = (y * 19) & 0xFF
        p.append(cipherText[z] ^ x ^ y)
    return bytearray(p)

def isEnglishText(byte):
    punctuations = ".,'-:{}"
    try:
        for char in byte.decode('utf-8'):
            if not (char.isalnum() or char.isspace() or char in punctuations):
                return False
    except UnicodeDecodeError as e:
        return False
    return True

def problem2():
    with open("cipher2.txt", "rb") as file:
        cipherText = file.read()
    # BEGIN SOLUTION
    # plainText = ....
    print(cipherText)
    
    # END SOLUTION
    #print(plainText.decode())


def problem3():
    with open("cipher3.txt", "rb") as file:
        cipher_text = file.read()
    # BEGIN SOLUTION

    # END SOLUTION
    #print(plain_text.decode('utf-8'))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n\nProblem 1 \n\n")
    problem1()
    # print("\n\nProblem 2 \n\n")
    # problem2()
    #print("\n\nProblem 3 \n\n")
    #problem3()