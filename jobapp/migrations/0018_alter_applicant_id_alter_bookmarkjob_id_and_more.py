# Generated by Django 4.0.4 on 2022-05-27 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0017_alter_applicant_id_alter_bookmarkjob_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bookmarkjob',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]