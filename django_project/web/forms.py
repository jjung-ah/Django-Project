from django import forms
from web.models import User, Content


class UserForm(forms.ModelForm):
    class Meta:
        model = User  # 사용할 모델
        fields = ['user_name', 'email']  # UserForm에서 사용할 User 모델의 속성
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {
            'subject': '사용자 아이디',
            'content': '사용자 이메일',
        }


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['content']
        labels = {
            'content': '요청사항',
        }