from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from medicalapp.views.home import index, CreateMedicalRecordView, UserRecordListView, RecordUpdateView,\
    RecordDetailView, RecordDeleteView, pie_chart, contact, DashboardView

urlpatterns = [
    path('', index, name='home'),
    path('about/', contact, name='contact'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('create-records/', CreateMedicalRecordView.as_view(), name='create-medical-record'),
    path('records/<int:id>/update', RecordUpdateView.as_view(), name='update-medical-record'),
    path('records/<int:pk>/delete', RecordDeleteView.as_view(), name='delete-medical-record'),
    path('user-record/', UserRecordListView.as_view(), name='medical-record-list'),
    path('record-detail/<int:id>/', RecordDetailView.as_view(), name='medical-record-detail'),
    path('pie-chart/', pie_chart, name='pie-chart'),

]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
