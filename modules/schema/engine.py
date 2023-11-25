from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from modules.schema.models import Base

project_root = Path(__file__).parent.parent.parent
sqlite_db_file_path = project_root.resolve() / 'switchbot-plugs.db'

engine = create_engine(f"sqlite:///{sqlite_db_file_path.as_posix()}", echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
