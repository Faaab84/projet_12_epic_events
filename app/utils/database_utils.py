from sqlalchemy.orm import DeclarativeBase
from db import SessionLocal


def commit_to_db(model_instance: DeclarativeBase) -> bool:

    session = SessionLocal()
    try:
        session.add(model_instance)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"Error committing to database: {e}")
        return False
    finally:
        session.close()