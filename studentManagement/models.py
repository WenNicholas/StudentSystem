from django.db import models
from datetime import datetime

# Create your models here.
# 课程表
class CourseModel(models.Model):
    stu_id = models.CharField(max_length=15, verbose_name='学生id')
    course = models.CharField(max_length=30, verbose_name='课程')
    grade = models.IntegerField(default=60, verbose_name='分数')
    class Meta():
        db_table = 'new_course'
    def __str__(self):
        return '学生Id：  课程：  分数： '.format(self.stu_id, self.course, self.grade)

# 学生信息表
class StudentInformationModel(models.Model):
    user_id = models.CharField(max_length=15, verbose_name='用户id')
    stu_id = models.CharField(max_length=15,verbose_name='学生id')
    stu_name = models.CharField(max_length=30, verbose_name='学生姓名')
    stu_phone = models.CharField(max_length=20, verbose_name='学生电话')
    stu_address = models.CharField(max_length=30, verbose_name='学生地址')
    stu_faculty = models.CharField(max_length=20, verbose_name='院系')
    stu_major = models.CharField(max_length=30, verbose_name='专业')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    update_time = models.DateTimeField(auto_now=True, verbose_name='最后修改日期')
    time_test = models.DateTimeField(default=datetime.now)
    # 取消外键（外键是可用的）
    # stu_course = models.ForeignKey('CourseModel', on_delete=True)
    class Meta():
        db_table = 'new_studentinformation'

# 学生用户名密码表
class StudentModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=10, verbose_name='用户名')
    password = models.CharField(max_length=10, verbose_name='密码')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    update_time = models.DateTimeField(auto_now=True, verbose_name='最后修改日期')
    time_test = models.DateTimeField(default=datetime.now)
    class Meta():
        db_table = 'new_student'

