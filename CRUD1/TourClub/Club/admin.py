from django.contrib import admin
from .models import Category, Route, Instructor, Tourist, Equipment, Trip, Booking, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    pass


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    pass


@admin.register(Tourist)
class TouristAdmin(admin.ModelAdmin):
    pass


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    pass


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass