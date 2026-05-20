import random
from faker import Faker
from sqlalchemy.orm import Session
from models import engine, Base, Student, Course

fake = Faker()


def create_tables():
    Base.metadata.create_all(engine)
    print("Таблиці створено")


def seed_data():
    with Session(engine) as session:
        # Створюємо 5 курсів
        courses = [
            Course(name="Python", description="Основи Python"),
            Course(name="SQL", description="Бази даних"),
            Course(name="JavaScript", description="Веб розробка"),
            Course(name="Docker", description="Контейнеризація"),
            Course(name="Git", description="Система контролю версій"),
        ]
        session.add_all(courses)
        session.flush()

        # Створюємо 20 студентів і рандомно записуємо на курси
        for _ in range(20):
            student = Student(
                name=fake.name(),
                email=fake.unique.email()
            )
            # Кожен студент записується на 1-3 випадкових курси
            student.courses = random.sample(courses, k=random.randint(1, 3))
            session.add(student)

        session.commit()
        print("Дані додано: 5 курсів, 20 студентів")


def add_student(name, email, course_name):
    with Session(engine) as session:
        course = session.query(Course).filter_by(name=course_name).first()
        if not course:
            print(f"Курс '{course_name}' не знайдено")
            return

        student = Student(name=name, email=email)
        student.courses.append(course)
        session.add(student)
        session.commit()
        print(f"Студента '{name}' додано на курс '{course_name}'")


def get_students_by_course(course_name):
    with Session(engine) as session:
        course = session.query(Course).filter_by(name=course_name).first()
        if not course:
            print(f"Курс '{course_name}' не знайдено")
            return
        print(f"\nСтуденти курсу '{course_name}':")
        for student in course.students:
            print(f"  - {student.name} ({student.email})")


def get_courses_by_student(student_name):
    with Session(engine) as session:
        student = session.query(Student).filter_by(name=student_name).first()
        if not student:
            print(f"Студента '{student_name}' не знайдено")
            return
        print(f"\nКурси студента '{student_name}':")
        for course in student.courses:
            print(f"  - {course.name}")


def update_student(student_id, new_name=None, new_email=None):
    with Session(engine) as session:
        student = session.get(Student, student_id)
        if not student:
            print(f"Студента з id={student_id} не знайдено")
            return
        if new_name:
            student.name = new_name
        if new_email:
            student.email = new_email
        session.commit()
        print(f"Студента оновлено: {student}")


def delete_student(student_id):
    with Session(engine) as session:
        student = session.get(Student, student_id)
        if not student:
            print(f"Студента з id={student_id} не знайдено")
            return
        session.delete(student)
        session.commit()
        print(f"Студента з id={student_id} видалено")


if __name__ == "__main__":

    create_tables()
    seed_data()

    add_student("Юрій Давидяк", "yurii@example.com", "Python")

    get_students_by_course("Python")
    get_courses_by_student("Юрій Давидяк")

    update_student(1, new_name="Сара Коннор")
    delete_student(2)