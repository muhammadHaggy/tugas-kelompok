from django import forms

class FormGalangDana(forms.Form):
    OPTIONS = (
        ('', '--Pilih--'),
        ('Makanan', 'Makanan'),
        ('Pendidikan', 'Penyuluhan Pendidikan Gizi')
    )
    tipe = forms.ChoiceField(required=True,
                              choices=OPTIONS,
                              label='Tipe Galang Dana',
                              widget=forms.Select(attrs={'class': 'form-select form-select-sm',
                                                         'aria-label': '.form-select-sm example'}))
    judul = forms.CharField(required=True, 
                            max_length=50,
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'contoh: Bantu Pangan Korban Letusan Gunung Semeru'}))
    deskripsi = forms.CharField(required=True,
                                widget=forms.Textarea(attrs={'class': 'form-control',
                                                             'rows': '3',
                                                             'placeholder': 'kamu bisa ceritakan apa yang membuat kamu ingin membuka galang dana ini'}))
    target = forms.IntegerField(required=True,
                                label='Dana yang Dibutuhkan',
                                widget=forms.NumberInput(attrs={'class': 'form-control'}))
    foto = forms.ImageField(required=True,
                            widget=forms.FileInput(attrs={'class': 'form-control'}))