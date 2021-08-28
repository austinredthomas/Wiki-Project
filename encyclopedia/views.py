from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    if not util.get_entry(title):
        return render(request, "encyclopedia/error.html")
    else:
        return render(request, "encyclopedia/title.html", {
            "entry": util.get_entry(title)
    })

def search(request):
    if request.method == "POST":
        q = request.POST['q']
        if not util.get_entry(q):
            return render(request, "encyclopedia/search.html", {
                "q":q,
                "entries":util.list_entries(),
            })
        else:
            return render(request, "encyclopedia/title.html", {
                "entry": util.get_entry(q)
                })
    else:
        return render(request, "encyclopedia/search.html")

