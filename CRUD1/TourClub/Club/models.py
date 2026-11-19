from django.db import models

MAX_LENGTH = 255


class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование категории')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Route(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование маршрута')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    difficulty = models.CharField(max_length=50, verbose_name='Сложность')
    length_km = models.FloatField(verbose_name='Протяжённость, км')
    duration_days = models.PositiveIntegerField(default=1, verbose_name='Длительность, дней')
    photo = models.ImageField(upload_to='routes/%Y/%m/%d/', null=True, blank=True, verbose_name='Изображение')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return f"{self.name} ({self.difficulty})"

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'


class Instructor(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    photo = models.ImageField(upload_to='instructors/%Y/%m/%d/', null=True, blank=True, verbose_name='Фото')
    experience_years = models.PositiveIntegerField(default=0, verbose_name='Стаж, лет')
    is_active = models.BooleanField(default=True, verbose_name='Работает')

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = 'Инструктор'
        verbose_name_plural = 'Инструкторы'


class Tourist(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = 'Турист'
        verbose_name_plural = 'Туристы'


class Equipment(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование снаряжения')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена аренды')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    photo = models.ImageField(upload_to='equipment/%Y/%m/%d/', null=True, blank=True, verbose_name='Изображение')
    is_available = models.BooleanField(default=True, verbose_name='Доступно')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Снаряжение'
        verbose_name_plural = 'Снаряжение'


class Trip(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название похода')
    route = models.ForeignKey(Route, on_delete=models.PROTECT, verbose_name='Маршрут')
    instructor = models.ForeignKey(Instructor, on_delete=models.PROTECT, verbose_name='Инструктор')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания')
    max_participants = models.PositiveIntegerField(default=10, verbose_name='Макс. участников')
    is_open = models.BooleanField(default=True, verbose_name='Набор открыт')

    def __str__(self):
        return f"{self.name} ({self.start_date})"

    class Meta:
        verbose_name = 'Поход'
        verbose_name_plural = 'Походы'


class Booking(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, verbose_name='Поход')
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE, verbose_name='Турист')
    booking_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата бронирования')
    is_paid = models.BooleanField(default=False, verbose_name='Оплачено')

    def __str__(self):
        return f"Бронь #{self.pk} — {self.tourist}"

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'


class Review(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, verbose_name='Поход')
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE, verbose_name='Турист')
    rating = models.PositiveIntegerField(default=5, verbose_name='Оценка')
    text = models.TextField(verbose_name='Текст отзыва')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отзыва')

    def __str__(self):
        return f"Отзыв от {self.tourist} — {self.rating}/5"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'