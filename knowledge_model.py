from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):

   __tablename__ = 'students'
   series_id = Column(Integer, primary_key=True)
   name = Column(String)
   rating = Column(Integer)
   craziness = Column(Boolean)

   def __repr__(self):
		if self.rating >7:
   			return("if you want to learn about: {} \n"
              		 "you should look at Wikipedia article called: {} \n"
              		 "We gave this article a rating of: {}"
              		 " out of 10").format(self.name, self.name, self.rating)
   		else:
			return("unfortunately, this article does not have a better rating. Maybe, this is an article that should be repaced soon!"
        		"it got a: {}"
        		" out of 10 ").format(self.rating)
               





	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

	