from django.db import models
from django.urls import reverse

# Create your models here.


class Gener(models.Model):
    name = models.CharField(
        max_length=200, verbose_name="Жанр книг", help_text="Введите жанр книги"
    )

    def __str__(self) -> str:
        return self.name


class Language(models.Model):
    name = models.CharField(
        max_length=20, verbose_name="Язык книги", help_text="Введите язык книги"
    )

    def __str__(self) -> str:
        return self.name


class Publisher(models.Model):
    name = models.CharField(
        max_length=20,
        help_text="Введите наименование издательства",
        verbose_name="Издательства",
    )

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    first_name = models.CharField(
        max_length=100, help_text="Введите имя автора", verbose_name="Имя автора"
    )

    last_name = models.CharField(
        max_length=100,
        help_text="Введите фамилию автора",
        verbose_name="Фамилия автора",
    )

    surname = models.CharField(
        max_length=100,
        help_text="Введите отчество автора(если есть)",
        verbose_name="Фамилия отчество",
        null=True,
        blank=True,
    )

    date_of_birth = models.DateField(
        help_text="Введите дату рождения",
        verbose_name="Дата рождения",
        null=True,
        blank=True,
    )

    about = models.TextField(
        help_text="Введите сведения об авторе",
        verbose_name="Сведения об авторе",
        null=True,
        blank=True,
    )

    photo = models.ImageField(
        upload_to="images",
        help_text="Прекрепите фото автора(если есть)",
        verbose_name="Фото автора",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.last_name


class Book(models.Model):
    title = models.CharField(
        max_length=200,
        help_text="Введите название книги",
        verbose_name="Название книги",
    )

    gener = models.ForeignKey(
        "Gener",
        on_delete=models.CASCADE,
        help_text="Введите жанр для книги",
        verbose_name="Жанр книги",
        null=True,
    )

    language = models.ForeignKey(
        "language",
        on_delete=models.CASCADE,
        help_text="Введите язык для книги",
        verbose_name="Язык книги",
        null=True,
    )

    publisher = models.ForeignKey(
        "Publisher",
        on_delete=models.CASCADE,
        help_text="Выберите язык издательство",
        verbose_name="Издательство",
        null=True,
    )

    year = models.CharField(
        max_length=4, help_text="Введите год издания", verbose_name="Год издания"
    )

    author = models.ManyToManyField(
        "Author",
        help_text="Выберите автора(авторов) книги",
        verbose_name="Автор(аворы) книги",
    )

    summary = models.TextField(
        max_length=1000,
        help_text="Введите краткое описание книги",
        verbose_name="Аннотация книги",
    )

    isbn = models.CharField(
        max_length=13,
        help_text="Должно содержать 13 символов",
        verbose_name="ISBN книги",
    )

    price = models.DecimalField(
        decimal_places=2,
        max_digits=7,
        help_text="Введите цену книги",
        verbose_name="Цена (руб.)",
    )

    photo = models.ImageField(
        upload_to="images",
        help_text="Вставте изображение обложки книги",
        verbose_name="Изображение обложки",
        blank=True, null=True 
    )

    photo_url = models.CharField(
        max_length=200,
        help_text="URL-photo",
        verbose_name="URL-photo",
        blank=True, null=True
    )

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        """Возврощает URL-адрес для доступа к определённому экземпляру книги"""
        return reverse("book_detail", args=[str(self.id)])


class Status(models.Model):
    name = models.CharField(
        max_length=20,
        help_text="Введите статус экземпляра книге",
        verbose_name="Статус экземпляра книге",
    )

    def __str__(self) -> str:
        return self.name


class BookInstance(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE, null=True)

    status = models.ForeignKey(
        "Status",
        on_delete=models.CASCADE,
        null=True,
        help_text="Изменить состояние экземпляра",
        verbose_name="Cтaтyc экземпляра книги",
    )

    inv_nom = models.CharField(
        max_length=20,
        null=True,
        help_text="Введите инвентарный номер экземпляра",
        verbose_name="Инвентарный номер",
    )

    due_back = models.DateField(
        null=True,
        blank=True,
        help_text="Введите конец срока статуса",
        verbose_name="Дaтa окончания статуса",
    )

    # Метoданные
    class Meta:
        """Сортировка экз. книги(по дате окончание(due_back))"""

        ordering = ["due_back"]

    def __str__(self) -> str:
        """Неформальный вывод экз. книги по шаблону"""
        return "%s %s %s" % (self.inv_nom, self.book, self.status)
