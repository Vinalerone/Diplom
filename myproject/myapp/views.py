from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import (
    Institute, 
    Head_of_the_educational_program,
    News,
    Employee,
    Department,
    EducationalProgram,
    Matrix,
    Passport,
    Scheme
)

from django.views.generic import ListView
from .models import EducationalProgram  # Или ваша модель
from django.views.generic import TemplateView
# ТУТ ОЛ

from django.views.generic import TemplateView, ListView
from .models import News, EducationalProgram

# Для сохранения новостей
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import News  # Добавьте этот импорт
import json
# Для РОП ГЛ Меню
from django.shortcuts import render
from .models import EducationalProgram

def OLPageView(request):
    programs = EducationalProgram.objects.prefetch_related(
        'passports',  # Изменили с passport_set
        'schemes',    # Изменили с scheme_set
        'matrices'    # Изменили с matrix_set
    ).all()
    
    program_data = []
    
    for program in programs:
        passport = program.passports.first()  # Изменили с passport_set
        scheme = program.schemes.first()      # Изменили с scheme_set
        matrix = program.matrices.first()     # Изменили с matrix_set
        
        # Паспорт
        passport_status = "отсутствует"
        passport_date = ""
        if passport:
            passport_date = passport.add_date.strftime("%d.%m.%Y") if passport.add_date else ""
            passport_status = "сдан" if passport.assessment == 1 else "не_сдан"
        
        # Схема
        scheme_status = "отсутствует"
        scheme_date = ""
        if scheme:
            scheme_date = scheme.creation_date.strftime("%d.%m.%Y") if scheme.creation_date else ""
            scheme_status = scheme.status
        
        # Матрица
        matrix_status = "отсутствует"
        matrix_date = ""
        if matrix:
            matrix_date = matrix.add_date.strftime("%d.%m.%Y") if matrix.add_date else ""
            matrix_status = "сдан" if matrix.assessment == 1 else "не_сдан"
        
        # Общий статус
        overall_status = "не_сдан"
        if passport_status == "сдан" and scheme_status == "сдана" and matrix_status == "сдан":
            overall_status = "сдан"
        
        program_data.append({
    'year': program.enrollment_year,
    'specialty_code': program.specialty_code,
    'name': program.name or "Не указано",
    'abbreviation': program.abbreviation or "-",  # Правильно получаем аббревиатуру из объекта program
    'head': str(program.head) if program.head else "Не указан",
    'passport_status': passport_status,
    'passport_date': passport_date,
    'scheme_status': scheme_status,
    'scheme_date': scheme_date,
    'matrix_status': matrix_status,
    'matrix_date': matrix_date,
    'overall_status': overall_status,
        })
    
    return render(request, 'myproject/pages_ol/smain/index.html', {'programs': program_data})


# Временный виев для новостей РОП
# myapp/views.py
from django.http import HttpResponse
from .models import News

def debug_news_view(request):
    news = News.objects.all().order_by('-created_at')
    response = "<h1>Последние новости (всего: {})</h1>".format(news.count())
    for item in news:
        response += f"""
        <div style="margin: 20px; padding: 10px; border: 1px solid #ccc;">
            <h3>{item.created_at.date()}</h3>
            <p>{item.content}</p>
        </div>
        """
    return HttpResponse(response)
# Новости РОП
class BaseProgramView:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_lis'] = News.objects.all().order_by('-created_at')
        return context
    
class ROPPageView(BaseProgramView, TemplateView):  # BaseProgramView должен быть ПЕРВЫМ
    template_name = 'myproject/pages_rop/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Важно!
        context['programs'] = EducationalProgram.objects.all()
        return context


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
# Редактирование и удаление новостей
def delete_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        news.delete()
        messages.success(request, 'Новость успешно удалена')
        return redirect('ol-news')
    
    # Для GET запроса показываем страницу подтверждения
    return render(request, 'myproject/pages_ol/news/confirm_delete.html', {'news': news})

def edit_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        new_content = request.POST.get('content')
        if new_content:
            news.content = new_content
            news.save()
            messages.success(request, 'Новость успешно обновлена')
            return redirect('ol-news')
    
    # Для GET запроса показываем форму редактирования
    return render(request, 'myproject/pages_ol/news/edit_news.html', {
        'news': news,
        'form_action': reverse('edit_news', args=[news.pk])
    })

# Показывание новостей

def news_index(request):
    news_items = News.objects.all().order_by('-created_at')
    return render(request, 'myapp/pages_ol/news/index.html', {'news_items': news_items})


@csrf_exempt
def save_news(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if not data.get('content'):
                return JsonResponse({'success': False, 'error': 'Текст новости не может быть пустым'})
                
            news = News.objects.create(content=data['content'])
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request'})


class OlOt1View(TemplateView):
    template_name = 'myproject/pages_ol/reports/reports_OOP/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем все объекты Passport.
        # Используем select_related для получения связанных EducationalProgram и Head_of_the_educational_program
        # в одном запросе, что более эффективно.
        passports = Passport.objects.select_related(
            'educational_program',
            'educational_program__head'
        ).all()
        passport_list_data = []
        for passport in passports:
            program = passport.educational_program
            head = program.head if program else None # Руководитель связан с программой
            # Формируем данные для одной строки таблицы
            passport_data = {
                'year': program.enrollment_year if program else "-",
                'program_info': f"{program.specialty_code if program else '-'} {program.name if program else 'Не указана'} {program.abbreviation if program else '-'}",
                'head_name': str(head) if head else "Не указан",
                # Форматируем дату в ДД.ММ.ГГ
                'add_date_formatted': passport.add_date.strftime('%d.%m.%y') if passport.add_date else "-",
                # Используем get_assessment_display для получения читаемого статуса
                'assessment_status': passport.get_assessment_display(),
            }
            passport_list_data.append(passport_data)
        # Добавляем список данных паспортов в контекст шаблона
        context['passport_list'] = passport_list_data
        return context

class OlOt2View(TemplateView):
    template_name = 'myproject/pages_ol/reports/reports_OL/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем все объекты Matrix.
        # Используем select_related для получения связанных EducationalProgram,
        # Head_of_the_educational_program и Employee в одном запросе.
        matrices = Matrix.objects.select_related(
            'educational_program',
            'educational_program__head', # Связь через educational_program
            'licensing_employee' # Связь напрямую
        ).all()
        matrix_list_data = []
        for matrix in matrices: # Цикл по каждой матрице
            program = matrix.educational_program
            head = program.head if program else None # Руководитель связан с программой
            licensing_employee = matrix.licensing_employee
            # Формируем данные для одной строки таблицы
            matrix_data = {
                'empty_column': '', # Оставляем первый столбец пустым, как в примере
                'year': program.enrollment_year if program else "-",
                'program_info': f"{program.specialty_code if program else '-'} {program.name if program else 'Не указана'} {program.abbreviation if program else '-'}",
                # Используем дату добавления РОП из матрицы
                'add_date_formatted': matrix.add_date.strftime('%d.%m.%y') if matrix.add_date else "-",
                # Используем дату проверки ОЛ из матрицы
                'check_date_formatted': matrix.check_date.strftime('%d.%m.%y') if matrix.check_date else "-",
                # Используем get_assessment_display для получения читаемого статуса оценки матрицы
                # Ваша модель Matrix имеет поле assessment, но статус "Не проверен"
                # не соответствует вариантам 'сдан' (1) или 'не сдан' (2).
                # Возможно, это статус из поля comment или другая логика.
                # Временно будем использовать get_assessment_display, но вам может потребоваться адаптировать это.
                'assessment_status': matrix.get_assessment_display() if matrix.assessment is not None else "Не проверен",
            }
            matrix_list_data.append(matrix_data)
        # Добавляем список данных матриц в контекст шаблона
        context['matrix_list'] = matrix_list_data
        return context

class BaseProgramView:
    """Базовый класс с общим функционалом"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = News.objects.all().order_by('-created_at')[:5]
        return context

# class OLPageView(BaseProgramView, TemplateView):
#     """Главная страница ОЛ"""
#     template_name = 'myproject/pages_ol/smain/index.html'  # Английский путь

class KK(BaseProgramView, TemplateView):
    """Главная страница ОЛ"""
    template_name = 'myproject/pages_ol/index.html'  # Английский путь

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['test'] = "Тестовые данные"  # Добавим тестовые данные
    return context


class OLAnalysisView(TemplateView):
    template_name = 'myproject/pages_ol/analysis/index.html'  # Добавлен префикс myproject/

class OLNewsView(BaseProgramView, TemplateView):
    """Страница объявлений"""
    template_name = 'myproject/pages_ol/news/index.html'

class OLReportsView(BaseProgramView, TemplateView):
    """Базовая страница отчётов"""
    template_name = 'myproject/pages_ol/reports/index.html'
# Ниже РОП
# class ROPPageView(BaseProgramView, TemplateView):
#     template_name = 'myproject/pages_rop/index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)  # <- Важно!
#         context['programs'] = EducationalProgram.objects.all()
#         return context
    
# class BaseProgramView:
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)  # <- Важно!
#         context['news_lis'] = News.objects.all().order_by('-created_at')
#         return context

class ProgramListView(BaseProgramView, ListView):
    """Список образовательных программ"""
    model = EducationalProgram
    template_name = 'myproject/program_list.html'
    context_object_name = 'programs'
    queryset = EducationalProgram.objects.all()  # Явно указываем queryset



# from .forms import (
#     InstituteForm,
#     HeadOfProgramForm,
#     NewsForm,
#     EmployeeForm,
#     DepartmentForm,
#     EducationalProgramForm,
#     MatrixForm,
#     PassportForm,
#     SchemeForm
# )

# Institute Views
class InstituteListView(ListView):
    model = Institute
    template_name = 'institute_list.html'
    context_object_name = 'institutes'

class InstituteDetailView(DetailView):
    model = Institute
    template_name = 'institute_detail.html'

class InstituteCreateView(CreateView):
    model = Institute
    # form_class = InstituteForm
    template_name = 'institute_form.html'
    success_url = reverse_lazy('institute-list')

class InstituteUpdateView(UpdateView):
    model = Institute
    # form_class = InstituteForm
    template_name = 'institute_form.html'
    success_url = reverse_lazy('institute-list')

class InstituteDeleteView(DeleteView):
    model = Institute
    template_name = 'institute_confirm_delete.html'
    success_url = reverse_lazy('institute-list')

# Head of Educational Program Views
class HeadOfProgramListView(ListView):
    model = Head_of_the_educational_program
    template_name = 'head_of_program_list.html'
    context_object_name = 'heads'

class HeadOfProgramDetailView(DetailView):
    model = Head_of_the_educational_program
    template_name = 'head_of_program_detail.html'

class HeadOfProgramCreateView(CreateView):
    model = Head_of_the_educational_program
    # form_class = HeadOfProgramForm
    template_name = 'head_of_program_form.html'
    success_url = reverse_lazy('head-of-program-list')

class HeadOfProgramUpdateView(UpdateView):
    model = Head_of_the_educational_program
    # form_class = HeadOfProgramForm
    template_name = 'head_of_program_form.html'
    success_url = reverse_lazy('head-of-program-list')

class HeadOfProgramDeleteView(DeleteView):
    model = Head_of_the_educational_program
    template_name = 'head_of_program_confirm_delete.html'
    success_url = reverse_lazy('head-of-program-list')

# News Views
class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    ordering = ['-created_at']
    paginate_by = 10

class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'

class NewsCreateView(CreateView):
    model = News
    # form_class = NewsForm
    template_name = 'news_form.html'
    success_url = reverse_lazy('news-list')

class NewsUpdateView(UpdateView):
    model = News
    # form_class = NewsForm
    template_name = 'news_form.html'
    success_url = reverse_lazy('news-list')

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news_confirm_delete.html'
    success_url = reverse_lazy('news-list')

# Employee Views
class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'
    ordering = ['surname', 'name']

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_detail.html'

class EmployeeCreateView(CreateView):
    model = Employee
    # form_class = EmployeeForm
    template_name = 'employee_form.html'
    success_url = reverse_lazy('employee-list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    # form_class = EmployeeForm
    template_name = 'employee_form.html'
    success_url = reverse_lazy('employee-list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_confirm_delete.html'
    success_url = reverse_lazy('employee-list')

# Department Views
class DepartmentListView(ListView):
    model = Department
    template_name = 'department_list.html'
    context_object_name = 'departments'
    ordering = ['name']

class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'department_detail.html'

class DepartmentCreateView(CreateView):
    model = Department
    # form_class = DepartmentForm
    template_name = 'department_form.html'
    success_url = reverse_lazy('department-list')

class DepartmentUpdateView(UpdateView):
    model = Department
    # form_class = DepartmentForm
    template_name = 'department_form.html'
    success_url = reverse_lazy('department-list')

class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'department_confirm_delete.html'
    success_url = reverse_lazy('department-list')

# Educational Program Views
class EducationalProgramListView(ListView):
    model = EducationalProgram
    template_name = 'educational_program_list.html'
    context_object_name = 'programs'
    ordering = ['-enrollment_year', 'name']

class EducationalProgramDetailView(DetailView):
    model = EducationalProgram
    template_name = 'educational_program_detail.html'

class EducationalProgramCreateView(CreateView):
    model = EducationalProgram
    # form_class = EducationalProgramForm
    template_name = 'educational_program_form.html'
    success_url = reverse_lazy('educational-program-list')

class EducationalProgramUpdateView(UpdateView):
    model = EducationalProgram
    # form_class = EducationalProgramForm
    template_name = 'educational_program_form.html'
    success_url = reverse_lazy('educational-program-list')

class EducationalProgramDeleteView(DeleteView):
    model = EducationalProgram
    template_name = 'educational_program_confirm_delete.html'
    success_url = reverse_lazy('educational-program-list')

# Matrix Views
class MatrixListView(ListView):
    model = Matrix
    template_name = 'matrix_list.html'
    context_object_name = 'matrices'
    ordering = ['-add_date']

class MatrixDetailView(DetailView):
    model = Matrix
    template_name = 'matrix_detail.html'

class MatrixCreateView(CreateView):
    model = Matrix
    # form_class = MatrixForm
    template_name = 'matrix_form.html'
    success_url = reverse_lazy('matrix-list')

class MatrixUpdateView(UpdateView):
    model = Matrix
    # form_class = MatrixForm
    template_name = 'matrix_form.html'
    success_url = reverse_lazy('matrix-list')

class MatrixDeleteView(DeleteView):
    model = Matrix
    template_name = 'matrix_confirm_delete.html'
    success_url = reverse_lazy('matrix-list')

# Passport Views
class PassportListView(ListView):
    model = Passport
    template_name = 'passport_list.html'
    context_object_name = 'passports'
    ordering = ['-add_date']

class PassportDetailView(DetailView):
    model = Passport
    template_name = 'passport_detail.html'

class PassportCreateView(CreateView):
    model = Passport
    # form_class = PassportForm
    template_name = 'passport_form.html'
    success_url = reverse_lazy('passport-list')

class PassportUpdateView(UpdateView):
    model = Passport
    # form_class = PassportForm
    template_name = 'passport_form.html'
    success_url = reverse_lazy('passport-list')

class PassportDeleteView(DeleteView):
    model = Passport
    template_name = 'passport_confirm_delete.html'
    success_url = reverse_lazy('passport-list')

# Scheme Views
class SchemeListView(ListView):
    model = Scheme
    template_name = 'scheme_list.html'
    context_object_name = 'schemes'
    ordering = ['-creation_date']

class SchemeDetailView(DetailView):
    model = Scheme
    template_name = 'scheme_detail.html'

class SchemeCreateView(CreateView):
    model = Scheme
    # form_class = SchemeForm
    template_name = 'scheme_form.html'
    success_url = reverse_lazy('scheme-list')

class SchemeUpdateView(UpdateView):
    model = Scheme
    # form_class = SchemeForm
    template_name = 'scheme_form.html'
    success_url = reverse_lazy('scheme-list')

class SchemeDeleteView(DeleteView):
    model = Scheme
    template_name = 'scheme_confirm_delete.html'
    success_url = reverse_lazy('scheme-list')

# Home View
def home(request):
    latest_news = News.objects.order_by('-created_at')[:5]
    programs_count = EducationalProgram.objects.count()
    matrices_count = Matrix.objects.count()
    passports_count = Passport.objects.count()
    
    context = {
        'latest_news': latest_news,
        'programs_count': programs_count,
        'matrices_count': matrices_count,
        'passports_count': passports_count,
    }
    
    return render(request, 'home.html', context)