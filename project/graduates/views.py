from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Graduate


def index(request):
    graduates = Graduate.objects.all()
    paginator = Paginator(graduates, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'index.html',
        {'page': page, 'paginator': paginator},
    )


def graduate_view(request, id):
    graduate = get_object_or_404(Graduate, id=id)
    return render(
        request,
        'singlePage.html',
        {'graduate': graduate},
    )
