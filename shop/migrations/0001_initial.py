# Generated by Django 3.2.7 on 2021-10-07 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('slug', models.SlugField(max_length=300, primary_key=True, serialize=False, unique=True)),
                ('create_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=120)),
                ('img', models.ImageField(default='author.png', upload_to='shop/book/author/')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': ' Author',
                'verbose_name_plural': ' Authors',
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('slug', models.SlugField(max_length=300, primary_key=True, serialize=False, unique=True)),
                ('create_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255)),
                ('ISBN', models.CharField(max_length=30)),
                ('year', models.CharField(default=2021, max_length=10)),
                ('price', models.FloatField(default=0)),
                ('discount', models.FloatField(default=0, null=True)),
                ('noPage', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('img', models.ImageField(default='book.png', upload_to='shop/book/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='shop.author')),
            ],
            options={
                'verbose_name': ' Book',
                'verbose_name_plural': ' Books',
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('slug', models.SlugField(max_length=300, primary_key=True, serialize=False, unique=True)),
                ('create_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': ' Category',
                'verbose_name_plural': ' Categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.book')),
            ],
            options={
                'verbose_name': ' Order Detail',
                'verbose_name_plural': ' Orders Details',
                'db_table': 'orderdetails',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True, editable=False)),
                ('price', models.FloatField()),
                ('status', models.CharField(choices=[('Processing', 'Processing'), ('On Hold', 'On Hold'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Refunded', 'Refunded'), ('Failed', 'Failed')], max_length=30)),
                ('OrderDetail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.orderdetails')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.useraddress')),
            ],
            options={
                'verbose_name': ' Order',
                'verbose_name_plural': ' Orders',
                'db_table': 'Order',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='shop.category'),
        ),
    ]
