from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    response = "You got here! try /random_word route"
    return HttpResponse(response)


def rand_word(request):
    new_rand_word = get_random_string(14)

    if not "rand_word_counter" in request.session:
        request.session["rand_word_counter"] = 1
    else:
        request.session["rand_word_counter"] += 1

    context = {
        "new_random_word": new_rand_word,
        "random_counter": request.session["rand_word_counter"]
    }

    return render(request, "random_word/index.html", context)


def reset(request):
    request.session.clear()
    return redirect("/random_word")
