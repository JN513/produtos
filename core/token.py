import jwt
from produtos.settings import SECRET_KEY, EMAIL_HOST_USER
from time import  time
from django.core.mail import send_mail
from django.contrib.auth.models import User

class Token():

    def __init__(self, request=None, email=None, token=None):
        if email:
            self._id = self.get_id(email)
            self._email = email
        if request:
            self._path = self.get_path(request)
        if token:
            self._token = token
        else:
            token = ""
        self.algoritmo = "HS256"

    def make_token(self, expires_in=3600):
        payload={"confirm_email":self._id, "exp": time()+expires_in}
        self._token = jwt.encode(payload,SECRET_KEY,self.algoritmo).decode('utf-8')

        return self._token

    def envia_token_por_email(self):
        body = self._path+"confirm/"+self._token
        send_mail('Confirmação de email', body, EMAIL_HOST_USER, [self._email], fail_silently=False)


    def check_token(self):
        decoded = jwt.decode(self._token,key=SECRET_KEY)['confirm_email']
        return decoded

    def get_id(self, email):
        id=User.objects.filter(email=email).values_list('id',flat=True).get()
        return id

    def get_path(self, request):
        path = request.build_absolute_uri()
        path = path.strip(request.get_full_path())
        path+="/"

        return path
