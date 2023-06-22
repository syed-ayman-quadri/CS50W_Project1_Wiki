from django.shortcuts import render
from django.http import HttpResponse
from . import util
import markdown2
import random

def convert(title):
    content = util.get_entry(title)
    markdowner = markdown2.Markdown()
    if content != None:
        return markdowner.convert(content)
    else:
        return None

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    html = convert(title)
    if html == None:
        return render(request, "encyclopedia/error.html", {
            'output':'This entry does not exist.'
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            'title':title,
            'content':html
        })
    
def search(request):
    if request.method == 'POST':
        query = request.POST['q']
        html = convert(query)
        if html:
            return render(request, 'encyclopedia/entry.html', {
                'title':query ,
                'content':html
            })
        else:
            list = util.list_entries()
            replies = []
            for entry in list:
                if query.lower() in entry.lower():
                    replies.append(entry)
            return render(request, 'encyclopedia/search.html', {
                'replies':replies
            })
        
def createpage(request):
    if request.method == 'GET':
        return render(request, 'encyclopedia/createpage.html')
    else:
        title = request.POST['title']
        content = request.POST['content']
        if util.get_entry(title):
            return render(request, 'encyclopedia/error.html', {
                'output':'Page already exists'
            })
        else:
            util.save_entry(title, content)
            html = convert(title)
            return render(request, 'encyclopedia/entry.html', {
                'title':title,
                'content':html
            })
        
def edit(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = util.get_entry(title)
        return render(request, 'encyclopedia/edit.html', {
            'title':title,
            'content':content
        })
    
def saved(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html = convert(title)
        return render(request, 'encyclopedia/entry.html', {
            'title': title,
            'content':html
        })

def randomom(request):
    list = util.list_entries()
    randomom_entry = random.choice(list)
    html = convert(randomom_entry)
    return render(request, 'encyclopedia/entry.html', {
        'title':randomom_entry,
        'content': html
    })