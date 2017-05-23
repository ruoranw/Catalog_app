import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Student(Base):
    # Set the date table which includes id, date
    __tablename__ = 'student'

    id = Column(Integer,primary_key=True)
    name = Column(String(80),nullable=False)


class Class(Base):
    __tablename__ = 'class'

    id = Column(Integer,primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    teacher = Column(String(80))
    student_id = Column(Integer, ForeignKey('student.id'))
    student = relationship(Student)




engine = create_engine('sqlite:///studentclass.db')


Base.metadata.create_all(engine)






