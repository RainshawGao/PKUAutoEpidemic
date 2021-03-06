from django import forms
from .models import Info
from utils.forms import FormMixin


class InfoCreateForm(forms.ModelForm, FormMixin):
    class Meta:
        model = Info
        exclude = ['is_delete']
        widgets = {
            'xh': forms.TextInput(attrs={'class': 'form-control'}),
            'pwd': forms.TextInput(attrs={'class': 'form-control'}),
            'sfhx': forms.Select(attrs={'class': 'form-control'}),
            'dqszdsm': forms.TextInput(attrs={'class': 'form-control'}),
            'dqszddjsm': forms.TextInput(attrs={'class': 'form-control'}),
            'dqszdxjsm': forms.TextInput(attrs={'class': 'form-control'}),
            'dqszdxxdz': forms.TextInput(attrs={'class': 'form-control'}),
            'sfmjqzbl': forms.Select(attrs={'class': 'form-control'}),
            'sfmjmjz': forms.Select(attrs={'class': 'form-control'}),
            'sfxfd': forms.Select(attrs={'class': 'form-control'}),
            'sfxfd_jr': forms.Select(attrs={'class': 'form-control'}),
            'sfzgfxdq': forms.Select(attrs={'class': 'form-control'}),
            'jrtw': forms.TextInput(attrs={'class': 'form-control'}),
            'sfczzz': forms.Select(attrs={'class': 'form-control'}),
            'dwdzxx': forms.TextInput(attrs={'class': 'form-control'}),
            'dwjd': forms.TextInput(attrs={'class': 'form-control'}),
            'dwwd': forms.TextInput(attrs={'class': 'form-control'}),
            'yqzd': forms.Select(attrs={'class': 'form-control'}),
            'jkm': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'serverchan_token': forms.TextInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'pwd': '您的IAAA密码，值得注意的是，您不能开启OTP双重认证。',
            'dqszdsm': '这些信息的获取参见<a href="https://blog.ruixiaolu.com/archives/2020/05/23/79.html">如何获取省市编号</a>',
            'dqszddjsm': '这些信息的获取参见<a href="https://blog.ruixiaolu.com/archives/2020/05/23/79.html">如何获取省市编号</a>',
            'dqszdxjsm': '这些信息的获取参见<a href="https://blog.ruixiaolu.com/archives/2020/05/23/79.html">如何获取省市编号</a>',
            'dqszdxxdz': '这些信息的获取参见<a href="https://blog.ruixiaolu.com/archives/2020/05/23/79.html">如何获取省市编号</a>',
            'dwdzxx': '这些信息的获取参见<a href="https://blog.ruixiaolu.com/archives/2020/05/23/79.html">如何获取定位编号</a>',
            'dwjd': '这些信息的获取参见<a href="https://blog.ruixiaolu.com/archives/2020/05/23/79.html">如何获取定位编号</a>',
            'dwwd': '这些信息的获取参见<a href="https://blog.ruixiaolu.com/archives/2020/05/23/79.html">如何获取定位编号</a>',
            'email': '本项必填',
            'serverchan_token': '请按照<a href="http://sc.ftqq.com/3.version">ServerChan官网教程</a>获取您的SecretKey并填入',
        }
