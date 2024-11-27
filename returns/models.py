# returns/models.py
from django.db import models

class Return(models.Model):
    PRODUCT_CATEGORIES = [
        ('Apparel', 'Apparel'),
        ('Electronics', 'Electronics'),
        # Add more categories as needed
    ]

    RETURN_REASONS = [
        ('Wrong Size', 'Wrong Size'),
        ('Damaged', 'Damaged'),
        ('No Longer Needed', 'No Longer Needed'),
        # Add more reasons as needed
    ]

    product_id = models.CharField(max_length=50)
    product_category = models.CharField(max_length=50, choices=PRODUCT_CATEGORIES)
    return_reason = models.CharField(max_length=50, choices=RETURN_REASONS)
    return_date = models.DateField()
    customer_feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Return {self.product_id} - {self.return_reason}'
