# Generated by Django 5.0 on 2023-12-23 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_complaintform_complintid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintform',
            name='ComplintId',
            field=models.CharField(default='CM34172056', max_length=10, null=True),
        ),
    ]
