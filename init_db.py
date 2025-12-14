from db import engine, Base
from app.models.user import User
from app.models.customer import Customer
from app.models.collaborator import Collaborator
from app.models.contract import Contract
from app.models.event import Event
from app.models.department import Department
from app.models.status import Status
from sqlalchemy.schema import CreateTable

Base.metadata.create_all(bind=engine)
print("Tables créées avec succès.")

for table in Base.metadata.tables.values():
    print(CreateTable(table).compile(engine))