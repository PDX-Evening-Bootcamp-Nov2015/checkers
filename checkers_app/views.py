from django.shortcuts import render


#### Create your views here.
def main(request):
    data = {}
    return render(request, 'checkers_app/getgames.html', data)

def accept(request):
    if request.POST:
        num = request.POST
        print(num)

### Helper functions here:

def is_king(piece_id):
    pass
