from flask import Flask, render_template




class APP:
    def __init__(self):
        self.app = Flask(__name__) 

    def get_app(self):
        return self.app
    
    def run(self):
        self.app.run()


