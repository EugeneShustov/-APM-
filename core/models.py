from django.db import models
from django.utils import timezone

class Order(models.Model):
    STATUS_CHOICES = [
        ('ready', 'Готово к работе'),
        ('progress', 'В работе'),
        ('done', 'Готово'),
        ('refused', 'Брак'),
    ]

    number = models.CharField("Номер заказа", max_length=20, unique=True)
    name = models.CharField("Название", max_length=100)
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default='ready')
    start = models.DateTimeField("Начало", null=True, blank=True)
    end = models.DateTimeField("Окончание", null=True, blank=True)

    material = models.CharField("Материал", max_length=100)
    operation_count = models.PositiveIntegerField("Кол-во операций", default=1)
    unit_price = models.DecimalField("Цена за операцию", max_digits=10, decimal_places=2)

    comment = models.TextField("Комментарий", blank=True)
    attachment = models.FileField("Файл", upload_to='attachments/', null=True, blank=True)

    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    @property
    def total_price(self):
        return self.operation_count * self.unit_price

    def take_to_work(self):
        self.status = 'progress'
        self.start = timezone.now()
        self.save(update_fields=['status', 'start'])

    def mark_done(self):
        self.status = 'done'
        self.end = timezone.now()
        self.save(update_fields=['status', 'end'])

    def mark_refused(self):
        self.status = 'refused'
        self.end = timezone.now()
        self.save(update_fields=['status', 'end'])

    def __str__(self):
        return f"{self.number} — {self.name} ({self.get_status_display()})"

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"
        ordering = ['-created_at']
