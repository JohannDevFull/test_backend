from django.db import models
from django.contrib.auth.models import (
  AbstractBaseUser,
  PermissionsMixin,
  BaseUserManager
)



# Create your models here.

class UserManager( BaseUserManager ):
  def create_user( self , email , password , **extra_fields ):
    if not email:
      raise ValueError( 'El campo email es requerido' )
    user = self.model( email = email , **extra_fields  )
    user.set_password(password)
    user.save( using = self._db )

    return user
  
  def create_superuser( self , email , password ):
    user = self.create_user(  email , password  )
    user.is_staff = True
    user.is_superuser = True
    user.save( using = self._db )

    return user


class User( AbstractBaseUser , PermissionsMixin ):
  name = models.CharField( max_length = 255 ) 
  last_name = models.CharField( max_length = 255 )
  email = models.EmailField( unique = True )
  is_active = models.BooleanField( default = True )
  is_staff = models.BooleanField( default = False )

  objects = UserManager()

  USERNAME_FIELD = 'email'