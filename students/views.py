from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# READ
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

# CREATE
def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'students/form.html', {'form': form})

# UPDATE
def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'students/form.html', {'form': form})

# DELETE
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/delete.html', {'student': student})