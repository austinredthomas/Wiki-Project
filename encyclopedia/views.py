from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    if not util.get_entry(title):
        return render(request, "encyclopedia/error.html", {
            "message":"404 error: not found."
        })
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

def new(request):
    if request.method == "POST":
        markdown = request.POST['markdown']
        title = request.POST['title']
        entries = util.list_entries()
        for entry in entries:
            if entry == title:
                return render(request, "encyclopedia/error.html", {
                "message":"An entry with this title already exists."
                })
        util.save_entry(title, markdown)
        return render(request, "encyclopedia/title.html", {
            "entry":util.get_entry(title)
        })
    else:
        return render(request, "encyclopedia/new.html")
