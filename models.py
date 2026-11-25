from sqlalchemy import create_engine, Column,Integer, String,ForeignKey,Boolean,Float

from sqlalchemy.ext.declarative import declarative_base

db = create_engine('sqlite:///pizzaria,db')# base de dados SQlite
Base = declarative_base() #classe base para os modelos

class user(Base):
    __tablename__ = 'user' # Nome da Tabela
    id  = Column("id",Integer,primaryKey=True,autoicrement=True)
    name = Column("name",String)
    email = Column("email",String,nullable=True)
    password = Column("password",String,nullable=False)
    active = Column("active", Boolean)
    admin = Column('admin',Boolean,default=False)

    def __int__(self,name,email,password,active=True, admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.admin = admin

class order(Base):
    __tablename__ = 'user' # Nome da Tabela
    id  = Column("id",Integer,primaryKey=True,autoicrement=True)
    user = Column("user",ForeignKey("users_id"),nullable=False)
    status = Column("status",String,nullable=True)
    price= Column("prince",Float)

    def __int__(self,user,status="pending", price=0):
         self.user = user
         self.status = status
         self.price = price

class orderItems(Base):
    __tablename__ = 'user' # Nome da Tabela
    id  = Column("id",Integer,primaryKey=True,autoicrement=True)
    quantiny = Column("quantity",Integer("users_id"),nullable=False)
    flavour = Column("flavour",String)
    size = Column("size",String)
    unit_price = Column("unit_price",float)
    order = Column("order",ForeignKey ("orders.id"))
    
    def __int__(self,quantiny,flavour,size,unit_price,order):
         self.quantiny = quantiny
         self.flavour = flavour
         self.size = size
         self.unit_price = unit_price
         self.order = order

         

    
         
           