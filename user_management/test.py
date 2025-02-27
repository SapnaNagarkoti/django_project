from django.http import JsonResponse

def webhook_verify(request):
    if request.method == "GET":
        verify_token = "facebook"  # Same as the one you set in Facebook App
        if request.GET.get("hub.verify_token") == verify_token:
            return JsonResponse({"hub.challenge": request.GET.get("hub.challenge")})
        return JsonResponse({"error": "Verification failed"}, status=403)
