from django.db import models
from django.core.validators import RegexValidator, EmailValidator

class Contato(models.Model):
    # Campos OBRIGATÓRIOS
    email = models.EmailField(
        verbose_name="E-mail",
        validators=[EmailValidator(message="E-mail inválido.")],
        unique=True  # Garante que cada e-mail seja único no sistema
    )
    
    telefone = models.CharField(
        max_length=15,
        verbose_name="Telefone",
        validators=[
            RegexValidator(
                r'^\(\d{2}\) \d{4,5}-\d{4}$',
                'Formato inválido. Use: (XX) XXXX-XXXX ou (XX) XXXXX-XXXX.'
            )
        ]
    )

    # Campos OPCIONAIS para colocar no projeto
    telefone_secundario = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="Telefone Secundário",
        validators=[
            RegexValidator(
                r'^\(\d{2}\) \d{4,5}-\d{4}$',
                'Formato inválido. Use: (XX) XXXX-XXXX ou (XX) XXXXX-XXXX.'
            )
        ]
    )

    def __str__(self):
        return f"{self.email} | {self.telefone}"

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"