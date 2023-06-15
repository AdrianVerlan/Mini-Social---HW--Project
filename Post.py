class Post:
    def __init__(self, id, title,body,author):
        self.id = id
        self.title = title
        self.body = body

        self.author = author
        self.comments = []
    
    def __str__(self):
        return f"Post({self.id})\n{self.title}\n{self.body} ({self.author})\n"