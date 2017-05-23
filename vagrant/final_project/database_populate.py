from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Student, Class

engine = create_engine('sqlite:///studentclass.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

firstStudent = Student(name = "Johnny")
session.add(firstStudent)
session.commit()

classOne = Class(name="Math", description="The class Math contains methods for performing basic numeric operations such as the elementary exponential, logarithm, square root, and trigonometric functions.",
                 teacher="Ted", student=firstStudent)

session.add(classOne)
session.commit()

classTwo = Class(name="Spanish", description="The class teaches students how to speak Spanish.",
                 teacher="Lily", student=firstStudent)

session.add(classTwo)
session.commit()

classThree = Class(name="Biology", description="The class teaches nature science.",
                  teacher="Miller", student=firstStudent)



secondStudent = Student(name = "Sally")
session.add(secondStudent)
session.commit()

classOne = Class(name="DIY", description="The class makes students do stuff by their own.",
                 teacher="Alicia", student=secondStudent)

session.add(classOne)
session.commit()

classTwo = Class(name="psychology", description="The class teaches students the science of communication",
                 teacher="Ted", student=secondStudent)

session.add(classTwo)
session.commit()

classThree = Class(name="Biology", description="The class teaches nature science.",
                  teacher="Miller", student=secondStudent)

session.add(classThree)
session.commit()

# The 3rd student

thirdStudent = Student(name = "Sara")
session.add(thirdStudent)
session.commit()

classOne = Class(name="Biology", description="The class teaches nature science.",
                  teacher="Miller", student=thirdStudent)

session.add(classOne)
session.commit()

classTwo = Class(name="Spanish", description="The class teaches students how to speak Spanish.",
                 teacher="Lily", student=firstStudent)

session.add(classTwo)
session.commit()

classThree = Class(name="Biology", description="The class teaches nature science.",
                  teacher="Miller", student=secondStudent)

session.add(classThree)
session.commit()

print "added students and classes!"












