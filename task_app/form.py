from django import forms
from .models import studends, teacher



class registerform(forms.ModelForm):
    username=forms.CharField(label="username",max_length=100)
    password=forms.CharField(label="username",max_length=100)

    class Meta:
        model=teacher
        fields='__all__'

    def clean(self):
        cleandata=super().clean()
        username=cleandata.get("username")
        passwor=cleandata.get("password")
        confirm_password=cleandata.get("confirm_password")
        if teacher.objects.filter(username=username).exists():
            raise forms.ValidationError("User already exist")
        if passwor and confirm_password and passwor !=confirm_password:
            raise forms.ValidationError("password not matched")

class loginform(forms.ModelForm):
    username=forms.CharField(label="username",max_length=100)
    password=forms.CharField(label="username",max_length=100)

    class Meta:
        model=teacher
        fields='__all__'

    def clean(self):
        cleandata=super().clean()
        username=cleandata.get("username")
        password=cleandata.get("password")

        if not teacher.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is wrong")

        





class markform(forms.ModelForm):
    name=forms.CharField(label="name",max_length=100)
    subject=forms.CharField(label="subject",max_length=100)
    mark=forms.IntegerField(label="mark")

    class Meta:
        model=studends
        fields='__all__'

    def clean(self):
        cleandata=super().clean()
        name=cleandata.get("name")
        subject=cleandata.get("subject")
        mark=cleandata.get("mark")
        
        if not isinstance(mark,int):
            raise forms.ValidationError("")
        if  not mark > 0 and not mark < 100:
            raise forms.ValidationError("Mark shoud be in 1 to 100")
        if not name.isalpha():
            raise forms.ValidationError("numers not allow in name")
        if not subject.isalpha():
            raise forms.ValidationError("numers not allow in subject")
    
   