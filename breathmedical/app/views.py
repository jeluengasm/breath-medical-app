from django.views.generic import TemplateView
from django.core.exceptions import PermissionDenied


class HomeView(TemplateView):
    template_name = 'app/home.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context[""] = 
        return context


class PatientView(TemplateView):
    template_name = 'app/patient.html'
    patient_id = None

    def dispatch(self, request, *args, **kwargs):
        self.patient_id = kwargs.pop('patient_id', None)
        if self.patient_id != 1:
            raise PermissionDenied("Not allowed. This user id doesn't exist")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient_id"] = self.patient_id
        return context

class UserLoginView(TemplateView):
    template_name = 'app/login_form.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
