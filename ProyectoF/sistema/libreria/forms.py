from django import froms
from .models import Libro

class LibroForm forms.class LibroForm(forms.ModelForm):
    
    class Meta:
        model = Libro
        fields = ( '__all__ ' )
