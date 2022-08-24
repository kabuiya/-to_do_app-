
from .models import Activities
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ActivitySerializer
from rest_framework import status


@api_view(['GET', 'POST'])
def to_do(request):
    if request.method == 'GET':
        things = Activities.objects.all()
        serializer = ActivitySerializer(things, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'key': 'value'}, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def to_do_update(request, pk):
    try:
        thing = Activities.objects.get(id=pk)
    except Activities.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ActivitySerializer(thing, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ActivitySerializer(thing, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        thing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
