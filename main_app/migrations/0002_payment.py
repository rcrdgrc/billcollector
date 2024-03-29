# Generated by Django 2.2 on 2019-06-12 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('payment_type', models.CharField(choices=[('C', 'Check-Mail'), ('D', 'Debit Card'), ('E', 'ETF Transfer')], default='C', max_length=1)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Bill')),
            ],
        ),
    ]
