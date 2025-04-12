# OOP

class User:
    def __init__(self, id, username, followers = 0):
        self.id = id
        self.username = username
        self.followers = followers
        self.following = 0

    def login(self):
        print("User {1} logged in")

    def follow(self, user):
        user.followers += 1
        self.following += 1



user_web = User("1f3g8a", "gdpp")
print(user_web.username)

user_mobile = User("a23ff4", "less")
user_mobile.follow(user_web)

print(user_web.followers)
print(user_mobile.following)