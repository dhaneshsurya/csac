from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field


class SiteSettings(models.Model):
    college_name_en = models.CharField(max_length=200, default="Chaitanya Science and Arts College")
    college_name_hi = models.CharField(max_length=200, default="चैतन्य विज्ञान एवं कला महाविद्यालय, पामगढ़")
    tagline = models.CharField(max_length=300, default="An Autonomous College, Approved by UGC | Accredited with Grade 'A' by NAAC")
    address_line1 = models.CharField(max_length=200, default="PAMGARH, JANJGIR-CHAMPA (C.G.), 495554")
    address_line2 = models.CharField(max_length=200, default="Affiliated to Shaheed Nandkumar Patel Vishwavidyalaya, Raigarh")
    phone = models.CharField(max_length=20, default="+91-9425540666")
    email = models.EmailField(default="chaitanyapamgarh@gmail.com")
    facebook_url = models.URLField(blank=True, default="https://www.facebook.com/ChaitanyaPamgarh/")
    youtube_url = models.URLField(blank=True, default="https://www.youtube.com/@ChaitanyaCollegePamgarh")
    instagram_url = models.URLField(blank=True)
    google_maps_embed = models.TextField(blank=True)
    established_year = models.IntegerField(default=2001)

    # Logo fields
    college_logo = models.ImageField(upload_to='logos/', blank=True, null=True, verbose_name="College Logo (Header/Footer)")
    college_logo_mobile = models.ImageField(upload_to='logos/', blank=True, null=True, verbose_name="Mobile Logo")
    logo2 = models.ImageField(upload_to='logos/', blank=True, null=True, verbose_name="Logo 2 (NAAC A)")
    logo3 = models.ImageField(upload_to='logos/', blank=True, null=True, verbose_name="Logo 3")
    logo4 = models.ImageField(upload_to='logos/', blank=True, null=True, verbose_name="Logo 4")
    logo5 = models.ImageField(upload_to='logos/', blank=True, null=True, verbose_name="Logo 5")

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.college_name_en

    def get_college_logo(self):
        if self.college_logo:
            return self.college_logo.url
        from django.templatetags.static import static
        return static('assets/csac_pmg.svg')

    def get_logo2(self):
        if self.logo2:
            return self.logo2.url
        from django.templatetags.static import static
        return static('assets/images/logo_naac_a.png')

    def get_logo3(self):
        if self.logo3:
            return self.logo3.url
        from django.templatetags.static import static
        return static('assets/images/logo_2.png')

    def get_logo4(self):
        if self.logo4:
            return self.logo4.url
        from django.templatetags.static import static
        return static('assets/images/logo_3.png')

    def get_logo5(self):
        if self.logo5:
            return self.logo5.url
        from django.templatetags.static import static
        return static('assets/images/logo_4.png')

    def get_mobile_logo(self):
        if self.college_logo_mobile:
            return self.college_logo_mobile.url
        from django.templatetags.static import static
        return static('assets/csac_mobile.svg')


class MarqueeNotice(models.Model):
    text = models.CharField(max_length=300)
    link = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Marquee Notice"

    def __str__(self):
        return self.text[:80]


class BannerSlide(models.Model):
    caption = models.CharField(max_length=300)
    image = models.ImageField(upload_to='banner/', blank=True)
    image_url = models.URLField(blank=True, help_text="Use this for external S3 URLs if no local image")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.caption

    def get_image(self):
        if self.image:
            return self.image.url
        return self.image_url


class AccreditationLogo(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='accreditation/', blank=True)
    image_url = models.URLField(blank=True)
    link = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

    def get_image(self):
        return self.image.url if self.image else self.image_url


class StatCounter(models.Model):
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=20, help_text="e.g. 8000+")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.value} - {self.label}"


class CollegeInfo(models.Model):
    """About section text blocks"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    section = models.CharField(max_length=50, choices=[
        ('about', 'About'),
        ('vision', 'Vision'),
        ('mission', 'Mission'),
        ('governance', 'Governance'),
        ('features', 'Distinctive Features'),
    ])
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "College Info Section"

    def __str__(self):
        return f"{self.section} - {self.title}"


class Leadership(models.Model):
    ROLE_CHOICES = [
        ('principal', 'Principal'),
        ('director', 'Director/Founder'),
        ('vice_principal', 'Vice Principal'),
        ('chairman', 'Chairman'),
    ]
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
    qualification = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='leadership/', blank=True)
    message = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.get_role_display()})"


class Committee(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=250, blank=True, null=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class CommitteeMember(models.Model):
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, related_name='members')
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=200)
    role_in_committee = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class CommitteeActivity(models.Model):
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, related_name='activities')
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='committees/activities/', blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-date']
        verbose_name = "Committee Activity"
        verbose_name_plural = "Committee Activities"

    def __str__(self):
        return f"{self.committee.name} - {self.title}"


class CommitteeGalleryImage(models.Model):
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='committees/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Committee Gallery Image"
        verbose_name_plural = "Committee Gallery Images"

    def __str__(self):
        return f"Gallery Image for {self.committee.name}"



class Policy(models.Model):
    title = models.CharField(max_length=200)
    document = models.FileField(upload_to='policies/', blank=True)
    document_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Policies"

    def __str__(self):
        return self.title


class Achievement(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='achievements/', blank=True)
    image_url = models.URLField(blank=True)
    year = models.IntegerField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-year', 'order']

    def __str__(self):
        return self.title


class Notice(models.Model):
    CATEGORY_CHOICES = [
        ('latest', 'Latest'),
        ('exam', 'Exam'),
        ('admission', 'Admission'),
        ('students', 'Students'),
    ]
    title = models.CharField(max_length=300)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='latest')
    document = models.FileField(upload_to='notices/', blank=True)
    document_url = models.URLField(blank=True)
    published_date = models.DateField(default=timezone.now)
    show_in_marquee = models.BooleanField(default=False, verbose_name="Show in Marquee")
    marquee_flag = models.CharField(max_length=50, blank=True, null=True, verbose_name="Marquee Flag (Optional)", help_text="Custom text to highlight in the marquee (e.g. 'NEW', 'URGENT')")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title}"


class ImportantLink(models.Model):
    name = models.CharField(max_length=150)
    url = models.URLField()
    category = models.CharField(max_length=50, choices=[
        ('important', 'Important Links'),
        ('quick', 'Quick Links'),
    ], default='important')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class CareerGuidanceSubmission(models.Model):
    fname = models.CharField(max_length=100, verbose_name="First Name")
    lname = models.CharField(max_length=100, verbose_name="Last Name")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Phone")
    msg = models.TextField(verbose_name="Message/Comments")
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = "Career Guidance Submission"

    def __str__(self):
        return f"{self.fname} {self.lname} - {self.email}"


class SocialScheme(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100) # e.g. "Women Education"
    description = models.TextField()
    image = models.ImageField(upload_to='social_schemes/', blank=True)
    image_url = models.URLField(blank=True)
    link = models.CharField(max_length=200, blank=True, help_text="e.g. social-schemes/1/index.html")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Social Scheme"

    def __str__(self):
        return self.title

    def get_image(self):
        return self.image.url if self.image else self.image_url


class Testimonial(models.Model):
    student_name = models.CharField(max_length=150)
    program = models.CharField(max_length=150, help_text="e.g. M.Sc. Zoology (2022-23)")
    rating = models.PositiveIntegerField(default=5, help_text="1 to 5 stars")
    text = models.TextField()
    photo = models.ImageField(upload_to='testimonials/', blank=True)
    photo_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'student_name']

    def __str__(self):
        return self.student_name

    def get_photo(self):
        return self.photo.url if self.photo else self.photo_url


class Event(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateField()
    time = models.CharField(max_length=50, blank=True) # e.g. "11 a.m."
    location = models.CharField(max_length=200, default="College Auditorium")
    image = models.ImageField(upload_to='events/', blank=True, null=True, help_text="Upload event brochure/poster (300x200px recommended)")
    image_url = models.URLField(blank=True, help_text="External URL for brochure/poster if not uploaded locally")
    link = models.URLField(blank=True)
    description = CKEditor5Field('Description', config_name='extends', blank=True, help_text="Detailed description of the upcoming event")
    brochure = models.FileField(upload_to='events/brochures/', blank=True, null=True, help_text="Upload event brochure or registration details (PDF)")
    registration_link = models.URLField(blank=True, max_length=500, help_text="External URL for online registration (e.g. Google Form)")
    youtube_url = models.URLField(blank=True, max_length=500, help_text="Optional YouTube video URL (watch link or short link)")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return self.image.url
        if self.image_url:
            return self.image_url
        from django.templatetags.static import static
        return static('assets/images/feature/admission.jpg')

    def get_youtube_embed_url(self):
        if not self.youtube_url:
            return None
        import re
        regex = r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})'
        match = re.search(regex, self.youtube_url)
        if match:
            video_id = match.group(1)
            return f"https://www.youtube.com/embed/{video_id}"
        return self.youtube_url


class Happening(models.Model):
    title = models.CharField(max_length=300)
    category = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to='happenings/', blank=True)
    image_url = models.URLField(blank=True, max_length=500)
    link = models.CharField(max_length=200, blank=True, help_text="e.g. /event-details/148/index.html")
    date = models.DateField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    
    # New fields
    department = models.ForeignKey(
        'academics.Department',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='happenings',
        verbose_name="Department"
    )
    description = CKEditor5Field('Description', config_name='extends', blank=True)
    participants_count = models.PositiveIntegerField(blank=True, null=True, verbose_name="Number of Participants")
    brochure = models.FileField(upload_to='happenings/brochures/', blank=True, null=True, help_text="Upload brochure or registration form (PDF)")
    registration_link = models.URLField(blank=True, max_length=500, help_text="Link for registration (Google Form etc.)")
    banner_image_url = models.URLField(blank=True, max_length=500, help_text="Custom header banner image URL")
    is_nss_activity = models.BooleanField(default=False, verbose_name="Is NSS Activity", help_text="Check if this event/happening is part of NSS activities and should appear in the NSS page slider")
    is_iic_activity = models.BooleanField(default=False, verbose_name="Is IIC Activity", help_text="Check if this event/happening is part of IIC activities and should appear in the IIC page slider")

    class Meta:
        ordering = ['order', '-date']
        verbose_name = "Happening"

    def __str__(self):
        return self.title

    def get_image(self):
        return self.image.url if self.image else self.image_url


class HappeningImage(models.Model):
    happening = models.ForeignKey(Happening, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='happenings/gallery/', blank=True)
    image_url = models.URLField(blank=True, max_length=500, help_text="External URL for image if not uploaded locally")
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Happening Gallery Image"
        verbose_name_plural = "Happening Gallery Images"

    def __str__(self):
        return f"Gallery Image for {self.happening.title}"

    def get_image(self):
        return self.image.url if self.image else self.image_url


class QuickLinkCard(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=200, help_text="e.g. 'students:merit_list' (Django name) or a relative path '/about/'")
    icon = models.FileField(upload_to='icons/', blank=True, null=True, help_text="Upload custom SVG/PNG icon. Falls back to 07.svg.")
    icon_url = models.URLField(blank=True)
    fa_icon = models.CharField(max_length=100, blank=True, help_text="FontAwesome icon class name, e.g. 'fa-graduation-cap', 'fa-building', 'fa-book-open'")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    # Custom design fields
    bg_color = models.CharField(max_length=7, default="#ffffff", help_text="HEX color for card background, e.g. #ffffff or #B71A34")
    bg_image = models.ImageField(upload_to='cards/', blank=True, null=True, help_text="Upload custom background image for the card.")
    overlay_color = models.CharField(max_length=7, default="#000000", help_text="HEX color for background overlay, e.g. #000000")
    overlay_opacity = models.FloatField(default=0.0, help_text="Overlay opacity between 0.0 (fully transparent) and 1.0 (fully opaque)")

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "Quick Link Card"
        verbose_name_plural = "Quick Link Cards"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse, NoReverseMatch
        try:
            return reverse(self.link)
        except NoReverseMatch:
            return self.link

    def get_icon(self):
        if self.icon:
            return self.icon.url
        if self.icon_url:
            return self.icon_url
        from django.templatetags.static import static
        return static('assets/images/icon/07.svg')


class AboutPage(models.Model):
    # Header & Breadcrumb
    page_title = models.CharField(max_length=200, default="About Chaitanya Science and Arts College")
    breadcrumb_image = models.ImageField(
        upload_to='breadcrumbs/about/',
        blank=True, null=True,
        verbose_name="Breadcrumb Background Image",
        help_text="Upload a custom breadcrumb banner image for the About page."
    )
    breadcrumb_image_url = models.URLField(
        blank=True,
        verbose_name="Breadcrumb Image URL (External)",
        help_text="Use an external URL if not uploading a local image. Leave blank to use theme default."
    )

    # About Us Section
    about_us_title = models.CharField(max_length=200, default="About Us")
    about_us_description_1 = CKEditor5Field('About Us Description 1', config_name='extends', blank=True, default="")
    about_us_description_2 = CKEditor5Field('About Us Description 2', config_name='extends', blank=True, default="")
    about_us_description_3 = CKEditor5Field('About Us Description 3', config_name='extends', blank=True, default="")
    about_us_image_url = models.CharField(max_length=500, default="https://chaitanyafiles01.s3.amazonaws.com/aboutImages/COLLEGE_BUILDING.jpg")

    # Stats next to image
    stat1_value = models.CharField(max_length=50, default="8000+")
    stat1_label = models.CharField(max_length=150, default="Undergradute & Graduate Students")
    stat1_icon = models.CharField(max_length=150, default="assets/images/icon/11.svg")

    stat2_value = models.CharField(max_length=50, default="50+")
    stat2_label = models.CharField(max_length=150, default="Chaitanya College Faculty and Staff")
    stat2_icon = models.CharField(max_length=150, default="assets/images/icon/12.svg")

    stat3_value = models.CharField(max_length=50, default="5000+")
    stat3_label = models.CharField(max_length=150, default="Chaitanya College Alumni Worldwide")
    stat3_icon = models.CharField(max_length=150, default="assets/images/icon/13.svg")

    # Fun facts in the red bar
    funfact1_value = models.CharField(max_length=50, default="90%")
    funfact1_label = models.CharField(max_length=150, default="Graduate success rate")

    funfact2_value = models.CharField(max_length=50, default="Top 10")
    funfact2_label = models.CharField(max_length=150, default="Colleges in CG that Create Futures")

    funfact3_value = models.CharField(max_length=50, default="No. 1")
    funfact3_label = models.CharField(max_length=150, default="In Innovation & Entrepreneurship")

    # Vision & Mission
    mission_statement = CKEditor5Field('Mission Statement', config_name='extends', blank=True, default="")
    vision_title = models.CharField(max_length=100, default="Vision")
    vision_text = CKEditor5Field('Vision Text', config_name='extends', blank=True, default="")
    mission_title = models.CharField(max_length=100, default="Mission")
    mission_text_1 = CKEditor5Field('Mission Text 1', config_name='extends', blank=True, default="")
    mission_text_2 = CKEditor5Field('Mission Text 2', config_name='extends', blank=True, default="")

    # Governance
    governance_title = models.CharField(max_length=200, default="Governance")
    governance_text = CKEditor5Field('Governance Text', config_name='extends', blank=True, default="")

    # Distinctive Features
    features_title = models.CharField(max_length=200, default="Distinctive Features of the College")
    features_list = models.TextField(help_text="Enter distinctive features, one per line", default="")

    # Testimonial
    testimonial_text = CKEditor5Field('Testimonial Text', config_name='extends', blank=True, default="")
    testimonial_author = models.CharField(max_length=150, default="VK Gupta")
    testimonial_author_image = models.ImageField(upload_to='about/', blank=True, null=True)

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"

    def __str__(self):
        return self.page_title

    def get_breadcrumb_image(self):
        """Returns the breadcrumb image URL: uploaded file > external URL > empty."""
        if self.breadcrumb_image:
            return self.breadcrumb_image.url
        return self.breadcrumb_image_url or ''


class Recognition(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='recognition/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Recognition Document"
        verbose_name_plural = "Recognition Documents"

    def __str__(self):
        return self.title


class UGCTable(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the custom table (e.g. UGC Files, Autonomy Grant Documents)")
    order = models.PositiveIntegerField(default=0, help_text="Sorting order of tables on the UGC page")
    is_active = models.BooleanField(default=True, help_text="Toggle table visibility on the front end")

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "UGC Table"
        verbose_name_plural = "UGC Tables"

    def __str__(self):
        return self.name


class UGCDocument(models.Model):
    ugc_table = models.ForeignKey(UGCTable, on_delete=models.CASCADE, related_name='documents', help_text="Select the table this document belongs to")
    sn = models.PositiveIntegerField(default=1, verbose_name="S.N.", help_text="Serial number inside the table")
    title = models.CharField(max_length=300, verbose_name="Name of the file/document")
    file = models.FileField(upload_to='ugc/documents/', blank=True, null=True, help_text="Upload local PDF/document")
    file_url = models.URLField(blank=True, max_length=500, help_text="External URL link (if not uploading local file)")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['sn', 'id']
        verbose_name = "UGC Document"
        verbose_name_plural = "UGC Documents"

    def __str__(self):
        return f"[{self.ugc_table.name}] {self.title}"

    def get_file_url(self):
        if self.file:
            return self.file.url
        return self.file_url


class UGCPageSettings(models.Model):
    heading = models.CharField(max_length=200, default="University Grants Commission (UGC) Recognition")
    description = models.TextField(default="Chaitanya Science and Arts College is recognized under Sections 2(f) and 12(B) of the UGC Act, 1956. This recognition establishes our credibility as a premier institution of higher learning eligible for central assistance and academic development programs. The college is committed to maintaining high standards of education, research, and infrastructure as mandated by the UGC.")
    
    # Show/hide controls
    show_ugc_details = models.BooleanField(default=True, verbose_name="Show UGC Details Cards", help_text="Check to show the Autonomy, 2(f)/12(B), and Autonomy Benefits cards section")
    
    # Autonomy Card
    autonomy_status_title = models.CharField(max_length=150, default="Autonomous")
    autonomy_status_subtitle = models.CharField(max_length=150, default="UGC Autonomous Status")
    autonomy_status_text = models.TextField(default="Empowered to design its own curriculum, conduct examinations, and evaluate student performance.")
    
    # 2(f)/12(B) Card
    status_2f_12b_title = models.CharField(max_length=150, default="2(f) and 12(B) Status")
    status_2f_12b_text = models.TextField(default="The recognition under Section 2(f) signifies that our college is a recognized higher education institution.\n\nThe Section 12(B) status makes the college eligible to receive developmental grants from the UGC and other central agencies for teaching, research, and infrastructure upgrades.")
    
    # Autonomy Benefits Card
    benefits_title = models.CharField(max_length=150, default="Autonomy Benefits")
    benefits_list = models.TextField(default="Modernized, industry-relevant curriculum.\nChoice-Based Credit System (CBCS).\nFaster result processing and publication.\nFocus on skill-based and vocational courses.", help_text="Enter one benefit per line")
    
    # Grants Section
    show_grants_section = models.BooleanField(default=True, verbose_name="Show UGC & Central Funding Support Table", help_text="Check to show the UGC & Central Funding Support grants table")
    grants_title = models.CharField(max_length=200, default="UGC & Central Funding Support")

    class Meta:
        verbose_name = "UGC Page Settings"
        verbose_name_plural = "UGC Page Settings"

    def __str__(self):
        return "UGC Page Settings"


class UGCGrant(models.Model):
    scheme = models.CharField(max_length=200, verbose_name="Scheme / Funding Agency")
    purpose = models.CharField(max_length=300, verbose_name="Purpose of Grant")
    impact = models.CharField(max_length=300, verbose_name="Impact & Upgrades")
    order = models.PositiveIntegerField(default=0, help_text="Sorting order of rows in the table")
    is_active = models.BooleanField(default=True, verbose_name="Show in Table", help_text="Uncheck to hide this row from the table")

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "UGC Grant / Funding Record"
        verbose_name_plural = "UGC Grant / Funding Records"

    def __str__(self):
        return f"{self.scheme} - {self.purpose[:50]}"


class PopupAnnouncement(models.Model):
    title = models.CharField(max_length=200, help_text="Title of the announcement (for internal identification)")
    image = models.ImageField(upload_to='popup_announcements/', blank=True, null=True, help_text="Upload a poster/image for the popup")
    image_url = models.URLField(blank=True, help_text="Or enter an external image URL if no local file is uploaded")
    text = CKEditor5Field('Announcement Content', config_name='extends', blank=True, help_text="Custom rich text details shown inside the modal")
    link = models.URLField(blank=True, help_text="Optional custom link to redirect users (e.g., Admission page)")
    link_text = models.CharField(max_length=100, default="Learn More", help_text="Action button label")
    is_active = models.BooleanField(default=False, help_text="Check to display this announcement in the popup list on the homepage")
    show_once_per_session = models.BooleanField(default=True, help_text="If checked, the popup will only display once per browser session. Otherwise, it will show on every homepage load.")
    order = models.PositiveIntegerField(default=0, help_text="Display order in the popup list (lower numbers appear first)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Popup Announcement"
        verbose_name_plural = "Popup Announcements"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return self.image.url
        return self.image_url




class BreadcrumbSettings(models.Model):
    """
    Singleton model — holds the site-wide default breadcrumb background image.
    Only one row should ever exist. Controlled via the singleton guard in admin.
    """
    default_image = models.ImageField(
        upload_to='breadcrumbs/',
        blank=True, null=True,
        verbose_name="Default Background Image",
        help_text="Upload the default breadcrumb banner image used across all pages."
    )
    default_image_url = models.URLField(
        blank=True,
        verbose_name="Default Image URL (External)",
        help_text="Use an external URL if you are not uploading a local image."
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Enable Per-Page Overrides",
        help_text="When checked, per-page breadcrumb overrides can replace the global default. "
                  "When unchecked, all pages use only the global default image above."
    )

    class Meta:
        verbose_name = "Breadcrumb Settings (Global Default)"
        verbose_name_plural = "Breadcrumb Settings (Global Default)"

    def __str__(self):
        return "Global Breadcrumb Settings"

    def get_image(self):
        """Returns the resolved URL for the default image, or empty string."""
        if self.default_image:
            return self.default_image.url
        return self.default_image_url or ''


class PageBreadcrumb(models.Model):
    """
    Per-page breadcrumb image override.
    Each row targets one specific page via page_key.
    """
    PAGE_KEY_CHOICES = [
        # Core app
        ('about',                    'About Us'),
        ('committees',               'Committees'),
        ('committee_detail',         'Committee Detail'),
        ('policies',                 'Policies'),
        ('recognition',              'Achievements & Recognition'),
        ('staff_teaching',           'Teaching Staff'),
        ('staff_nonteaching',        'Non-Teaching Staff'),
        ('notices',                  'Notice Board'),
        ('contact',                  'Contact Us'),
        ('nss',                      'NSS'),
        ('iic',                      'IIC'),
        ('ugc',                      'UGC'),
        ('nep',                      'NEP 2020'),
        ('sports',                   'Sports'),
        ('co_po',                    'CO PO'),
        ('happenings',               'Recent Happenings'),
        ('happening_detail',         'Happening Detail'),
        ('event_detail',             'Event Detail'),
        # Academics
        ('academics_programs',       'Programs Offered'),
        ('academics_calendar',       'Academic Calendar'),
        ('academics_dept_detail',    'Department Detail'),
        # Students
        ('students_admission',       'Admission Procedure'),
        ('students_online_admission','Online Admission'),
        ('students_fee_structure',   'Fee Structure'),
        ('students_scholarship',     'Scholarship'),
        ('students_library',         'Library'),
        ('students_alumni',          'Alumni'),
        ('students_merit_list',      'Merit List'),
        # NAAC
        ('naac_home',                'NAAC'),
        ('naac_iqac',                'IQAC'),
        ('naac_iiqa',                'IIQA'),
        ('naac_ssr',                 'SSR'),
        ('naac_dvv',                 'DVV'),
        ('naac_atr',                 'ATR'),
        # Gallery
        ('gallery_images',           'Image Gallery'),
        ('gallery_videos',           'Video Gallery'),
        ('gallery_news',             'News Gallery'),
        # Feedback
        ('feedback_student',         'Student Feedback'),
        ('feedback_parent',          'Parent Feedback'),
        ('feedback_faculty',         'Faculty Feedback'),
        ('feedback_alumni',          'Alumni Feedback'),
        # Grievances
        ('grievances_anti_ragging',  'Anti Ragging Committee'),
        ('grievances_icc',           'Internal Complaints Committee (ICC)'),
        ('grievances_redressal',     'Grievance Redressal'),
        ('grievances_submit',        'Submit a Grievance'),
        # Custom pages
        ('custom_page',              'Custom Page'),
    ]

    page_key = models.CharField(
        max_length=60,
        choices=PAGE_KEY_CHOICES,
        unique=True,
        verbose_name="Page",
        help_text="Select the page this breadcrumb image applies to."
    )
    custom_image = models.ImageField(
        upload_to='breadcrumbs/pages/',
        blank=True, null=True,
        verbose_name="Custom Background Image",
        help_text="Upload a custom breadcrumb banner image for this specific page."
    )
    custom_image_url = models.URLField(
        blank=True,
        verbose_name="Custom Image URL (External)",
        help_text="Use an external URL for the image if not uploading locally."
    )
    use_default = models.BooleanField(
        default=False,
        verbose_name="Use Global Default Image",
        help_text="Check this to ignore the custom image above and use the site-wide "
                  "default breadcrumb image instead."
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Active",
        help_text="When checked, this page-level override is applied. "
                  "Uncheck to disable and fall back to the global default."
    )

    class Meta:
        verbose_name = "Page Breadcrumb Override"
        verbose_name_plural = "Page Breadcrumb Overrides"
        ordering = ['page_key']

    def __str__(self):
        return f"{self.get_page_key_display()} — {'Default' if self.use_default else 'Custom'}"

    def get_image(self):
        """Returns the resolved image URL for this page override."""
        if self.custom_image:
            return self.custom_image.url
        return self.custom_image_url or ''


class NSSPageSettings(models.Model):
    banner_title = models.CharField(max_length=200, default="National Service Scheme Chaitanya Science and Arts College, Pamgarh")
    banner_description = models.TextField(default="The NSS symbol is based on the 'Rath Wheel' of the Konark Sun Temple of Orissa. The giant wheel portrays the cycles of creation, preservation and release and signifies the movement in life across time and space. The design of the symbol, a simplified form of Sun Chariot Wheel primarily depicts movement. The wheel signifies the progressive cycle of life. It also stands for dynamism and progressive outlook of youth.")
    banner_image = models.ImageField(upload_to='nss/', blank=True, null=True)
    banner_image_url = models.URLField(blank=True, help_text="External URL for banner image if not uploaded locally")
    banner_icon = models.FileField(upload_to='nss/icons/', blank=True, null=True, help_text="SVG/PNG icon for banner")
    banner_icon_url = models.URLField(blank=True, help_text="External URL for banner icon if not uploaded locally")
    
    about_title = models.CharField(max_length=200, default="Our NSS Activities")
    about_description = models.TextField(default="The NSS Unit consists of 100 student volunteers. The Program Officer is expected to motivate the student youth to understand the values and philosophy of NSS. The overall functions of Program Officer are to help the students to plan, implement and evaluate the activities of NSS under his/her charge and give proper guidance and directions to the student volunteers.")

    class Meta:
        verbose_name = "NSS Page Settings"
        verbose_name_plural = "NSS Page Settings"

    def __str__(self):
        return "NSS Page Settings"

    def get_banner_image(self):
        if self.banner_image:
            return self.banner_image.url
        if not self.banner_image_url:
            return ""
        if self.banner_image_url.startswith(('http://', 'https://', '/')):
            return self.banner_image_url
        from django.conf import settings
        return f"{settings.MEDIA_URL}{self.banner_image_url}"

    def get_banner_icon(self):
        if self.banner_icon:
            return self.banner_icon.url
        if not self.banner_icon_url:
            return ""
        if self.banner_icon_url.startswith(('http://', 'https://', '/')):
            return self.banner_icon_url
        from django.conf import settings
        return f"{settings.MEDIA_URL}{self.banner_icon_url}"


class NSSActivity(models.Model):
    serial_number = models.CharField(max_length=10, help_text="e.g. 01, 02")
    title = models.CharField(max_length=300)
    fa_icon = models.CharField(max_length=100, default="fa-star", help_text="FontAwesome icon class name, e.g. 'fa-user-md', 'fa-tooth', 'fa-tree'")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'serial_number']
        verbose_name = "NSS Activity"
        verbose_name_plural = "NSS Activities"

    def __str__(self):
        return f"{self.serial_number} - {self.title}"


class NSSGalleryImage(models.Model):
    image = models.ImageField(upload_to='nss/gallery/', blank=True, null=True)
    image_url = models.URLField(blank=True, help_text="External URL for image if not uploaded locally")
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "NSS Gallery Image"
        verbose_name_plural = "NSS Gallery Images"

    def __str__(self):
        return self.caption or f"NSS Gallery Image {self.id}"

    def get_image(self):
        if self.image:
            return self.image.url
        if not self.image_url:
            return ""
        if self.image_url.startswith(('http://', 'https://', '/')):
            return self.image_url
        from django.conf import settings
        return f"{settings.MEDIA_URL}{self.image_url}"


class IICPageSettings(models.Model):
    title = models.CharField(max_length=200, default="INSTITUTION'S INNOVATION COUNCIL (IIC)")
    sub_title = models.CharField(max_length=200, default="Ministry of Education Supported")
    description = models.TextField(default="In the year 2018, the Ministry of Education (MoE) through MoE’s Innovation Cell (MIC) launched the Institution’s Innovation Council (IIC) program in collaboration with AICTE for Higher Educational Institutions (HEIs) to systematically foster the culture of innovation and start-up ecosystem in education institutions. Primarily, IIC’s role is to engage large number of faculty, students and staff in various innovation and entrepreneurship related activities such as ideation, Problem solving, Proof of Concept development, Design Thinking, IPR, project handling and management at Pre-incubation/Incubation stage, etc., so that innovation and entrepreneurship ecosystem gets established and stabilized in HEIs.")
    about_image_1 = models.ImageField(upload_to='iic/', blank=True, null=True)
    about_image_1_url = models.CharField(max_length=300, blank=True)
    about_image_2 = models.ImageField(upload_to='iic/', blank=True, null=True)
    about_image_2_url = models.CharField(max_length=300, blank=True)

    class Meta:
        verbose_name = "IIC Page Settings"
        verbose_name_plural = "IIC Page Settings"

    def __str__(self):
        return self.title

    def get_about_image_1(self):
        if self.about_image_1:
            return self.about_image_1.url
        if not self.about_image_1_url:
            return ""
        if self.about_image_1_url.startswith(('http://', 'https://', '/')):
            return self.about_image_1_url
        from django.conf import settings
        return f"{settings.MEDIA_URL}{self.about_image_1_url}"

    def get_about_image_2(self):
        if self.about_image_2:
            return self.about_image_2.url
        if not self.about_image_2_url:
            return ""
        if self.about_image_2_url.startswith(('http://', 'https://', '/')):
            return self.about_image_2_url
        from django.conf import settings
        return f"{settings.MEDIA_URL}{self.about_image_2_url}"


class IICGalleryImage(models.Model):
    image = models.ImageField(upload_to='iic/gallery/', blank=True, null=True)
    image_url = models.URLField(blank=True, help_text="External URL for image if not uploaded locally")
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "IIC Gallery Image"
        verbose_name_plural = "IIC Gallery Images"

    def __str__(self):
        return self.caption or f"IIC Gallery Image {self.id}"

    def get_image(self):
        if self.image:
            return self.image.url
        if not self.image_url:
            return ""
        if self.image_url.startswith(('http://', 'https://', '/')):
            return self.image_url
        from django.conf import settings
        return f"{settings.MEDIA_URL}{self.image_url}"



