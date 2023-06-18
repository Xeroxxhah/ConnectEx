from sqlalchemy import create_engine, Column, ForeignKey, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from uuid import uuid4


base = declarative_base()



class Users(base):

    __tablename__ = 'users'

    cnic = Column('cnic', String, primary_key=True)
    username = Column('username', String)
    password = Column('password', String)
    gender = Column('gender', String)
    role = Column('role', String)
    address = Column('address', String)
    education = Column('education', String)
    experience = Column('experience', String)
    profile_pic_id = Column('profile_pic_id', String)


    def __init__(self, cnic, username, password, role, address, education, experience, profile_pic_id, gender):

        self.cnic = cnic
        self.username = password
        self.role = role
        self.gender = gender
        self.address = address
        self.education = education
        self.experience = experience