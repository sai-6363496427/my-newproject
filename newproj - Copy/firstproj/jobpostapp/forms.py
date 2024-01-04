from django import forms
from jobpostapp.models import job,add_job,comment,subscribe

class sai(forms.ModelForm):
    class Meta:
        model = job
        fields = "__all__"

class kumar(forms.ModelForm):
        class Meta:
            model = add_job
            fields = "__all__"


class com(forms.ModelForm):
     class Meta:
          model = comment
          fields =['content','name','email']
        
class sub(forms.ModelForm):
     class Meta:
          model = subscribe
          fields='__all__'



