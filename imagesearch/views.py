from django.shortcuts import render


def search_upload(request):
    return render(request, 'imagesearch/search_upload.html', {})
