class Comment:
    def __init__(self,id,body,author_id, post_id):
        self.id    = id        
        self.body  = body
        
        self.author_id = author_id        
        self.post_id = post_id

    def __str__(self):
        return f"Author({self.author_id}) Post({self.post_id})\n Coment{self.id}\n {self.body}\n"
