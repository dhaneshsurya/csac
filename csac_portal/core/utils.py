from django.db import transaction

def seed_default_menu_items():
    from .models import MenuItem

    if MenuItem.objects.exists():
        return

    # Structure: (title, url, is_named_url, open_in_new_tab, order, [children])
    defaults = [
        ("Home", "core:home", True, False, 1, []),
        
        ("About Us", "core:about", True, False, 2, [
            ("About Institute", "core:about", True, False, 1, []),
            ("Achievements & Recognition", "core:recognition", True, False, 2, []),
            ("Staff", "#", False, False, 3, [
                ("Teaching", "core:staff_teaching", True, False, 1, []),
                ("Non-Teaching", "core:staff_nonteaching", True, False, 2, [])
            ]),
            ("Committees", "core:committees", True, False, 4, []),
            ("Policies", "core:policies", True, False, 5, []),
            ("Infrastructure", "core:infrastructure", True, False, 6, []),
            ("Our Products", "core:products", True, False, 7, [])
        ]),
        
        ("Academics", "academics:programs", True, False, 3, [
            ("Arts", "#", False, False, 1, [
                ("Hindi", "academics:department_detail 'hindi'", True, False, 1, []),
                ("English", "academics:department_detail 'english'", True, False, 2, []),
                ("Sociology", "academics:department_detail 'sociology'", True, False, 3, []),
                ("Geography", "academics:department_detail 'geography'", True, False, 4, []),
                ("Social Work", "academics:department_detail 'social-work'", True, False, 5, []),
                ("Political Science", "academics:department_detail 'political-science'", True, False, 6, []),
                ("History", "academics:department_detail 'history'", True, False, 7, [])
            ]),
            ("Science", "#", False, False, 2, [
                ("Zoology", "academics:department_detail 'zoology'", True, False, 1, []),
                ("Physics", "academics:department_detail 'physics'", True, False, 2, []),
                ("Chemistry", "academics:department_detail 'chemistry'", True, False, 3, []),
                ("Mathematics", "academics:department_detail 'mathematics'", True, False, 4, []),
                ("Botany", "academics:department_detail 'botany'", True, False, 5, []),
                ("Forestry", "academics:department_detail 'forestry'", True, False, 6, []),
                ("Computer Science", "academics:department_detail 'computer-science'", True, False, 7, [])
            ]),
            ("Programs Offered", "academics:programs", True, False, 3, []),
            ("CO PO", "core:co_po", True, False, 4, []),
            ("Academic Calendar", "academics:academic_calendar", True, False, 5, [])
        ]),
        
        ("Student Corner", "students:admission", True, False, 4, [
            ("Admission Procedure", "students:admission", True, False, 1, []),
            ("University Admission", "https://www.snpvraigarh.in/", False, True, 2, []),
            ("Online Admission", "students:online_admission", True, False, 3, []),
            ("Fee Structure", "students:fee_structure", True, False, 4, []),
            ("Result", "https://www.snpvraigarh.in/", False, True, 5, []),
            ("Scholarship", "students:scholarship", True, False, 6, []),
            ("Library", "students:library", True, False, 7, []),
            ("Alumni", "students:alumni", True, False, 8, []),
            ("Merit List", "students:merit_list", True, False, 9, [])
        ]),
        
        ("NAAC", "naac:naac_home", True, False, 5, [
            ("NAAC", "naac:naac_home", True, False, 1, []),
            ("IQAC", "naac:iqac", True, False, 2, [
                ("IIQA", "naac:iiqa", True, False, 1, []),
                ("SSR", "naac:ssr", True, False, 2, []),
                ("DVV", "naac:dvv", True, False, 3, []),
                ("ATR", "naac:atr", True, False, 4, [])
            ])
        ]),
        
        ("Feedback", "#", False, False, 6, [
            ("Student's Feedback", "feedback:student_feedback", True, False, 1, []),
            ("Parent's Feedback", "feedback:parent_feedback", True, False, 2, []),
            ("Faculty's Feedback", "feedback:faculty_feedback", True, False, 3, []),
            ("Alumni's Feedback", "feedback:alumni_feedback", True, False, 4, [])
        ]),
        
        ("Grievances", "#", False, False, 7, [
            ("Anti Ragging Committee", "grievances:anti_ragging", True, False, 1, []),
            ("Internal Complaints Committee (ICC)", "grievances:icc", True, False, 2, []),
            ("Grievance Redressal Committee", "grievances:redressal", True, False, 3, []),
            ("Submit a Grievance", "grievances:submit_grievance", True, False, 4, [])
        ]),
        
        ("UGC", "core:ugc", True, False, 8, []),
        
        ("Gallery", "#", False, False, 9, [
            ("Image Gallery", "gallery:image_gallery", True, False, 1, []),
            ("Video Gallery", "gallery:video_gallery", True, False, 2, []),
            ("News Gallery", "gallery:news_gallery", True, False, 3, [])
        ]),
        
        ("Student Login", "https://chaitanyapamgarh.onlineexamforms.com/student.aspx", False, True, 10, [])
    ]

    with transaction.atomic():
        def create_items(item_list, parent=None):
            for title, url, is_named_url, open_tab, order, children in item_list:
                item = MenuItem.objects.create(
                    title=title,
                    url=url,
                    is_named_url=is_named_url,
                    open_in_new_tab=open_tab,
                    order=order,
                    parent=parent
                )
                if children:
                    create_items(children, parent=item)

        create_items(defaults)
