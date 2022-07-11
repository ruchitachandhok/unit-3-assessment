from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import Widget
from main_app.forms import WidgetForm


# Create your views here.

# Define the home view
def home(request):
    form = WidgetForm()
    allWidgets = Widget.objects.all()
    print(allWidgets)
    return render(request, 'home.html', {'form':form, 'allWidgets': allWidgets})


def addwidget(request):
  # create a ModelForm instance using the data in request.POST
  form = WidgetForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_widget = form.save(commit=False)
    new_widget.save()
    print(new_widget)
  return redirect('home')

def deletewidget(request, widget_id):
    widget = Widget.objects.get(id=widget_id)
    widget.delete()
    print(widget)
    return redirect('home')
  