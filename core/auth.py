from .model import Users, base
from .utils import Utils
from sqlalchemy.orm import sessionmaker



class Auth:

    def __init__(self):
        self.helper = Utils()
        self.db_engine = self.helper.connect_db()
        base.metadata.create_all(bind=self.db_engine)
        self.Session = sessionmaker(bind=self.db_engine)
        self.session = self.Session()
        self.__is_authenticated = False

    def create_user(self, cnic, username, password, education,experience,role,address):
        user = Users(cnic,username,password,role,address,education,experience)
        self.session.add(user)
        self.session.commit()