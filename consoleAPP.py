from User import User
from Post import Post
from Comment import Comment

u1 = User(1, "Ion","a.verlan@mail.ru","123456")
u2 = User(2, "Ivan","i.ven@mail.ru","12345622")

#p1 = Post(1,"Wonderful","This is body text ",1)
#p2 = Post(2,"Succes","This is body text ",1)
p3 = Post(3,"Hey Hello","This is body text ",2)

c1 = Comment(1,"This is wonderful picture",1,1)
c2 = Comment(2,"Thak You",2,1)
c3 = Comment(1,"You are so preety",2,2)
c4 = Comment(2,"Thaks you too!",1,2)

print(u1)
print(u2)

#print(p1)
#print(p2)


print(c1)
print(c2)
print(c3)
print(c4)