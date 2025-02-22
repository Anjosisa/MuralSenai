# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import AAluno, Cadastro, ACurso, Login, ATurma

class FormLogin(AuthenticationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class FormCadastro(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    PROFISSAO_CHOICES = [
        ('coordenador', 'Coordenador'),
        ('colaborador', 'Colaborador'),
    ]
    profissao = forms.ChoiceField(choices=PROFISSAO_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    criarsenha = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

class FormAluno(forms.Form):
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nome_pai = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nome_mae = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    turma = forms.ModelChoiceField(
        queryset=ATurma.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Selecione uma Turma"
    )

    observacoes = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

class FormCurso(forms.ModelForm):
    class Meta:
        model = ACurso
        fields = ['curso', 'icon']  # Inclua todos os campos que deseja editar

class FormTurma(forms.Form):
    turma = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    periodo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    curso = forms.ModelChoiceField(
        queryset=ACurso.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Selecione um curso"
    )