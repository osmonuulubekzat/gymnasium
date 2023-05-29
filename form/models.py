from django.db import models


# Create your models here.
class Student(models.Model):
    full_name = models.CharField(verbose_name="ФИО", max_length=120)
    image_path = models.ImageField(verbose_name="Сүрөтү", upload_to="images", blank=True)
    gender = models.CharField(verbose_name="Жынысы", max_length=120)
    birth_day = models.CharField(verbose_name="Тууган күнү", max_length=120)
    class_of_year = models.CharField(verbose_name="Бүтүргөн классы", max_length=120)
    region = models.TextField(verbose_name="Жашаган жери", )
    phone_number_student = models.CharField(verbose_name="Окуучунун телефон номери", max_length=120)
    name_of_dud_mum = models.TextField(verbose_name="Ата-энесини аты-жөнү", )
    phone_of_dud_mum = models.CharField(verbose_name="Ата-энесинин телефону", max_length=120)
    name_guardian = models.CharField(verbose_name="Жоопту киши", max_length=120)
    phone_guardian = models.CharField(verbose_name="Жоопту кишинин номери", max_length=120)
    whatsapp = models.CharField(verbose_name="Ватсап номери", max_length=120)
    interesting_lesson = models.TextField(verbose_name="Кызыккан сабагы", )
    success = models.TextField(verbose_name="Ийгиликтери", max_length=120)
    hobbies = models.TextField(verbose_name="Өнөрлөрү(Жөндөмдүүлүктөрү)", max_length=120)
    date_of_saving = models.DateTimeField(verbose_name="", auto_now_add=True, blank=True)

    class Meta:
        verbose_name = "8-Класс"
        verbose_name_plural = "8-Классс"

    def __str__(self):
        return self.full_name

class Student_9(models.Model):
    full_name = models.CharField(verbose_name="ФИО", max_length=120)
    image_path = models.ImageField(verbose_name="Сүрөтү", upload_to="images", blank=True)
    gender = models.CharField(verbose_name="Жынысы", max_length=120)
    birth_day = models.CharField(verbose_name="Тууган күнү", max_length=120)
    class_of_year = models.CharField(verbose_name="Бүтүргөн классы", max_length=120)
    region = models.TextField(verbose_name="Жашаган жери", )
    phone_number_student = models.CharField(verbose_name="Окуучунун телефон номери", max_length=120)
    name_of_dud_mum = models.TextField(verbose_name="Ата-энесини аты-жөнү", )
    phone_of_dud_mum = models.CharField(verbose_name="Ата-энесинин телефону", max_length=120)
    name_guardian = models.CharField(verbose_name="Жоопту киши", max_length=120)
    phone_guardian = models.CharField(verbose_name="Жоопту кишинин номери", max_length=120)
    whatsapp = models.CharField(verbose_name="Ватсап номери", max_length=120)
    interesting_lesson = models.TextField(verbose_name="Кызыккан сабагы", )
    success = models.TextField(verbose_name="Ийгиликтери", max_length=120)
    hobbies = models.TextField(verbose_name="Өнөрлөрү(Жөндөмдүүлүктөрү)", max_length=120)
    date_of_saving = models.DateTimeField(verbose_name="", auto_now_add=True, blank=True)

    class Meta:
        verbose_name = "9-Класс"
        verbose_name_plural = "9-Классс"

    def __str__(self):
        return self.full_name

class Student_10(models.Model):
    full_name = models.CharField(verbose_name="ФИО", max_length=120)
    image_path = models.ImageField(verbose_name="Сүрөтү", upload_to="images", blank=True)
    gender = models.CharField(verbose_name="Жынысы", max_length=120)
    birth_day = models.CharField(verbose_name="Тууган күнү", max_length=120)
    class_of_year = models.CharField(verbose_name="Бүтүргөн классы", max_length=120)
    region = models.TextField(verbose_name="Жашаган жери", )
    phone_number_student = models.CharField(verbose_name="Окуучунун телефон номери", max_length=120)
    name_of_dud_mum = models.TextField(verbose_name="Ата-энесини аты-жөнү", )
    phone_of_dud_mum = models.CharField(verbose_name="Ата-энесинин телефону", max_length=120)
    name_guardian = models.CharField(verbose_name="Жоопту киши", max_length=120)
    phone_guardian = models.CharField(verbose_name="Жоопту кишинин номери", max_length=120)
    whatsapp = models.CharField(verbose_name="Ватсап номери", max_length=120)
    interesting_lesson = models.TextField(verbose_name="Кызыккан сабагы", )
    success = models.TextField(verbose_name="Ийгиликтери", max_length=120)
    hobbies = models.TextField(verbose_name="Өнөрлөрү(Жөндөмдүүлүктөрү)", max_length=120)
    date_of_saving = models.DateTimeField(verbose_name="", auto_now_add=True, blank=True)

    class Meta:
        verbose_name = "10-Класс"
        verbose_name_plural = "10-Классс"

    def __str__(self):
        return self.full_name


class Student_11(models.Model):
    full_name = models.CharField(verbose_name="ФИО", max_length=120)
    image_path = models.ImageField(verbose_name="Сүрөтү", upload_to="images", blank=True)
    gender = models.CharField(verbose_name="Жынысы", max_length=120)
    birth_day = models.CharField(verbose_name="Тууган күнү", max_length=120)
    class_of_year = models.CharField(verbose_name="Бүтүргөн классы", max_length=120)
    region = models.TextField(verbose_name="Жашаган жери", )
    phone_number_student = models.CharField(verbose_name="Окуучунун телефон номери", max_length=120)
    name_of_dud_mum = models.TextField(verbose_name="Ата-энесини аты-жөнү", )
    phone_of_dud_mum = models.CharField(verbose_name="Ата-энесинин телефону", max_length=120)
    name_guardian = models.CharField(verbose_name="Жоопту киши", max_length=120)
    phone_guardian = models.CharField(verbose_name="Жоопту кишинин номери", max_length=120)
    whatsapp = models.CharField(verbose_name="Ватсап номери", max_length=120)
    interesting_lesson = models.TextField(verbose_name="Кызыккан сабагы", )
    success = models.TextField(verbose_name="Ийгиликтери", max_length=120)
    hobbies = models.TextField(verbose_name="Өнөрлөрү(Жөндөмдүүлүктөрү)", max_length=120)
    date_of_saving = models.DateTimeField(verbose_name="", auto_now_add=True, blank=True)

    class Meta:
        verbose_name = "11-Класс"
        verbose_name_plural = "11-Классс"

    def __str__(self):
        return self.full_name

