# -*- encoding: utf-8 -*-

from .models import User
from django.contrib import auth
from .models import Contributors

class Validator(object):
    _post = None
    required =[]
    _message = ''

    def __init__(self,post):

        self._post = post

    def is_empty(self,field):
        if field == '' or field is None:
            return True
        return False

    def is_valid(self):

        for field in self.required:
            if self.is_empty(self._post[field]):

                self._message = 'el campo %s no puede ser vacio' % field
                return False

        return True

    def getMessage(self):
        return self._message

class FormRegistroValidator(Validator):

    def is_valid(self):

        if not super(FormRegistroValidator, self).is_valid():
            return False
        #validar que las contraseñas sehan iguales
        if not self._post['password1'] == self._post['password2']:
            self._message = 'Las contraseñas no coinciden'
            return False

        if User.objects.filter(username = self._post[('username')]).exists():
            self._message = 'El nombre de usuario ya esta en uso'
            return False    

        if User.objects.filter(email = self._post[('email')]).exists():
            self._message = 'El correo ya se encuentra registrado'
            return False
        #Por ultimo retornamos que en caso de que todo marche bien es correcto el formulario
        return True

       
class FormLoginValidator(Validator):
    acceso = None

    def is_valid(self):
        if not super(FormLoginValidator, self).is_valid():
            return False

        username = self._post['username']
        password = self._post['password']

        self.acceso = auth.authenticate(username = username, password = password )
        if self.acceso is None:
            self._message = 'Invalid user or password'
            return False
        return True

class FormChangePasswordValidator(Validator):

     def is_valid(self):

        if not super(FormChangePasswordValidator, self).is_valid():
            return False
        #validar que las contraseñas sehan iguales
        if not self._post['password1'] == self._post['password2']:
            self._message = 'Passwords do not match'
            return False
        return True

