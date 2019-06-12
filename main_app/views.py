from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bill
from .forms import PaymentForm
from django.http import HttpResponse

# class Bills:
#     def __init__(self, name, company, description, amount):
#         self.name = name
#         self.company = company
#         self.description = description
#         self.amount = amount

# bills = [
#     Bills('Joseph Luchiano', 'T-mobile', 'Owes since 1992', 5000),
#     Bills('Patty Brown', 'Visa', 'Owes since 2015', 45620),
#     Bills('Kellogg Williams', 'Mastercard', 'Owes since 2018', 100),
# ]

class BillCreate(CreateView):
  model = Bill
  fields = '__all__'
  success_url = '/bills/'

class BillUpdate(UpdateView):
  model = Bill
  # Let's make it impossible to rename a bill :)
  fields = ['company', 'description', 'amount']

class BillDelete(DeleteView):
  model = Bill
  success_url = '/bills/'

def bills_index(request):
    bills = Bill.objects.all()
    return render(request, 'bills/index.html', { 'bills': bills })

def bills_detail(request, bill_id):
  bill = Bill.objects.get(id=bill_id)
  payment_form = PaymentForm()
  return render(request, 'bills/detail.html', { 'bill': bill, payment_form: payment_form })

# Define the home view
def home(request):
  return HttpResponse('<h1>Pay Me</h1>') 
# Create your views here.

def about(request):
  return render(request, 'about.html')
