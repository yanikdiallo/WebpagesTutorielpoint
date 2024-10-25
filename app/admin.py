from django.contrib import admin
from .models import (
                    GeneralInfo ,Service,
                     Testimonial,frequentlyQuestion,
                     ContactFormLog
                     )

# Register your models here.
@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display =  [

        'company',
        'location',
        'email',
    ]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description'
    ]
    search_fields =[
        'title'
    ]


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'user_job_title',
        'rating_count',

    ]

    def display_rating_count(self,obj):
        return '*' * obj.rating_count
    
    display_rating_count.short_description ="Rating"


@admin.register(frequentlyQuestion)
class requentlyQuestionAdmin(admin.ModelAdmin):
    list_display =[
        'question',
        'answer',
    ]



@admin.register(ContactFormLog)
class ContactFormLogAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'is_succes',
        'is_error',
        'action_time',
    ]
