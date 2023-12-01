from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from random import randrange
import markdown2

from . import util

def edit(request, edit):
    if request.method == "POST":
        content = request.POST.get("new_content")
        util.save_entry(edit, content)
        return HttpResponseRedirect("/wiki/" + edit)
    f = util.get_entry(edit)
    return render(request, "encyclopedia/edit.html", {
        "title": edit,
        "content": f
    })


def entry(request, title):
    if util.get_entry(title) == None:
        return HttpResponse("Error page not found")
    f = markdown2.markdown(util.get_entry(title))
    return render(request, "encyclopedia/entry.html", {
        "content": f,
        "title": title
    })
    

def index(request):
    if request.method == "POST":
        search = str(request.POST.get("q")).lower()
        entries = util.list_entries()
        entries = [x.lower() for x in entries]
        if search in entries:
            return HttpResponseRedirect("/wiki/" + search)
        return HttpResponseRedirect("/wiki/search/" + search)       
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def new(request):
    if request.method == "POST":
        title = request.POST.get("new_title")
        content = request.POST.get("new_content")
        entries = util.list_entries()
        entries = [x.lower() for x in entries]
        if title.lower() in entries:
            return HttpResponse("Error entry already exists")
        util.save_entry(title, content)
        return HttpResponseRedirect("/wiki")
    return render(request, "encyclopedia/new.html")


def random(request):
    entries = util.list_entries()
    i = randrange(len(entries))
    return HttpResponseRedirect("/wiki/" + entries[i])


def search(request, search):
    return render(request, "encyclopedia/search.html", {
        "entries": util.list_entries(),
        "search": search
    })

