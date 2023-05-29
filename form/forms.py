from django import forms
# import GeeksModel from models.py
from .models import Student


# create a ModelForm
class Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    # # specify the name of model to use
    # full_name = forms.CharField(label="ФИО", max_length=120)
    # image_path = forms.ImageField()
    # gender = forms.CharField(label="Жынысы", max_length=120)
    # birth_day = forms.CharField(label="Тууган күнү", max_length=120)
    # class_of_year = forms.CharField(label="Бүтүргөн классы", max_length=120)
    # region = forms.CharField(label="Жашаган жери",)
    # phone_number_student = forms.CharField(label="Окуучунун телефон номери", max_length=120)
    # name_of_dud_mum = forms.CharField(label="Ата-энесини аты-жөнү", max_length=120)
    # phone_of_dud_mum = forms.CharField(label="Ата-энесинин телефону", max_length=120)
    # name_guardian = forms.CharField(label="Жоопту киши", max_length=120)
    # phone_guardian = forms.CharField(label="Жоопту кишинин номери", max_length=120)
    # whatsapp = forms.CharField(label="Ватсап номери", max_length=120)
    # interesting_lesson = forms.CharField(label="Кызыккан сабагы", )
    # success = forms.CharField(label="Ийгиликтери", max_length=120)
    # hobbies = forms.CharField(label="Өнөрлөрү(Жөндөмдүүлүктөрү)", max_length=120)
    class Meta:

        model = Student
        exclude = ("date_of_saving",)
        fields = "__all__"
