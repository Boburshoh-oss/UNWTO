from rest_framework.generics import ListAPIView


class MyListAPIView(ListAPIView):
    def paginate_queryset(self, queryset):
        """
        Return a single page of results, or `None` if pagination is disabled.
        """
        if self.paginator is None:
            return None
        if 'all' in self.request.query_params:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)
