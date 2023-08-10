from django.contrib import admin
from .models import Attendance,StudentExtra,TeacherExtra,Notice, Subject, Marksheet, MidtermResult
# Register your models here. (by sumit.luv)
class StudentExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentExtra, StudentExtraAdmin)

class TeacherExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(TeacherExtra, TeacherExtraAdmin)

# class MidtermResultAdmin(admin.ModelAdmin):
#     pass  
# admin.site.register(MidtermResult, MidtermResultAdmin)
admin.site.register(MidtermResult)

class AttendanceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Attendance, AttendanceAdmin)

class NoticeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Notice, NoticeAdmin)

admin.site.register(Subject)

admin.site.register(Marksheet)
