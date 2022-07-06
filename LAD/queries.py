quer_t0 = """SELECT team_member_detail.id AS team_member_id,team_grades.team_id,login.last_login,
team_grades.theme,

team_member_detail.contact as phone_no,
team_member_detail.email,
team_member_detail.elsiLab,
team_member_detail.year,
team_member_detail.otherComp,
team_member_detail.sub_ros,
team_member_detail.sub_ip,
team_member_detail.sub_emb_c,
team_member_detail.sub_ml,
team_member_detail.sub_ap,
team_member_detail.sub_cs,
team_member_detail.sub_mss,
team_member_detail.sub_fpga,
team_member_detail.sub_mm,
team_member_detail.sub_de

FROM team_member_detail,team_grades,login
WHERE team_member_detail.team_id = team_grades.team_id
AND team_member_detail.id = login.team_member_id
AND team_grades.team_id=login.team_id
AND team_member_detail.team_id IN (SELECT team_details.id FROM team_details WHERE team_details.eyrc=1)
-- and team_member_detail.team_id<2670
-- and team_member_detail.team_id>10
AND team_member_detail.team_id NOT IN (SELECT task0_status.team_id FROM task0_status);
"""
# AND team_member_detail.team_id NOT IN (SELECT team_grades.team_id FROM team_grades WHERE team_grades.task0_graded=1);

quer_t1 = """
SELECT  tf3.team_id, tf3.theme,login.last_login,tf3.team_member_id,
(tmd.email) as email,
(tmd.contact) as phone_no,

case 
when tf3.task0Simplicity ="Strongly Agree" then 10
when tf3.task0Simplicity ="Agree" then 8
when tf3.task0Simplicity ="Nuetral" or  tf3.task0Simplicity ="Neutral" then 6
when tf3.task0Simplicity ="Disagree" then 4
when tf3.task0Simplicity ="Strongly Disagree" then 2
END as rateTask,

case 
when tf3.forumUseful ="Strongly Agree" then 10
when tf3.forumUseful ="Agree" then 8
when tf3.forumUseful ="Neutral" or tf3.forumUseful="Nuetral" then 6
when tf3.forumUseful ="Disagree" then 4
when tf3.forumUseful ="Strongly Disagree" then 2
END AS rateUsefulness,

case 
when tf3.task0ResourceHelpful="Strongly Agree" then 10
when tf3.task0ResourceHelpful ="Agree" then 8
when tf3.task0ResourceHelpful ="Nuetral" or tf3.task0ResourceHelpful="Neutral" then 6
when tf3.task0ResourceHelpful ="Disagree" then 4
when tf3.task0ResourceHelpful ="Strongly Disagree" then 2
END as rateResource,

case 
when tf3.rateSelfKnowledgeBefore_1 ="Very High" then 10
when tf3.rateSelfKnowledgeBefore_1 ="High" then 8
when tf3.rateSelfKnowledgeBefore_1 ="Neutral" or tf3.rateSelfKnowledgeBefore_1="Nuetral" then 6
when tf3.rateSelfKnowledgeBefore_1 ="Low" then 4
when tf3.rateSelfKnowledgeBefore_1 ="Very Low" then 2
when tf3.rateSelfKnowledgeBefore_1 ="N/A" then 0
END AS rateSelfKnowledgeBefore,
case 
when tf3.rateSelfKnowledgeAfter_1 ="Very High" then 10
when tf3.rateSelfKnowledgeAfter_1 ="High" then 8
when tf3.rateSelfKnowledgeAfter_1 ="Neutral" or tf3.rateSelfKnowledgeAfter_1="Nuetral" then 6
when tf3.rateSelfKnowledgeAfter_1 ="Low" then 4
when tf3.rateSelfKnowledgeAfter_1 ="Very Low" then 2
when tf3.rateSelfKnowledgeAfter_1 ="N/A" then 0
END AS rateSelfKnowledgeAfter,
tg.task0_marks,
tg.task0_penalty

FROM task0_feedback tf3, team_grades tg,login,team_member_detail tmd 
WHERE tg.team_id = tf3.team_id
AND tf3.team_member_id=login.team_member_id
AND tmd.id = login.team_member_id
-- and tf3.team_id<2670
-- and tf3.team_id>10
AND tf3.team_id NOT IN (SELECT task1_status.team_id FROM task1_status);
"""
# AND tg.team_id NOT IN (SELECT task1_status.team_id FROM task1_status GROUP BY task1_status.team_id)

quer_t2 = """SELECT  tf3.team_id, tf3.theme,lg.last_login,tf3.team_member_id,
(tf3.rateTask1) AS rateTask1,
(tmd.email) as email,
(tmd.contact) as phone_no,
(tf3.rateTask1Design) AS rateTask1Design,
(tf3.rateSelfContribution) AS rateSelfContribution,
(tf3.rateResource) AS rateResource,
((tf3.rateDifficulty_1+tf3.rateDifficulty_2+tf3.rateDifficulty_3)/3) AS rateDifficulty,
(tf3.rateLiveSessionUsefulness) AS rateLiveSessionUsefulness,
tg.task0_marks,
tg.task0_penalty,
(tg.task1a_marks+tg.task1b_marks+tg.task1c_marks) AS task1_marks,
(tg.task1a_penalty+tg.task1b_penalty+tg.task1c_penalty) AS task1_penalty
FROM task1_feedback tf3, team_grades tg ,login lg,team_member_detail tmd 
WHERE tg.team_id = tf3.team_id
AND tf3.team_id = lg.team_id
AND tmd.id = lg.team_member_id
AND tf3.team_member_id = lg.team_member_id
-- and tf3.team_id<2670
-- and tf3.team_id>10
AND team_member_detail.team_id NOT IN (SELECT task2_status.team_id FROM task2_status);
"""
# AND tg.team_id NOT IN (SELECT task2_status.team_id FROM task2_status GROUP BY task2_status.team_id)

quer_t3 = """
SELECT  s1.team_id,s1.theme,login.last_login,s1.team_member_id,
(tmd.email) as email,
(tmd.contact) as phone_no,
(s1.rateTheme) AS ratetheme,
(s1.rateProblemStatement) AS rateProblemStatement,
(s1.rateKnowledgeOfPreviousTask) AS rateKnowledgeOfPreviousTask,

(s1.rateInstructorResponse) AS rateInstructorResponse,
(s1.rateStudentResponse) AS rateStudentResponse,
((s1.rateCollaborativeSkillsAfter-s1.rateCollaborativeSkillsBefore)+(s1.ratePeerLearningAfter-s1.ratePeerLearningBefore)+s1.rateHandsOnSkillsAfter-s1.rateHandsOnSkillsBefore) AS rateSkills,
(s1.rateThemeDesign) AS rateThemeDesign,
(s1.rateMyPerformance) AS rateMyPerformance,
(s1.rateMyLearning) AS rateMyLearning,
(s1.rateMyFocus) AS rateMyFocus,
(s1.rateSressLevel) AS rateSressLevel,
(s1.rateWorkManagement) AS rateWorkManagement,
(s1.rateWorkOnEyrc-(s1.workOnAcademics+s1.workOnTimePass)) AS rateWork,
s1.covidCase,
(tf3.rateTask2) AS rateTask2,
(tf3.rateTask2Design) AS rateTask2Design,
(tf3.rateSelfContribution) AS rateSelfContribution,
(tf3.rateResource) AS rateResource,
((tf3.rateDifficulty_1+tf3.rateDifficulty_2+tf3.rateDifficulty_3)/3) AS rateDifficulty,
(tf3.rateLiveSessionUsefulness) AS rateLiveSessionUsefulness,
tg.task0_marks,
tg.task0_penalty,
(tg.task1a_marks+tg.task1b_marks+tg.task1c_marks) AS task1_marks,
(tg.task1a_penalty+tg.task1b_penalty+tg.task1c_penalty) AS task1_penalty,
(tg.task2a_marks+tg.task2b_marks) AS task2_marks,
(tg.task2a_penalty+tg.task2b_penalty) AS task2_penalty
FROM stage1_feedback s1, task2_feedback tf3, team_grades tg,login,team_member_detail tmd  
WHERE s1.team_member_id = tf3.team_member_id 
AND s1.team_id=tf3.team_id
AND tg.team_id = s1.team_id
AND tmd.id = login.team_member_id
AND tf3.team_member_id=login.team_member_id
AND s1.theme!="SM"
-- and tf3.team_id<2670
-- and tf3.team_id>10
AND team_member_detail.team_id NOT IN (SELECT task3_status.team_id FROM task3_status)

UNION

SELECT  s1.team_id,s1.theme,login.last_login,s1.team_member_id,
(tmd.email) as email,
(tmd.contact) as phone_no,
(s1.rateTheme) AS ratetheme,
(s1.rateProblemStatement) AS rateProblemStatement,
(s1.rateKnowledgeOfPreviousTask) AS rateKnowledgeOfPreviousTask,
(s1.rateInstructorResponse) AS rateInstructorResponse,
(s1.rateStudentResponse) AS rateStudentResponse,
((s1.rateCollaborativeSkillsAfter-s1.rateCollaborativeSkillsBefore)+(s1.ratePeerLearningAfter-s1.ratePeerLearningBefore)+s1.rateHandsOnSkillsAfter-s1.rateHandsOnSkillsBefore) AS rateSkills,
(s1.rateThemeDesign) AS rateThemeDesign,
(s1.rateMyPerformance) AS rateMyPerformance,
(s1.rateMyLearning) AS rateMyLearning,
(s1.rateMyFocus) AS rateMyFocus,
(s1.rateSressLevel) AS rateSressLevel,
(s1.rateWorkManagement) AS rateWorkManagement,
(s1.rateWorkOnEyrc-(s1.workOnAcademics+s1.workOnTimePass)) AS rateWork,
s1.covidCase,
(tf3.rateTask2) AS rateTask2,
(tf3.rateTask2Design) AS rateTask2Design,
(tf3.rateSelfContribution) AS rateSelfContribution,
(tf3.rateResource) AS rateResource,
((tf3.rateDifficulty_1+tf3.rateDifficulty_2+tf3.rateDifficulty_3)/3) AS rateDifficulty,
(tf3.rateLiveSessionUsefulness) AS rateLiveSessionUsefulness,
tg.task0_marks,
tg.task0_penalty,
(tg.task1a_marks+tg.task1b_marks+tg.task1c_marks) AS task1_marks,
(tg.task1a_penalty+tg.task1b_penalty+tg.task1c_penalty) AS task1_penalty,
(tg.task2a_marks+tg.task2b_marks) AS task2_marks,
(tg.task2a_penalty+tg.task2b_penalty) AS task2_penalty
FROM stage1_feedback s1, task2_feedback tf3, team_grades tg,login ,team_member_detail tmd 
WHERE s1.team_member_id = tf3.team_member_id 
AND s1.team_id=tf3.team_id
AND tg.team_id = s1.team_id
AND tf3.team_member_id=login.team_member_id
AND tmd.id = login.team_member_id
-- and tf3.team_id<2670
-- and tf3.team_id>10
AND s1.team_id IN (SELECT team_details.id FROM team_details WHERE team_details.stg2=1)
AND team_member_detail.team_id NOT IN (SELECT task3_status.team_id FROM task3_status);
"""
# AND s1.team_id NOT IN (SELECT task3_status.team_id FROM task3_status GROUP BY task3_status.team_id)
# AND s1.team_id NOT IN (SELECT task3_status.team_id FROM task3_status GROUP BY task3_status.team_id)


quer_t4 = """
SELECT  s1.team_id,s1.theme,login.last_login,s1.team_member_id,
(tmd.email) as email,
(tmd.contact) as phone_no,
(s1.rateTheme) AS ratetheme,
(s1.rateProblemStatement) AS rateProblemStatement,
(s1.rateKnowledgeOfPreviousTask) AS rateKnowledgeOfPreviousTask,
(s1.rateInstructorResponse) AS rateInstructorResponse,
(s1.rateStudentResponse) AS rateStudentResponse,
((s1.rateCollaborativeSkillsAfter-s1.rateCollaborativeSkillsBefore)+(s1.ratePeerLearningAfter-s1.ratePeerLearningBefore)+s1.rateHandsOnSkillsAfter-s1.rateHandsOnSkillsBefore) AS rateSkills,
(s1.rateThemeDesign) AS rateThemeDesign,
(s1.rateMyPerformance) AS rateMyPerformance,
(s1.rateMyLearning) AS rateMyLearning,
(s1.rateMyFocus) AS rateMyFocus,
(s1.rateSressLevel) AS rateSressLevel,
(s1.rateWorkManagement) AS rateWorkManagement,
(s1.rateWorkOnEyrc-(s1.workOnAcademics+s1.workOnTimePass)) AS rateWork,
s1.teamOrindividual,
(tf3.rateTask3) AS rateTask,
(tf3.rateTask3Design) AS rateTaskDesign,
(tf3.rateSelfContribution) AS rateSelfContribution,
(tf3.rateResource) AS rateResource,
((tf3.rateDifficulty_1+tf3.rateDifficulty_2+tf3.rateDifficulty_3)/3) AS rateDifficulty,
(tf3.rateLiveSessionUsefulness) AS rateLiveSessionUsefulness,
(tg.task1a_marks+tg.task1b_marks+tg.task1c_marks) AS task1_marks,
(tg.task1a_penalty+tg.task1b_penalty+tg.task1c_penalty) AS task1_penalty,
(tg.task2a_marks+tg.task2b_marks) AS task2_marks,
(tg.task2a_penalty+tg.task2b_penalty) AS task2_penalty,
tg.task3_marks,
tg.task3_penalty
FROM stage1_feedback s1, task3_feedback tf3, team_grades tg,login ,team_member_detail tmd 
WHERE s1.team_member_id = tf3.team_member_id 
AND s1.team_id=tf3.team_id
AND tg.team_id = s1.team_id
AND tmd.id = login.team_member_id
-- and tf3.team_id<2670
-- and tf3.team_id>10
AND tf3.team_member_id=login.team_member_id
AND s1.theme!="SM"
AND team_member_detail.team_id NOT IN (SELECT task4_status.team_id FROM task4_status);

UNION

SELECT  s1.team_id,s1.theme,login.last_login,s1.team_member_id,
(tmd.email) as email,
(tmd.contact) as phone_no,
(s1.rateTheme) AS ratetheme,
(s1.rateProblemStatement) AS rateProblemStatement,
(s1.rateKnowledgeOfPreviousTask) AS rateKnowledgeOfPreviousTask,
(s1.rateInstructorResponse) AS rateInstructorResponse,
(s1.rateStudentResponse) AS rateStudentResponse,

((s1.rateCollaborativeSkillsAfter-s1.rateCollaborativeSkillsBefore)+(s1.ratePeerLearningAfter-s1.ratePeerLearningBefore)+s1.rateHandsOnSkillsAfter-s1.rateHandsOnSkillsBefore) AS rateSkills,
(s1.rateThemeDesign) AS rateThemeDesign,
(s1.rateMyPerformance) AS rateMyPerformance,
(s1.rateMyLearning) AS rateMyLearning,
(s1.rateMyFocus) AS rateMyFocus,
(s1.rateSressLevel) AS rateSressLevel,
(s1.rateWorkManagement) AS rateWorkManagement,
(s1.rateWorkOnEyrc-(s1.workOnAcademics+s1.workOnTimePass)) AS rateWork,

s1.teamOrindividual,
(tf3.rateTask2) AS rateTask,
(tf3.rateTask2Design) AS rateTaskDesign,
(tf3.rateSelfContribution) AS rateSelfContribution,
(tf3.rateResource) AS rateResource,
((tf3.rateDifficulty_1+tf3.rateDifficulty_2+tf3.rateDifficulty_3)/3) AS rateDifficulty,
(tf3.rateLiveSessionUsefulness) AS rateLiveSessionUsefulness,
(tg.task1a_marks+tg.task1b_marks+tg.task1c_marks) AS task1_marks,
(tg.task1a_penalty+tg.task1b_penalty+tg.task1c_penalty) AS task1_penalty,
(tg.task2a_marks+tg.task2b_marks) AS task2_marks,
(tg.task2a_penalty+tg.task2b_penalty) AS task2_penalty,
tg.task3_marks,
tg.task3_penalty
FROM stage1_feedback s1, task2_feedback tf3, team_grades tg,login ,team_member_detail tmd 
WHERE s1.team_member_id = tf3.team_member_id 
AND s1.team_id=tf3.team_id
AND tg.team_id = s1.team_id
-- and tf3.team_id<2670
-- and tf3.team_id>10
AND tf3.team_member_id=login.team_member_id
AND tmd.id = login.team_member_id
AND s1.team_id IN (SELECT team_details.id FROM team_details WHERE team_details.stg2=1)
AND team_member_detail.team_id NOT IN (SELECT task4_status.team_id FROM task4_status);
"""
# AND s1.team_id NOT IN (SELECT task4_status.team_id FROM task4_status GROUP BY task4_status.team_id)
# AND s1.team_id NOT IN (SELECT task4_status.team_id FROM task4_status GROUP BY task4_status.team_id)

quer_t5 = """
SELECT  s1.team_id,s1.theme,login.last_login,s1.team_member_id,
(tmd.email) as email,
(tmd.contact) as phone_no,
(s1.rateTheme) AS ratetheme,
(s1.rateProblemStatement) AS rateProblemStatement,
(s1.rateKnowledgeOfPreviousTask) AS rateKnowledgeOfPreviousTask,
(s1.rateInstructorResponse) AS rateInstructorResponse,
(s1.rateStudentResponse) AS rateStudentResponse,
(s1.rateThemeDesign) AS rateThemeDesign,
(s1.rateMyPerformance) AS rateMyPerformance,
(s1.rateMyLearning) AS rateMyLearning,
(s1.rateMyFocus) AS rateMyFocus,
(s1.rateSressLevel) AS rateStressLevel,
(s1.rateWorkOnEyrc-(s1.workOnAcademics+s1.workOnTimePass)) AS rateWork,
(tf3.rateTask4) AS rateTask4,
(tf3.rateTask4Design) AS rateTask4Design,
(tf3.rateSelfContribution) AS rateSelfContribution,
(tf3.rateResource) AS rateResource,
(tf3.rateLiveSessionUsefulness) AS rateLiveSessionUsefulness,
(tg.task1a_marks+tg.task1b_marks+tg.task1c_marks) AS task1_marks,
(tg.task1a_penalty+tg.task1b_penalty+tg.task1c_penalty) AS task1_penalty,
(tg.task2a_marks+tg.task2b_marks) AS task2_marks,
(tg.task2a_penalty+tg.task2b_penalty) AS task2_penalty,
tg.task3_marks,
tg.task3_penalty,
(tg.task4a_marks+tg.task4b_marks+tg.task4c_marks) AS task4_marks,
(tg.task4a_penalty+tg.task4b_penalty+tg.task4c_penalty) AS task4_penalty

FROM stage1_feedback s1, task4_feedback tf3, team_grades tg,login ,team_member_detail tmd 
WHERE s1.team_member_id = tf3.team_member_id 
AND s1.team_id=tf3.team_id
AND tf3.team_member_id=login.team_member_id
AND tmd.id = login.team_member_id
AND tg.team_id = s1.team_id
-- and tf3.team_id<2670
-- and tf3.team_id>10
AND team_member_detail.team_id NOT IN (SELECT task5_status.team_id FROM task5_status);
"""
# AND s1.team_id NOT IN (SELECT task5_status.team_id FROM task5_status GROUP BY task5_status.team_id)

quer_t6 = """
SELECT  s1.team_id,s1.theme,login.last_login,s1.team_member_id,
(tmd.email) as email,
(tmd.contact) as phone_no,
(s1.rateTheme) AS ratetheme,
(s1.rateProblemStatement) AS rateProblemStatement,
(s1.rateKnowledgeOfPreviousTask) AS rateKnowledgeOfPreviousTask,
(s1.rateInstructorResponse) AS rateInstructorResponse,
(s1.rateStudentResponse) AS rateStudentResponse,
((s1.rateCollaborativeSkillsAfter-s1.rateCollaborativeSkillsBefore)+(s1.ratePeerLearningAfter-s1.ratePeerLearningBefore)+s1.rateHandsOnSkillsAfter-s1.rateHandsOnSkillsBefore) AS rateSkills,
(s1.rateThemeDesign) AS rateThemeDesign,
(s1.rateMyPerformance) AS rateMyPerformance,
(s1.rateMyLearning) AS rateMyLearning,
(s1.rateMyFocus) AS rateMyFocus,
(s1.rateSressLevel) AS rateStressLevel,
(s1.rateWorkManagement) AS rateWorkManagement,
(s1.rateWorkOnEyrc-(s1.workOnAcademics+s1.workOnTimePass)) AS rateWork,
s1.teamOrindividual,
(tf3.rateTask5) AS rateTask5,
(tf3.rateTask5Design) AS rateTask5Design,
(tf3.rateSelfContribution) AS rateSelfContribution,
(tf3.rateResource) AS rateResource,
((tf3.rateDifficulty_1+tf3.rateDifficulty_2+tf3.rateDifficulty_3)/3) AS rateDifficulty,
(tf3.rateLiveSessionUsefulness) AS rateLiveSessionUsefulness,
(tg.task2a_marks+tg.task2b_marks) AS task2_marks,
(tg.task2a_penalty+tg.task2b_penalty) AS task2_penalty,
tg.task3_marks,
tg.task3_penalty,
(tg.task4a_marks+tg.task4b_marks+tg.task4c_marks) AS task4_marks,
(tg.task4a_penalty+tg.task4b_penalty+tg.task4c_penalty) AS task4_penalty,
tg.task5_marks,
tg.task5_penalty
FROM stage1_feedback s1, task5_feedback tf3, team_grades tg,login ,team_member_detail tmd 
WHERE s1.team_member_id = tf3.team_member_id 
AND s1.team_id=tf3.team_id
AND tg.team_id = s1.team_id
AND tf3.team_member_id=login.team_member_id
AND tmd.id = login.team_member_id
-- and tf3.team_id<2670
-- and tf3.team_id>10
AND team_member_detail.team_id NOT IN (SELECT task6_status.team_id FROM task6_status);
"""
# AND s1.team_id NOT IN (SELECT task6_status.team_id FROM task6_status GROUP BY task6_status.team_id)


def team_ind(x):
    if x == 'team':
        x = 1
    else:
        x = 0
    return x


def yes_no(x):
    if x == "yes":
        x = 1
    else:
        x = 0
    return x


data_g = """SELECT id as team_id,theme FROM `team_details` where eyrc=1"""
