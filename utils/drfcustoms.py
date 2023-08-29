from rest_framework.response import Response
from rest_framework import status

def get_paginated_response(*, pagination_class, serializer_class, queryset, request, view, status=status.HTTP_200_OK):
    paginator = pagination_class()

    page = paginator.paginate_queryset(queryset, request, view=view)

    if page is not None:
        serializer = serializer_class(page, many=True)
        serializer.context['request'] = request
        return paginator.get_paginated_response(serializer.data)

    serializer = serializer_class(queryset, many=True)

    return Response(data=serializer.data, status=status)