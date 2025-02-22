#! /usr/bin/env python3

from sqlalchemy import create_engine
from models import Base

import pandas as pd

engine = create_engine("sqlite:///classroom.db", echo=True)
# conn = engine.connect()
Base.metadata.create_all(engine)

classroom_df = pd.read_csv("./data/classroom.csv")
student_df = pd.read_csv("./data/student.csv")

classroom_df.to_sql("classroom", engine, if_exists="append", index=False)
student_df.to_sql("student", engine, if_exists="append", index=False)
