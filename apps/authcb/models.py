from datetime import datetime, timedelta
from django.db import (models, transaction)
from django.utils import timezone
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, Permission, Group)
from django.conf import settings
import jwt


# class PermissionCore(Permission):
#     class Meta:
#         proxy = True
#         verbose_name = 'Permissão'
#         verbose_name_plural = 'Permissões'
#
#
# class GroupCore(Group):
#     class Meta:
#         proxy = True
#         verbose_name = 'Grupo'
#         verbose_name_plural = 'Grupos'


class AuthcbUserManager(BaseUserManager):

    def create_user(self, email, password):
        """
        Creates and saves a User with the given email,and password.
        """
        if not email:
            raise ValueError('O Campo email é obrigatorio')
        try:
            with transaction.atomic():

                user = self.model(
                    email=self.normalize_email(email),
                )
                user.set_password(password)
                user.save(using=self.db)
                return user
        except:
            raise

    def create_superuser(self, email, password='master'):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class AuthcbUser(AbstractBaseUser):
    """
    An abstract core class implementing a fully featured User model with
    admin-compliant permissions.

    """
    help_mail = 'O email será usado como parte das credenciais para acesso ao sistema'

    email = models.EmailField(max_length=255, unique=True, help_text=help_mail)
    is_active = models.BooleanField('Ativo?', default=True)
    # is_staff = models.BooleanField('Membro do time?', default=False)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    is_admin = models.BooleanField('Admin?', default=False)

    # Only for admin interace
    help_active = "Somente usuários ativos podem ter acesso ao sistema"
    help_staff = "Para ter acesso o painel admin é preciso fazer parte do staff"

    groups = models.ManyToManyField(Group, verbose_name='Grupo', blank=True)
    user_permissions = models.ManyToManyField(Permission, blank=True)
    first_name = models.CharField('Nome', max_length=60, blank=True)
    last_name = models.CharField('Sobrenome', max_length=60, blank=True)
    username = models.CharField('Username', max_length=60, blank=True)
    date_joined = models.DateTimeField('Data do registro', default=timezone.now)
    # is_super_user = models.BooleanField('Admin?', default=False)

    USERNAME_FIELD = 'email'

    objects = AuthcbUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
