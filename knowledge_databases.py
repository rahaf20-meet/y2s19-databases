from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_series(name, rating, craziness):
    series_object = Knowledge(
        name=name,
        rating=rating,
        craziness=craziness)
    session.add(series_object)
    session.commit()

# add_series("Gumball", 9, True)

def query_all_articles():
	series = session.query(Knowledge).all()
  	return series

print(query_all_articles())

def delete_article_by_topic(name):
	session.query(Knowledge).filter_by(
    name=name).delete()
   	session.commit()

def delete_all_articles():
	session.query(Knowledge).delete()
   	session.commit()

# delete_all_articles()
# print(query_all_articles())

def edit_article_rating(update_rating,name):
	series_object = session.query(Knowledge).filter_by(name=name).first()
	series_object.rating = update_rating
	session.commit()

edit_article_rating(8,"cukur")

print(query_all_articles())
