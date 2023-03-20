from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = "postgresql://root:56HkUXLG8OH2sM7lCwomcCK6BKj25LbT@dpg-cfgke202i3mg6pdqrutg-a.frankfurt-postgres.render.com/testdb2_jwe2"

engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
