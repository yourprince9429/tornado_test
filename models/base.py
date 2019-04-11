from models import Base,engine

def create_all():
    Base.metadata.create_all(bind=engine)
