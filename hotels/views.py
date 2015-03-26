# Create your views here.
import datetime
import logging
import random
from django.shortcuts import render
from google.appengine.ext import db
from models import Review
from django.shortcuts import redirect

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def reviews(request):
    reviews = db.GqlQuery("SELECT * FROM Review")
    # logger.info(reviews)
    return render(request, 'reviews.html', {'reviews' : reviews})


def add_review(request):
    if request.method == 'POST':
        items = request.POST
        r = Review(location=items['location'], description=items['review'], title=items['title']) # , star_rating=int(items['stars'])
        r.date = datetime.datetime.now().date()
        r.id = str(random.getrandbits(32))
        r.put()
        return redirect('/reviews')
    else:
        return render(request, 'add_review.html')

def get_review(request, id):
    reviews = db.GqlQuery("SELECT * FROM Review WHERE id = :1", id)
    logging.info("The id is: " + id)
    return render(request, "review.html", {'reviews': reviews})