from django.views.decorators.http
import require_http_methods
@require_http_methods(["GET","POST"])
def my_view(request):
    pass