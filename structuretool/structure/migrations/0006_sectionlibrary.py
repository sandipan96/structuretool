# Generated by Django 3.1.7 on 2021-03-10 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0005_auto_20210304_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionLibrary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(max_length=10)),
                ('profileCodeInner', models.CharField(max_length=10)),
                ('profileCodeOuter', models.CharField(max_length=10)),
                ('addReinfInner', models.CharField(max_length=10)),
                ('addReinfOuter', models.CharField(max_length=10)),
                ('addInserts', models.CharField(max_length=3)),
                ('drawing', models.ImageField(default='default.jpg', upload_to='section_pics')),
            ],
        ),
    ]
