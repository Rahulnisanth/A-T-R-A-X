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
            "description": "Project Description",
            "start_date": "Started Date",
            "end_date": "Ended Date",
            "project_link": "Project Link / GitHub Link",
        }
        for name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "form-control item",
                    "placeholder": custom_names.get(name),
                    "required": True,
                }
            )


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["body"]
        widgets = {
            "body": forms.Textarea(attrs={"rows": 4, "cols": 5}),
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "form-control item",
                    "required": True,
                    "placeholder": "Add your comments here . . . ",
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
