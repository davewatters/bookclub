# Generated by Django 3.2 on 2022-03-26 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220325_1846'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={},
        ),
        migrations.AlterModelOptions(
            name='meetup',
            options={'ordering': ['title']},
        ),
        migrations.RenameField(
            model_name='book',
            old_name='updated_on',
            new_name='last_modified',
        ),
        migrations.AlterField(
            model_name='meetup',
            name='meetup_date',
            field=models.DateField(),
        ),
    ]
