from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship

engine = create_engine("sqlite:///students.db", echo=False)


class Base(DeclarativeBase):
    pass


enrollment = Table(
    "enrollment",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id")),
    Column("course_id", Integer, ForeignKey("courses.id"))
)


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    courses = relationship("Course", secondary=enrollment, back_populates="students")

    def __repr__(self):
        return f"Student(id={self.id}, name={self.name})"


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)

    students = relationship("Student", secondary=enrollment, back_populates="courses")

    def __repr__(self):
        return f"Course(id={self.id}, name={self.name})"