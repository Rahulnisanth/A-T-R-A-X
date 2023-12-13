from django.forms import ModelForm
from .models import *
from django import forms


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "media",
            "domain",
            "name",
            "description",
            "start_date",
            "end_date",
            "project_link",
        ]

    media = forms.FileField(widget=forms.FileInput(attrs={"id": "custom-file-input"}))

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        custom_names = {
            "domain": "Domain",
            "name": "Project Title",
            "description": "Description",
            "start_date": "Started Date",
            "end_date": "Ending Date",
            "project_link": "Project Link",
        }
        for name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "form-control item",
                    "placeholder": custom_names.get(name),
                    "required": True,
                }
            )


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = [
            "role",
            "company_name",
            "average_salary",
            "location",
            "mode",
            "experience",
            "description",
            "qualification",
            "contact",
            "email",
            "related_link",
        ]

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        custom_names = {
            "role": "Job Role",
            "company_name": "Company Name",
            "average_salary": "Average Salary",
            "location": "Location",
            "mode": "Mode",
            "experience": "Minimum Experience",
            "description": "About Job & Role",
            "qualification": "Minimum Qualification",
            "contact": "Contact Number",
            "email": "Contact Email",
            "related_link": "Any Related Links",
        }
        for name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "form-control item",
                    "placeholder": custom_names.get(name),
                    "required": True,
                }
            )
