from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
# Create your views here.

class AboutView(View):
    def get(self,request):
        data = {"ID":100,
                "Full_name" : "Aswin.P.Anilkumar",
                "Professional_Title" : "Python Developer",
                "BIO" : "A passionate programmer",
                "DOB" : "2005-10-11",
                "Email" : "aswinanil79@proton.me",
                "Contact_Number" : 9895929469,
                "Location" : "Njarakkal,Ernakulam",
                "GitHub_URL" : "https://github.com/AswinAnil1110",
                "Linkedin_URL" : "https://linkedin.com/in/AswinAnil1110"}
        return JsonResponse(data)

class Education(View):
    def get(self,request):
        data = {"ID" : 12131,
                "Institution" : "MGAJAS College",
                "Degree/Course" : "BCA",
                "University" : "Mahatma Gandhi",
                "Location" : "North Paravur",
                "Start_Year" : 2023,
                "End_Year" : 2026,
                "Grade/CGPA" : "7.14",
                "Description" : "Course Completed"}
        return JsonResponse(data)

class ProjectView(View):
    def get(self, request):
        data = [
            {
                "id":1,
                "title":"First_Aid",
                "short_description":"AI-based first aid suggestion based on symptoms",
                "technologies_used":["Python","Django","Google GenAI SDK"],
                "live_url":"https://first_aid.example.com",
                "github_url":"https://github.com/yourusername/first_aid",
                "image_url":"https://api.yourdomain.com/media/projects/first_aid",
                "featured":True
            },
            {
                "id":2,
                "title":"FoodBox",
                "short_description":"AI-based food odering application",
                "technologies_used":["Python","Django","Google GenAI SDK"],
                "live_url":"https://foodbox.example.com",
                "github_url":"https://github.com/yourusername/foodbox",
                "image_url":"https://api.yourdomain.com/media/projects/foodbox",
                "featured":True
            },
            {
                "id":3,
                "title":"Interview prep blog",
                "short_description":"Educational application for programming intrviews.",
                "technologies_used":["Python","Django","Google GenAI SDK"],
                "live_url":"https://interview_prep.example.com",
                "github_url":"https://github.com/yourusername/interview_prep",
                "image_url":"https://api.yourdomain.com/media/projects/interview_prep",
                "featured":True
            }
        ]
        return JsonResponse(data,safe=False)

class SkillsView(View):
    def get(self,request):
        data = [
            {
                "id":101,
                "Skill_Name":"Python",
                "Category":"Programming Language",
                "Proficiency_Level":"Advanced",
                "Years_of_Experience":4
            },
            {
                "id":102,
                "Skill_Name":"React",
                "Category":"FrontEnd",
                "Proficiency_Level":"Intermediate",
                "Years_of_Experience":2
            },
            {
                "id":103,
                "Skill_Name":"Django",
                "Category":"BackEnd",
                "Proficiency_Level":"Advanced",
                "Years_of_Experience":3
            }
        ]
        return JsonResponse(data,safe=False)

class ExperienceView(View):
    def get(self,request):
        data = [
            {
                "id":10,
                "Job_Title":"Python Intern",
                "Company_Name":"Infosys",
                "Location":"Kakkanad",
                "Employment_Type":"Intern",
                "Start_Date":"2023-01-17",
                "End_Date":"2023-07-01",
                "Currently_Working":"Yes",
                "Description":"Internship Completed"
            },
            {
                "id":11,
                "Job_Title":"Python Programmer",
                "Company_Name":"Amazon",
                "Location":"Cochin",
                "Employment_Type":"Programmer",
                "Start_Date":"2023-08-10",
                "End_Date":"2025-10-11",
                "Currently_Working":"Yes",
                "Description":"None"
            },
            {
                "id":12,
                "Job_Title":"Django Programmer",
                "Company_Name":"Infosys",
                "Location":"Kakkanad",
                "Employment_Type":"Backend Developer",
                "Start_Date":"2025-11-01",
                "End_Date":"2026-07-01",
                "Currently_Working":"Yes",
                "Description":"None"
            }
        ]
        return JsonResponse(data,safe=False)

class CertificateView(View):
    def get(self,request):
        data = [
            {
                "id":500,
                "Certification_Name":"Python FullStack",
                "Issuing_Organization":"Luminar Technolab",
                "Issued_Date":"2025-10-11"
            },
            {
                "id":501,
                "Certification_Name":"Data Analyst",
                "Issuing_Organization":"HACA",
                "Issued_Date":"2026-04-01"
            },
            {
                "id":502,
                "Certificate_Name":"Data Mining",
                "Issusing_Organization":"Luminar Technolab",
                "Issued_Date":"2026-04-02"
            }
        ]
        return JsonResponse(data,safe=False)

class ServiceView(View):
    def get(self,request):
        data = [
            {
                "id":900,
                "Service_Name":"Web Development",
                "Description" :"Can Make Any Website as per User Request",
                "Technologies":"Python,Django,Gemini"
            },
            {
                "id":901,
                "Service_Name":"Database Management",
                "Description" :"Deals With all Updations in Database",
                "Technologies":"Sqlite,MySQL"
            }
        ]
        return JsonResponse(data,safe=False)

    