def search_name_by_class(name, Klass):
    return Klass.objects.filter(name__iexact=name)
