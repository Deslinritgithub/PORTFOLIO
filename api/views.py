from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.
class AboutView(View):
    def get(self,request):
        data={
            "ID": 100,
            "FullName": "Arshit",
            "Professional Title":"Software Developer",
            "Bio":"demo",
            "Email":"mjdeslin@mail.com",
            "Contact":8848232303,
            "DOB":"17-12-2004",
            "Github URL":"https://github.com/Deslinritgithub",
            "Linkedin URL":"abcd"

        }
        return JsonResponse(data)

class EducationView(View):
    def get(self,request):
        data1={
            "ID":102,
            "Instittution":"AEC",
            "Degree/Course":"BCA",
            "University":"calicut",
            "Start Year":"2022",
            "End Year":"2026",
            "Grade 0r CGPA":"7.46",
            "Description":"demo"
        }
        return JsonResponse(data1)

class ProjectView(View):
    def get(Self,request):
        data3=[
            {
                "id":111,
                "title":"Intern Tracking System",
                "short description":"This is a web application that helps to track the interns and their progress.",
                "long description":"This is a web application that helps to track the interns and their progress. It allows the admin to add, edit and delete the interns. The interns can also update their progress and the admin can view the progress of all the interns.",
                "technologies used":["python","Django","HTML","CSS","Javascript"],
                "live url":"demo",
                "github url":"https://github.com/ArshitAji/intern-navigators.git",
                "image url":"image",
                "featured":True
                                     
            },
            {
                "id":112,
                "title":"E-Commerce Website",
                "short description":"This is a full-stack e-commerce website built with Django and React.",
                "long description":"This is a full-stack e-commerce website built with Django and React. It includes features like user authentication, product management, shopping cart, and payment processing.",
                "technologies used":["python","Django","React","PostgreSQL"],
                "live url":"demo",
                "github url":"https://github.com/ArshitAji/intern-navigators.git",
                "image url":"image",
                "featured":True
            },
            {
                "id":113,
                "title":"Portfolio Website",
                "short description":"This is a personal portfolio website built with Django and React.",
                "long description":"This is a personal portfolio website built with Django and React. It includes features like user authentication, project management, and contact form.",
                "technologies used":["python","Django","React","PostgreSQL"],
                "live url":"demo",
                "github url":"https://github.com/ArshitAji/intern-navigators.git",
                "image url":"image",
                "featured":True
            }
        ]
        return JsonResponse(data3,safe=False)

class SkillsView(View):
    def get(Self,request):
        skills=[
            {
                "id":200,
                "skill name":"python",
                "category":"pyhton programmer",
                "proficiency level":"Beginner",
                "Years of Experience":2
            },
            {
                "id":201,
                "skill name":"SQL",
                "Category":"Database Management",
                "proficiency level":"Intermediate",
                "Years of Experience":3
            }
        ]
        return JsonResponse(skills,safe=False)

class ExperienceView(View):
    def get(self,request):
        experience=[
            {
                "id:":300,
                "job title":"Software Developer",
                "location":"Kochi",
                "employment type":"Full time",
                "start date":"2022-01-01",
                "end date":"2023-01-01",
                "currently working":False,
                "Description":"Worked on various projects and gained experience in software development."
            },
            {
                "id":301,
                "job title":"Intern",
                "location":"Kochi",
                "employment type":"Full time",
                "start date":"2024-01-01",
                "end date":"2026-06-06",
                "currently working":False,
                "Description":"Worked on various projects and gained experience in software development."
            }
        ]
        return JsonResponse(experience,safe=False)

class CertificateView(View):
    def get(self,request):
        certificates=[
            {
                "id":400,
                "certificate name":"Python for Beginners",
                "organization name":"Coursera",
                "isssues year":"2022"
            },
            {
                "id":401,
                "certificate name":"Django for Beginners",
                "organization name":"Udemy",
                "isssues year":"2023"
            }
        ]
        return JsonResponse(certificates,safe=False)

class ServiceView(View):
    def get(self,request):
        services=[
            {
                "id":500,
                "service name":"Web Development",
                "description":"I provide web development services using Django and React.",
                "technologies":["python","Django","React","PostgreSQL"]
            },
            {
                "id":501,
                "service name":"Mobile App Development",
                "description":"I provide mobile app development services using React Native.",
                "technologies":["React Native","JavaScript","HTML","CSS"]
            }
        ]
        return JsonResponse(services,safe=False)