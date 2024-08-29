from django.shortcuts import render
from django.db.models import Sum  # Import Sum from django.db.models
from .models import Stock  # Import your Stock model

def stock_analysis(request):
    top_performing_stocks = Stock.objects.order_by('-last_quarter_performance')[:10]
    growing_sectors = Stock.objects.values('sector').annotate(total_volume=Sum('daily_trading_volume')).order_by('-total_volume')[:5]

    context = {
        'top_performing_stocks': top_performing_stocks,
        'growing_sectors': growing_sectors,
    }
    return render(request, 'analysis/stock_analysis.html', context)
