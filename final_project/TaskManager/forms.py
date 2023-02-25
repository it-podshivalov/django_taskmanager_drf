# from .models import Task, Project, Status
# from django import forms
# from utilities.forms import BootstrapMixin

# class TaskFilterForm(BootstrapMixin, forms.ModelForm):
#     q = forms.CharField(required=False, label="Search")

#     Project = forms.ModelChoiceField(
#         queryset=Project.objects.all(), required=False, to_field_name="Name"
#     )


#     Name = forms.CharField(
#         required=False,
#     )

#     class Meta:
#         model = Task
#         fields = []