from sqlalchemy import create_engine



class Utils:

    def __init__(self):
        pass 

    def connect_db(self):
        self.host = 'your_host'
        self.port = 'your_port'
        self.user = 'your_username'
        self.password = 'your_password'
        self.database = 'your_database_name'
        self.connection_string = f'mysql+mysqlconnector://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'
        self.engine = create_engine(self.connection_string)

        return self.engine


