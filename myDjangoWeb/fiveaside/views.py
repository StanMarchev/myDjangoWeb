from django.shortcuts import render

# Create your views here.
def five_a_side(request):
    return render(request, 'fiveaside/fiveaside.html')