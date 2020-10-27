from django.shortcuts import redirect


def redirect_to_index(request):
    return redirect('index_url', permanent=True)