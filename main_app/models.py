from django.db import models
from django.urls import reverse
# Create your models here.


PAY = (
    ('C', 'Check-Mail'),
    ('D', 'Debit Card'),
    ('E', 'ETF Transfer')
)

class Bill(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    amount = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'bill_id': self.id})

class Payment(models.Model):
    date = models.DateField('Due Date')
    payment_type = models.CharField(
        max_length=1,
        choices=PAY,
        default=PAY[0][0]
    )
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)#this will delete everythig behind the key

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_payment_type_display()} on {self.date}"