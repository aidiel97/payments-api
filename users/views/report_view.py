from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.use_cases.generate_user_report import generate_user_report

@api_view(['GET'])
def report_view(request):
    report = generate_user_report()
    return Response({'report': report})
