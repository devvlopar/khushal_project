from django.shortcuts import render

# Create your views here.
def seller_index(request):
    #condition is given because we want to varify that seller has 
    # logged in or not
    try:
        request.session['seller_email']
        return render(request, 'seller_index.html')
    except:
        return render(request, 'seller_login.html')


def seller_register(request):
    if request.method == 'GET':
        return render(request, 'seller_register.html')
    else:
        try:
            Buyer.objects.get(email = request.POST['email'])
            return render(request, 'seller_register.html', {'msg': 'Email Is Already registered!!'})
        except:
            if request.POST['password'] == request.POST['repassword']:
                s = "Ecommerce Registration!!"
                global user_data
                user_data = [request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password']]
                global c_otp
                c_otp = randrange(1000,9999)
                m = f'Hello User!!\nYour OTP is {c_otp}'
                f = settings.EMAIL_HOST_USER
                r = [request.POST['email']]
                send_mail(s, m, f, r)
                return render(request, 'otp.html', {'msg': 'Check Your MailBox'})
            else:
                return render(request, 'seller_register.html', {'msg': 'Both Passwords do not match!!'})


