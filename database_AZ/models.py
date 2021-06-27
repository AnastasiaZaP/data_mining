from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)


Base = declarative_base()

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(2048), unique=True, nullable=False)
    title = Column(String, nullable=False, unique=False)
    author_id = Column(Integer, ForeignKey('author.id'), nullable=False)
    tag_id = Column(Integer, ForeignKey('tag.id'), nullable=False)
    author = relationship('Author', backref='posts')
    tag = relationship('Tag', backref='posts')

class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(2048), unique=True, nullable=False)
    name = Column(String, unique=False, nullable=False)

class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(2048), unique=True, nullable=False)
    name = Column(String, unique=False, nullable=False)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(2048), unique=True, nullable=False)
    name = Column(String, unique=False, nullable=False)