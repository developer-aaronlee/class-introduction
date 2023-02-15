class User:
    def __init__(self, userid, username):
        self.userid = userid
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1

user_1 = User(1, "a")
user_2 = User(2, "b")
user_3 = User(3, "c")

print(user_1.userid)

user_3.follow(user_2)
print(user_2.follower)
print(user_2.following)
print(user_3.follower)
print(user_3.following)