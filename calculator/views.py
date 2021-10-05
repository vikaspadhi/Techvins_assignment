from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, "calculator/index.html")


def evaluate(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    operator = request.POST['operation']
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2 
    elif operator == '/':
        result = num1 / num2 
    data = {
        "result": result,
    }
    return render(request ,"calculator/index.html",context=data)