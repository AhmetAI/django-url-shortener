from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import Url, CustomURLValidator
from django.http import Http404


def indexView(request):
    if request.method == "POST":
        link = request.POST["link"]

        validate = CustomURLValidator()
        try:
            validate(link)
        except ValidationError:
            error_message = "Invalid URL"
            return render(request, "core/index.html", {"error_message": error_message})

        shortLink = Url(original_url=link)
        shortLink.save()
        return render(request, "core/index.html", {"link": link, "shorten_url": shortLink})
    
    return render(request, "core/index.html")



def shorten_url(request, short_url_slug):
    try:
        url = Url.objects.get(short_url_slug=short_url_slug)
        full_url = url.original_url

        if not full_url.startswith(('http://', 'https://')):
            full_url = 'http://' + full_url
        
        return redirect(full_url)
    except Url.DoesNotExist:
        return redirect("/")


