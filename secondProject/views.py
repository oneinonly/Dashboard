from django.shortcuts import render, redirect
def home(req):
     
    return render(req, 'Home.html' )

def about(req):
    return render(req, 'About.html')

def index_view(request):
    return render(request, "index.html")


def nav(request):
    return render(request, "index.html")



# def marksheet_1(request):
#     return render(request, "marksheet_form.html")



def contact(req):
    context = {
        'name': "netligent",
        'profile': "SOFTWARE DEVELOPER",
        'Salary': 364364,
        'department': "information technology",
        'att': ['A', 'P', 'A', 'A', 'P'],
        'desc': "Hello I am working as a Software developer"
    }
    return render(req, 'contact.html', context)

def candidate_view(request):
    # Backend data (jo aap template ko bhejna chahte ho)
    context = {
        'name': 'Arun Kumar',
        'age': 25,
        'skills': ['Python', 'Django', 'JavaScript']
    }
    return render(request, 'candidate.html', context)

def result_view(request):
    data = {
        "roll_no": "1100853",
        "school": "GOVT SR SEC SCH, SRINAGAR ROAD, AJMER",
        "year": 2024,
        "name": "Ganesh",
        "mother": "Parvati",
        "father": "Shiv",
        "gender": 'Male',
        "dob": '01-01-2000',
        "medium": 'English',
        "subjects": [
            {"name": "HINDI", "th": 68, "ss": 20, "pr": 0},
            {"name": "ENGLISH", "th": 58, "ss": 20, "pr": 0},
            {"name": "SCIENCE", "th": 63, "ss": 20, "pr": 0},
            {"name": "SOC.SCIENCE", "th": 66, "ss": 20, "pr": 0},
            {"name": "MATHEMATICS", "th": 62, "ss": 20, "pr": 0},
            {"name": "SANSKRIT", "th": 62, "ss": 20, "pr": 0},
        ],
        "total": 499,
        "percentage": 83.17,
        "result": "First Division",
    }
    return render(request, "result.html", data)
def admitcard_view(request):
    data = {
        "roll_no": "631005633",
        "name": "ARUN AHIRWAR",
        "father": "RAMESH AHIRWAR",
        "cnic": "61101-0134843-2",
        "paper_type": "FULLSTACK DEVELOPMENT",
        "test_date": "Sunday 1st September, 2025",
        "report_time": "08:00 AM",
        "center": "MAULANA AZAD,  BHOPAL",
        "photo": "/static/images/photo.jpg",  # apni image static folder me rakhna
    }
    return render(request, "admitcard_view.html", data)

def resume_view(request):
    name = request.GET.get('name')
    role = request.GET.get('role')
    email = request.GET.get('email')
    phone = request.GET.get('phone')
    skills = request.GET.getlist('skills')

    context = {
        'name': name,
        'role': role,
        'email': email,
        'phone': phone,
        'skills': skills
    }
    return render(request, "resume.html", context)

def post_view(request):
    name = request.POST.get('name')
    role = request.POST.get('role')
    email = request.POST.get('email')  
    phone = request.POST.get('phone')
    skills = request.POST.getlist('skills')

    context = {
        'name': name,
        'role': role,
        'email': email,
        'phone': phone,
        'skills': skills
    }
    return render(request, "post.html", context)

def register(request):
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        username = request.POST.get('username')
        password = request.POST.get('password') # Note: Do NOT store raw passwords. Use Django's built-in User model.
        address = request.POST.get('address')
        blood_group = request.POST.get('blood_group')

        # Store data in session for redirection
        request.session['form_data'] = {
            'name': name,
            'gender': gender,
            'dob': dob,
            'username': username,
            'password': password,
            'address': address,
            'blood_group': blood_group,
        }

        # Redirect to the preview page
        return redirect(preview)  # Change 'preview' to 'marksheet' if you want to go to marksheet page after registration
    
    return render(request, 'registration.html')

def preview(request):
    # Retrieve data from the session
    form_data = request.session.get('form_data', {})
    return render(request, 'preview.html', {'form_data': form_data})

# from django.shortcuts import render, redirect

def marksheet_form(request):
#     """Renders the initial form for data entry."""
    
    return render(request, 'marksheet_form.html')

def display_marksheet(request):
    """Processes form data and displays the final marksheet."""
    if request.method == 'POST':
        # --- Student Information ---
        context = {
            'roll_no': request.POST.get('roll_no'),
            'examinee_name': request.POST.get('examinee_name'),
            'gender': request.POST.get('gender'),
            'school': request.POST.get('school'),
            'mother_name': request.POST.get('mother_name'),
            'father_name': request.POST.get('father_name'),
            'date_of_birth': request.POST.get('date_of_birth'),
            'year': request.POST.get('year'),
            'medium': request.POST.get('medium'),
        }

        # --- Marks Processing ---
        subjects = ['hindi', 'english', 'science', 'soc_science', 'mathematics', 'sanskrit']
        grand_total = 0
        
        for subject in subjects:
            try:
                # Get Theory (TH) and Sessional (SS) marks, default to 0 if not provided
                th_marks = int(request.POST.get(f'{subject}_th', 0))
                ss_marks = int(request.POST.get(f'{subject}_ss', 0))
                
                # In this marksheet, Practical (PR) is always 0
                pr_marks = 0 
                
                total = th_marks + ss_marks + pr_marks
                grand_total += total
                
                context[f'{subject}_th'] = th_marks
                context[f'{subject}_ss'] = ss_marks
                context[f'{subject}_pr'] = pr_marks
                context[f'{subject}_total'] = total
            except ValueError:
                # Handle cases where marks are not valid integers
                # For simplicity, we'll just set them to 0
                context[f'{subject}_th'] = 0
                context[f'{subject}_ss'] = 0
                context[f'{subject}_pr'] = 0
                context[f'{subject}_total'] = 0


        # --- Final Calculations ---
        # Assuming maximum marks for each of the 6 subjects is 100
        total_max_marks = 600
        percentage = (grand_total / total_max_marks) * 100 if total_max_marks > 0 else 0
        
        context['total_marks_obtain'] = grand_total
        context['percentage'] = f"{percentage:.2f}%" # Format to 2 decimal places

        return render(request, 'display_marksheet.html', context)
    
    # If accessed via GET, redirect back to the form
    return redirect('marksheet_form')
