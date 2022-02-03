from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import User, Results
from django.db.utils import IntegrityError
from django.contrib import messages
import numpy as np

def form(request):
    return render(request, 'form.html')

def results(request):
    return render(request, 'results.html')

def registration(request):
    return render(request, 'registration.html')

def SignUp(request):
    try:
        if request.method == "POST":
            user = User()
            Login = request.POST.get("login")
            Pass = request.POST.get("password")
            if len(Login) > 4 and len(Pass) > 4:
                user.Login = request.POST.get("login")
                user.Password = request.POST.get("password")
                user.save()
                return HttpResponseRedirect("http://127.0.0.1:8000/form")
            else:
                data = {
                    'login': Login,
                    'password': Pass,
                }
                messages.error(request, 'Логин и пароль должны быть больше чем 4 символа')
                return render(request, "registration.html", data)
    except IntegrityError:
        data = {
            'login': Login,
            'password': Pass,
        }
        messages.error(request, 'Пользователь с таким логином уже есть. Попробуйте другой')
        return render(request, "registration.html", data)

def calculate(request):
    if request.method == "POST":
        username = request.POST.get("login")
        password = request.POST.get("password")
        seq1 = request.POST.get("seq1")
        seq2 = request.POST.get("seq2")
        try:
            checkUserLogin = User.objects.get(Login=username, Password=password)
            if checkUserLogin is not None:
                result = levenshtein(seq1, seq2)
                data = {
                    'username': username,
                    'password': password,
                    'seq1': seq1,
                    'seq2': seq2,
                    'ans': result
                }
                tmp = Results.objects.create(sequence1=seq1, sequence2=seq2, result=result, userId=checkUserLogin.id)
                messages.success(request, "Вычисления проведены успешно и добавлены в базу данных")
                return render(request, "form.html", data)
        except User.DoesNotExist:
            messages.error(request, "Неверный логин или пароль")
            data = {
                'username': username,
                'password': password,
            }
            return render(request, "form.html", data)
    return HttpResponseRedirect("http://127.0.0.1:8000/form")

def checkResults(request):
    if request.method == "POST":
        username = request.POST.get("login")
        password = request.POST.get("password")
        try:
            checkUserData = User.objects.get(Login=username, Password=password)
            datas = Results.objects.filter(userId=checkUserData.id)
            return render(request, "results.html", {'datas': datas})
        except User.DoesNotExist:
            messages.error(request, "Неверный логин или пароль")
            data = {
                'login': username,
                'password': password,
            }
            return render(request, "results.html", data)

    return HttpResponseRedirect("http://127.0.0.1:8000/Results")


def levenshtein(seq1, seq2):
    if seq1 is None or seq2 is None:
        message = 'Введены неверные данные'
        return message
    else:
        size_x = len(seq1) + 1
        size_y = len(seq2) + 1
        matrix = np.zeros ((size_x, size_y))
        for x in range(size_x):
            matrix [x, 0] = x
        for y in range(size_y):
            matrix [0, y] = y

        for x in range(1, size_x):
            for y in range(1, size_y):
                if seq1[x-1] == seq2[y-1]:
                    matrix [x,y] = min(
                        matrix[x-1, y] + 1,
                        matrix[x-1, y-1],
                        matrix[x, y-1] + 1
                    )
                else:
                    matrix [x,y] = min(
                        matrix[x-1,y] + 1,
                        matrix[x-1,y-1] + 1,
                        matrix[x,y-1] + 1
                    )
        return (matrix[size_x - 1, size_y - 1])