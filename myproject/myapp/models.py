from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
    
# Модель Institute
class Institute(models.Model):
    name = models.CharField("Название института", max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Институт"
        verbose_name_plural = "Институты"

# Модель Head_of_the_educational_program
class Head_of_the_educational_program(models.Model):
    id_Institute = models.ForeignKey(Institute, on_delete=models.CASCADE, null=True, verbose_name="Институт")
    surname = models.CharField("Фамилия", max_length=30)
    name = models.CharField("Имя", max_length=30)
    patronymic = models.CharField("Отчество", max_length=30)
    post = models.CharField("Должность", max_length=40)

    def __str__(self) -> str:
        return f"{self.surname} {self.name} {self.patronymic}"

    class Meta:
        verbose_name = "Руководитель образовательной программы"
        verbose_name_plural = "Руководители образовательных программ"

# Модель News
class News(models.Model):
    # Дата создания новости (автоматически добавляется при создании записи)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    
    # Текст новости
    content = models.TextField("Новость")

    def formatted_date(self):
        return self.created_at.strftime("%d.%m.%y")  # 27.03.22

    def __str__(self):
        return f"Новость от {self.formatted_date()}"
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

# Модель Employee (Сотрудник отдела лицензирования)
class Employee(models.Model):
    # Фамилия
    surname = models.CharField("Фамилия", max_length=50)

    # Имя
    name = models.CharField("Имя", max_length=50)

    # Отчество
    patronymic = models.CharField("Отчество", max_length=50)

    # Должность
    position = models.CharField("Должность", max_length=100)

    def __str__(self) -> str:
        return f"{self.surname} {self.name} {self.patronymic}"

    class Meta:
        verbose_name = "Сотрудник отдела лицензирования"
        verbose_name_plural = "Сотрудники отдела лицензирования"

    ordering = ['surname', 'name']    

# ВЫПУСКАЮЩИЕ КАФЕДРЫ
class Department(models.Model):
    """Модель для выпускающих кафедр"""
    id_department = models.AutoField(
        "ID Выпускающей кафедры",
        primary_key=True,
        help_text="Уникальный идентификатор кафедры"
    )
    
    id_institute = models.ForeignKey(
        Institute,
        on_delete=models.CASCADE,
        verbose_name="ID Института",
        related_name='departments',
        help_text="Институт, к которому относится кафедра"
    )
    
    name = models.CharField(
        "Наименование выпускающей кафедры",
        max_length=255,
        help_text="Полное название кафедры"
    )

    class Meta:
        verbose_name = "Выпускающая кафедра"
        verbose_name_plural = "Выпускающие кафедры"
        ordering = ['name']  # Сортировка по названию по умолчанию
        db_table = 'departments'  # Название таблицы в БД (опционально)

    def __str__(self):
        return f"{self.name} (Институт: {self.id_institute.name})"
    
#Образовательная программа

class EducationalProgram(models.Model):
    """Модель образовательной программы"""
    STATUS_CHOICES = [
        ('сдана', 'сдана'),
        ('не_сдана', 'не_сдана')
    ]
    
    id_program = models.AutoField(
        "ID Образовательной программы",
        primary_key=True
    )
    
    name = models.CharField(
        "Наименование программы",
        max_length=255,
        help_text="Полное название образовательной программы"
    )
    
    abbreviation = models.CharField(
        "Аббревиатура",
        max_length=20,
        help_text="Сокращенное название (например, ПМИ)"
    )
    
    specialty_code = models.CharField(
        "Шифр специальности",
        max_length=15,
        help_text="Код специальности по ФГОС"
    )
    
    enrollment_year = models.PositiveIntegerField(
        "Год набора",
        validators=[
            MinValueValidator(2000),
            MaxValueValidator(2030)
        ]
    )
    
    status = models.CharField(
        "Статус",
        max_length=15,
        choices=STATUS_CHOICES,
        default='development'
    )
    
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        verbose_name="Выпускающая кафедра"
    )
    
    head = models.ForeignKey(
        Head_of_the_educational_program,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Руководитель программы"
    )

    class Meta:
        verbose_name = "Образовательная программа"
        verbose_name_plural = "Образовательные программы"
        ordering = ['-enrollment_year', 'name']
        constraints = [
            models.UniqueConstraint(
                fields=['abbreviation', 'enrollment_year'],
                name='unique_program_abbreviation_per_year'
            )
        ]

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"
    
#Матрица

class Matrix(models.Model):
    """Модель матрицы компетенций"""
    ASSESSMENT_CHOICES = [
        (1, 'сдан'),
        (2, 'не сдан')
    ]
    
    id_matrix = models.AutoField(
        "ID Матрицы",
        primary_key=True
    )

    educational_program = models.ForeignKey(
        EducationalProgram,
        on_delete=models.CASCADE,
        verbose_name="Образовательная программа",
        related_name='matrices',
        # limit_choices_to={'status': 'development'}, # Временно закомментировать для отладки
        help_text="Выберите образовательную программу из списка"
    )
    
    
    licensing_employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Сотрудник ОЛ",
        #limit_choices_to={'position__icontains': 'лицензирования'},
        help_text="Выберите сотрудника отдела лицензирования"
    )
    
    add_date = models.DateField(
        "Дата добавления РОП",
        auto_now_add=True,
        editable=False  # Добавляем это, чтобы поле не отображалось в форме
    )
    
    check_date = models.DateField(
        "Дата проверки ОЛ",
        null=True,
        blank=True
    )
    
    document_link = models.URLField(
        "Ссылка на документ",
        max_length=500,
        blank=True
    )
    
    comment = models.TextField(
        "Комментарий ОЛ",
        blank=True,
        max_length=1000
    )
    
    assessment = models.PositiveSmallIntegerField(
        "Оценка",
        choices=ASSESSMENT_CHOICES,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Матрица компетенций"
        verbose_name_plural = "Матрицы компетенций"
        ordering = ['-add_date']

    def __str__(self):
        return f"Матрица для {self.educational_program}"
    
#ПАСПОРТ
from django.db import models
from django.utils.translation import gettext_lazy as _

class Passport(models.Model):
    """Модель паспорта образовательной программы"""
    ASSESSMENT_CHOICES = [
        (1, 'сдан'),
        (2, 'не_сдан')
    ]
    
    id_matrix = models.AutoField(
        _("ID Паспорта"),
        primary_key=True
    )
    
    educational_program = models.ForeignKey(
        EducationalProgram,
        on_delete=models.CASCADE,
        verbose_name="Образовательная программа",
        related_name='passports',
        # limit_choices_to={'status': 'development'}, # Временно закомментировать для отладки
        help_text="Выберите образовательную программу из списка"
    )
    
    licensing_employee = models.ForeignKey(
        'Employee',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Сотрудник ОЛ"),
        limit_choices_to={'position__icontains': 'лицензирования'},
        help_text=_("Выберите сотрудника отдела лицензирования")
    )
    
    add_date = models.DateField(
        _("Дата добавления РОП"),
        auto_now_add=True,
        editable=False
    )
    
    assessment = models.IntegerField(
        _("Статус проверки"),
        choices=ASSESSMENT_CHOICES,
        default=2
    )
    
    document_link = models.FileField(
        _("Файл документа"),
        upload_to='passports/',
        null=True,
        blank=True
    )
    
    class Meta:
        verbose_name = _("Паспорт ОП")
        verbose_name_plural = _("Паспорта ОП")
        ordering = ['-add_date']
    
    def __str__(self):
        return f"Паспорт {self.educational_program} от {self.add_date.strftime('%d.%m.%Y')}"
    
    def get_status_display(self):
        return dict(self.ASSESSMENT_CHOICES).get(self.assessment, 'не_сдан')
    
    #Схема формирования компетенций.

class Scheme(models.Model):
    """Модель схемы формирования приложений"""
    STATUS_CHOICES = [
        ('сдана', 'сдана'),
        ('не_сдана', 'не_сдана'),
    ]
    
    id_scheme = models.AutoField(
        "ID Схемы",
        primary_key=True,
        help_text="Уникальный идентификатор схемы"
    )
    

    educational_program = models.ForeignKey(
        EducationalProgram,
        on_delete=models.CASCADE,
        verbose_name="Образовательная программа",
        related_name='schemes',
        # limit_choices_to={'status': 'development'}, # Временно закомментировать для отладки
        help_text="Выберите образовательную программу из списка"
    )
    
    responsible_employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Ответственный сотрудник",
        limit_choices_to={'position__icontains': 'лицензирования'},
        help_text="Сотрудник отдела лицензирования"
    )
    
    creation_date = models.DateField(
        "Дата создания",
        auto_now_add=True,
        help_text="Дата формирования схемы"
    )
    
    approval_date = models.DateField(
        "Дата утверждения",
        null=True,
        blank=True,
        help_text="Дата утверждения схемы"
    )
    
    document_link = models.URLField(
        "Ссылка на документ",
        max_length=500,
        blank=True,
        help_text="Ссылка на схему в облачном хранилище"
    )
    
    comments = models.TextField(
        "Комментарии",
        blank=True,
        max_length=2000,
        help_text="Замечания по схеме"
    )
    
    status = models.CharField(
        "Статус",
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft',
        help_text="Текущий статус схемы"
    )

    class Meta:
        verbose_name = "Схема формирования компетенций"
        verbose_name_plural = "Схемы формирования компетенций"
        ordering = ['-creation_date']
        db_table = 'schemes'

    def __str__(self):
        return f"Схема {self.id_scheme} ({self.educational_program})"