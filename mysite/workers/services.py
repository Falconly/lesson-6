from .models import Worker


def get_worker(request):
    worker = Worker.objects.order_by('-id').first()
    if not worker:
        worker = Worker.objects.first()
    return worker
