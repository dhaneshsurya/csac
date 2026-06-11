from .models import SiteSettings, MarqueeNotice, ImportantLink, Notice
from .models import BreadcrumbSettings, PageBreadcrumb, MenuItem


def site_context(request):
    """Makes site-wide data available in every template"""
    try:
        settings_obj = SiteSettings.objects.first()
    except Exception:
        settings_obj = None

    # Retrieve standard marquee notices
    mn_list = MarqueeNotice.objects.filter(is_active=True)

    # Retrieve uploaded notices set to show in marquee
    n_list = Notice.objects.filter(show_in_marquee=True, is_active=True).order_by('-published_date')

    # Build unified marquee notices list without duplicates
    combined_marquee = []
    seen = set()

    # Process Notice objects first (since they contain more metadata/flags)
    for n in n_list:
        normalized_text = n.title.strip().lower()
        seen.add(normalized_text)
        link = n.document.url if n.document else n.document_url
        combined_marquee.append({
            'text': n.title,
            'link': link,
            'flag': n.marquee_flag,
        })

    # Process MarqueeNotice objects second, skipping duplicates
    for mn in mn_list:
        normalized_text = mn.text.strip().lower()
        if normalized_text in seen:
            continue
        seen.add(normalized_text)
        combined_marquee.append({
            'text': mn.text,
            'link': mn.link,
            'flag': None,
        })

    important_links = ImportantLink.objects.filter(category='important')
    quick_links = ImportantLink.objects.filter(category='quick')

    # ------------------------------------------------------------------
    # Breadcrumb image resolver
    # Pre-resolves all page keys into a dict so templates can use
    # dot-notation:  breadcrumb_images.about  (no function call needed)
    # ------------------------------------------------------------------
    try:
        _bc_global = BreadcrumbSettings.objects.first()
    except Exception:
        _bc_global = None

    try:
        _bc_pages = {pb.page_key: pb for pb in PageBreadcrumb.objects.all()}
    except Exception:
        _bc_pages = {}

    def _resolve(page_key):
        """
        Resolves the breadcrumb image for a given page key.

        - The global default image ALWAYS applies if uploaded (regardless of is_active).
        - is_active controls whether per-page overrides can replace the global.
        - Per-page override with use_default=True → global image.
        - Per-page override with custom image → that image (only when is_active=True).
        """
        global_img = _bc_global.get_image() if _bc_global else ''

        # If per-page overrides are enabled, check for one
        if _bc_global and _bc_global.is_active:
            page_override = _bc_pages.get(page_key)
            if page_override and page_override.is_active:
                if page_override.use_default:
                    return global_img
                img = page_override.get_image()
                if img:
                    return img

        # Always fall back to the global image
        return global_img

    # Build a flat dict for every known page key
    _all_keys = [
        'about', 'committees', 'committee_detail', 'policies', 'recognition',
        'staff_teaching', 'staff_nonteaching', 'notices', 'contact', 'nss',
        'iic', 'ugc', 'nep', 'sports', 'co_po', 'happenings',
        'happening_detail', 'event_detail',
        'academics_programs', 'academics_calendar', 'academics_dept_detail',
        'students_admission', 'students_online_admission', 'students_fee_structure',
        'students_scholarship', 'students_library', 'students_alumni',
        'students_merit_list',
        'naac_home', 'naac_iqac', 'naac_iiqa', 'naac_ssr', 'naac_dvv', 'naac_atr',
        'gallery_images', 'gallery_videos', 'gallery_news',
        'feedback_student', 'feedback_parent', 'feedback_faculty', 'feedback_alumni',
        'grievances_anti_ragging', 'grievances_icc', 'grievances_redressal',
        'grievances_submit', 'custom_page', 'infrastructure',
    ]
    breadcrumb_images = {k: _resolve(k) for k in _all_keys}

    try:
        from .utils import seed_default_menu_items
        seed_default_menu_items()
        navbar_menu = MenuItem.objects.filter(parent=None, is_active=True).prefetch_related('children', 'children__children')
    except Exception:
        navbar_menu = []

    return {
        'site_settings': settings_obj,
        'marquee_notices': combined_marquee,
        'important_links': important_links,
        'quick_links': quick_links,
        'breadcrumb_images': breadcrumb_images,
        'navbar_menu': navbar_menu,
    }
