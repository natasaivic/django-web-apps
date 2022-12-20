from django.shortcuts import render
from .models import Transaction
from django.views.generic import ListView
from django.core.paginator import Paginator


class TransactionListView(ListView):
    paginate_by = 2
    model = Transaction


def index(request):
    transactions = Transaction.objects.order_by("transaction_date")
    paginator = Paginator(transactions, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template_variables = {
        'page_obj': page_obj,
    }
    return render(request, "transactions_app/index.html", context=template_variables)

