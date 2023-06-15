from Post import Post
from Comment import Comment
class User:
    def __init__(self,id, username, email, pasword,):
        self.id        = id
        self.username  = username
        self.email     = email
        self.pasword   = pasword
        
        self.posts = []
        self.comments = []
    def __str__(self):
        return f"User ({self.id})\n{self.username}\n"
    
    def addPost (self, postid, posttitle, postbody ):
        post = Post(postid, posttitle, postbody,self)
        self.posts.append(post)
        return post
    
    def addComment (self, comment_id, comment_body, post):
        comment = Comment(comment_id, comment_body, post, self)
        self.comments.append(comment)
        post.comments.append(comment)

    def removePost (self,post_id):
        for post in self.posts:
            if post.id == post_id:
                self.posts.remove(post)
                print("Post was removed successfully")
    
    def removeComment(self, comment_id):
        for comment in self.comments:
             if comment.id == comment_id:
                self.comments.remove(comment)
                print("Comment was removed successfully")

