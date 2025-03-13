from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from .serializers import ContactSerializer
from .models import ContactMessage
@api_view(['POST','GET'])
def contact_form_submission(request):
    serializer = ContactSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()  # Save to database (optional)

        # Send Email
        name = serializer.validated_data['name']
        email = serializer.validated_data['email']
        message = serializer.validated_data['message']

        subject = f"New Contact Form Submission from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(
            subject,
            body,
            "kumarakash0465@gmail.com",  # Sender Email (use your Gmail)
            ["kumarakash0465@gmail.com"],  # Your email to receive the message
            fail_silently=False,
        )

        return Response({"message": "Message sent successfully!"}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
