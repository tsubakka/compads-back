from django.db import models

################################################################################

class ClientType(models.Model):
    client_type = models.TextField(max_length=50)
    class Meta:
        verbose_name = "Client type"
        verbose_name_plural = "Client types"
    def __unicode__(self):
        return self.client_type
    def __str__(self):
        return self.client_type

class Client(models.Model):
    client_type = models.ForeignKey(ClientType, on_delete=models.PROTECT)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    company_name = models.TextField(blank=True, null=True)
    tax_number = models.TextField(blank=True, null=True)
    registration_number = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
    def __unicode__(self):
        if self.client_type_id == 1:
            uc= '%s %s' % (self.first_name, self.last_name)
        else:
            uc= (self.company_name)
        return uc
    def __str__(self):
        if self.client_type_id == 1:
            uc= '%s %s' % (self.first_name, self.last_name)
        else:
            uc= (self.company_name)
        return uc

    def client_name(self):
        if self.client_type_id == 1:
            uc= '%s %s' % (self.first_name, self.last_name)
        else:
            uc= (self.company_name)
        return uc

################################################################################

class PhoneType(models.Model):
    phone_type = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.phone_type
    def __str__(self):
        return self.phone_type

class Phone(models.Model):
    client = models.ForeignKey(Client, related_name="client_phones")
    phone_type = models.ForeignKey(PhoneType, on_delete=models.PROTECT)
    country_code = models.IntegerField(blank=False, null=False)
    area_code = models.IntegerField(blank=False, null=False)
    phone_number = models.IntegerField(blank=False, null=False)
    def __unicode__(self):
        return '+ %s %s %s' % (self.country, self.area_code, self.phone_number)
    def __str__(self):
        return '+ %s %s %s' % (self.country, self.area_code, self.phone_number)

################################################################################

class EmailType(models.Model):
    email_type = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.email_type
    def __str__(self):
        return self.email_type

class Email(models.Model):
    client = models.ForeignKey(Client, related_name='client_emails')
    email_type = models.ForeignKey(EmailType, on_delete=models.PROTECT)
    email_address = models.EmailField(blank=False, null=False)
    def __unicode__(self):
        return self.email_address
    def __str__(self):
        return self.email_address

################################################################################

class AddressType(models.Model):
    address_type = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.address_type
    def __str__(self):
        return self.address_type

class Address(models.Model):
    client = models.ForeignKey(Client, related_name="client_addresses")
    address_type = models.ForeignKey(AddressType)
    country = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    station = models.TextField(blank=True, null=True)
    zip_code = models.IntegerField(blank=False, null=False)
    address1 = models.TextField(blank=True, null=True)
    address2 = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
    def __unicode__(self):
        return '%s %s, %s %s, %s - %s' % (self.zip_code, self.station, self.address1, self.address2 , self.region, self.country )
    def __str__(self):
        return '%s %s, %s %s, %s - %s' % (self.zip_code, self.station, self.address1, self.address2 , self.region, self.country )

################################################################################

class BirthDate(models.Model):
    client = models.OneToOneField(Client, related_name="client_birthdate")
    year = models.IntegerField(blank=False, null=False)
    month = models.IntegerField(blank=False, null=False)
    day = models.IntegerField(blank=False, null=False)
    class Meta:
        verbose_name = "Birth Date"
        verbose_name_plural = "Birth Dates"
    def __unicode__(self):
        return '%s.%s.%s.' % (self.year, self.month, self.day)
    def __str__(self):
        return '%s.%s.%s.' % (self.year, self.month, self.day)

################################################################################
