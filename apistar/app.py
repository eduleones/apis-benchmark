from typing import List
from apistar import App, Route, types, validators
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base

from apistar_sqlalchemy.components import SQLAlchemySessionComponent
from apistar_sqlalchemy.event_hooks import SQLAlchemyTransactionHook
from apistar_sqlalchemy import database


# Model
Base = automap_base()
class MyProduct(database.Base):
    __tablename__ = 'api_product'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    description = Column(String)    

Base.prepare()

class MyProductType(types.Type):
    id = validators.Integer(allow_null=True, default=None)
    name = validators.String()
    category = validators.String()
    description = validators.String()


# View
def get_products(session: Session) -> List[MyProductType]:
    return [MyProductType(product) for product in session.query(MyProduct).all()]



# Routes
routes = [
    Route('/api/', 'GET', get_products),
]


components = [
    SQLAlchemySessionComponent(url='postgresql://postgres:apisbtest0011@192.168.99.100/api_test'),
]

event_hooks = [
    SQLAlchemyTransactionHook(),
]

app = App(routes=routes, components=components, event_hooks=event_hooks)



if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)