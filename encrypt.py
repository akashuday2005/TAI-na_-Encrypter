from cryptography.fernet import Fernet;
import sqlite3

class Encryption:

    @staticmethod
    def encrytion(file_path):

        # generate fernet key..
        key = Fernet.generate_key()
        fernet = Fernet(key)

        # reads file
        with open(file_path, "rb") as files:
            plaintext = files.read()
        
        # encrypt the data
        cypertext = fernet.encrypt(plaintext)

        # write encrypted data into file
        with open(file_path, "wb") as files:
            files.write(cypertext)

        
        Encryption.store_key(file_path, key)  



    # storing keys into database
    @staticmethod
    def store_key(file_path, key):
        conn = sqlite3.connect("keys.db")
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO Keys (file_name, key_value) VALUES (? , ?)",(file_path,key.decode()))  
        conn.commit()
        conn.close()

    
    @staticmethod
    def fetch_key(file_path):
        conn = sqlite3.connect("keys.db")
        cursor = conn.cursor()
        cursor.execute("SELECT key_value FROM KEYS WHERE file_name = ?",(file_path,))
        row = cursor.fetchone() # query row result stored as tuple

        # select key_value from the tuple
        if row: 
           return row[0].encode()

        # if row is None return error
        else:
            raise ValueError("No key found for particular File..")



    @staticmethod
    def decrytion(file_path):

        # fetching key from dataBase using static function
        key = Encryption.fetch_key(file_path)
        fernet = Fernet(key)

        # Reading file..
        with open(file_path,"rb") as file:
            cipher_text = file.read()


        # Decrypt
        plain_text = fernet.decrypt(cipher_text)

        # Writing into file..
        with open(file_path,"wb") as file:
            file.write(plain_text)


