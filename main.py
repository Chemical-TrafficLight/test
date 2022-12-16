class Post():
    def __init__(self, nickname, time, message, like=None):
        self.nickname = nickname
        self.time = time
        self.like = like
        self.message = message

    def print_info(self):
        print(self.nickname, self.time, self.message, self.like)

    def add_like(self):
        print('Вы поставили лайк на пост!')

class Comment():
    def __init__(self, comment):
        self.comment = []

    def add_comment(self, comment):
        self.comment.append(Comment(comment))


post1 = Post('Kosmi', '12:25', 'Типа привет')
post1.print_info()
post1.add_like()

