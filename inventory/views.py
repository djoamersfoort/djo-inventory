from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET
from .models import Item, Location, Property
import base64
import imghdr
import operator
from functools import reduce
from django.db.models import Q


@require_GET
def v1_items(request):
    items = Item.objects.all()

    results = []
    for item in items:
        results.append({
            "id": item.id,
            "name": item.name,
            "description": item.description,
            "location": item.location.name,
            "location_id": item.location.id,
            "url": item.url
        })

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
            "url": item.url,
            "properties": [prop.name for prop in item.properties.all()]
        }
    }
    return JsonResponse(data=result)


@require_GET
def v1_item_search(request, keyword):
    try:
        keywords = keyword.split()
        query = reduce(operator.and_,
                       [Q(name__icontains=word) | Q(description__icontains=word) | Q(properties__name__icontains=word)
                        for word in keywords])
        items = Item.objects.filter(query).distinct()
    except Item.DoesNotExist:
        return JsonResponse({'result': 'No items were found!'})

    results = []
    for item in items:
        results.append({
            "id": item.id,
            "name": item.name,
            "description": item.description,
            "location": item.location.name,
            "location_description": item.location.description,
            "location_id": item.location.id,
            "url": item.url,
            "properties": [prop.name for prop in item.properties.all()]
        })

    json_result = {'result': 'ok',
                   'items': results}

    return JsonResponse(data=json_result)


# @require_http_methods(['GET', 'POST', 'DELETE'])
@require_GET
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


@require_GET
def v1_location_by_id(request, location_id):
    try:
        location = Location.objects.get(pk=location_id)
    except Location.DoesNotExist:
        return JsonResponse(data={'result': 'No such location!'}, status=404)

    b64_photo = None
    if location.photo is not None:
        b64_photo = base64.encodebytes(location.photo).decode('ascii')

    result = {
        'result': 'ok',
        'location': {
            "id": location.id,
            "name": location.name,
            "description": location.description,
            "photo": b64_photo
        }
    }
    return JsonResponse(data=result)


@require_GET
def v1_location_photo(request, location_id):
    try:
        location = Location.objects.get(pk=location_id)
    except Location.DoesNotExist:
        return JsonResponse(data={'result': 'No such location!'}, status=404)

    if location.photo is None:
        return JsonResponse(data={'result': 'This location does not have a valid photo!'}, status=404)

    image_type = imghdr.what('', location.photo)
    if image_type is None:
        return JsonResponse(data={'result': 'This location does not have a valid photo!'}, status=404)

    return HttpResponse(content_type='image/{0}'.format(image_type), content=location.photo)


@require_GET
def v1_properties(request):
    if request.method == 'GET':
        props = Property.objects.all()
        result = []
        for prop in props:
            result.append({
                "id": prop.id,
                "name": prop.name
            })
        return JsonResponse(data={'result': 'ok', 'properties': result})
