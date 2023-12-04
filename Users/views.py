from django.shortcuts import render

from Users.models import CustomUser

def register_page(request):
    return render(request, 'Users/register_page.html')

def register_action(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        authentication_type = request.POST.get('authentication_type')
        newsletter_consent = request.POST.get('newsletter')
        terms_consent = request.POST.get('terms')
        data_processing_consent = request.POST.get('data_processing')

        # Create the user first without custom fields
        new_user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        # Update custom fields after creating the user
        new_user.phone_number = phone_number
        new_user.authentication_type = authentication_type
        new_user.newsletter_consent = True if newsletter_consent == 'on' else False
        new_user.terms_consent = True if terms_consent == 'on' else False
        new_user.data_processing_consent = True if data_processing_consent == 'on' else False
        new_user.save()

        return render(request, 'Core/index.html')

    return render(request, 'Users/register_page.html')