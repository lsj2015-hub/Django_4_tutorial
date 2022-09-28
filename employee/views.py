from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Employee, BlogPosts
# Create your views here.

def index(request):
  my_employees = Employee.objects.all().order_by('name')
  template = loader.get_template('employee/index.html')
  context = {
    'my_employees': my_employees
  }
  return HttpResponse(template.render(context, request))

def create(request):
  template = loader.get_template('employee/create_page.html')
  return HttpResponse(template.render({}, request))

def create_data(request):
  name = request.POST['name']
  title = request.POST['title']
  new_employee = Employee(name=name, title=title)
  new_employee.save()
  return HttpResponseRedirect(reverse('employee'))

def delete(request, id):
  delete_employee = Employee.objects.get(id=id)
  delete_employee.delete()
  return HttpResponseRedirect(reverse('employee'))

def update(request, id):
  update_employee = Employee.objects.get(id=id)
  template = loader.get_template('employee/update_page.html')
  context = {
    'Employee': update_employee
  }
  return HttpResponse(template.render(context, request))
 
def update_data(request, id):
  update_name = request.POST['name']
  update_title = request.POST['title']
  update_employee = Employee.objects.get(id=id)
  update_employee.name = update_name
  update_employee.title = update_title
  update_employee.save()
  return HttpResponseRedirect(reverse('employee'))

def blog(request):
  posts = BlogPosts.objects.all()
  featured_posts = BlogPosts.objects.filter(featured=True)
  template = loader.get_template('employee/blog.html')
  context = {
    'posts': posts,
    'featured_posts': featured_posts
  }

  return HttpResponse(template.render(context, request))

def detail_page(request, id):
  detail_post = BlogPosts.objects.get(id=id)
  template = loader.get_template('employee/detail_page.html')
  context = {
    'post': detail_post
  }
  return HttpResponse(template.render(context, request))
