from django.http import JsonResponse


def index(request):
    json = [
    {
        "header": "Title",
        "title": "title 1",
        "price": 10,        "description" : "desc1",
        "image": "image1"


    },
    {
        "header": "Price",
        "title": "title 2",
        "price": 500,
        "description" : "desc2",
        "image" : "image2"


    },

        {
            "header": "Images",
            "title": "title 1",
            "price": 10, "description": "desc1",
            "image": "image1"

        }
    ]
    print(f"returning {json} from index")
    return JsonResponse(json, safe=False)