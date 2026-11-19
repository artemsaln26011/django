from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Route, Instructor, Equipment, Trip, Tourist
from .forms import (
    RouteForm,
    InstructorForm,
    EquipmentForm,
    TripForm,
    TouristForm,
)


# ============================================================
# Route (Маршруты)
# ============================================================
class RouteListView(ListView):
    model = Route
    template_name = 'routes/route_list.html'
    context_object_name = 'routes'


class RouteDetailView(DetailView):
    model = Route
    template_name = 'routes/route_detail.html'
    context_object_name = 'route'


class RouteCreateView(CreateView):
    model = Route
    form_class = RouteForm
    template_name = 'routes/route_form.html'
    success_url = reverse_lazy('route_list')


class RouteUpdateView(UpdateView):
    model = Route
    form_class = RouteForm
    template_name = 'routes/route_form.html'
    success_url = reverse_lazy('route_list')


class RouteDeleteView(DeleteView):
    model = Route
    template_name = 'routes/route_confirm_delete.html'
    success_url = reverse_lazy('route_list')


# ============================================================
# Instructor (Инструкторы)
# ============================================================
class InstructorListView(ListView):
    model = Instructor
    template_name = 'instructors/instructor_list.html'
    context_object_name = 'instructors'


class InstructorDetailView(DetailView):
    model = Instructor
    template_name = 'instructors/instructor_detail.html'
    context_object_name = 'instructor'


class InstructorCreateView(CreateView):
    model = Instructor
    form_class = InstructorForm
    template_name = 'instructors/instructor_form.html'
    success_url = reverse_lazy('instructor_list')


class InstructorUpdateView(UpdateView):
    model = Instructor
    form_class = InstructorForm
    template_name = 'instructors/instructor_form.html'
    success_url = reverse_lazy('instructor_list')


class InstructorDeleteView(DeleteView):
    model = Instructor
    template_name = 'instructors/instructor_confirm_delete.html'
    success_url = reverse_lazy('instructor_list')


# ============================================================
# Equipment (Снаряжение)
# ============================================================
class EquipmentListView(ListView):
    model = Equipment
    template_name = 'equipment/equipment_list.html'
    context_object_name = 'equipment_items'


class EquipmentDetailView(DetailView):
    model = Equipment
    template_name = 'equipment/equipment_detail.html'
    context_object_name = 'equipment'


class EquipmentCreateView(CreateView):
    model = Equipment
    form_class = EquipmentForm
    template_name = 'equipment/equipment_form.html'
    success_url = reverse_lazy('equipment_list')


class EquipmentUpdateView(UpdateView):
    model = Equipment
    form_class = EquipmentForm
    template_name = 'equipment/equipment_form.html'
    success_url = reverse_lazy('equipment_list')


class EquipmentDeleteView(DeleteView):
    model = Equipment
    template_name = 'equipment/equipment_confirm_delete.html'
    success_url = reverse_lazy('equipment_list')


# ============================================================
# Trip (Походы)
# ============================================================
class TripListView(ListView):
    model = Trip
    template_name = 'trips/trip_list.html'
    context_object_name = 'trips'


class TripDetailView(DetailView):
    model = Trip
    template_name = 'trips/trip_detail.html'
    context_object_name = 'trip'


class TripCreateView(CreateView):
    model = Trip
    form_class = TripForm
    template_name = 'trips/trip_form.html'
    success_url = reverse_lazy('trip_list')


class TripUpdateView(UpdateView):
    model = Trip
    form_class = TripForm
    template_name = 'trips/trip_form.html'
    success_url = reverse_lazy('trip_list')


class TripDeleteView(DeleteView):
    model = Trip
    template_name = 'trips/trip_confirm_delete.html'
    success_url = reverse_lazy('trip_list')


# ============================================================
# Tourist (Туристы)
# ============================================================
class TouristListView(ListView):
    model = Tourist
    template_name = 'tourists/tourist_list.html'
    context_object_name = 'tourists'


class TouristDetailView(DetailView):
    model = Tourist
    template_name = 'tourists/tourist_detail.html'
    context_object_name = 'tourist'


class TouristCreateView(CreateView):
    model = Tourist
    form_class = TouristForm
    template_name = 'tourists/tourist_form.html'
    success_url = reverse_lazy('tourist_list')


class TouristUpdateView(UpdateView):
    model = Tourist
    form_class = TouristForm
    template_name = 'tourists/tourist_form.html'
    success_url = reverse_lazy('tourist_list')


class TouristDeleteView(DeleteView):
    model = Tourist
    template_name = 'tourists/tourist_confirm_delete.html'
    success_url = reverse_lazy('tourist_list')