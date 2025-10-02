from cryptography.fernet import Fernet


class Encryter:

    def encryptFile(filename):
        key = Fernet.generate_key()
        fernet_lock = Fernet(key)

        with open(filename,"rb") as file:
            plain_text = file.read()
        cipher_text = fernet_lock.encrypt(plain_text)

        with open(filename, "wb") as e_file:
            e_file.write(cipher_text)
            
            


    def encryptImg():
        pass


