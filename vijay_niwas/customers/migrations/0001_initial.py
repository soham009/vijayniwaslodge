# Generated by Django 2.1.7 on 2019-05-16 06:40

import customers.models
import datetime
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Entry_No', models.IntegerField(default=customers.models.NewEntry.number, unique=True)),
                ('bill_date', models.DateField()),
                ('Name_of_Visitor', models.CharField(max_length=50)),
                ('No_of_visitors', models.CharField(max_length=50)),
                ('Age', models.CharField(max_length=50)),
                ('Citizenship', django_countries.fields.CountryField(max_length=2)),
                ('Address', models.TextField()),
                ('Arrived_from', models.CharField(max_length=50)),
                ('Departure_to', models.CharField(max_length=50)),
                ('Identity_Proof', models.CharField(choices=[('aadhar card', 'aadhar card'), ('pan card', 'pan card'), ('driving license', 'driving license'), ('passbook', 'passbook'), ('insurance', 'insurance')], max_length=50)),
                ('Identity_Proof_No', models.CharField(max_length=50)),
                ('Purpose_of_Visit', models.CharField(max_length=50)),
                ('Occupation', models.CharField(max_length=50)),
                ('check_in', models.DateTimeField(default=datetime.datetime.now)),
                ('Room_No', models.CharField(choices=[('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29')], default='', max_length=264)),
                ('Total_Amount', models.CharField(max_length=50)),
                ('Advance', models.CharField(max_length=50)),
                ('Remark', models.CharField(blank=True, max_length=50)),
                ('Date_of_bill', models.DateTimeField(auto_now=True)),
                ('Payment_Status', models.CharField(choices=[('PAID', 'PAID'), ('UNPAID', 'UNPAID')], default='', max_length=264)),
                ('images', models.FileField(blank=True, upload_to='')),
                ('check_out', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Customers',
                'verbose_name_plural': 'Fill Form For New Entry',
            },
        ),
        migrations.CreateModel(
            name='passengers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=344)),
                ('Address', models.CharField(default='', max_length=50)),
                ('Gender', models.CharField(default='', max_length=50)),
                ('Age', models.CharField(default='', max_length=50)),
                ('Identity_Proof', models.CharField(default='', max_length=50)),
                ('Identity_Proof_No', models.CharField(default='', max_length=50)),
                ('mobile', models.CharField(default='', max_length=264)),
            ],
            options={
                'verbose_name_plural': 'Customer List for Police Record',
            },
        ),
        migrations.AddField(
            model_name='newentry',
            name='Details_of_Other_Visitors',
            field=models.ManyToManyField(to='customers.passengers'),
        ),
    ]
