from flask import Flask, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Column, Integer, String


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:apisbtest0011@192.168.99.100/api_test'
db = SQLAlchemy(app)


Base = automap_base()
class MyProduct(Base):
    __tablename__ = 'api_product'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    description = Column(String)    

    @property
    def serialize(self):
       return {
           'id'     : self.id,
           'name'   : self.name,
           'category'  : self.category,
           'description' : self.description
       }

Base.prepare()



@app.route("/api/")
def getProductList():
    return jsonify(json_list=[i.serialize for i in db.session.query(MyProduct).all()])


if __name__ == '__main__':
    app.debug = 'True'
    app.run()
