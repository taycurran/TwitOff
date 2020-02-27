from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class User(db.Model):
    """Twitter users that we analyze"""
    id = db.Column(db.BigInteger, primary_key=True)
    screen_name = db.Column(db.String(128), nullable=False)
    followers_count = db.Column(db.Integer)
    latest_tweet_id = db.Column(db.BigInteger)

class Tweet(db.Model):
    """Tweets we pull"""
    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'))
    full_text = db.Column(db.Unicode(400))
    embedding = db.Column(db.PickleType)
    
    user = db.relationship("User", backref=db.backref("tweets", lazy=True))