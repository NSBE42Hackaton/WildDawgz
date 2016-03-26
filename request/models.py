from django.db import models
from django.db.models.signals import post_save

OS = (
	('OSX', 'Apple OSX'),
	('Windows', 'Windows'),
	('Linux', 'Linux'),
)

GENDER = (
	('MALE', 'MALE'),
	('FEMALE', 'FEMALE'),
	('NA', 'Choose not to answer'),	
)

ETHNICITY = (
	('Hispanic', 'Hispanic'),
	('White', 'White'),
	('Black', 'Black'),
	('Asian', 'Asian or Pacific Islander'),
	('Native', 'American Indian or Alaskan Native'),
	('NA', 'Choose not to answer'),		
)

GRADE = (
	('FIR', '1st - 4th'),
	('FIF', '5th - 6th'),
	('SIX', '6th - 8th'),
	('EIG', '8th - 12th'),
	('COL', 'College'),
	('NIL', 'NONE'),	
)

DEVICE = (
	('Desktop', 'Desktop'),
	('Laptop', 'Laptop'),
	('Tablet', 'Tablet'),
)

NEED = (
	('School', 'School'),
	('Personal', 'Personal'),
)

SOFTWARE = (
	('PHO', 'Adobe Photoshop'),
	('ILL', 'Adobe Illustrator'),
	('SOL', 'SolidWorks'),
	('XCO', 'Xcode Development'),
	('AND', 'Android Development'),
	('HTM', 'HTML'),
	('JAV', 'Java'),
	('PYT', 'Python'),
	('CPL', 'C++'),
	('UNI', 'Unity'),
)

class RequestParams(models.Model):
	user_Name = models.CharField(max_length=50, blank=False)
	first_Name = models.CharField(max_length=50, blank=False)
	last_Name = models.CharField(max_length=50, blank=False)
	OS = models.CharField(max_length=20, blank=False, choices=OS)
	device = models.CharField(max_length=20, blank=True, choices=DEVICE)
	need = models.CharField(max_length=20, blank=False, choices=NEED)
	software = models.CharField(max_length=20, blank=False, choices=SOFTWARE)
	grade = models.CharField(max_length=20, blank=True, choices=GRADE)
	gender = models.CharField(max_length=20, blank=True, choices=GENDER)
	ethnicity = models.CharField(max_length=20, blank=True, choices=ETHNICITY)
	zip_Code = models.CharField(max_length=10, blank=False)
	time_stamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	class Meta:
		get_latest_by = 'updated'

	def __unicode__(self):
		return self.user_Name