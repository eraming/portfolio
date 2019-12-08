import requests
import jinja2
from django.http import HttpResponse
from django.shortcuts import render, redirect 

# import os
# mailgun_api_key = os.environ["b7a00de6276e48b8c21113c0aea0a3ae-e470a504-9eb0e348"]

def home(request):
    context = {
    "active_link": "home/",
    }
    return render(request, 'home.html', context)

def gallery(request):
    context = {
    "active_link": "gallery/",
    }
    return render(request, 'gallery.html', context)

def projects(request):
    context = {
    "active_link": "projects/",
    }
    return render(request, 'projects.html', context)

def contact(request):
    context = {
    "active_link": "contact/",
    }
    if request.POST:
        send_email(request)
    return render(request, 'contact.html', context)

def github(request):
    # We can also combine Django with APIs. This does an API request, and then
    # renders the HTML template with the response, every time we visit this
    # view.
    response = requests.get('https://api.github.com/users/eraming/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)

def send_email(request):
    name = request.POST["name"]
    email = request.POST["email"]
    message = request.POST["message"]
    mailgun_message(name, email, message)
    return redirect("/")

def mailgun_message(name, email, message):
	return requests.post(
		"https://api.mailgun.net/v3/sandboxad0e4567092d4b7c9d82db09c8b3fc7c.mailgun.org/messages",
		auth=("api","b7a00de6276e48b8c21113c0aea0a3ae-e470a504-9eb0e348"),
		data={"from": (name, email),
			"to": "Era Ming <era.y.ming@gmail.com>",
			"subject": "Hello Era",
			"text": message})
