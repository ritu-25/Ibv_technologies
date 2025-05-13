from .forms import AssignmentForm

def assignment_form_context(request):
    return {'form': AssignmentForm()}
