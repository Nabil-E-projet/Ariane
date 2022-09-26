# Generated by Django 3.2.15 on 2022-09-25 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True,
                 max_length=25000, null=True, verbose_name='Name')),
                ('comments', models.CharField(blank=True,
                 max_length=25000, null=True, verbose_name='Comments')),
                ('created_at', models.DateTimeField(
                    auto_now_add=True, verbose_name='Created At')),
            ],
            options={
                'verbose_name': 'User Comments',
            },
        ),
    ]