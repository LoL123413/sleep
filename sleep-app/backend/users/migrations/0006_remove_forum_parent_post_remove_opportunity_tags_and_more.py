# Generated by Django 4.2.5 on 2023-10-16 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_opportunity_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='parent_post',
        ),
        migrations.RemoveField(
            model_name='opportunity',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Waitlist',
        ),
        migrations.DeleteModel(
            name='Forum',
        ),
        migrations.DeleteModel(
            name='Opportunity',
        ),
    ]
