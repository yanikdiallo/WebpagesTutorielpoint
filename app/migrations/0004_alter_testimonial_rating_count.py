# Generated by Django 5.0 on 2024-10-22 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='rating_count',
            field=models.IntegerField(choices=[(1, 'Un'), (2, 'Deux'), (3, 'Trois'), (4, 'Four')]),
        ),
    ]
