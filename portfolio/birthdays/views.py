from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Birthday
from .serializers import BirthdaySerializer


@api_view(["GET", "POST"])
def birthdays_list(request):
    if request.method == "GET":
        birthdays = Birthday.objects.all().order_by("date")
        serializer = BirthdaySerializer(birthdays, many=True)
        return Response(serializer.data)

    # POST
    serializer = BirthdaySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"]) 
def birthday_delete(request, pk: int):
    try:
        obj = Birthday.objects.get(pk=pk)
    except Birthday.DoesNotExist:
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"]) 
def birthdays_stats(request):
    today = timezone.localdate()
    total = Birthday.objects.count()
    this_month = Birthday.objects.filter(date__month=today.month).count()
    return Response({"total": total, "this_month": this_month})


@api_view(["GET"]) 
def birthdays_today(request):
    today = timezone.localdate()
    qs = Birthday.objects.filter(date__month=today.month, date__day=today.day).order_by("date")
    serializer = BirthdaySerializer(qs, many=True)
    return Response(serializer.data)

