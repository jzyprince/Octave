import os
import jinja2

from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '../templates')),
                                       extensions=['jinja2.ext.autoescape'],
                                       autoescape=True)

class Media(ndb.Model):
    views = ndb.IntegerProperty()
    link = ndb.StringProperty()
    media_type = ndb.StringProperty()
    date_created = ndb.StringProperty()
    media_nbr = ndb.IntegerProperty()
    upload_check=ndb.BooleanProperty()
    key_media = ndb.BlobKeyProperty()


class Tag(ndb.Model):
    name = ndb.StringProperty()
    media_names = ndb.StringProperty(repeated=True) #construct entities later from the name string

class User(ndb.Model):
    email = ndb.StringProperty()
    city = ndb.StringProperty()
    name = ndb.StringProperty()
    signature = ndb.StringProperty()
    role = ndb.StringProperty()
    profile_image= ndb.BlobProperty()
    followers = ndb.StringProperty(repeated=True) #Their emails
    shared_posts = ndb.KeyProperty(repeated=True)

class Post(ndb.Model):
    date = ndb.DateTimeProperty(auto_now_add=True)
    date_created = ndb.StringProperty()
    text = ndb.StringProperty()
    tags = ndb.StringProperty(repeated=True) # construct entities from the strings
    blob_key_media = ndb.BlobKeyProperty()
    user_key = ndb.KeyProperty()
    likes = ndb.IntegerProperty()

class Like(ndb.Model):
    user_key = ndb.KeyProperty(kind=User)
    post_key = ndb.KeyProperty(kind=Post)

class Reply(ndb.Model):
    date = ndb.DateTimeProperty(auto_now_add=True)
    user_key = ndb.KeyProperty(kind=User)
    reply = ndb.TextProperty()
    date_reply = ndb.StringProperty()
    post_key = ndb.KeyProperty(kind=Post)

class Playlist(ndb.Model):
    name = ndb.StringProperty()
    user_key = ndb.KeyProperty()
    key_media = ndb.BlobKeyProperty(repeated=True)
    privacy = ndb.StringProperty()
    date_created = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
    links = ndb.StringProperty(repeated=True)
    cover_url= ndb.StringProperty()
    upload_check=ndb.BooleanProperty()


class Artist(ndb.Model):
    user = ndb.StructuredProperty(User,repeated=False)
    cities_ad = ndb.StringProperty(repeated=True)
    users_to_share = ndb.IntegerProperty()