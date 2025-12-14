from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


DATABASE_URL = "postgresql+psycopg2://crm_user:balaramane@localhost:5432/crm_epic_events"

engine = create_engine(DATABASE_URL)
engine.connect()

Base = declarative_base()
print("Connexion à la base de données réussie.")