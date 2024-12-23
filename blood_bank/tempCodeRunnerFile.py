class Recipient2(models.Model):
    
    #user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="recipient")
    username = models.CharField(max_length=100)
    full_name = models.CharField(max_length=255, verbose_name="Full Name")
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    birth_date = models.DateField(verbose_name="Date of Birth")  # Changed 'dob' to 'birth_date'
    address = models.TextField(null=True, blank=True)
    contact = models.CharField(max_length=15, null=True, blank=True)
    nid_number = models.CharField(max_length=20, null=True, blank=True)
    by_date = models.DateField(null=True, blank=True)