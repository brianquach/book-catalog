"""
Copyright 2016 Brian Quach
Licensed under MIT (https://github.com/brianquach/udacity-nano-fullstack-catalog/blob/master/LICENSE)  # noqa
"""
from catalog import db


class User(db.Model):
    """User class represents a Catalog App user.

    Attributes:
        id: An integer of user's id.
        name: A string of user's name.
        email: A string of user's email address.
        picture: A string of URI to user's picture.
        catagory_items: A one-to-many relationship between User and
          CatagoryItems; contains a list of catagory_items created by user.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), nullable=False)
    email = db.Column(db.String(1000), nullable=False, unique=True)
    picture = db.Column(db.String(1000))
    catagory_items = db.relationship(
        'CatagoryItem',
        backref='user',
        lazy='dynamic'
    )

    def __init__(self, name, email, picture=None):
        """Initialize User.

        Args:
          name: user's name.
          email: user's email address.
          picture: URI to user's picture.
        """
        self.name = name
        self.email = email
        self.picture = picture

    def __repr__(self):
        """Represents User.

        Returns:
          A string that respresents the User object.
        """
        return '<User {0}>'.format(self.email)

    @property
    def serialize(self):
        """Serialize User object into a dictionary.

        Makes it easier to convert User class into json or xml form.

        Returns:
          A dictionary that holds key/value pairs that represent the User
          class.
        """
        return {
            'id': self.id,
            'name': self.name,
            'address': self.email,
            'picture': self.picture
        }


class Catagory(db.Model):
    """Catagory class represents a Catalog App catagory.

    Attributes:
        id: An integer of catagory's id.
        name: A string of catgory's name.
        catagory_items: A one-to-many relationship between a Catagory and
          CatagoryItem; contains a list of items grouped by the catagory.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    catagory_items = db.relationship(
        'CatagoryItem',
        backref='catagory',
        lazy='dynamic'
    )

    def __init__(self, name):
        """Initialize Catagory.

        Args:
          name: catagory's name.
        """
        self.name = name

    def __repr__(self):
        """Represents Catagory.

        Returns:
          A string that respresents the Catagory object.
        """
        return '<Catagory {0}>'.format(self.name)

    @property
    def serialize(self):
        """Serialize Catagory object into a dictionary.

        Makes it easier to convert Catagory class into json or xml form.

        Returns:
          A dictionary that holds key/value pairs that represent the Catagory
          class.
        """
        return {
            'id': self.id,
            'name': self.name,
            'items': [ci.serialize for ci in self.catagory_items]
        }


class CatagoryItem(db.Model):
    """CatagoryItem class represents a Catalog App item.

    Attributes:
      id: An integer of item's id.
      name: A string of item's name.
      author: A string of item's author (for books).
      description: A string of item's description.
      picture: A string of URI to item's picture.
      user_id: An integer of the user's id who created the item.
      catagory_id: An integer of the catagory that item belongs to.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), nullable=False)
    author = db.Column(db.String(1000), nullable=False)
    description = db.Column(db.Text)
    picture = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    catagory_id = db.Column(
        db.Integer,
        db.ForeignKey('catagory.id'),
        nullable=False
    )

    def __init__(self, name, author, catagory_id, description=None,
                 picture=None, user_id=None):
        """Initialize CatagoryItem.

        Args:
          name: name of item.
          author: author--for books--of item.
          description: description of item.
          picture: URI to picture of item.
          catagory_id: id of the catagory that the item belongs in.
          user_id: id of the user that created the item.
        """
        self.name = name
        self.author = author
        self.description = description
        self.picture = picture
        self.catagory_id = catagory_id
        self.user_id = user_id

    def __repr__(self):
        """Represents CatagoryItem.

        Returns:
          A string that respresents the CatagoryItem object.
        """
        return '<CatagoryItem {0}>'.format(self.name)

    @property
    def serialize(self):
        """Serialize CatagoryItem object into a dictionary.

        Makes it easier to convert CatagoryItem class into json or xml form.

        Returns:
          A dictionary that holds key/value pairs that represent the
          CatagoryItem class.
        """
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'description': self.description,
            'picture': self.picture
        }
