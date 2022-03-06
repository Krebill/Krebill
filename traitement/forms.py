from django.forms import ModelForm
from .models import *


class Projetform(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'thumbnail', 'body']
    
    def __init__(self,*args,**kwargs):
        super(Projetform, self).__init__(*args,**kwargs)
        
        self.fields['title'].widget.attrs.update(
            {'class':'form-control','placeholder':'Titre'})
        
        self.fields['thumbnail'].widget.attrs.update()
        
        self.fields['body'].widget.attrs.update(
            {'class':'form-control','placeholder':'Commentaires ....'})

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['nom', 'email', 'sujet', 'message']
    
    def __init__(self,*args,**kwargs):
        super(MessageForm, self).__init__(*args,**kwargs)
        
        self.fields['nom'].widget.attrs.update(
            {'class':'form-control','placeholder':'nom'})
        self.fields['email'].widget.attrs.update(
            {'class':'form-control','placeholder':'ex:xxxxxxx@gmail.com'})
        self.fields['sujet'].widget.attrs.update(
            {'class':'form-control','placeholder':'sujet'})
        self.fields['message'].widget.attrs.update(
            {'class':'form-control','placeholder':'message'})
        
class SkillForm(ModelForm):
    class Meta:
        model = skill
        fields = '__all__'
    
    def __init__(self,*args,**kwargs):
        super(SkillForm, self).__init__(*args,**kwargs)
        
        self.fields['title'].widget.attrs.update(
            {'class':'form-control'})
        self.fields['body'].widget.attrs.update(
            {'class':'form-control'})
        

class EndoForm(ModelForm):
    class Meta:
        model = Endocement
        fields = '__all__'
        exclude = ['featured','approuvé']
    
    def __init__(self,*args,**kwargs):
        super(EndoForm, self).__init__(*args,**kwargs)
        
        self.fields['nom'].widget.attrs.update(
            {'class':'form-control'})
        self.fields['body'].widget.attrs.update(
            {'class':'form-control'})
        
class CommentForm(ModelForm):
    class Meta:
        model = comment
        fields = '__all__'
        exclude = ['projet']
    
    def __init__(self,*args,**kwargs):
        super(CommentForm, self).__init__(*args,**kwargs)        
        self.fields['nom'].widget.attrs.update(
            {'class':'form-control'})
        self.fields['body'].widget.attrs.update(
            {'class':'form-control'})
        
        
        