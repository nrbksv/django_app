from django.shortcuts import render


# Create your views here.
def calculation(request):
    if request.method == 'GET':
        return render(request, 'calculation.html')
    elif request.method == 'POST':
        num_1 = int(request.POST.get('num_1'))
        num_2 = int(request.POST.get('num_2'))
        action = request.POST.get('action')
        result = None
        if action == '+':
            result = num_1 + num_2
        elif action == '-':
            result = num_1 - num_2
        elif action == '*':
            result = num_1 * num_2
        elif action == '/':
            result = num_1 / num_2
        context = {
            'first': num_1,
            'second': num_2,
            'action': action,
            'result': result,
            'equal': '=',
            'res_label': 'Result:'
        }

        return render(request, 'calculation.html', context)
