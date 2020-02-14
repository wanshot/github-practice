from django.http import HttpResponse

from .models import Question


def index(request):
    """http://lvh.me:8000/s/29b407fe87774b0496609535eea67ced
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    # outputは以下参照
    # http://lvh.me:8000/s/97a743087f9a472c90e96f44938b3036
    return HttpResponse(output)


def index2():
    # TODO: http://lvh.me:8000/s/45a8c2b829f64c67903ea7f508d8d0fc
    pass
