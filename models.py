def update_attrs(obj, updated_dict):
    updated_attrs = []
    for attribute, value in updated_dict.items():
        setattr(obj, attribute, value)
        updated_attrs.append(attribute)
    print(updated_attrs)


class User:
    def __init__(self, email, username, hashed_password, first_name, last_name, about_me,
                 photo=None, is_admin=False):
        self.email = email
        self.username = username
        self.hashed_password = hashed_password
        self.first_name = first_name
        self.last_name = last_name
        self.about_me = about_me
        self.photo = photo
        self.is_admin = is_admin
        self.blocked_users = []
        self.deleted = False

    def delete_account(self):
        self.deleted = True

    def update_account(self, updated_dict):
        update_attrs(self, updated_dict)

    def block_user(self, user):
        self.blocked_users.append(user)
        return self.blocked_users

    def __eq__(self, other):
        return self.email == other.email and self.username == other.username


class Tag:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.deleted = False

    def delete_tag(self):
        self.deleted = True

    def update_tag(self, updated_dict):
        update_attrs(self, updated_dict)


class Country:
    def __init__(self, name, geodata):
        self.name = name
        self.geodata = geodata
        self.deleted = False

    def delete_country(self):
        self.deleted = True


class Post:
    def __init__(self, title, text, created_at, hashtags, author, country):
        self.title = title
        self.text = text
        self.created_at = created_at
        self.hashtags = hashtags
        self.author = author
        self.country = country
        self.deleted = False

    def delete_post(self):
        self.deleted = True

    def update_post(self, updated_dict):
        update_attrs(self, updated_dict)


class Message:
    def __init__(self, message, sender, reciever, date):
        self.message = message
        self.sender = sender
        self.reciever = reciever
        self.date = date

    def update_message(self, message):
        self.message = message

    def __eq__(self, other):
        return self.message == other.message and self.reciever == other.reciever and self.date == other.date and self.sender == other.sender
