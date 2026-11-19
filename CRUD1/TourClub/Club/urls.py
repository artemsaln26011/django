from django.urls import path
from django.views.generic import RedirectView

from .views import (
    # Route
    RouteListView,
    RouteDetailView,
    RouteCreateView,
    RouteUpdateView,
    RouteDeleteView,
    # Instructor
    InstructorListView,
    InstructorDetailView,
    InstructorCreateView,
    InstructorUpdateView,
    InstructorDeleteView,
    # Equipment
    EquipmentListView,
    EquipmentDetailView,
    EquipmentCreateView,
    EquipmentUpdateView,
    EquipmentDeleteView,
    # Trip
    TripListView,
    TripDetailView,
    TripCreateView,
    TripUpdateView,
    TripDeleteView,
    # Tourist
    TouristListView,
    TouristDetailView,
    TouristCreateView,
    TouristUpdateView,
    TouristDeleteView,
)


urlpatterns = [
    # ===== Главная → редирект на список маршрутов =====
    path('', RedirectView.as_view(url='/routes/', permanent=False)),

    # ===== Route (Маршруты) =====
    path('routes/', RouteListView.as_view(), name='route_list'),
    path('routes/<int:pk>/', RouteDetailView.as_view(), name='route_detail'),
    path('routes/create/', RouteCreateView.as_view(), name='route_create'),
    path('routes/<int:pk>/update/', RouteUpdateView.as_view(), name='route_update'),
    path('routes/<int:pk>/delete/', RouteDeleteView.as_view(), name='route_delete'),

    # ===== Instructor (Инструкторы) =====
    path('instructors/', InstructorListView.as_view(), name='instructor_list'),
    path('instructors/<int:pk>/', InstructorDetailView.as_view(), name='instructor_detail'),
    path('instructors/create/', InstructorCreateView.as_view(), name='instructor_create'),
    path('instructors/<int:pk>/update/', InstructorUpdateView.as_view(), name='instructor_update'),
    path('instructors/<int:pk>/delete/', InstructorDeleteView.as_view(), name='instructor_delete'),

    # ===== Equipment (Снаряжение) =====
    path('equipment/', EquipmentListView.as_view(), name='equipment_list'),
    path('equipment/<int:pk>/', EquipmentDetailView.as_view(), name='equipment_detail'),
    path('equipment/create/', EquipmentCreateView.as_view(), name='equipment_create'),
    path('equipment/<int:pk>/update/', EquipmentUpdateView.as_view(), name='equipment_update'),
    path('equipment/<int:pk>/delete/', EquipmentDeleteView.as_view(), name='equipment_delete'),

    # ===== Trip (Походы) =====
    path('trips/', TripListView.as_view(), name='trip_list'),
    path('trips/<int:pk>/', TripDetailView.as_view(), name='trip_detail'),
    path('trips/create/', TripCreateView.as_view(), name='trip_create'),
    path('trips/<int:pk>/update/', TripUpdateView.as_view(), name='trip_update'),
    path('trips/<int:pk>/delete/', TripDeleteView.as_view(), name='trip_delete'),

    # ===== Tourist (Туристы) =====
    path('tourists/', TouristListView.as_view(), name='tourist_list'),
    path('tourists/<int:pk>/', TouristDetailView.as_view(), name='tourist_detail'),
    path('tourists/create/', TouristCreateView.as_view(), name='tourist_create'),
    path('tourists/<int:pk>/update/', TouristUpdateView.as_view(), name='tourist_update'),
    path('tourists/<int:pk>/delete/', TouristDeleteView.as_view(), name='tourist_delete'),
]