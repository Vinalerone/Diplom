from django.contrib import admin
from django import forms
from .models import Institute, Head_of_the_educational_program, News, Employee, Matrix, Passport, Scheme
from django.utils.html import format_html
from django.db import models

from django.contrib.admin.sites import site
if Matrix in site._registry:
    site.unregister(Matrix)

from .models import (
    Institute,
    Head_of_the_educational_program,
    News,
    Employee,
    Department,
    EducationalProgram  # Добавляем импорт новой модели
)
# ЖИВ
# Регистрация модели Institute
@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    
    list_display = ('name',)  # Отображаемое поле
    search_fields = ('name',)  # Поиск по названию
    ordering = ('name',)  # Сортировка по названию

# Форма для модели Head_of_the_educational_program
class HeadOfTheEducationalProgramForm(forms.ModelForm):
    class Meta:
        model = Head_of_the_educational_program
        widgets = {
            'surname': forms.TextInput(attrs={'placeholder': 'Иванов'}),
            'name': forms.TextInput(attrs={'placeholder': 'Иван'}),
            'patronymic': forms.TextInput(attrs={'placeholder': 'Иванович'}),
        }
        fields = '__all__'

# Админ-класс для модели Head_of_the_educational_program
@admin.register(Head_of_the_educational_program)
class HeadOfTheEducationalProgramAdmin(admin.ModelAdmin):
    form = HeadOfTheEducationalProgramForm
    list_display = ('surname', 'name', 'patronymic', 'post', 'id_Institute')
    list_display_links = ('surname', 'name', 'patronymic')
    search_fields = ('surname', 'name', 'patronymic', 'post')
    list_filter = ('id_Institute', 'post')
    fieldsets = (
        ('ФИО', {
            'fields': ('surname', 'name', 'patronymic')
        }),
        ('Должность и институт', {
            'fields': ('post', 'id_Institute')
        }),
    )
    
    def get_changeform_initial_data(self, request):
        return {'post': 'Руководитель ОП'}
    
    # НОВОСТИ
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    # Поля для отображения в списке
    list_display = ('formatted_date', 'short_content')
    
    # Поля для поиска
    search_fields = ('content',)
    
    # Фильтры
    list_filter = ('created_at',)
    
    # Порядок сортировки (новые сверху)
    ordering = ('-created_at',)
    
    # Настройки формы редактирования
    fields = ('content',)  # created_at не включаем, так как auto_now_add=True
    
    # Поля только для чтения
    readonly_fields = ('created_at',)
    
    # Кастомные методы для отображения
    def formatted_date(self, obj):
        return obj.created_at.strftime('%d.%m.%Y %H:%M')
    formatted_date.short_description = 'Дата создания'
    formatted_date.admin_order_field = 'created_at'
    
    def short_content(self, obj):
        return format_html(
            '<span title="{}">{}</span>',
            obj.content,
            obj.content[:100] + '...' if len(obj.content) > 100 else obj.content
        )
    short_content.short_description = 'Содержание'
    
    # Автоматическое форматирование текста при сохранении
    def save_model(self, request, obj, form, change):
        obj.content = obj.content.strip()
        super().save_model(request, obj, form, change)


 # СОТРУДНИКИ ОЛ
class EmployeeAdminForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'surname': forms.TextInput(attrs={
                'placeholder': 'Иванов',
                'class': 'vTextField'
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Иван',
                'class': 'vTextField'
            }),
            'patronymic': forms.TextInput(attrs={
                'placeholder': 'Иванович',
                'class': 'vTextField'
            }),
            'position': forms.TextInput(attrs={
                'placeholder': 'Специалист по лицензированию',
                'class': 'vTextField'
            }),
        }

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id_department', 'name', 'id_institute')
    search_fields = ('name', 'id_institute__name')
    list_filter = ('id_institute',)

@admin.register(EducationalProgram)
class EducationalProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'department', 'head', 'status', 'enrollment_year')
    list_filter = ('status', 'department', 'enrollment_year')
    # search_fields: head__surname и head__name работают при наличии autocomplete_fields или raw_id_fields для head
    search_fields = ('name', 'abbreviation', 'specialty_code', 'head__surname', 'head__name')
    raw_id_fields = ('head',) # raw_id_fields и autocomplete_fields можно использовать вместе или по отдельности
    autocomplete_fields = ('head',) # autocomplete_fields требует настройки search_fields на связанной модели Head_of_the_educational_program
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'abbreviation', 'specialty_code', 'enrollment_year', 'status')
        }),
        ('Ответственные', {
            'fields': ('department', 'head')
        }),
    )

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic', 'position')
    search_fields = ('surname', 'name', 'patronymic', 'position')
    list_filter = ('position',)
    
    # Фильтр для отображения только сотрудников ОЛ
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(position__icontains='лицензирования')

@admin.register(Matrix)
class MatrixAdmin(admin.ModelAdmin):
    list_display = ('educational_program', 'get_licensing_employee', 'add_date', 'assessment_status')
    search_fields = ('educational_program__name', 'educational_program__abbreviation')
    autocomplete_fields = ['licensing_employee']
    
    def get_licensing_employee(self, obj):
        if obj.licensing_employee:
            return f"{obj.licensing_employee.surname} {obj.licensing_employee.name[0]}.{obj.licensing_employee.patronymic[0]}."
        return "Не назначен"
    get_licensing_employee.short_description = 'Сотрудник ОЛ'
    get_licensing_employee.admin_order_field = 'licensing_employee__surname'
    
    def assessment_status(self, obj):
        return obj.get_assessment_display() if obj.assessment else "Не оценена"
    assessment_status.short_description = 'Оценка'
    
    # Фильтр для выбора только сотрудников ОЛ
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "licensing_employee":
            kwargs["queryset"] = Employee.objects.filter(position__icontains='лицензирования')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
#     #Passport
# @admin.register(Passport)
# class PassportAdmin(admin.ModelAdmin):
#     list_display = ('educational_program', 'get_licensing_employee', 'add_date', 'assessment_status')
#     search_fields = ('educational_program__name', 'educational_program__abbreviation')
#     autocomplete_fields = ['licensing_employee']
    
#     def get_licensing_employee(self, obj):
#         if obj.licensing_employee:
#             return f"{obj.licensing_employee.surname} {obj.licensing_employee.name[0]}.{obj.licensing_employee.patronymic[0]}."
#         return "Не назначен"
#     get_licensing_employee.short_description = 'Сотрудник ОЛ'
#     get_licensing_employee.admin_order_field = 'licensing_employee__surname'
    
#     def assessment_status(self, obj):
#         return obj.get_assessment_display() if obj.assessment else "Не оценена"
#     assessment_status.short_description = 'Оценка'

from django.contrib import admin
from .models import Passport, EducationalProgram, Employee # Убедитесь, что импортировали все необходимые модели
@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    list_display = ('educational_program', 'add_date', 'get_assessment_display')
    list_filter = ('assessment', 'add_date')
    search_fields = ('educational_program__name',)
    
    # Добавляем 'educational_program' в raw_id_fields
    raw_id_fields = ('educational_program', 'licensing_employee',)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            # Фильтруем по значению 1, которое соответствует 'сдан' в ASSESSMENT_CHOICES
            qs = qs.filter(assessment=1)
        return qs

    
    # Фильтр для выбора только сотрудников ОЛ
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "licensing_employee":
            kwargs["queryset"] = Employee.objects.filter(position__icontains='лицензирования')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Scheme)
class SchemeAdmin(admin.ModelAdmin):
    list_display = (
        'id_scheme', 
        'get_educational_program', 
        'get_responsible_employee', 
        'status', 
        'creation_date'
    )
    list_filter = ('status', 'educational_program__department')
    search_fields = (
        'educational_program__name',
        'educational_program__abbreviation',
        'responsible_employee__surname'
    )
    date_hierarchy = 'creation_date'
    autocomplete_fields = ['educational_program', 'responsible_employee']
    readonly_fields = ('creation_date',)
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('educational_program', 'responsible_employee', 'status')
        }),
        ('Документы', {
            'fields': ('document_link', 'comments')
        }),
        ('Даты', {
            'fields': ('approval_date',),
            'classes': ('collapse',)
        }),
    )

    def get_educational_program(self, obj):
        return f"{obj.educational_program.abbreviation} ({obj.educational_program.specialty_code})"
    get_educational_program.short_description = 'Программа'
    get_educational_program.admin_order_field = 'educational_program__name'

    def get_responsible_employee(self, obj):
        if obj.responsible_employee:
            return f"{obj.responsible_employee.surname} {obj.responsible_employee.name[0]}."
        return "Не назначен"
    get_responsible_employee.short_description = 'Ответственный'
    get_responsible_employee.admin_order_field = 'responsible_employee__surname'    
        