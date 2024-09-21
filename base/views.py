from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import *
import requests
# Create your views here.

# because we have extended the default user model we no longer have to reference django.contrib.auth.models.User so get_user_model() is usefull
User = get_user_model()

# because we are not letting user to enter password for login or signup, so we sat a global password
PASSWORD = 'Kingsmen786'


# this function is called during some one visits "http://127.0.0.1:8000/signup" and will render "------"
def signup_page(request):
    # if user is already logged in he should be redirected to main page
    if request.user.is_authenticated:
        return redirect('main_page')

    # the values of this dictionary can be accessed in templates using keys
    context = {}

    # if user submits form with POST method, this if statement will be executed
    if request.method == 'POST':
        # grabing the username that was sent from frontend having input name = username in template 'base/auth/signup_page.html'
        username = request.POST['username']

        user = User.objects.create_user(username=username, password=PASSWORD)

        if user is None:
            messages.error(request, 'Something went wrong.')
            return redirect('signup_page')
        else:
            user.save()
            messages.success(request, 'Signup successfull')
            login(request, user)
            return redirect('main_page')
    return render(request, 'base/auth/signup_page.html', context)

# this function is called during some one visits "http://127.0.0.1:8000/login" and will render base/auth/login_page.html
def login_page(request):
    if request.user.is_authenticated:
        return redirect('main_page')

    context = {}
    # if user submits form with POST method, this if statement will be executed
    if request.method == 'POST':
        username = request.POST['username']
        # checks the credentials are correct?
        # if correct, it will return User object otherwise None
        user = authenticate(request, username=username, password=PASSWORD)

        # checking that the user is successfully authenticated
        if user is None:
            messages.error(request, 'User not found')
            return redirect('login_page')
        
        # registering user as logged in to some specific ip of client
        # adding server session entry
        login(request, user)
        messages.success(request, 'Logged in.')
        return redirect('main_page')

    return render(request, 'base/auth/login_page.html', context)

# this function is called during some one visits "http://127.0.0.1:8000/" and will render base/main/main_page.html
# @login_required is decorator which runs code of checking if user is authenticated or not, main_page() is a protected route so it ensures that user is logged in otherwise it is going to redirect to login page
@login_required
def main_page(request):
    context = {}

    # list of all the users who current user follows
    followings_users = request.user.following_users.all()


    # filtering if creator of the question is in the list of current following users.
    # getting all those question that were created by those users who are in the list of current user's "following_users"
    questions = Question.objects.filter(created_by__in=followings_users)

    # getting subjects and subtopics of those users who current logged in user user follows
    user_subjects = Subject.objects.filter(created_by__in=followings_users)
    user_subtopics = Subtopic.objects.filter(created_by__in=followings_users)

    # putting all the variables to context dictionary so that (main_page.html) will have access to them
    context['user_subjects'] = user_subjects
    context['user_subtopics'] = user_subtopics

    context['all_questions'] = questions
    context['user_subjects'] = user_subjects
    context['user_subtopics'] = user_subtopics
    return render(request, 'base/main/main_page.html', context)


# this function is called during some one visits "http://127.0.0.1:8000/all_questions_page" and will render base/main/all_questions_page.html
@login_required
def all_questions_page(request):
    context = {}

    # total questions and directly adding to context dictionary for frontend (all_questions_page.html) use
    context['all_questions'] = Question.objects.all()
    return render(request, 'base/main/all_questions_page.html', context)

# this function is called during some one visits "http://127.0.0.1:8000/post_question_page" and will render base/main/post_question_page.html
@login_required
def post_question_page(request):
    context = {}

    context['user_questions'] = Question.objects.filter(created_by=request.user).order_by('-created_at')

    user_subjects = Subject.objects.filter(created_by=request.user)
    user_subtopics = Subtopic.objects.filter(created_by=request.user)

    context['user_subjects'] = user_subjects
    context['user_subtopics'] = user_subtopics
    # if user submits form with POST method, this if statement will be executed
    if request.method == 'POST':
        title = request.POST['title']
        answer = request.POST['answer']
        subject_id = request.POST['subject']
        subtopic_id = request.POST['subtopic']
        
        # checking if user hasn't selected any subject
        # if not selected, user will be redirected to 'post_question_page' with message of 'please select a subject'
        if subject_id == "":
            messages.warning(request, 'Please Select a Subject')
            return redirect('post_question_page')



        try:
            subject = Subject.objects.get(id=int(str(subject_id)))
        except:
            messages.warning(request, 'Subject Does not exist. <a></a>')
            return redirect('post_question_page')

        question = Question(title=title, answer=answer, created_by=request.user, subject=subject)

        # if user has optionally selected a subtopic as well, the question will be included with subtopic as well
        if subtopic_id != "":
            subtopic = Subtopic.objects.get(id=int(str(subtopic_id)))
            question.subtopic = subtopic

        question.save()
        messages.success(request, 'Created a Question.')

    return render(request, 'base/main/post_question_page.html', context)



# this function is called during some one visits "http://127.0.0.1:8000/filter_questions_page" and will render base/main/filter_questions_page.html
@login_required
def filter_questions_page(request):
    context = {}

    if request.method == 'POST':
        subject_id = request.POST['subject']
        subtopic_id = request.POST['subtopic']

        if subject_id == "":
            messages.error(request, 'Please Select a subject.')
            return redirect('main_page')
        
        filtered_questions = Question.objects.filter(subject_id=subject_id)


        # of optionally user has selected subtopic as well, the questions will be filltered accourdingly
        if subtopic_id != "":
            filtered_questions.filter(subtopic_id=subtopic_id)
        
        context['filtered_questions'] = filtered_questions


    return render(request, 'base/main/filter_questions_page.html', context)

# this function is called during some one visits "http://127.0.0.1:8000/get_ans/<id of question>" resoponds with string response that will be putted at the end of question section
@login_required
def get_ans(request, question_id):
    context = {}
    current_question = Question.objects.get(id=question_id)
    # string response which will be concaticated to question cell's text at end 
    return HttpResponse(f'\nAnswer: {current_question.answer}')


# this function is called during some one visits "http://127.0.0.1:8000/find_accounts_page" and will render base/accounts/find_accounts_page.html
@login_required
def find_accounts_page(request):
    context = {}

    # filtering users that will exclude current user and sort by descending order of User.date_joined field
    all_users = User.objects.all().exclude(id=request.user.id).order_by('-date_joined')

    context['all_users'] = all_users

    if request.method == 'POST':
        username = request.POST['username']

        # searching with username
        # newly registered users will be on top
        users = User.objects.exclude(id=request.user.id).filter(username__icontains=username).order_by('-date_joined')
        print('post method', users)

        context['all_users'] = users

    return render(request, 'base/accounts/find_accounts_page.html', context)

# this function is called during some one visits "http://127.0.0.1:8000/create_subject" and will render base/main/create_subject.html
@login_required
def create_subject(request):
    context = {}
    if request.method == 'POST':
        subject_title = request.POST['title']

        # simply creating subject
        subject = Subject(title=subject_title, created_by=request.user)
        subject.save()
        messages.success(request, 'Created a Subject')
        return redirect('post_question_page')
    return render(request, 'base/main/create_subject.html', context)

# this function is called during some one visits "http://127.0.0.1:8000/create_subtopic" and will render base/main/create_subtopic.html
@login_required
def create_subtopic(request):
    context = {}
    if request.method == 'POST':
        subtopic_title = request.POST['title']

        subtopic = Subtopic(title=subtopic_title, created_by=request.user)
        subtopic.save()
        messages.success(request, 'Created a Subtopic')
        return redirect('post_question_page')
    return render(request, 'base/main/create_subtopic.html', context)

# this function is called during some one visits "http://127.0.0.1:8000/follow_unfollow/<with user id>" and will redirect to find_accounts_page
@login_required
def follow_unfollow(request, user_id):
    user = User.objects.get(id=user_id)
    current_user = User.objects.get(id=request.user.id)

    # if user is in in the current users following list is will remove it 
    if user in current_user.following_users.all():
        current_user.following_users.remove(user)
        messages.info(request, f'You are unfollowing {user.username}')

    # if user is not in in the current users following list is will add it 
    else:
        messages.success(request, f'You are following {user.username}')
        current_user.following_users.add(user)
    return redirect('find_accounts_page')




# this function is called during some one visits "http://127.0.0.1:8000/logout" and will redirect to login page
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out.')
    return redirect('login_page')