from cryptography.fernet import Fernet

class Encryter:


    def __init__(self):
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key) 



    
        