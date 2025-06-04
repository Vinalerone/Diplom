from django.core.management.base import BaseCommand
from myapp.models import (
    Institute,
    Department,
    Head_of_the_educational_program,
    Employee,
    EducationalProgram,
    News,
    Matrix,
    Passport,
    Scheme
)
from django.utils import timezone

class Command(BaseCommand):
    help = 'Заполняет базу данных тестовыми данными'

    def handle(self, *args, **options):
        # 1. Создаем институт
        institute = Institute.objects.create(name="Институт информационных технологий")
        
        # 2. Создаем кафедру
        department = Department.objects.create(
            id_institute=institute,
            name="Кафедра программной инженерии"
        )
        
        # 3. Создаем руководителя ОП
        head = Head_of_the_educational_program.objects.create(
            id_Institute=institute,
            surname="Иванов",
            name="Иван",
            patronymic="Иванович",
            post="Руководитель ОП"
        )
        
        # 4. Создаем сотрудника ОЛ
        employee = Employee.objects.create(
            surname="Петрова",
            name="Мария",
            patronymic="Сергеевна",
            position="Специалист отдела лицензирования"
        )
        
        # 5. Создаем образовательные программы
        program1 = EducationalProgram.objects.create(
            name="Информационные системы и технологии",
            abbreviation="ИСТ",
            specialty_code="09.04.02",
            enrollment_year=2024,
            status="не_сдана",
            department=department,
            head=head
        )
        
        program2 = EducationalProgram.objects.create(
            name="Программная инженерия",
            abbreviation="ПИ",
            specialty_code="09.04.04",
            enrollment_year=2025,
            status="не_сдана",
            department=department,
            head=head
        )
        
        # 6. Создаем новости
        News.objects.create(
            content="Сообщаем о внесении изменений в требования к лицензированию по ОПК 4. С 01.12.2023 вступают в силу новые нормативные акты."
        )
        
        News.objects.create(
            content="Обновлены требования к оформлению матрицы компетенций. Пожалуйста, ознакомьтесь с новыми шаблонами."
        )
        
        # 7. Создаем матрицы, паспорта и схемы
        Matrix.objects.create(
            educational_program=program1,
            licensing_employee=employee,
            assessment=2,
            comment="Не соответствует приказу ректора №267-О от 20.02.25"
        )
        
        Passport.objects.create(
            educational_program=program1,
            licensing_employee=employee,
            assessment=1
        )
        
        Scheme.objects.create(
            educational_program=program1,
            responsible_employee=employee,
            status="не_сдана",
            comments="Отсутствует раздел по формированию профессиональных компетенций"
        )
        
        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена тестовыми данными!'))