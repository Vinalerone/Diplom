from rest_framework import serializers
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

class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = '__all__'
        read_only_fields = ('id',)

class HeadOfProgramSerializer(serializers.ModelSerializer):
    id_Institute = InstituteSerializer(read_only=True)
    id_Institute_id = serializers.PrimaryKeyRelatedField(
        queryset=Institute.objects.all(),
        source='id_Institute',
        write_only=True,
        required=True
    )

    class Meta:
        model = Head_of_the_educational_program
        fields = '__all__'
        read_only_fields = ('id',)

class NewsSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = News
        fields = '__all__'
        read_only_fields = ('id', 'created_at')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ('id',)

class DepartmentSerializer(serializers.ModelSerializer):
    id_institute = InstituteSerializer(read_only=True)
    id_institute_id = serializers.PrimaryKeyRelatedField(
        queryset=Institute.objects.all(),
        source='id_institute',
        write_only=True,
        required=True
    )

    class Meta:
        model = Department
        fields = '__all__'
        read_only_fields = ('id_department',)

class EducationalProgramSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        source='department',
        write_only=True,
        required=True
    )

    head = HeadOfProgramSerializer(read_only=True)
    head_id = serializers.PrimaryKeyRelatedField(
        queryset=Head_of_the_educational_program.objects.all(),
        source='head',
        write_only=True,
        required=False,
        allow_null=True
    )

    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = EducationalProgram
        fields = '__all__'
        read_only_fields = ('id_program',)
        extra_kwargs = {
            'status': {'write_only': True}
        }

class MatrixSerializer(serializers.ModelSerializer):
    educational_program = EducationalProgramSerializer(read_only=True)
    educational_program_id = serializers.PrimaryKeyRelatedField(
        queryset=EducationalProgram.objects.filter(status='development'),
        source='educational_program',
        write_only=True,
        required=True
    )

    licensing_employee = EmployeeSerializer(read_only=True)
    licensing_employee_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(),
        source='licensing_employee',
        write_only=True,
        required=False,
        allow_null=True
    )

    assessment_display = serializers.CharField(source='get_assessment_display', read_only=True)
    add_date = serializers.DateField(format="%Y-%m-%d", read_only=True)
    check_date = serializers.DateField(format="%Y-%m-%d", required=False, allow_null=True)

    class Meta:
        model = Matrix
        fields = '__all__'
        read_only_fields = ('id_matrix', 'add_date')
        extra_kwargs = {
            'assessment': {'write_only': True}
        }

class PassportSerializer(serializers.ModelSerializer):
    educational_program = EducationalProgramSerializer(read_only=True)
    educational_program_id = serializers.PrimaryKeyRelatedField(
        queryset=EducationalProgram.objects.filter(status='development'),
        source='educational_program',
        write_only=True,
        required=True
    )

    licensing_employee = EmployeeSerializer(read_only=True)
    licensing_employee_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.filter(position__icontains='лицензирования'),
        source='licensing_employee',
        write_only=True,
        required=False,
        allow_null=True
    )

    assessment_display = serializers.CharField(source='get_assessment_display', read_only=True)
    add_date = serializers.DateField(format="%Y-%m-%d", read_only=True)
    check_date = serializers.DateField(format="%Y-%m-%d", required=False, allow_null=True)

    class Meta:
        model = Passport
        fields = '__all__'
        read_only_fields = ('id_matrix', 'add_date')
        extra_kwargs = {
            'assessment': {'write_only': True}
        }

class SchemeSerializer(serializers.ModelSerializer):
    educational_program = EducationalProgramSerializer(read_only=True)
    educational_program_id = serializers.PrimaryKeyRelatedField(
        queryset=EducationalProgram.objects.filter(status='development'),
        source='educational_program',
        write_only=True,
        required=True
    )

    responsible_employee = EmployeeSerializer(read_only=True)
    responsible_employee_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.filter(position__icontains='лицензирования'),
        source='responsible_employee',
        write_only=True,
        required=False,
        allow_null=True
    )

    status_display = serializers.CharField(source='get_status_display', read_only=True)
    creation_date = serializers.DateField(format="%Y-%m-%d", read_only=True)
    approval_date = serializers.DateField(format="%Y-%m-%d", required=False, allow_null=True)

    class Meta:
        model = Scheme
        fields = '__all__'
        read_only_fields = ('id_scheme', 'creation_date')
        extra_kwargs = {
            'status': {'write_only': True}
        }