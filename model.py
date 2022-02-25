from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#USUARIO = "root"
#SENHA = "Userroot!"
#HOST = "localhost"
#PORT = 3308
#BANCO = "cadastro_e_login"

CONN = "sqlite:///projeto2.db"
#CONN = f"mysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"
engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = "Pessoa"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    email = Column(String(200))
    senha = Column(String(100))
    
Base.metadata.create_all(engine)