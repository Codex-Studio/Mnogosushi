from django.contrib import admin
from rangefilter.filter import DateRangeFilter
from datetime import date, timedelta, datetime
from django.utils.translation import gettext as _
from django.db.models import Sum, Count

from apps.billing.models import Billing, BillingProduct, SaleSummary

# Register your models here.
class CustomDateFieldListFilter(admin.DateFieldListFilter):
    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)
        self.title = _('Дата')
        self.links = (
            (_('Сегодня'), {
                self.lookup_kwarg_since: str(date.today()),
            }),
            (_('Вчера'), {
                self.lookup_kwarg_since: str(date.today() - timedelta(days=1)),
                self.lookup_kwarg_until: str(date.today() - timedelta(days=1)),
            }),
            (_('Последние 7 дней'), {
                self.lookup_kwarg_since: str(date.today() - timedelta(days=7)),
            }),
            (_('Последние 30 дней'), {
                self.lookup_kwarg_since: str(date.today() - timedelta(days=30)),
            }),
        )

class ProductTabularInline(admin.TabularInline):
    model = BillingProduct
    extra = 0

@admin.register(SaleSummary)
class SaleSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/sale_summary_change_list.html'
    date_hierarchy = 'created'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            # 'title': ,
            'total': Count('id'),
            'total_sales': Sum('total_price'),
        }

        response.context_data['summary'] = list(
            qs.values('billing_products').annotate(**metrics).order_by('-created')
        )
        print(response)
        print(metrics)

        return response

@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_price', 'address', 'payment_method', 'phone', 'billing_receipt_type', 'payment_code', 'created', 'status')
    search_fields = ('id', 'total_price', 'address', 'payment_method', 'phone', 'billing_receipt_type', 'payment_code', 'created', 'status')
    inlines = [ProductTabularInline]
    list_filter = (('created', DateRangeFilter), ('created', CustomDateFieldListFilter),)  # Добавляем фильтр по дате


@admin.register(BillingProduct)
class BillingProductAdmin(admin.ModelAdmin):
    list_display = ('billing', 'product', 'quantity', 'price', 'status')
    list_filter = (('created', DateRangeFilter), ('created', CustomDateFieldListFilter),)  # Добавляем фильтр по дате
