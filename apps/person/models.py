from django.db import models
from django.contrib.auth.hashers import make_password

# -------------------------------
# Person & Names
# -------------------------------
class Person(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthdate = models.DateField(null=True, blank=True)
    contact_info = models.TextField(blank=True)

    def __str__(self):
        return f"{self.id} - {self.gender}"


class PersonName(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='names')
    given_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    preferred = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.given_name} {self.last_name}"


# -------------------------------
# Patient
# -------------------------------
class Patient(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='patient')
    medical_record_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.medical_record_number


# -------------------------------
# User
# -------------------------------
class User(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='user')
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    status = models.CharField(max_length=20, default='active')
    last_login = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # hash password before saving
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


# -------------------------------
# Role & Privilege
# -------------------------------
class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Privilege(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='roles')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='users')

    class Meta:
        unique_together = ('user', 'role')

    def __str__(self):
        return f"{self.user.username} - {self.role.name}"


class RolePrivilege(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='privileges')
    privilege = models.ForeignKey(Privilege, on_delete=models.CASCADE, related_name='roles')

    class Meta:
        unique_together = ('role', 'privilege')

    def __str__(self):
        return f"{self.role.name} - {self.privilege.name}"

