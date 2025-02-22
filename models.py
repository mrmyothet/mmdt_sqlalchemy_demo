## Ref - https://docs.sqlalchemy.org/en/20/orm/quickstart.html#declare-models

# pip install --upgrade "sqlalchemy>=2.0"

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "student"

    student_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    age: Mapped[int]
    academic_year: Mapped[int]

    classroom_id: Mapped[int] = mapped_column(
        ForeignKey("classroom.classroom_id"), nullable=False
    )
    classroom: Mapped["Classroom"] = relationship(back_populates="student_list")


class Classroom(Base):
    __tablename__ = "classroom"

    classroom_id: Mapped[int] = mapped_column(primary_key=True)
    classroom_name: Mapped[str] = mapped_column(nullable=False)

    student_list: Mapped[list["Student"]] = relationship(
        back_populates="classroom", cascade="all, delete-orphan"
    )
