from django.contrib import admin
from .models import Plan

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['user', 'desired_job', 'desired_region', 'career_gap_years']
