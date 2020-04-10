from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from ..filters import Filter
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django_filters.views import FilterView
from django.core.mail import EmailMessage
from django.template.loader import get_template
import sweetify
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from ..forms import MedicalHistoryForm, ContactForm
from ..models import MedicalHistory


User = get_user_model()


def index(request):
    return render(request, 'home.html', {})


def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            name = request.POST.get(
                'name'
                , '')
            email = request.POST.get(
                'email'
                , '')
            message = request.POST.get('message', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'name': name,
                'email': email,
                'message': message,
                }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "TIPSTAR" + '',
                ['tipstar3@gmail.com'],
                headers={'Reply-To': email}
            )
            email.send()
            return redirect('home')

    return render(request, 'contact.html', {'form': form_class})


class DashboardView(FilterView, LoginRequiredMixin):
    model = MedicalHistory
    template_name = 'dashboard.html'
    filterset_class = Filter
    paginate_by = 5
    ordering = ['id']
    strict = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = Filter(self.request.GET, queryset=self.get_queryset())
        query = self.request.GET.copy()
        if 'page' in query:
            del query['page']
        context['queries'] = query
        return context


# post a Medical record
class CreateMedicalRecordView(LoginRequiredMixin, CreateView):
    model = MedicalHistory
    form_class = MedicalHistoryForm
    template_name = 'createrecords.html'
    success_url = reverse_lazy('home')
    context_object_name = 'medicalhistory'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(CreateMedicalRecordView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            sweetify.success(self.request, title='Successfully created job!', text='You have successfully created Medical record', icon='sucsess', button="OK", timer=3000)
            return self.form_valid(form)
        else:
            sweetify.error(self.request, title='Error', text='Unsuccessful. Kindly try again', icon='error', button='Close', timer=5000)
            return self.form_invalid(form)


# List view of Post for a specific user
class UserRecordListView(LoginRequiredMixin, ListView):
    model = MedicalHistory
    template_name = 'user_record.html'
    context_object_name = 'records'
    ordering = ['-created_at']
    paginate_by = 3

    def get_queryset(self):
        user = self.request.user
        return MedicalHistory.objects.filter(user=user).distinct().order_by('-created_at')


class RecordDetailView(DetailView):
    model = MedicalHistory
    template_name = 'record_detail.html'
    context_object_name = 'record'
    pk_url_kwarg = 'id'


# Update a Medical Record
class RecordUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MedicalHistory
    # fields = ['illness', 'symptoms', 'additional_info', 'disability', 'medications']
    form_class = MedicalHistoryForm
    template_name = 'update_form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('medical-record-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        record = self.get_object()
        if self.request.user == record.user:
            return True
        return False


# Delete a Medical History
class RecordDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MedicalHistory
    template_name = 'record_confirm_delete.html'
    success_url = reverse_lazy('medical-record-list')

    def test_func(self):
        record = self.get_object()
        # Only users that created the post are permitted to delete the post
        if self.request.user == record.user:
            return True


def pie_chart(request):
    count = {'Anxiety': 0, 'Arthritis': 0, 'Asthma': 0, 'Anemia': 0, 'Cancer': 0,
             'Corona_virus': 0, 'Diabetes': 0, 'Ebola': 0, 'HIV': 0
             }

    queryset = MedicalHistory.objects.values('illness')
    for entry in queryset:
        for values in entry['illness']:
            count[values] += 1

    labels = [*count.keys()]
    data = [*count.values()]

    return render(request, 'chart.html', {
        'labels': labels,
        'data': data,
    })


def error_404(request, exception):
    data = {}
    return render(request, 'error_404.html', data)


def error_500(request):
    data = {}
    return render(request, 'error_500.html', data)

