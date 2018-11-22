# Generated by Django 2.1.2 on 2018-11-07 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181003_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employeetype',
            field=models.ForeignKey(on_delete='CASCADE', to='app.EmployeeType'),
        ),
    ]
