# Generated by Django 4.2.5 on 2023-10-23 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_forum_parent_post_remove_opportunity_tags_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sleep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=5)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
