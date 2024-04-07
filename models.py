from sqlalchemy import boolean, Column, Integer, String,CheckConstraint
from database import Base
special_chars_regex = r"[^\w\s]"  

class User(Base):
    tablename='studentusers'
    id=Column(Integer, primary_key=True, index=True)
    username=Column(String(50), unique=True)
    emailid=Column(String(70),unique=True)
    pwd = Column(String(128), nullable=False)
    pwd_constraint = CheckConstraint("length(pwd) >= 12 AND (pwd REGEXP :special_chars_regex IS NOT NULL) AND (pwd REGEXP '[A-Z]' IS NOT NULL)", deferrable=True, name="pwd_complexity")


class Emp(Base):
    tablename='employeeusers'
    eid=Column(Integer, primary_key=True, index=True)
    eusername=Column(String(50), unique=True)
    eemailid=Column(String(70),unique=True)
    epwd = Column(String(128), nullable=False)
    epwd_constraint = CheckConstraint("length(epwd) >= 12 AND (epwd REGEXP :special_chars_regex IS NOT NULL) AND (epwd REGEXP '[A-Z]' IS NOT NULL)", deferrable=True, name="epwd_complexity")