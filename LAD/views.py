from functools import lru_cache
from tkinter import FLAT
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from json import dumps
from django.db.models import Count
from django.db import connection
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from .models import User
from django.contrib.auth import authenticate
import datetime
import requests
from requests.structures import CaseInsensitiveDict
import os
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Create your views here.
import pickle
import pandas as pd
import json
from LAD.queries import (
    quer_t0,
    quer_t1,
    quer_t2,
    quer_t3,
    quer_t4,
    quer_t5,
    quer_t6,
    data_g,
    yes_no,
    team_ind,
)
from LAD.parameters import task_0, task_1, task_2, task_3, task_4, task_5, task_6
from LAD.feedback_queries import (
    task0_feed_box,
    task1_feed_box,
    task2_feed_box,
    task3_feed_box,
    task4_feed_box,
    task5_feed_box,
    stage1_feed_box_1,
    stage1_feed_box_2,
    stage1_feed_box_3,
    stage1_feed_box_4,
    task0_feed_box_legend,
    task1_feed_box_legend,
    task2_feed_box_legend,
    task3_feed_box_legend,
    task4_feed_box_legend,
    task5_feed_box_legend,
    stage1_feed_box_1_legend,
    stage1_feed_box_2_legend,
    stage1_feed_box_3_legend,
    stage1_feed_box_4_legend
)

############################# NEW IMPORTS ################################
# from piazza_api.rpc import PiazzaRPC
# from piazza_api import Piazza


#### ID and password for piazza login
# p = PiazzaRPC("kftixq5ewfwa8")
# p.user_login(email='',password='')

#### reading csv file of piazza data
pd.options.mode.chained_assignment = None  # default='warn'
SB = pd.read_csv("./piazza_stats/SB.csv")
VB = pd.read_csv("./piazza_stats/VB.csv")
VD = pd.read_csv("./piazza_stats/VD.csv")
NB = pd.read_csv("./piazza_stats/NB.csv")
SM = pd.read_csv("./piazza_stats/SM2.csv")
SM1 = pd.read_csv("./piazza_stats/SM1.csv")

#### creating frames for merging
frames = [SB, VB, VD, NB, SM]
frames1 = [SB, VB, VD, NB, SM1]

#### stage 2 dataframe
result = pd.concat(frames)
result.drop(["groups", "role"], axis=1, inplace=True)
result.fillna(0)

#### Stage 1 dataframe
result1 = pd.concat(frames1)
result1.drop(["groups", "role"], axis=1, inplace=True)
result1.fillna(0)


headers = CaseInsensitiveDict()
# headers["Content-Type"] = "multipart/form-data"
# headers["Api-Key"] = "187fa3a33adfd398305d2754044a9b26097eb680bc9154e5fe9a12a48ccf0074"
# headers["Api-Username"] = "ptp28"

headers["Content-Type"] = os.environ.get("Content_Type")
headers["Api-Key"] = os.environ.get("Api_Key")
headers["Api-Username"] = os.environ.get("Api_Username")

files = {"limit": "ALL"}
userTheme = None
# def userTheme():
#     return user_theme

#### function for login of user
def login(request):
    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # print("\n\n####\nUser: ", user)
            theme = User.objects.get(username=username)
            # global userTheme
            # userTheme = theme.theme
            # userTheme = User.objects.all()
            # for element in theme:
            # print("\n\n", theme.values(), "\n\n")
            # print("\n\n########\nLOGIN:", theme)
            auth.login(request, user)
            return redirect("/dashboard")
        else:
            return redirect("/login")
    else:
        return render(request, "login.html")


#### function for logging out user
def logout(request):
    auth.logout(request)
    return redirect("/login")


#### function for dashboard
def dashboard(request):

    # cur = connections["discourse"].cursor()
    # discourse_query = "SELECT DISTINCT topics.id,topics.title,topics.category_id,categories.name from topics,categories,users where topics.category_id=categories.id  AND topics.user_id=users.id AND users.moderator is true order by  categories.name;"
    
    # To get the theme of the user
    theme = User.objects.get(username=request.user).theme
    # print("\n\n###########\nTheme: ", theme)
    
    # discourse_topics = pd.read_sql(discourse_query, con=connections["discourse"])
    seen_url = "https://discuss.e-yantra.org/admin/plugins/explorer/queries/10/run"
    resp = requests.post(seen_url, headers=headers, data=files)
    discourse_topics = pd.DataFrame(resp.json()["rows"], columns=resp.json()["columns"])
    discourse_categories = discourse_topics[["name", "category_id"]]
    discourse_categories = (
        discourse_categories.groupby(["name", "category_id"]).max().reset_index()
    )
    discourse_categories = discourse_categories.to_json()
    discourse_topics = discourse_topics.to_json()
    # print("\n\n#####################\nDiscourse Topics: ", discourse_topics)
    # print("\n\n#####################\nDiscourse Categories: ", discourse_categories)
    # j = cur.execute(discourse_query)
    # discourse_topics = cur.fetchall()
    # discourse_topics = dumps(discourse_topics)

    url_general = "https://discuss.e-yantra.org/admin/plugins/explorer/queries/6/run"
    resp_general = requests.post(url_general, headers=headers, data=files)
    # print("\n\n#####################\nurl general: ", resp_general.json()["rows"][0][3])
    
    url_instruct = "https://discuss.e-yantra.org/admin/plugins/explorer/queries/7/run"
    resp_instruct = requests.post(url_instruct, headers=headers, data=files)
    # print("\n\n#####################\nurl instructor: ", resp_instruct.json()["rows"][0])


    url_student = "https://discuss.e-yantra.org/admin/plugins/explorer/queries/8/run"
    resp_student = requests.post(url_student, headers=headers, data=files)
    # print("\n\n#####################\nurl student: ", resp_student.json()["rows"][0])
    stats = {
        "posts": int(resp_general.json()["rows"][0][0])
        + int(resp_general.json()["rows"][0][1])
        + int(resp_general.json()["rows"][0][2]),
        "questions": int(resp_general.json()["rows"][0][1]),
        "i_answers": int(resp_instruct.json()["rows"][0][0]),
        "s_answers": int(resp_student.json()["rows"][0][0]),
        "net_time": 0,
        "anon_pool": 0,
        "response_time": int(resp_general.json()["rows"][0][3].split('.')[0]),
        "theme": "VBSBNBSMVD",
    }
    id=int(os.environ.get("Current_Task"))
    # id = 0
    team_data = pd.read_csv("./pred_csv_files/task_{}_pred.csv".format(id))
    cursor = connection.cursor()
    sql_sub_thistask = """SELECT theme,COUNT(team_id) AS submitted FROM (SELECT * FROM task{}_status GROUP BY team_id) v GROUP by theme;""".format(
        id
    )
    #### get students submitted this task
    j = cursor.execute(sql_sub_thistask)
    this_task = cursor.fetchall()
    this_task = dumps(this_task)

    if id == 0:
        #### get list of parameters
        parameters = task_0

        #### set threshold value
        thresh = 0.8
    if id == 1:
        #### get list of parameters
        parameters = task_1

        #### set threshold value
        thresh = 0.66
    if id == 2:
        #### get list of parameters
        parameters = task_2

        #### set threshold value
        thresh = 0.6
    if id == 3:
        #### get list of parameters
        parameters = task_3

        #### set threshold value
        thresh = 0.65
    if id == 4:
        #### get list of parameters
        parameters = task_4

        #### set threshold value
        thresh = 0.65
    if id == 5:
        #### get list of parameters
        parameters = task_5

        #### set threshold value
        thresh = 0.77

    if id == 6:
        #### get list of parameters
        parameters = task_6

        #### set threshold value
        thresh = 0.79

    js = team_data.to_json()
    parameters = dumps(parameters)

    return render(
        request,
        "dashboard.html",
        {
            "theme":theme,
            "piazza_stats": stats,
            "json_data": js,
            "parameters": parameters,
            "thresh": thresh,
            "this_task": this_task,
            "current_task": id,
            "discourse_topics": discourse_topics,
            "discourse_categories": discourse_categories,
        },
    )


def temp(request):
    return render(request, "temp.html")


############# SIGNUP CHANGES ##############
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        # print("\n\nForm:\n", request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            #### load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get("password1")

            #### login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            auth.login(request, user)

            #### redirect user to home page
            return redirect("/task/0")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


# @lru_cache
def models_stats(request, id=None):
    #### create cursor instance
    team_data = pd.read_csv(
        "./pred_csv_files/task_{}_pred.csv".format(id), encoding="utf-8"
    )
    time1 = team_data["time_stamp"][0][:-7]
    fmt = "%Y-%m-%d %H:%M:%S"
    td = datetime.datetime.now() - datetime.datetime.strptime(time1, fmt)
    td_mins = int(round(td.total_seconds() / 60))
    cursor = connection.cursor()
    t = "Task" + str(id)
    t = dumps(t)

    #### declaring Required SQL queries
    sql_sub_by_date = '''SELECT COUNT(id) AS No_of_submissions,theme, CONVERT(CAST(created_at AS DATE), CHAR) AS Date_of_submission FROM task{}_status GROUP BY CAST(created_at AS DATE),theme;'''.format(id)
    # sql_sub_by_date = """SELECT COUNT(u.team_member_id) AS No_of_submissions,theme,CONVERT(CAST(u.created_at AS DATE), CHAR) as Date_of_submission
    #                     FROM login u,team_details td,team_member_detail tmd 
    #                     WHERE uri="profile_home" 
    #                     AND u.team_member_id = tmd.id
    #                     AND tmd.team_id = td.id
    #                     AND td.theme IS NOT NULL
    #                     GROUP BY DATE(u.created_at),td.theme 
    #                     ORDER by DATE(u.created_at) DESC LIMIT 60;"""
    sql_task_list = """SELECT team_id,theme,CONVERT(MAX(task{0}_date), CHAR) AS date_of_submit FROM task{0}_status GROUP BY team_id;""".format(
        id
    )
    sql_total = """SELECT theme,COUNT(id) AS submitted FROM (SELECT * FROM team_details WHERE eyrc=1  GROUP BY id) v GROUP by theme;"""
    sql_sub_thistask = """SELECT theme,COUNT(team_id) AS submitted FROM (SELECT * FROM task{}_status GROUP BY team_id) v GROUP by theme;""".format(
        id
    )
    if id != 0:
        sql_sub_prev_task = """SELECT theme,COUNT(team_id) AS submitted FROM (SELECT * FROM task{}_status GROUP BY team_id) v GROUP by theme;""".format(
            id - 1
        )
    else:
        sql_sub_prev_task = """SELECT theme,COUNT(team_id) AS submitted FROM (SELECT * FROM task{}_status GROUP BY team_id) v GROUP by theme;""".format(
            id
        )

    #### Executing queries
    #### get total No. of students in theme
    i = cursor.execute(sql_total)
    total = cursor.fetchall()
    total = dumps(total)
    # print("\n\nTotal: ", total)

    #### get students submitted this task
    j = cursor.execute(sql_sub_thistask)
    this_task = cursor.fetchall()
    this_task = dumps(this_task)

    #### get students submitted previous task
    k = cursor.execute(sql_sub_prev_task)
    prev_task = cursor.fetchall()
    prev_task = dumps(prev_task)

    #### get list teams submitted this task for table
    cursor.execute(sql_task_list)
    this_task_list = cursor.fetchall()
    this_task_list = dumps(this_task_list)
    # this_task_list = []
    #### get submission by date
    cursor.execute(sql_sub_by_date)
    sub_by_date = cursor.fetchall()
    sub_by_date = dumps(sub_by_date)
    # sub_by_date = []

    if id == 0:
        #### get list of parameters
        parameters = task_0

        #### set threshold value
        thresh = 0.8
    if id == 1:
        #### get list of parameters
        parameters = task_1

        #### set thresholdtask_2 value
        thresh = 0.66
    if id == 2:
        #### get list of parameters
        parameters = task_2

        #### set threshold value
        thresh = 0.6
    if id == 3:
        #### get list of parameters
        parameters = task_3

        #### set threshold value
        thresh = 0.65
    if id == 4:
        #### get list of parameters
        parameters = task_4

        #### set threshold value
        thresh = 0.65
    if id == 5:
        #### get list of parameters
        parameters = task_5

        #### set threshold value
        thresh = 0.77

    if id == 6:
        #### get list of parameters
        parameters = task_6

        #### set threshold value
        thresh = 0.79

    #### get details for email and phone No. column
    s = pd.read_csv(
        "./contact_info_csv_files/task_{}_contact.csv".format(id), encoding="utf-8"
    )
    m = s.to_json()
    js = team_data.to_json()
    parameters = dumps(parameters)
    #### Sending data to HTML
    if request.user.is_authenticated:
        return render(
            request,
            "index.html",
            {
                "theme": User.objects.get(username=request.user).theme,
                "total": total,
                "this_task": this_task,
                "prev_task": prev_task,
                "taskname": t,
                "sub_this_task": this_task_list,
                "sub_by_date": sub_by_date,
                "json_data": js,
                "parameters": parameters,
                "thresh": thresh,
                "details": m,
            },
        )
    else:
        return redirect("login")


# SELECT team_grades.team_id,team_grades.theme,team_grades.task3_penalty,AVG(task0_marks) as Task0, AVG(task1a_marks+task1b_marks+task1c_marks) as Task1,AVG(task2a_marks+task2b_marks) as Task2,AVG(task3_marks) as Task3,AVG(rateTask3),AVG(rateTask3Design),AVG(rateSelfContribution),AVG(rateResource),AVG(rateForumUsefulness) FROM team_grades,task3_feedback WHERE team_grades.team_id = task3_feedback.team_id GROUP BY team_id
# SELECT team_grades.team_id,team_grades.theme,AVG(task0_marks) as Task0, AVG(task1a_marks+task1b_marks+task1c_marks) as Task1,AVG(task2a_marks+task2b_marks) as Task2,AVG(task3_marks) as Task3,AVG(rateTask3),AVG(rateTask3Design),AVG(rateSelfContribution),AVG(rateResource),AVG(rateForumUsefulness) FROM team_grades,task3_feedback WHERE team_grades.team_id = task3_feedback.team_id AND team_grades.team_id NOT IN (SELECT team_id FROM task4_status GROUP BY team_id) GROUP BY team_id
# task6-threshold-0.8
# @lru_cache
# def prediction(request):
#     scaler = StandardScaler()
#     pca = PCA()
#     log = pickle.load(open('pred_t6_pca.sav', 'rb'))
#     new_data = pd.read_sql(quer_t6, con=connection)
#     new_data['teamOrindividual'] = new_data['teamOrindividual'].apply(
#         team_ind)
#     new_data['covidCase'] = new_data['covidCase'].apply(yes_no)
#     new_data['rateMotivation'] = new_data['rateMotivation'].apply(
#         yes_no)
#     new_up_data = new_data.groupby('team_id', as_index=False).mean()
#     total_data = pd.read_sql(data_g, con=connection)
#     new_fi_data = total_data.merge(
#         new_up_data, on='team_id', how='right')
#     t2 = new_fi_data[['rateMyPerformance',
#                       'rateMyLearning', 'rateMyFocus', 'rateStressLevel', 'rateWorkManagement']]
#     t3 = new_fi_data[['rateTask5Design', 'rateSelfContribution',
#                       'rateResource', 'rateDifficulty', 'rateLiveSessionUsefulness']]
#     t4 = new_fi_data[['ratetheme', 'rateProblemStatement',
#                       'rateKnowledgeOfPreviousTask', 'rateInstructorResponse', 'rateStudentResponse']]
#     t2 = scaler.fit(t2).transform(t2)
#     t3 = scaler.fit(t3).transform(t3)
#     t4 = scaler.fit(t4).transform(t4)
#     t2 = pca.fit(t2).transform(t2)
#     t3 = pca.fit(t3).transform(t3)
#     t4 = pca.fit(t4).transform(t4)
#     new_fi_data.drop(['rateMyPerformance', 'rateMyLearning', 'rateMyFocus', 'rateStressLevel', 'rateWorkManagement', 'rateTask5Design', 'rateSelfContribution', 'rateResource', 'rateDifficulty',
#                       'rateLiveSessionUsefulness', 'ratetheme', 'rateProblemStatement', 'rateKnowledgeOfPreviousTask', 'rateInstructorResponse', 'rateStudentResponse'], axis=1, inplace=True)
#     new_fi_data["pca_1_1"] = t2[:, 0]
#     new_fi_data["pca_2_1"] = t3[:, 0]
#     new_fi_data["pca_3_1"] = t4[:, 0]
#     team_data = new_fi_data[['team_id', "theme"]]
#     new_fi_data.drop(['team_id', 'theme'], axis=1, inplace=True)
#     print(new_fi_data.columns)
#     predictions = log.predict(new_fi_data)
#     conf = log.predict_proba(new_fi_data)[:, 1]
#     confidence = pd.DataFrame(conf, columns=['confidence'])
#     predict = pd.DataFrame(predictions)
#     team_data["prediction"] = predict
#     team_data["confidence"] = confidence
#     js = team_data.to_json()
#     j = json.loads(js)
#     j = dumps(j)
#     return render(request, "predictions.html", {"json_data": j})


# def taskData2(request,id):
#     team_data = pd.read_csv("./pred_csv_files/task_{}_pred.csv".format(id),encoding='utf-8')
#     time1 = team_data["time_stamp"][0][:-7]
#     fmt = '%Y-%m-%d %H:%M:%S'
#     td = datetime.datetime.now() - datetime.datetime.strptime(time1, fmt)
#     td_mins = int(round(td.total_seconds() / 60))

#     if td_mins<120:
#         cursor = connection.cursor()
#         sql_sub_thistask = """SELECT theme,COUNT(team_id) AS submitted FROM (SELECT * FROM task{}_status GROUP BY team_id) v GROUP by theme;""".format(
#             id
#         )
#         #### get students submitted this task
#         j = cursor.execute(sql_sub_thistask)
#         this_task = cursor.fetchall()
#         this_task = dumps(this_task)

#         if id==0:
#             #### get data from database
#             new_data = pd.read_sql(quer_t0, con=connection)

#             #### get list of parameters
#             parameters = task_0

#             #### set threshold value
#             thresh = 0.8
#         if id==1:
#             #### get data from database
#             new_data = pd.read_sql(quer_t1, con=connection)

#             #### get list of parameters
#             parameters = task_1

#             #### set threshold value
#             thresh = 0.66
#         if id==2:
#             #### get data from database
#             new_data = pd.read_sql(quer_t2, con=connection)

#             #### get list of parameters
#             parameters = task_2

#             #### set threshold value
#             thresh = 0.6
#         if id==3:
#             #### get data from database
#             new_data = pd.read_sql(quer_t3, con=connection)

#             #### get list of parameters
#             parameters = task_3

#             #### set threshold value
#             thresh = 0.65
#         if id==4:
#             #### get data from database
#             new_data = pd.read_sql(quer_t4, con=connection)

#             #### get list of parameters
#             parameters = task_4

#             #### set threshold value
#             thresh = 0.65
#         if id==5:
#             #### get data from database
#             new_data = pd.read_sql(quer_t5, con=connection)

#             #### get list of parameters
#             parameters = task_5

#             #### set threshold value
#             thresh = 0.77

#         if id==6:
#             #### get data from database
#             new_data = pd.read_sql(quer_t6, con=connection)

#             #### get list of parameters
#             parameters = task_6

#             #### set threshold value
#             thresh = 0.79

#         #### get details for email and phone No. column
#         details = new_data[["team_id", "team_member_id", "email", "phone_no"]]

#         #### list of all the teams in the task
#         teams = list(details["team_id"].unique())
#         d = {}
#         #### max no of team members
#         team_mem = 4

#         #### loop to get all team members data
#         for i in teams:
#             j = details[details["team_id"] == i].shape[0]
#             k = details[details["team_id"] == i]["email"].reset_index()
#             l = details[details["team_id"] == i]["phone_no"].reset_index()
#             lst = []
#             lst1 = []
#             lst3 = []
#             for w in range(j):
#                 lst.append(k["email"].loc[w])
#                 lst1.append(l["phone_no"].loc[w])
#             if j < team_mem:
#                 rem = team_mem - j
#                 lst.extend([0] * rem)
#                 lst1.extend([0] * rem)

#             lst3.append(lst)
#             lst3.append(lst1)
#             d[i] = lst3
#         s = pd.DataFrame.from_dict(d)

#         m = s.to_json()
#         js = team_data.to_json()
#         parameters = dumps(parameters)
#         return JsonResponse(
#             {
#                 "json_data": js,
#                 "parameters": parameters,
#                 "thresh": thresh,
#                 "details": m,
#                 "this_task": this_task,
#             }
#         )
#     else:
#         return taskData(request,id)


def taskData(request, id):
    #### declaring all variables
    team_data = 0
    new_fi_data = 0
    piazza_data = 0
    new_data = 0
    scaler = StandardScaler()
    pca = PCA()
    print(id)
    thresh = 0
    details = 0
    mapping_file = pd.read_csv("./piazza_stats/mapping_eylad_to_discourse.csv")

    ##### Piazza data using api
    # SB = (p.get_stats(nid='kia22579y074p9')) #url of theme 1
    # VB = (p.get_stats(nid='kftixq5ewfwa8'))
    # VD = (p.get_stats(nid='kia22579y074p9'))
    # NB = (p.get_stats(nid='kia22579y074p9'))
    # SM2 = (p.get_stats(nid='kia22579y074p9'))
    # SM1 = (p.get_stats(nid='kia22579y074p9'))

    # SB = pd.DataFrame(SM["users"]) #url of theme 1
    # VB = pd.DataFrame(VB["users"])
    # VD = pd.DataFrame(VD["users"])
    # NB = pd.DataFrame(NB["users"])
    # SM2 = pd.DataFrame(SM2["users"])
    # SM1 = pd.DataFrame(SM1["users"])

    # frames = [SB, VB, VD, NB, SM2]
    # frames1 = [SB, VB, VD, NB, SM1]
    # result = pd.concat(frames)
    # result.drop(['groups', 'role',"lti_ids"], axis=1, inplace=True)
    # result.fillna(0)
    # result1 = pd.concat(frames1)
    # result1.drop(['groups', 'role',"lti_ids"], axis=1, inplace=True)
    # result1.fillna(0)

    #### create cursor instance
    cursor = connection.cursor()
    sql_sub_thistask = """SELECT theme,COUNT(team_id) AS submitted FROM (SELECT * FROM task{}_status GROUP BY team_id) v GROUP by theme;""".format(
        id
    )
    #### get students submitted this task
    j = cursor.execute(sql_sub_thistask)
    this_task = cursor.fetchall()
    this_task = dumps(this_task)

    login_query = 'SELECT team_member_id,COUNT(created_at) AS login_count FROM `user_activity` WHERE uri="profile_home" GROUP BY team_member_id;'
    login_data = pd.read_sql(login_query, con=connection)

    general_url = "https://discuss.e-yantra.org/admin/plugins/explorer/queries/4/run"
    resp = requests.post(general_url, headers=headers, data=files)
    discourse_data = pd.DataFrame(resp.json()["rows"], columns=resp.json()["columns"])

    followups_url = "https://discuss.e-yantra.org/admin/plugins/explorer/queries/3/run"
    resp = requests.post(followups_url, headers=headers, data=files)
    followups = pd.DataFrame(resp.json()["rows"], columns=resp.json()["columns"])

    reply_to_followups_url = "https://discuss.e-yantra.org/admin/plugins/explorer/queries/5/run"

    resp = requests.post(reply_to_followups_url, headers=headers, data=files)
    reply_to_followups = pd.DataFrame(
        resp.json()["rows"], columns=resp.json()["columns"]
    )

    discourse_data = discourse_data.merge(
        followups, how="left", left_on="user_id", right_on="user_id"
    )

    discourse_data = discourse_data.merge(
        reply_to_followups, how="left", left_on="user_id", right_on="user_id"
    )

    discourse_data.fillna(value=0,inplace=True)

    if id == 0:

        #### get the model based on task
        log = pickle.load(open("./models/pred_t0.sav", "rb"))

        #### get data from database
        new_data = pd.read_sql(quer_t0, con=connection)

        #### fill NaN with 0
        new_data = new_data.fillna(0)

        #### get details for email and phone No. column
        details = new_data[["team_id", "team_member_id", "email", "phone_no"]]

        #### for merging piazza data with database when using api
        # new_data = new_data.merge(result1,how='left', left_on='email', right_on='email')

        #### droping unwanted columns
        new_data.drop(["email", "phone_no"], axis=1, inplace=True)

        #### merging piazza data with database using csv file
        # new_database = new_data.merge(
        #     result1, how="left", left_on="team_member_id", right_on="team_member_id"
        # )

        new_data = new_data.merge(
            login_data, how="left", left_on="team_member_id", right_on="team_member_id"
        )

        new_database = new_data.merge(
            mapping_file,
            how="left",
            left_on="team_member_id",
            right_on="team_member_id",
        )

        new_database = new_database.merge(
            discourse_data, how="left", left_on="user_id", right_on="user_id"
        )

        new_database.fillna(value=0,inplace=True)

        #### drop unwanted columns
        new_database.drop(["team_member_id", "user_id"], axis=1, inplace=True)

        #### create copy to extract piazza data
        piazza_data = new_database

        #### get mean of data grouped by id
        new_up_data = new_data.groupby("team_id", as_index=False).mean()

        #### group by team_id
        new_data = new_data.groupby("team_id", as_index=False)

        #### get login data
        last_login_data = new_data.max()[["team_id", "last_login", "login_count"]]

        #### teams eligible for eyrc
        total_data = pd.read_sql(data_g, con=connection)

        #### merge data to get only eligible teams
        new_fi_data = total_data.merge(new_up_data, on="team_id", how="right")

        #### drop unwanted column
        new_fi_data.drop(["team_member_id"], axis=1, inplace=True)

        #### get list of parameters
        parameters = task_0

        #### set threshold value
        thresh = 0.8
    elif id == 1:
        #### get the model based on task
        log = pickle.load(open("./models/pred_t1.sav", "rb"))

        #### get data from database
        new_data = pd.read_sql(quer_t1, con=connection)

        #### get details for email and phone No. column
        details = new_data[["team_id", "team_member_id", "email", "phone_no"]]

        #### for merging piazza data with database when using api
        # new_data = new_data.merge(result1,how='left', left_on='email', right_on='email')

        #### droping unwanted columns
        new_data.drop(["email", "phone_no"], axis=1, inplace=True)

        #### merging piazza data with database using csv file
        # new_database = new_data.merge(
        #     result1, how="left", left_on="team_member_id", right_on="team_member_id"
        # )

        new_data = new_data.merge(
            login_data, how="left", left_on="team_member_id", right_on="team_member_id"
        )

        new_database = new_data.merge(
            mapping_file,
            how="left",
            left_on="team_member_id",
            right_on="team_member_id",
        )

        new_database = new_database.merge(
            discourse_data, how="left", left_on="user_id", right_on="user_id"
        )

        new_database.fillna(value=0,inplace=True)

        #### drop unwanted columns
        new_database.drop(["team_member_id", "user_id"], axis=1, inplace=True)

        #### create copy to extract piazza data
        piazza_data = new_database

        #### get mean of data grouped by id
        new_database = new_database.groupby("team_id", as_index=False).mean()

        #### teams eligible for eyrc
        total_data = pd.read_sql(data_g, con=connection)

        #### merge data to get only eligible teams
        new_database = total_data.merge(new_database, on="team_id", how="right")

        #### fill NaN with 0
        new_database = new_database.fillna(0)

        #### group by team_id
        new_data = new_data.groupby("team_id", as_index=False)

        #### get login data
        last_login_data = new_data.max()[["team_id", "last_login", "login_count"]]

        #### create new instance of database
        new_fi_data = new_database

        #### Select parameters for PCA
        t5 = new_fi_data[
            ["answers", "edits to answers", "followups", "reply to followups"]
        ]

        #### Apply PCA to the values
        t5 = scaler.fit(t5).transform(t5)
        t5 = pca.fit(t5).transform(t5)

        #### drop unwanted column
        new_fi_data.drop(
            ["answers", "edits to answers", "followups", "reply to followups"],
            axis=1,
            inplace=True,
        )

        #### Adding PCA column
        new_fi_data["pca_1_1"] = t5[:, 0]

        #### set threshold value
        thresh = 0.66

        #### get list of parameters
        parameters = task_1
    elif id == 2:
        scaler = StandardScaler()
        pca = PCA()

        #### get the model based on task
        log = pickle.load(open("./models/pred_t2.sav", "rb"))

        #### get data from database
        new_data = pd.read_sql(quer_t2, con=connection)

        #### get details for email and phone No. column
        details = new_data[["team_id", "team_member_id", "email", "phone_no"]]

        #### for merging piazza data with database when using api
        # new_data = new_data.merge(result1,how='left', left_on='email', right_on='email')

        #### droping unwanted columns
        new_data.drop(["email", "phone_no"], axis=1, inplace=True)

        #### group by team_id and get max count
        last_login_data = new_data.groupby("team_id", as_index=False).max()[
            ["team_id", "last_login", "login_count"]
        ]

        #### merging piazza data with database using csv file
        # new_database = new_data.merge(
        #     result1, how="left", left_on="team_member_id", right_on="team_member_id"
        # )

        new_data = new_data.merge(
            login_data, how="left", left_on="team_member_id", right_on="team_member_id"
        )

        new_database = new_data.merge(
            mapping_file,
            how="left",
            left_on="team_member_id",
            right_on="team_member_id",
        )

        new_database = new_database.merge(
            discourse_data, how="left", left_on="user_id", right_on="user_id"
        )

        new_database.fillna(value=0,inplace=True)

        #### drop unwanted columns
        new_database.drop(["team_member_id", "user_id"], axis=1, inplace=True)

        #### create copy to extract piazza data
        piazza_data = new_database

        #### get mean of data grouped by id
        new_database = new_database.groupby("team_id", as_index=False).mean()

        #### teams eligible for eyrc
        total_data = pd.read_sql(data_g, con=connection)

        #### merge data to get only eligible teams
        new_database = total_data.merge(new_database, on="team_id", how="right")

        #### fill NaN with 0
        new_database = new_database.fillna(0)

        #### create new instance of database
        new_fi_data = new_database

        #### Select parameters for PCA
        t5 = new_fi_data[
            ["answers", "edits to answers", "followups", "reply to followups"]
        ]

        #### Apply PCA to the values
        t5 = scaler.fit(t5).transform(t5)
        t5 = pca.fit(t5).transform(t5)

        #### drop unwanted column
        new_fi_data.drop(
            ["answers", "edits to answers", "followups", "reply to followups"],
            axis=1,
            inplace=True,
        )

        #### Adding PCA column
        new_fi_data["pca_1_1"] = t5[:, 0]

        #### set threshold value
        thresh = 0.6

        #### get list of parameters
        parameters = task_2
    elif id == 3:
        scaler = StandardScaler()
        pca = PCA()
        #### get the model based on task
        log = pickle.load(open("./models/pred_t3.sav", "rb"))

        #### get data from database
        new_data = pd.read_sql(quer_t3, con=connection)

        #### get details for email and phone No. column
        details = new_data[["team_id", "team_member_id", "email", "phone_no"]]

        #### for merging piazza data with database when using api
        # new_data = new_data.merge(result1,how='left', left_on='email', right_on='email')

        #### droping unwanted columns
        new_data.drop(["email", "phone_no"], axis=1, inplace=True)

        new_data["covidCase"] = new_data["covidCase"].apply(yes_no)

        #### merging piazza data with database using csv file
        # new_database = new_data.merge(
        #     result, how="left", left_on="team_member_id", right_on="team_member_id"
        # )

        new_data = new_data.merge(
            login_data, how="left", left_on="team_member_id", right_on="team_member_id"
        )

        new_database = new_data.merge(
            mapping_file,
            how="left",
            left_on="team_member_id",
            right_on="team_member_id",
        )

        new_database = new_database.merge(
            discourse_data, how="left", left_on="user_id", right_on="user_id"
        )

        new_database.fillna(value=0,inplace=True)

        #### drop unwanted columns
        new_database.drop(["team_member_id", "user_id"], axis=1, inplace=True)

        #### create copy to extract piazza data
        piazza_data = new_database

        #### get mean of data grouped by id
        new_database = new_database.groupby("team_id", as_index=False).mean()

        #### teams eligible for eyrc
        total_data = pd.read_sql(data_g, con=connection)

        #### merge data to get only eligible teams
        new_database = total_data.merge(new_database, on="team_id", how="right")

        #### fill NaN with 0
        new_database = new_database.fillna(0)

        #### group by team_id
        new_data = new_data.groupby("team_id", as_index=False)

        #### get login data
        last_login_data = new_data.max()[["team_id", "last_login", "login_count"]]

        #### teams eligible for eyrc
        total_data = pd.read_sql(data_g, con=connection)

        #### create new instance of database
        new_fi_data = new_database

        #### Select parameters for PCA
        t2 = new_fi_data[
            [
                "rateMyPerformance",
                "rateMyLearning",
                "rateMyFocus",
                "rateSressLevel",
                "rateWork",
            ]
        ]
        t3 = new_fi_data[
            ["rateTask2", "rateTask2Design", "rateSelfContribution", "rateResource"]
        ]
        t4 = new_fi_data[
            [
                "ratetheme",
                "rateProblemStatement",
                "rateKnowledgeOfPreviousTask",
                "rateInstructorResponse",
                "rateStudentResponse",
            ]
        ]
        t5 = new_fi_data[
            ["answers", "edits to answers", "followups", "reply to followups"]
        ]

        #### Apply PCA to the values
        t2 = scaler.fit(t2).transform(t2)
        t3 = scaler.fit(t3).transform(t3)
        t4 = scaler.fit(t4).transform(t4)
        t5 = scaler.fit(t5).transform(t5)
        t2 = pca.fit(t2).transform(t2)
        t3 = pca.fit(t3).transform(t3)
        t4 = pca.fit(t4).transform(t4)
        t5 = pca.fit(t5).transform(t5)

        #### drop unwanted column
        new_fi_data.drop(
            [
                "rateMyPerformance",
                "rateMyLearning",
                "rateMyFocus",
                "rateSressLevel",
                "rateWork",
                "rateTask2",
                "rateTask2Design",
                "rateSelfContribution",
                "rateResource",
                "ratetheme",
                "rateProblemStatement",
                "rateKnowledgeOfPreviousTask",
                "rateInstructorResponse",
                "rateStudentResponse",
                "answers",
                "edits to answers",
                "followups",
                "reply to followups",
            ],
            axis=1,
            inplace=True,
        )

        #### Adding PCA columns
        new_fi_data["pca_1_1"] = t2[:, 0]
        new_fi_data["pca_2_1"] = t3[:, 0]
        new_fi_data["pca_3_1"] = t4[:, 0]
        new_fi_data["pca_4_1"] = t5[:, 0]

        #### set threshold value
        thresh = 0.65

        #### get list of parameters
        parameters = task_3
    elif id == 4:
        scaler = StandardScaler()
        pca = PCA()
        #### get the model based on task
        log = pickle.load(open("./models/pred_t4.sav", "rb"))

        #### get data from database
        new_data = pd.read_sql(quer_t4, con=connection)

        #### get details for email and phone No. column
        details = new_data[["team_id", "team_member_id", "email", "phone_no"]]

        #### for merging piazza data with database when using api
        # new_data = new_data.merge(result1,how='left', left_on='email', right_on='email')

        #### droping unwanted columns
        new_data.drop(["email", "phone_no"], axis=1, inplace=True)

        new_data["teamOrindividual"] = new_data["teamOrindividual"].apply(team_ind)

        #### group by team_id and get max count
        last_login_data = new_data.groupby("team_id", as_index=False).max()[
            ["team_id", "last_login", "login_count"]
        ]

        #### merging piazza data with database using csv file
        # new_database = new_data.merge(
        #     result, how="left", left_on="team_member_id", right_on="team_member_id"
        # )

        new_data = new_data.merge(
            login_data, how="left", left_on="team_member_id", right_on="team_member_id"
        )

        new_database = new_data.merge(
            mapping_file,
            how="left",
            left_on="team_member_id",
            right_on="team_member_id",
        )

        new_database = new_database.merge(
            discourse_data, how="left", left_on="user_id", right_on="user_id"
        )

        new_database.fillna(value=0,inplace=True)
        #### drop unwanted columns
        new_database.drop(["team_member_id", "user_id"], axis=1, inplace=True)

        #### create copy to extract piazza data
        piazza_data = new_database

        #### get mean of data grouped by id
        new_database = new_database.groupby("team_id", as_index=False).mean()

        #### teams eligible for eyrc
        total_data = pd.read_sql(data_g, con=connection)

        #### merge data to get only eligible teams
        new_database = total_data.merge(new_database, on="team_id", how="right")

        #### fill NaN with 0
        new_database = new_database.fillna(0)

        #### create new instance of database
        new_fi_data = new_database

        #### Select parameters for PCA
        t2 = new_fi_data[
            [
                "rateMyPerformance",
                "rateMyLearning",
                "rateMyFocus",
                "rateSressLevel",
                "rateWork",
            ]
        ]
        t3 = new_fi_data[
            ["rateTask", "rateTaskDesign", "rateSelfContribution", "rateResource"]
        ]
        t4 = new_fi_data[
            [
                "ratetheme",
                "rateProblemStatement",
                "rateKnowledgeOfPreviousTask",
                "rateInstructorResponse",
                "rateStudentResponse",
            ]
        ]
        t5 = new_fi_data[
            ["answers", "edits to answers", "followups", "reply to followups"]
        ]

        #### Apply PCA to the values
        t2 = scaler.fit(t2).transform(t2)
        t3 = scaler.fit(t3).transform(t3)
        t4 = scaler.fit(t4).transform(t4)
        t5 = scaler.fit(t5).transform(t5)
        t2 = pca.fit(t2).transform(t2)
        t3 = pca.fit(t3).transform(t3)
        t4 = pca.fit(t4).transform(t4)
        t5 = pca.fit(t5).transform(t5)

        #### drop unwanted column
        new_fi_data.drop(
            [
                "rateMyPerformance",
                "rateMyLearning",
                "rateMyFocus",
                "rateSressLevel",
                "rateWork",
                "rateTask",
                "rateTaskDesign",
                "rateSelfContribution",
                "rateResource",
                "ratetheme",
                "rateProblemStatement",
                "rateKnowledgeOfPreviousTask",
                "rateInstructorResponse",
                "rateStudentResponse",
                "answers",
                "edits to answers",
                "followups",
                "reply to followups",
            ],
            axis=1,
            inplace=True,
        )

        #### Adding PCA columns
        new_fi_data["pca_1_1"] = t2[:, 0]
        new_fi_data["pca_2_1"] = t3[:, 0]
        new_fi_data["pca_3_1"] = t4[:, 0]
        new_fi_data["pca_4_1"] = t5[:, 0]

        #### set threshold value
        thresh = 0.65

        #### get list of parameters
        parameters = task_4
    elif id == 5:
        scaler = StandardScaler()
        pca = PCA()
        #### get the model based on task
        log = pickle.load(open("./models/pred_t5.sav", "rb"))

        #### get data from database
        new_data = pd.read_sql(quer_t5, con=connection)

        #### get details for email and phone No. column
        details = new_data[["team_id", "team_member_id", "email", "phone_no"]]

        #### for merging piazza data with database when using api
        # new_data = new_data.merge(result1,how='left', left_on='email', right_on='email')

        #### droping unwanted columns
        new_data.drop(["email", "phone_no"], axis=1, inplace=True)

        #### merging piazza data with database using csv file
        new_data = new_data.merge(
            login_data, how="left", left_on="team_member_id", right_on="team_member_id"
        )

        new_database = new_data.merge(
            mapping_file,
            how="left",
            left_on="team_member_id",
            right_on="team_member_id",
        )

        new_database = new_database.merge(
            discourse_data, how="left", left_on="user_id", right_on="user_id"
        )

        new_database.fillna(value=0,inplace=True)
        #### drop unwanted columns
        new_database.drop(["team_member_id", "user_id"], axis=1, inplace=True)

        #### create copy to extract piazza data
        piazza_data = new_database

        #### get mean of data grouped by id
        new_database = new_database.groupby("team_id", as_index=False).mean()

        #### teams eligible for eyrc
        total_data = pd.read_sql(data_g, con=connection)

        #### merge data to get only eligible teams
        new_database = total_data.merge(new_database, on="team_id", how="right")

        #### fill NaN with 0
        new_database = new_database.fillna(0)

        #### group by team_id
        new_data = new_data.groupby("team_id", as_index=False)

        #### get login data

        #### get login data
        last_login_data = new_data.max()[["team_id", "last_login", "login_count"]]

        #### teams eligible for eyrc
        total_data = pd.read_sql(data_g, con=connection)

        #### create new instance of database
        new_fi_data = new_database

        #### Select parameters for PCA
        t2 = new_fi_data[
            [
                "rateMyPerformance",
                "rateMyLearning",
                "rateMyFocus",
                "rateStressLevel",
                "rateWork",
            ]
        ]
        t3 = new_fi_data[
            ["rateTask4", "rateTask4Design", "rateSelfContribution", "rateResource"]
        ]
        t4 = new_fi_data[
            [
                "ratetheme",
                "rateProblemStatement",
                "rateKnowledgeOfPreviousTask",
                "rateInstructorResponse",
                "rateStudentResponse",
            ]
        ]
        t5 = new_fi_data[
            ["answers", "edits to answers", "followups", "reply to followups"]
        ]

        #### Apply PCA to the values
        t2 = scaler.fit(t2).transform(t2)
        t3 = scaler.fit(t3).transform(t3)
        t4 = scaler.fit(t4).transform(t4)
        t5 = scaler.fit(t5).transform(t5)
        t2 = pca.fit(t2).transform(t2)
        t3 = pca.fit(t3).transform(t3)
        t4 = pca.fit(t4).transform(t4)
        t5 = pca.fit(t5).transform(t5)

        #### drop unwanted column
        new_fi_data.drop(
            [
                "rateMyPerformance",
                "rateMyLearning",
                "rateMyFocus",
                "rateStressLevel",
                "rateWork",
                "rateTask4",
                "rateTask4Design",
                "rateSelfContribution",
                "rateResource",
                "ratetheme",
                "rateProblemStatement",
                "rateKnowledgeOfPreviousTask",
                "rateInstructorResponse",
                "rateStudentResponse",
                "answers",
                "edits to answers",
                "followups",
                "reply to followups",
            ],
            axis=1,
            inplace=True,
        )

        #### Adding PCA columns
        new_fi_data["pca_1_1"] = t2[:, 0]
        new_fi_data["pca_2_1"] = t3[:, 0]
        new_fi_data["pca_3_1"] = t4[:, 0]
        new_fi_data["pca_4_1"] = t5[:, 0]

        #### set threshold value
        thresh = 0.77

        #### get list of parameters
        parameters = task_5
    elif id == 6:
        scaler = StandardScaler()
        pca = PCA()

        #### get the model based on task
        log = pickle.load(open("./models/pred_t6.sav", "rb"))

        #### get data from database
        new_data = pd.read_sql(quer_t6, con=connection)

        #### get details for email and phone No. column
        details = new_data[["team_id", "team_member_id", "email", "phone_no"]]

        #### for merging piazza data with database when using api
        # new_data = new_data.merge(result1,how='left', left_on='email', right_on='email')

        #### droping unwanted columns
        new_data.drop(["email", "phone_no"], axis=1, inplace=True)

        new_data["teamOrindividual"] = new_data["teamOrindividual"].apply(team_ind)

        new_data = new_data.merge(
            login_data, how="left", left_on="team_member_id", right_on="team_member_id"
        )

        new_database = new_data.merge(
            mapping_file,
            how="left",
            left_on="team_member_id",
            right_on="team_member_id",
        )

        new_database = new_database.merge(
            discourse_data, how="left", left_on="user_id", right_on="user_id"
        )

        new_database.fillna(value=0,inplace=True)

        #### drop unwanted columns
        new_database.drop(["team_member_id", "user_id"], axis=1, inplace=True)

        #### create copy to extract piazza data
        piazza_data = new_database

        #### get mean of data grouped by id
        new_database = new_database.groupby("team_id", as_index=False).mean()

        #### teams eligible for eyrc
        total_data = pd.read_sql(data_g, con=connection)

        #### merge data to get only eligible teams
        new_database = total_data.merge(new_database, on="team_id", how="right")

        #### fill NaN with 0
        new_database = new_database.fillna(0)

        #### group by team_id
        new_data = new_data.groupby("team_id", as_index=False)

        #### get login data
        last_login_data = new_data.max()[["team_id", "last_login", "login_count"]]

        #### teams eligible for eyrc
        total_data = pd.read_sql(data_g, con=connection)

        #### create new instance of database
        new_fi_data = new_database

        #### Select parameters for PCA
        t2 = new_fi_data[
            [
                "rateMyPerformance",
                "rateMyLearning",
                "rateMyFocus",
                "rateStressLevel",
                "rateWork",
            ]
        ]
        t3 = new_fi_data[
            ["rateTask5", "rateTask5Design", "rateSelfContribution", "rateResource"]
        ]
        t4 = new_fi_data[
            [
                "ratetheme",
                "rateProblemStatement",
                "rateKnowledgeOfPreviousTask",
                "rateInstructorResponse",
                "rateStudentResponse",
            ]
        ]
        t5 = new_fi_data[
            [
                "posts",
                "answers",
                "edits to answers",
                "followups",
                "reply to followups",
            ]
        ]

        #### Apply PCA to the values
        t2 = scaler.fit(t2).transform(t2)
        t3 = scaler.fit(t3).transform(t3)
        t4 = scaler.fit(t4).transform(t4)
        t5 = scaler.fit(t5).transform(t5)
        t2 = pca.fit(t2).transform(t2)
        t3 = pca.fit(t3).transform(t3)
        t4 = pca.fit(t4).transform(t4)
        t5 = pca.fit(t5).transform(t5)

        #### drop unwanted column
        new_fi_data.drop(
            [
                "rateMyPerformance",
                "rateMyLearning",
                "rateMyFocus",
                "rateStressLevel",
                "rateWork",
                "rateTask5",
                "rateTask5Design",
                "rateSelfContribution",
                "rateResource",
                "ratetheme",
                "rateProblemStatement",
                "rateKnowledgeOfPreviousTask",
                "rateInstructorResponse",
                "rateStudentResponse",
                "posts",
                "answers",
                "edits to answers",
                "followups",
                "reply to followups",
            ],
            axis=1,
            inplace=True,
        )

        #### Adding PCA columns
        new_fi_data["pca_1_1"] = t2[:, 0]
        new_fi_data["pca_2_1"] = t3[:, 0]
        new_fi_data["pca_3_1"] = t4[:, 0]
        new_fi_data["pca_4_1"] = t5[:, 0]

        #### set threshold value
        thresh = 0.79

        #### get list of parameters
        parameters = task_6

    #### create team data dataframe
    team_data = new_fi_data[["team_id", "theme"]]

    #### drop unwanted columns
    new_fi_data.drop(["team_id", "theme"], axis=1, inplace=True)

    #### list of all the teams in the task
    teams = list(details["team_id"].unique())
    d = {}
    #### max no of team members
    team_mem = 4

    #### loop to get all team members data
    for i in teams:
        j = details[details["team_id"] == i].shape[0]
        k = details[details["team_id"] == i]["email"].reset_index()
        l = details[details["team_id"] == i]["phone_no"].reset_index()
        lst = []
        lst1 = []
        lst3 = []
        for w in range(j):
            lst.append(k["email"].loc[w])
            lst1.append(l["phone_no"].loc[w])
        if j < team_mem:
            rem = team_mem - j
            lst.extend([0] * rem)
            lst1.extend([0] * rem)

        lst3.append(lst)
        lst3.append(lst1)
        d[i] = lst3
    s = pd.DataFrame.from_dict(d)
    s.fillna(value=0,inplace=True)
    s.to_csv(
        "./contact_info_csv_files/task_{}_contact.csv".format(id),
        encoding="utf-8",
        index=False,
    )
    m = s.to_json()

    #### get important piazza data
    piazza_data = piazza_data.groupby("team_id", as_index=False).max()[
        ["team_id", "days online", "posts", "answers"]
    ]

    #### feed data in model and get predicted confidence
    conf = log.predict_proba(new_fi_data)[:, 1]

    #### create dataframe of confidence
    confidence = pd.DataFrame(conf, columns=["confidence"])

    # details_new = details.groupby("team_id")["team_member_id"].min()
    # details = details.merge(details_new,on="team_member_id",how="right")

    #### merge necessary data to team data datatable
    team_data["confidence"] = confidence
    team_data = team_data.merge(
        last_login_data, how="left", left_on="team_id", right_on="team_id"
    )
    team_data = team_data.merge(
        piazza_data, how="left", left_on="team_id", right_on="team_id"
    )
    team_data["time_stamp"] = datetime.datetime.now()
    #### Convert all data to JSON
    team_data.to_csv(
        "./pred_csv_files/task_{}_pred.csv".format(id), encoding="utf-8", index=False
    )
    print("Writing CSV files")
    parameters = dumps(parameters)
    js = team_data.to_json()

    # new_database = new_data.merge(
    #         result1, how="left", left_on="team_member_id", right_on="team_member_id"
    #     )
    # j = json.loads(js)
    # j = dumps(j)
    ############################# RENDER JSON DATA from here ################################
    return JsonResponse(
        {
            "json_data": js,
            "parameters": parameters,
            "thresh": thresh,
            "details": m,
            "this_task": this_task,
        }
    )


############################# NEW VIEW FOR AJAX - END ################################


def feedbackData(request, id):
    #### choose query based on task
    if id == 0:
        # data_g=task0_feed
        data_g_box = task0_feed_box
        legend = task0_feed_box_legend
    elif id == 1:
        # data_g=task1_feed
        data_g_box = task1_feed_box
        legend = task1_feed_box_legend
    elif id == 2:
        # data_g=task2_feed
        data_g_box = task2_feed_box
        legend = task2_feed_box_legend
    elif id == 3:
        # data_g=task3_feed
        data_g_box = task3_feed_box
        legend = task3_feed_box_legend
    elif id == 4:
        # data_g=task4_feed
        data_g_box = task4_feed_box
        legend = task4_feed_box_legend
    elif id == 5:
        # data_g=task5_feed
        data_g_box = task5_feed_box
        legend = task5_feed_box_legend
    elif id == 6:
        data_g_box = stage1_feed_box_1
        legend = stage1_feed_box_1_legend
    elif id == 7:
        data_g_box = stage1_feed_box_2
        legend = stage1_feed_box_2_legend
    elif id == 8:
        data_g_box = stage1_feed_box_3
        legend = stage1_feed_box_3_legend
    elif id == 9:
        data_g_box = stage1_feed_box_4
        legend = stage1_feed_box_4_legend

    # total_data = pd.read_sql(data_g, con=connection)
    # js = total_data.to_json()

    #### get data from database
    total_data_box = pd.read_sql(data_g_box, con=connection)
    total_data_box.drop("taskName", axis=1, inplace=True)

    #### Find min,q1,median,q3 and max
    x = total_data_box.groupby("theme").quantile([0, 0.25, 0.5, 0.75, 1])
    x2 = x.to_json()
    # quest_list = list(json.loads(js).keys())
    # print(quest_list)

    return JsonResponse({"box_chart_data": x2, "legend": legend})
    # return JsonResponse({"chart_data": js,"quest_list":quest_list,"box_chart_data":x2})


def feedbackTrack(request, id):
    #### get queries to be executed based on id
    if id == 0:
        data_g_box = [task0_feed_box]
    elif id == 1:
        data_g_box = [task1_feed_box, task0_feed_box]
    elif id == 2:
        data_g_box = [task2_feed_box, task1_feed_box, task0_feed_box]
    elif id == 3:
        data_g_box = [task3_feed_box, task2_feed_box, task1_feed_box, task0_feed_box]
    elif id == 4:
        data_g_box = [
            task4_feed_box,
            task3_feed_box,
            task2_feed_box,
            task1_feed_box,
            task0_feed_box,
        ]
    elif id == 5:
        data_g_box = [
            task5_feed_box,
            task4_feed_box,
            task3_feed_box,
            task2_feed_box,
            task1_feed_box,
            task0_feed_box,
        ]

    # total_data_box=pd.read_sql(data_g_box,con=connection)
    frames = []
    #### use for loop to fetch data from database and concat
    for query in data_g_box:
        holder = pd.read_sql(query, con=connection)
        frames.append(holder)
    total_data_box = pd.concat(frames)

    #### Find min,q1,median,q3 and max
    x = total_data_box.groupby(["theme", "taskName"]).quantile([0, 0.25, 0.5, 0.75, 1])

    #### convert to json
    x2 = x.to_json()

    #### return the data
    return JsonResponse({"all_feedback_data": x2})


def get_teams_seen(request, topic_id):
    discourse_mapping = pd.read_csv("./piazza_stats/mapping.csv")
    seen_url = "https://discuss.e-yantra.org/admin/plugins/explorer/queries/9/run"
    resp = requests.post(seen_url, headers=headers, data=files)
    discourse_topics = pd.DataFrame(resp.json()["rows"], columns=resp.json()["columns"])
    # print("\n\n###########\nDiscourse Topics: ", discourse_topics)
    discourse_topics.rename(columns={"user_id": "discourse_id"}, inplace=True)
    # print("\n\n###########\nDiscourse Topics: ", discourse_topics)
    # seen_url = "https://discuss.e-yantra.org/admin/plugins/explorer/queries/10/run"
    # resp = requests.post(seen_url, headers=headers, data=files)
    # all_cat_topics = pd.DataFrame(resp.json()["rows"], columns=resp.json()["columns"])

    # query = "select distinct user_id as discourse_id,topic_id from topic_views where topic_id in (SELECT topics.id from topics,categories,users where topics.category_id=categories.id  AND topics.user_id=users.id AND users.moderator is true);"
    query2 = "SELECT team_member_detail.team_id,team_member_detail.name,team_member_detail.email,team_member_detail.contact from team_member_detail;"
    data2 = pd.read_sql(query2, con=connection)
    data2.fillna(value=0, inplace=True)
    data2 = data2.drop_duplicates(subset="team_id", keep="first")
    # discourse_topics = pd.read_sql(query, con=connections["discourse"])

    discourse_topics = discourse_topics[discourse_topics["topic_id"] == topic_id]
    new_database = discourse_mapping.merge(
        discourse_topics, how="left", left_on="discourse_id", right_on="discourse_id"
    )
    # print("\n\n#######\nNew Database: ", new_database)
    new_database = new_database[new_database["discourse_id"].notna()]
    all_teams = new_database.groupby(["team_id"]).max().reset_index()
    seen_teams = (
        new_database[new_database["topic_id"].notna()]
        .groupby(["team_id"])
        .max()
        .reset_index()
    )
    unseen_teams = all_teams[~all_teams.team_id.isin(seen_teams.team_id)]

    seen_teams = seen_teams.merge(
        data2, how="left", left_on="team_id", right_on="team_id"
    )
    unseen_teams = unseen_teams.merge(
        data2, how="left", left_on="team_id", right_on="team_id"
    )

    st = seen_teams.to_json()
    ust = unseen_teams.to_json()

    return JsonResponse({"seen_teams": st, "unseen_teams": ust})
