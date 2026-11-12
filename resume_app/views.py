from django.shortcuts import render


def resume_view(request):
    resume_data = {
        'name': 'Aisha Rahman',
        'age': 27,
        'gender': 'female',
        'email': 'aisha.rahman@example.com',
        'skills': [
            'Python',
            'Django',
            'HTML5',
            'CSS3',
            'JavaScript',
            'Git and GitHub',
        ],
        'education': [
            {
                'degree': 'BSc in Computer Science',
                'institution': 'University of Dhaka',
                'year': '2021',
            },
            {
                'degree': 'Higher Secondary Certificate',
                'institution': 'Dhaka City College',
                'year': '2017',
            },
        ],
    }
    return render(request, 'resume_app/resume.html', {'resume': resume_data})
