from django.contrib import admin
from studentManagement.models import StudentInformationModel, CourseModel, StudentModel
# Register your models here.

class StudentInformationLine(admin.TabularInline):
    model = CourseModel
    extra = 3


class StudentInformationAdmin(admin.ModelAdmin):
    # 显示的字段，先后顺序表示显示顺序
    list_display = ['user_id', 'stu_id', 'stu_name', 'stu_phone', 'stu_address', 'stu_faculty', 'stu_major', 'create_time', 'update_time']
    # 以哪个来过滤
    list_filter = ['stu_id', 'stu_name']
    # 以哪个字段来搜索，admin中就会出现一个搜索栏
    search_fields = ['stu_name', 'stu_address', 'stu_faculty', 'stu_major']
    list_per_page = 5

class CourseAdmin(admin.ModelAdmin):
    list_display = ['stu_id', 'course', 'grade']
    # inlines = [StudentInformationLine, ]  # 谁的外键就写在哪边

class StudentAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'username', 'password', 'create_time', 'update_time']
    search_fields = ['user_id', 'username']
    actions_on_top = False
    actions_on_bottom = True

admin.site.register(StudentInformationModel, StudentInformationAdmin)
admin.site.register(CourseModel, CourseAdmin)
admin.site.register(StudentModel, StudentAdmin)
