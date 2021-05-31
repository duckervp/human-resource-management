# Generated by Django 3.2.3 on 2021-05-31 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_candidate_card_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='qualification',
            field=models.CharField(blank=True, choices=[('DH', 'Đại Học'), ('CD', 'Cao Đẳng'), ('TH', 'Thạc Sĩ'), ('TS', 'Tiến Sĩ')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='department',
            field=models.CharField(choices=[('N', 'Nhân Sự'), ('H', 'Hành Chính'), ('D', 'Đào Tạo')], max_length=1),
        ),
        migrations.AlterField(
            model_name='staff',
            name='role',
            field=models.IntegerField(choices=[(1, 'Quản Lý'), (2, 'Nhân Viên')], default=2),
        ),
        migrations.CreateModel(
            name='WorkDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('month', models.IntegerField(null=True)),
                ('year', models.IntegerField(null=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workDay', to='core.staff')),
            ],
        ),
        migrations.CreateModel(
            name='StaffSalaryBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_salary', models.IntegerField()),
                ('salary_coefficient', models.FloatField()),
                ('allowances_coefficient', models.FloatField()),
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='salaryBase', to='core.staff')),
            ],
        ),
        migrations.CreateModel(
            name='MonthSalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField(null=True)),
                ('year', models.IntegerField(null=True)),
                ('administrative', models.FloatField()),
                ('overtime', models.FloatField()),
                ('dayoff', models.FloatField()),
                ('holiday', models.FloatField()),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monthSalarys', to='core.staff')),
            ],
        ),
    ]
