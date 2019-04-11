def create_all_tables():
    from models.base import create_all
    create_all()

if __name__ == '__main__':

    create_all_tables()