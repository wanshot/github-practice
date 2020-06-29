from django.shortcuts import render


def page_detail(request, page_id):
    """ページ詳細

    * https://tracery.jp/s/491028b275ff4a168482d698a536394a
    """
    try:
        page = Page.objects.get(pk=page_id)
    except Page.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'pages/detail.html', {'page': page})
