from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_http_methods
from .models import Item
from django.db.models import Q


@require_GET
def v1_items(request):
    items = Item.objects.all()

    results = {}
    for item in items:
        result = {
            "name": item.name,
            "description": item.description,
            "location": item.location.name,
            "location_id": item.location.id,
            "url": item.url
        }
        results[item.id] = result

    json_result = {'result': 'ok',
                   'items': results}

    return JsonResponse(data=json_result)


def v1_get_item_by_id(request, item):
    result = {
        'result': 'ok',
        'item': {
            "id": item.id,
            "name": item.name,
            "description": item.description,
            "location": item.location.name,
            "location_description": item.location.description,
            "location_id": item.location.id,
            "url": item.url
        }
    }
    return JsonResponse(data=result)


@require_GET
def v1_item_search(request, keyword):
    try:
        items = Item.objects.get(Q(name__icontains=keyword) | Q(description__icontains=keyword))
    except Item.DoesNotExist:
        return JsonResponse({'result': 'No items were found!'})

    results = {}
    for item in items:
        results[item.id] = {
            "id": item.id,
            "name": item.name,
            "description": item.description,
            "location": item.location.name,
            "location_description": item.location.description,
            "location_id": item.location.id,
            "url": item.url
        }

    json_result = {'result': 'ok',
                   'items': results}

    return  JsonResponse(data=json_result)


@require_http_methods(['GET', 'POST', 'DELETE'])
def v1_item_by_id(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        return JsonResponse(data={'result': 'No such item!'}, status=404)

    if request.method == 'GET':
        return v1_get_item_by_id(request, item)
    #    elif request.method == 'POST':
    #        return v1_post_article_by_id(request, article)
    #    elif request.method == 'DELETE':
    #        return v1_delete_article_by_id(request, article)
    else:
        # Impossible
        return JsonResponse(data={'result': 'huh?'})
