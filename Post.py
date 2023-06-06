class Post:
    def __init__(self, id, title,body,author_id):
        self.id = id
        self.title = title
        self.body = body

        self.author_id = author_id
    
    def __str__(self):
        return f"Post({self.id})\n{self.title}\n{self.body} ({self.author_id})\n"