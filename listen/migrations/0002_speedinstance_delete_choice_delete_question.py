# Generated by Django 5.0.6 on 2024-06-09 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpeedInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recorded_at', models.DateTimeField(verbose_name='Date Recorded')),
                ('speed', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('direction', models.IntegerField(default=0)),
                ('custom_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
