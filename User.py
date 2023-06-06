class User:
    def __init__(self,id, username, email, pasword,):
        self.id        = id
        self.username  = username
        self.email     = email
        self.pasword   = pasword
        
    def __str__(self):
        return f"User ({self.id})\n{self.username}\n{self.email}\n"