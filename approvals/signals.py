import django.dispatch

article_approved = django.dispatch.Signal(providing_args=["article_id"])