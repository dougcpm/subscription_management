from django.db import models


class TenantPayment(models.Model):
    STATUS_PENDING = "pending"
    STATUS_PAID = "paid"
    STATUS_FAILED = "failed"
    STATUS_REFUNDED = "refunded"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pendente"),
        (STATUS_PAID, "Pago"),
        (STATUS_FAILED, "Falhou"),
        (STATUS_REFUNDED, "Estornado"),
    ]

    schema_name = models.CharField("Schema do tenant", max_length=100)
    client_name = models.CharField("Nome do cliente", max_length=255, blank=True)
    amount = models.DecimalField("Valor", max_digits=10, decimal_places=2)
    currency = models.CharField("Moeda", max_length=10, default="BRL")
    status = models.CharField("Status", max_length=10, choices=STATUS_CHOICES, default=STATUS_PAID)
    payment_date = models.DateField("Data do pagamento")
    reference = models.CharField("Referência", max_length=100, blank=True)
    notes = models.TextField("Observações", blank=True)
    invoice_file = models.FileField(
        "Nota fiscal (anexo)",
        upload_to="invoices/",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        verbose_name = "Pagamento de tenant"
        verbose_name_plural = "Pagamentos de tenants"
        ordering = ["-payment_date", "-created_at"]

    def __str__(self):
        return f"{self.schema_name} - {self.amount} {self.currency} ({self.status})"

