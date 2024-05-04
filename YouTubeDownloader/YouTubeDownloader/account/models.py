from django.db import models
from django.contrib.auth import models as auth_models
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from YouTubeDownloader.common.model_mixins import TimeStampedModel
from YouTubeDownloader.account.managers import AccountUserManager


class AccountUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin, TimeStampedModel):
    email = models.EmailField(
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )
    
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    
    USERNAME_FIELD = "email"
    
    objects = AccountUserManager()
    
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)