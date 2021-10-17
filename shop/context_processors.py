from shop.models import Category


def category(request):
    return {'category': Category.objects.filter(status=True)[:6]}
