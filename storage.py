class UserStorage:

    def __init__(self):
        self.users = []

    def add_user(self, user):
        try:
            user_ind = self.users.index(user)
            print('User already exists.')
        except ValueError:
            self.users.append(user)
            print('User is added.')

    def delete_user(self, user, mode):
        try:
            user_ind = self.users.index(user)
            password = input('write user password')
            if password == user.hashed_password:
                if mode == 't':
                    user.delete_account()
                    print('Deleted user account temporarily')
                elif mode == 'p':
                    self.users.remove(user)
                    print('Deleted user account permanently')
                else:
                    raise ValueError('Incorrect mode')
            else:
                print('Incorrect password. User not deleted.')
        except ValueError:
            print('User does not exist.')


class TagStorage:
    def __init__(self):
        self.tags = []

    def add_tag(self, tag):
        try:
            tag_ind = self.tags.index(tag)
            print('tag already exists.')
        except ValueError:
            self.tags.append(tag)
            print('tag is added.')

    def delete_tag(self, tag):
        try:
            tag_ind = self.tags.index(tag)
            self.tags.remove(tag)
            print('tag deleted')
        except ValueError:
            print('tag does not exist.')


class CountryStorage:
    def __init__(self):
        self.countries = []

    def add_country(self, country):
        self.countries.append(country)
        print('country added')


class PostStorage:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print('post added')

    def delete_post(self, post):
        try:
            post_ind = self.posts.index(post)
            self.posts.remove(post)
            print('post deleted')
        except ValueError:
            print('Post does not exist.')


class MessageStorage:
    def __init__(self):
        self.messages = []

    def add_message(self, message):
        if message.sender in message.reciever.blocked_users:
            print('you are blocked')
        else:
            self.messages.append(message)

    def delete_message(self, message):
        try:
            message_ind = self.messages.index(message)
            self.messages.remove(message)
            print('message deleted')
        except ValueError:
            print('message does not exist')
