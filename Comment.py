class Comment:
    def __init__(self,id,body,author, post):
        self.id    = id        
        self.body  = body
        
        self.author = author      
        self.post = post

    def __str__(self):
        return f"Author({self.author}) Post({self.post})\n Coment{self.id}\n {self.body}\n"
