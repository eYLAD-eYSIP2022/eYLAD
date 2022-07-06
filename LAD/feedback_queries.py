# task0_feed_box = """
#                 SELECT  (tf0.team_id) AS Entries,"Task 0" AS taskName, tf0.theme,
#                 (tf0.rateTask) AS rateTask,
#                 (tf0.rateUsefulness) AS rateUsefulness,
#                 (tf0.rateResource) AS rateResource,
#                 (tf0.rateEffectiveness) AS rateEffectiveness
#                 FROM task0_feedback tf0

# """

task0_feed_box = """
SELECT (team_id) AS Entries,"Task 0" AS taskName, theme,
case 
when themeEnjoy ="Strongly Agree" then 5
when themeEnjoy ="Agree" then 4
when themeEnjoy ="Nuetral" or themeEnjoy ="Neutral" then 3
when themeEnjoy ="Disagree" then 2
when themeEnjoy ="Strongly Disagree" then 1
END as themeEnjoy,
case 
when task0Simplicity ="Strongly Agree" then 5
when task0Simplicity ="Agree" then 4
when task0Simplicity ="Nuetral" or  task0Simplicity ="Neutral" then 3
when task0Simplicity ="Disagree" then 2
when task0Simplicity ="Strongly Disagree" then 1
END as task0Simplicity,
case 
when task0ResourceHelpful="Strongly Agree" then 5
when task0ResourceHelpful ="Agree" then 4
when task0ResourceHelpful ="Nuetral" or task0ResourceHelpful="Neutral" then 3
when task0ResourceHelpful ="Disagree" then 2
when task0ResourceHelpful ="Strongly Disagree" then 1
END as task0ResourceHelpful,
case 
when task0Resource ="Strongly Agree" then 5
when task0Resource ="Agree" then 4
when task0Resource ="Neutral" or task0Resource="Nuetral" then 3
when task0Resource ="Disagree" then 2
when task0Resource ="Strongly Disagree" then 1
END AS task0Resource,
case 
when rateSelfKnowledgeBefore_1 ="Very High" then 5
when rateSelfKnowledgeBefore_1 ="High" then 4
when rateSelfKnowledgeBefore_1 ="Neutral" or rateSelfKnowledgeBefore_1="Nuetral" then 3
when rateSelfKnowledgeBefore_1 ="Low" then 2
when rateSelfKnowledgeBefore_1 ="Very Low" then 1
when rateSelfKnowledgeBefore_1 ="N/A" then 0
END AS rateSelfKnowledgeBefore,
case 
when rateSelfKnowledgeAfter_1 ="Very High" then 5
when rateSelfKnowledgeAfter_1 ="High" then 4
when rateSelfKnowledgeAfter_1 ="Neutral" or rateSelfKnowledgeAfter_1="Nuetral" then 3
when rateSelfKnowledgeAfter_1 ="Low" then 2
when rateSelfKnowledgeAfter_1 ="Very Low" then 1
when rateSelfKnowledgeAfter_1 ="N/A" then 0
END AS rateSelfKnowledgeAfter,
case 
when forumUseful ="Strongly Agree" then 5
when forumUseful ="Agree" then 4
when forumUseful ="Neutral" or forumUseful="Nuetral" then 3
when forumUseful ="Disagree" then 2
when forumUseful ="Strongly Disagree" then 1
END AS forumUsefulness

from task0_feedback              """
task0_feed_box_legend = None

task1_feed_box = """SELECT (tf1.team_id) AS Entries,"Task 1" AS taskName, tf1.theme,
                case 
                when tf1.taskEasiness ="Strongly Agree" then 5
                when tf1.taskEasiness ="Agree" then 4
                when tf1.taskEasiness ="Neutral" or tf1.taskEasiness="Nuetral" then 3
                when tf1.taskEasiness ="Disagree" then 2
                when tf1.taskEasiness ="Strongly Disagree" then 1
                END AS taskEasiness,
                
                case 
                when tf1.taskEasiness_b ="Strongly Agree" then 5
                when tf1.taskEasiness_b ="Agree" then 4
                when tf1.taskEasiness_b ="Neutral" or tf1.taskEasiness_b="Nuetral" then 3
                when tf1.taskEasiness_b ="Disagree" then 2
                when tf1.taskEasiness_b ="Strongly Disagree" then 1
                END AS taskEasiness_b,
                
                case 
                when tf1.taskEasiness_c ="Strongly Agree" then 5
                when tf1.taskEasiness_c ="Agree" then 4
                when tf1.taskEasiness_c ="Neutral" or tf1.taskEasiness_c="Nuetral" then 3
                when tf1.taskEasiness_c ="Disagree" then 2
                when tf1.taskEasiness_c ="Strongly Disagree" then 1
                END AS taskEasiness_c,
                
                case 
                when tf1.rateTaskDifficulty ="Very High" then 5
                when tf1.rateTaskDifficulty ="High" then 4
                when tf1.rateTaskDifficulty ="Neutral" or tf1.rateTaskDifficulty="Nuetral" then 3
                when tf1.rateTaskDifficulty ="Low" then 2
                when tf1.rateTaskDifficulty ="Very Low" then 1
                when tf1.rateTaskDifficulty ="N/A" then 0
                END AS rateTaskDifficulty,
                
                case 
                when tf1.sessionHelpfulness ="Strongly Agree" then 5
                when tf1.sessionHelpfulness ="Agree" then 4
                when tf1.sessionHelpfulness ="Neutral" or tf1.sessionHelpfulness="Nuetral" then 3
                when tf1.sessionHelpfulness ="Disagree" then 2
                when tf1.sessionHelpfulness ="Strongly Disagree" then 1
                END AS sessionHelpfulness,
                
                case 
                when tf1.rateSelfContribution ="Very High" then 5
                when tf1.rateSelfContribution ="High" then 4
                when tf1.rateSelfContribution ="Neutral" or tf1.rateSelfContribution="Nuetral" then 3
                when tf1.rateSelfContribution ="Low" then 2
                when tf1.rateSelfContribution ="Very Low" then 1
                when tf1.rateSelfContribution ="N/A" then 0
                END AS rateSelfContribution,
                
                case 
                when tf1.rateResources ="Strongly Agree" then 5
                when tf1.rateResources ="Agree" then 4
                when tf1.rateResources ="Neutral" or tf1.rateResources="Nuetral" then 3
                when tf1.rateResources ="Disagree" then 2
                when tf1.rateResources ="Strongly Disagree" then 1
                END AS rateResources,
                
                case 
                when tf1.rateForumUsefulness ="Strongly Agree" then 5
                when tf1.rateForumUsefulness ="Agree" then 4
                when tf1.rateForumUsefulness ="Neutral" or tf1.rateForumUsefulness="Nuetral" then 3
                when tf1.rateForumUsefulness ="Disagree" then 2
                when tf1.rateForumUsefulness ="Strongly Disagree" then 1
                END AS rateForumUsefulness,
                
                case 
                when tf1.rateSelfContributionSatisfaction ="Strongly Agree" then 5
                when tf1.rateSelfContributionSatisfaction ="Agree" then 4
                when tf1.rateSelfContributionSatisfaction ="Neutral" or tf1.rateSelfContributionSatisfaction="Nuetral" then 3
                when tf1.rateSelfContributionSatisfaction ="Disagree" then 2
                when tf1.rateSelfContributionSatisfaction ="Strongly Disagree" then 1
                END AS rateSelfContributionSatisfaction,
                
                case 
                when tf1.rateTeamContributionSatisfaction ="Strongly Agree" then 5
                when tf1.rateTeamContributionSatisfaction ="Agree" then 4
                when tf1.rateTeamContributionSatisfaction ="Neutral" or tf1.rateTeamContributionSatisfaction="Nuetral" then 3
                when tf1.rateTeamContributionSatisfaction ="Disagree" then 2
                when tf1.rateTeamContributionSatisfaction ="Strongly Disagree" then 1
                END AS rateTeamContributionSatisfaction,
                
                case 
                when tf1.rateSelfKnowledgeBefore_1 ="Very High" then 5
                when tf1.rateSelfKnowledgeBefore_1 ="High" then 4
                when tf1.rateSelfKnowledgeBefore_1 ="Neutral" or tf1.rateSelfKnowledgeBefore_1="Nuetral" then 3
                when tf1.rateSelfKnowledgeBefore_1 ="Low" then 2
                when tf1.rateSelfKnowledgeBefore_1 ="Very Low" then 1
                when tf1.rateSelfKnowledgeBefore_1 ="N/A" then 0
                END AS rateSelfKnowledgeBefore_1,
                
                case 
                when tf1.rateSelfKnowledgeAfter_1 ="Very High" then 5
                when tf1.rateSelfKnowledgeAfter_1 ="High" then 4
                when tf1.rateSelfKnowledgeAfter_1 ="Neutral" or tf1.rateSelfKnowledgeAfter_1="Nuetral" then 3
                when tf1.rateSelfKnowledgeAfter_1 ="Low" then 2
                when tf1.rateSelfKnowledgeAfter_1 ="Very Low" then 1
                when tf1.rateSelfKnowledgeAfter_1 ="N/A" then 0
                END AS rateSelfKnowledgeAfter_1,
                
                case 
                when tf1.rateSelfKnowledgeBefore_2 ="Very High" then 5
                when tf1.rateSelfKnowledgeBefore_2 ="High" then 4
                when tf1.rateSelfKnowledgeBefore_2 ="Neutral" or tf1.rateSelfKnowledgeBefore_2="Nuetral" then 3
                when tf1.rateSelfKnowledgeBefore_2 ="Low" then 2
                when tf1.rateSelfKnowledgeBefore_2 ="Very Low" then 1
                when tf1.rateSelfKnowledgeBefore_2 ="N/A" then 0
                END AS rateSelfKnowledgeBefore_2,
                
                case 
                when tf1.rateSelfKnowledgeAfter_2 ="Very High" then 5
                when tf1.rateSelfKnowledgeAfter_2 ="High" then 4
                when tf1.rateSelfKnowledgeAfter_2 ="Neutral" or tf1.rateSelfKnowledgeAfter_2="Nuetral" then 3
                when tf1.rateSelfKnowledgeAfter_2 ="Low" then 2
                when tf1.rateSelfKnowledgeAfter_2 ="Very Low" then 1
                when tf1.rateSelfKnowledgeAfter_2 ="N/A" then 0
                END AS rateSelfKnowledgeAfter_2,
                
                case 
                when tf1.rateSelfKnowledgeBefore_3 ="Very High" then 5
                when tf1.rateSelfKnowledgeBefore_3 ="High" then 4
                when tf1.rateSelfKnowledgeBefore_3 ="Neutral" or tf1.rateSelfKnowledgeBefore_3="Nuetral" then 3
                when tf1.rateSelfKnowledgeBefore_3 ="Low" then 2
                when tf1.rateSelfKnowledgeBefore_3 ="Very Low" then 1
                when tf1.rateSelfKnowledgeBefore_3 ="N/A" then 0
                END AS rateSelfKnowledgeBefore_3,
                
                case 
                when tf1.rateSelfKnowledgeAfter_3 ="Very High" then 5
                when tf1.rateSelfKnowledgeAfter_3 ="High" then 4
                when tf1.rateSelfKnowledgeAfter_3 ="Neutral" or tf1.rateSelfKnowledgeAfter_3="Nuetral" then 3
                when tf1.rateSelfKnowledgeAfter_3 ="Low" then 2
                when tf1.rateSelfKnowledgeAfter_3 ="Very Low" then 1
                when tf1.rateSelfKnowledgeAfter_3 ="N/A" then 0
                END AS rateSelfKnowledgeAfter_3,
         
                case 
                when tf1.taskDifficulty ="Strongly Agree" then 5
                when tf1.taskDifficulty ="Agree" then 4
                when tf1.taskDifficulty ="Neutral" or tf1.taskDifficulty="Nuetral" then 3
                when tf1.taskDifficulty ="Disagree" then 2
                when tf1.taskDifficulty ="Strongly Disagree" then 1
                END AS taskDifficulty,
                
                case 
                when tf1.rateMember1 ="Strongly Agree" then 5
                when tf1.rateMember1 ="Agree" then 4
                when tf1.rateMember1 ="Neutral" or tf1.rateMember1="Nuetral" then 3
                when tf1.rateMember1 ="Disagree" then 2
                when tf1.rateMember1 ="Strongly Disagree" then 1
                END AS rateMember1,
                
                case 
                when tf1.rateMember2 ="Strongly Agree" then 5
                when tf1.rateMember2 ="Agree" then 4
                when tf1.rateMember2 ="Neutral" or tf1.rateMember2="Nuetral" then 3
                when tf1.rateMember2 ="Disagree" then 2
                when tf1.rateMember2 ="Strongly Disagree" then 1
                END AS rateMember2,
                
                case 
                when tf1.rateMember3 ="Strongly Agree" then 5
                when tf1.rateMember3 ="Agree" then 4
                when tf1.rateMember3 ="Neutral" or tf1.rateMember3="Nuetral" then 3
                when tf1.rateMember3 ="Disagree" then 2
                when tf1.rateMember3 ="Strongly Disagree" then 1
                END AS rateMember3

                FROM task1_feedback tf1"""
task1_feed_box_legend = None

task2_feed_box = """SELECT  (tf2.team_id) AS Entries,"Task 2" AS taskName, tf2.theme,
                (tf2.rateTask2) AS rateTask,
                (tf2.rateTask2Design) AS rateTaskDesign,
                (tf2.rateResource) AS rateResource,
                ((tf2.rateDifficulty_1+tf2.rateDifficulty_2+tf2.rateDifficulty_3)/3) AS rateDifficulty,
                (tf2.rateTask1Remarks) AS rateTaskRemarks,
                (tf2.rateForumUsefulness) AS rateForumUsefulness,
                (tf2.rateLiveSessionUsefulness) AS rateLiveSessionUsefulness,
                (tf2.rateEffectiveness) AS rateEffectiveness
                FROM task2_feedback tf2"""
task2_feed_box_legend = None

task3_feed_box = """SELECT  (tf3.team_id) AS Entries,"Task 3" AS taskName, tf3.theme,
                (tf3.rateTask3) AS rateTask,
                (tf3.rateTask3Design) AS rateTaskDesign,
                (tf3.rateResource) AS rateResource,
                ((tf3.rateDifficulty_1+tf3.rateDifficulty_2+tf3.rateDifficulty_3)/3) AS rateDifficulty,
                (tf3.rateLiveSessionUsefulness) AS rateLiveSessionUsefulness,
                (tf3.rateTaskRemarks) AS rateTaskRemarks,
                (tf3.rateEffectiveness) AS rateEffectiveness

                FROM task3_feedback tf3"""
task3_feed_box_legend = None

task4_feed_box = """SELECT  (tf4.team_id) AS Entries,"Task 4" AS taskName, tf4.theme,
                    (tf4.rateTask4) AS rateTask,
                    (tf4.rateTask4Design) AS rateTaskDesign,
                    (tf4.rateResource) AS rateResource,
                    (tf4.rateLiveSessionUsefulness) AS rateLiveSessionUsefulness,
                    (tf4.rateEffectiveness) AS rateEffectiveness,
                    ((tf4.rateDifficulty_1+tf4.rateDifficulty_2+tf4.rateDifficulty_3)/3) AS rateDifficulty,
                    (tf4.rateForumUsefulness) AS rateForumUsefulness,
                    (tf4.rateTaskRemarks) AS rateTaskRemarks
                FROM task4_feedback tf4"""
task4_feed_box_legend = None

task5_feed_box = """SELECT  (tf5.team_id) AS Entries,"Task 5" AS taskName, tf5.theme,
                (tf5.rateTask5) AS rateTask,
                (tf5.rateTask5Design) AS rateTaskDesign,
                (tf5.rateResource) AS rateResource,
                (tf5.rateEffectiveness) AS rateEffectiveness,
                ((tf5.rateDifficulty_1+tf5.rateDifficulty_2+tf5.rateDifficulty_3)/3) AS rateDifficulty,
                (tf5.rateForumUsefulness) AS rateForumUsefulness,
                (tf5.rateLiveSessionUsefulness) AS rateLiveSessionUsefulness,
                (tf5.rateTaskRemarks) AS rateTaskRemarks
                FROM task5_feedback tf5"""
task5_feed_box_legend = None

stage1_feed_box_1 = """SELECT  (s1.team_id) AS Entries,"Stage1_feedback_P1" AS taskName, s1.theme,
case 
when s1.rateThemeEasiness ="Very Easy" then 5
when s1.rateThemeEasiness ="Easy" then 4
when s1.rateThemeEasiness ="Neutral" or s1.rateThemeEasiness="Nuetral" then 3
when s1.rateThemeEasiness ="Difficult" then 2
when s1.rateThemeEasiness ="Very Difficult" then 1
END AS rateThemeEasiness,
case 
when s1.rateTaskProblemStatement ="Strongly Agree" then 5
when s1.rateTaskProblemStatement ="Agree" then 4
when s1.rateTaskProblemStatement ="Neutral" or s1.rateTaskProblemStatement="Nuetral" then 3
when s1.rateTaskProblemStatement ="Disagree" then 2
when s1.rateTaskProblemStatement ="Strongly Disagree" then 1
END AS rateTaskProblemStatement,
case 
when s1.rateTaskDifficulty ="Strongly Agree" then 5
when s1.rateTaskDifficulty ="Agree" then 4
when s1.rateTaskDifficulty ="Neutral" or s1.rateTaskDifficulty="Nuetral" then 3
when s1.rateTaskDifficulty ="Disagree" then 2
when s1.rateTaskDifficulty ="Strongly Disagree" then 1
END AS rateTaskDifficulty,
case 
when s1.rateTasksHelpfulness ="Strongly Agree" then 5
when s1.rateTasksHelpfulness ="Agree" then 4
when s1.rateTasksHelpfulness ="Neutral" or s1.rateTasksHelpfulness="Nuetral" then 3
when s1.rateTasksHelpfulness ="Disagree" then 2
when s1.rateTasksHelpfulness ="Strongly Disagree" then 1
END AS rateTasksHelpfulness,
case 
when s1.rateTaskResources ="Strongly Agree" then 5
when s1.rateTaskResources ="Agree" then 4
when s1.rateTaskResources ="Neutral" or s1.rateTaskResources="Nuetral" then 3
when s1.rateTaskResources ="Disagree" then 2
when s1.rateTaskResources ="Strongly Disagree" then 1
END AS rateTaskResources,
case 
when s1.rateTaskHosting ="Strongly Agree" then 5
when s1.rateTaskHosting ="Agree" then 4
when s1.rateTaskHosting ="Neutral" or s1.rateTaskHosting="Nuetral" then 3
when s1.rateTaskHosting ="Disagree" then 2
when s1.rateTaskHosting ="Strongly Disagree" then 1
END AS rateTaskHosting,
case 
when s1.externalResourses ="Strongly Agree" then 5
when s1.externalResourses ="Agree" then 4
when s1.externalResourses ="Neutral" or s1.externalResourses="Nuetral" then 3
when s1.externalResourses ="Disagree" then 2
when s1.externalResourses ="Strongly Disagree" then 1
END AS externalResourses
FROM stage1_feedback s1"""
stage1_feed_box_1_legend = "rateThemeEasiness: 5=>Very Easy, 1=>Very Difficult <br>" \
                           "rateTaskProblemStatement: 5=>Very Easy, 1=>Very Difficult <br>" \
                           "rateTaskProblemStatement: 5=>Strongly Agree, 1=>Strongly Disagree <br>" \
                           "rateTaskDifficulty: 5=>Strongly Agree, 1=>Strongly Disagree <br>" \
                           "rateTasksHelpfulness: 5=>Strongly Agree, 1=>Strongly Disagree <br>" \
                           "rateTaskResources: 5=>Strongly Agree, 1=>Strongly Disagree <br>" \
                           "rateTaskHosting: 5=>Strongly Agree, 1=>Strongly Disagree <br>" \
                           "externalResourses: 5=>Strongly Agree, 1=>Strongly Disagree <br>" \
                           ""

stage1_feed_box_2 = """SELECT  (s1.team_id) AS Entries,"Stage1_feedback_P2" AS taskName, s1.theme,
case 
when s1.discourseHelpfulness ="Strongly Agree" then 5
when s1.discourseHelpfulness ="Agree" then 4
when s1.discourseHelpfulness ="Neutral" or s1.discourseHelpfulness="Nuetral" then 3
when s1.discourseHelpfulness ="Disagree" then 2
when s1.discourseHelpfulness ="Strongly Disagree" then 1
END AS discourseHelpfulness,
case 
when s1.discourseInstructorResponse ="Strongly Agree" then 5
when s1.discourseInstructorResponse ="Agree" then 4
when s1.discourseInstructorResponse ="Neutral" or s1.discourseInstructorResponse="Nuetral" then 3
when s1.discourseInstructorResponse ="Disagree" then 2
when s1.discourseInstructorResponse ="Strongly Disagree" then 1
END AS discourseInstructorResponse,
case 
when s1.discourseStudentResponse ="Strongly Agree" then 5
when s1.discourseStudentResponse ="Agree" then 4
when s1.discourseStudentResponse ="Neutral" or s1.discourseStudentResponse="Nuetral" then 3
when s1.discourseStudentResponse ="Disagree" then 2
when s1.discourseStudentResponse ="Strongly Disagree" then 1
END AS discourseStudentResponse,
case 
when s1.discoursePosts ="Strongly Agree" then 5
when s1.discoursePosts ="Agree" then 4
when s1.discoursePosts ="Neutral" or s1.discoursePosts="Nuetral" then 3
when s1.discoursePosts ="Disagree" then 2
when s1.discoursePosts ="Strongly Disagree" then 1
END AS discoursePosts,
case 
when s1.discoursePolls ="Strongly Agree" then 5
when s1.discoursePolls ="Agree" then 4
when s1.discoursePolls ="Neutral" or s1.discoursePolls="Nuetral" then 3
when s1.discoursePolls ="Disagree" then 2
when s1.discoursePolls ="Strongly Disagree" then 1
END AS discoursePolls
FROM stage1_feedback s1"""
stage1_feed_box_2_legend = "discourseHelpfulness: 5=>Very Easy, 1=>Very Difficult <br>" \
                           "discourseInstructorResponse: 5=>Very Easy, 1=>Very Difficult <br>" \
                           "discourseStudentResponse: 5=>Very Easy, 1=>Very Difficult <br>" \
                           "discoursePosts: 5=>Very Easy, 1=>Very Difficult <br>" \
                           "discoursePolls: 5=>Very Easy, 1=>Very Difficult <br>" \
                           ""

stage1_feed_box_3 = """SELECT  (s1.team_id) AS Entries,"Stage1_feedback_P3" AS taskName, s1.theme,
case 
when s1.teamOrindividual ="4-member Team" then 4
when s1.teamOrindividual ="3-member Team" then 3
when s1.teamOrindividual ="2-member Team" then 2
when s1.teamOrindividual ="Individual" then 1
END AS teamOrindividual,
case 
when s1.rateCollaborativeSkillsBefore ="5" then 5
when s1.rateCollaborativeSkillsBefore ="4" then 4
when s1.rateCollaborativeSkillsBefore ="3" then 3
when s1.rateCollaborativeSkillsBefore ="2" then 2
when s1.rateCollaborativeSkillsBefore ="1" then 1
END AS rateCollaborativeSkillsBefore,
case 
when s1.rateCollaborativeSkillsAfter ="5" then 5
when s1.rateCollaborativeSkillsAfter ="4" then 4
when s1.rateCollaborativeSkillsAfter ="3" then 3
when s1.rateCollaborativeSkillsAfter ="2" then 2
when s1.rateCollaborativeSkillsAfter ="1" then 1
END AS rateCollaborativeSkillsAfter,
case 
when s1.rateSelfLearningSkillsBefore ="5" then 5
when s1.rateSelfLearningSkillsBefore ="4" then 4
when s1.rateSelfLearningSkillsBefore ="3" then 3
when s1.rateSelfLearningSkillsBefore ="2" then 2
when s1.rateSelfLearningSkillsBefore ="1" then 1
END AS rateSelfLearningSkillsBefore,
case 
when s1.rateSelfLearningSkillsAfter ="5" then 5
when s1.rateSelfLearningSkillsAfter ="4" then 4
when s1.rateSelfLearningSkillsAfter ="3" then 3
when s1.rateSelfLearningSkillsAfter ="2" then 2
when s1.rateSelfLearningSkillsAfter ="1" then 1
END AS rateSelfLearningSkillsAfter,
case 
when s1.ratePeerLearningBefore ="5" then 5
when s1.ratePeerLearningBefore ="4" then 4
when s1.ratePeerLearningBefore ="3" then 3
when s1.ratePeerLearningBefore ="2" then 2
when s1.ratePeerLearningBefore ="1" then 1
END AS ratePeerLearningBefore,
case 
when s1.ratePeerLearningAfter ="5" then 5
when s1.ratePeerLearningAfter ="4" then 4
when s1.ratePeerLearningAfter ="3" then 3
when s1.ratePeerLearningAfter ="2" then 2
when s1.ratePeerLearningAfter ="1" then 1
END AS ratePeerLearningAfter,
case 
when s1.rateHandsOnSkillsBefore ="5" then 5
when s1.rateHandsOnSkillsBefore ="4" then 4
when s1.rateHandsOnSkillsBefore ="3" then 3
when s1.rateHandsOnSkillsBefore ="2" then 2
when s1.rateHandsOnSkillsBefore ="1" then 1
END AS rateHandsOnSkillsBefore,
case 
when s1.rateHandsOnSkillsAfter ="5" then 5
when s1.rateHandsOnSkillsAfter ="4" then 4
when s1.rateHandsOnSkillsAfter ="3" then 3
when s1.rateHandsOnSkillsAfter ="2" then 2
when s1.rateHandsOnSkillsAfter ="1" then 1
END AS rateHandsOnSkillsAfter
FROM stage1_feedback s1"""
stage1_feed_box_3_legend = "teamOrindividual: 4=>4-member Team, 1=>Individual <br>" \
                           ""

stage1_feed_box_4 = """SELECT  (s1.team_id) AS Entries,"Stage1_feedback_P4" AS taskName, s1.theme,
case 
when s1.covidCase ="No" then 0
when s1.covidCase ="Yes" then 1
END AS covidCase,
case 
when s1.rateThemeDesign ="Strongly Agree" then 5
when s1.rateThemeDesign ="Agree" then 4
when s1.rateThemeDesign ="Neutral" or s1.rateThemeDesign="Nuetral" then 3
when s1.rateThemeDesign ="Disagree" then 2
when s1.rateThemeDesign ="Strongly Disagree" then 1
END AS rateThemeDesign,
case 
when s1.timeSpendEyrc ="less than 12 hours" then 1
when s1.timeSpendEyrc ="12-24 hours" then 2
when s1.timeSpendEyrc ="24-36 hours" then 3
when s1.timeSpendEyrc ="36-48 hours" then 4
when s1.timeSpendEyrc ="48-60 hours" then 5
when s1.timeSpendEyrc ="more than 60 hours" then 6
END AS timeSpendEyrc,
case 
when s1.timeSpendAcademics ="less than 12 hours" then 1
when s1.timeSpendAcademics ="12-24 hours" then 2
when s1.timeSpendAcademics ="24-36 hours" then 3
when s1.timeSpendAcademics ="36-48 hours" then 4
when s1.timeSpendAcademics ="48-60 hours" then 5
when s1.timeSpendAcademics ="more than 60 hours" then 6
END AS timeSpendAcademics,
case 
when s1.timeSpendRecreation ="less than 12 hours" then 1
when s1.timeSpendRecreation ="12-24 hours" then 2
when s1.timeSpendRecreation ="24-36 hours" then 3
when s1.timeSpendRecreation ="36-48 hours" then 4
when s1.timeSpendRecreation ="48-60 hours" then 5
when s1.timeSpendRecreation ="more than 60 hours" then 6
END AS timeSpendRecreation,
case 
when s1.timeSpendOther ="less than 12 hours" then 1
when s1.timeSpendOther ="12-24 hours" then 2
when s1.timeSpendOther ="24-36 hours" then 3
when s1.timeSpendOther ="36-48 hours" then 4
when s1.timeSpendOther ="48-60 hours" then 5
when s1.timeSpendOther ="more than 60 hours" then 6
END AS timeSpendOther,
case 
when s1.nonPandemicSelfContribution ="Strongly Agree" then 5
when s1.nonPandemicSelfContribution ="Agree" then 4
when s1.nonPandemicSelfContribution ="Neutral" or s1.nonPandemicSelfContribution="Nuetral" then 3
when s1.nonPandemicSelfContribution ="Disagree" then 2
when s1.nonPandemicSelfContribution ="Strongly Disagree" then 1
END AS nonPandemicSelfContribution,
case 
when s1.nonPandemicLearning ="Strongly Agree" then 5
when s1.nonPandemicLearning ="Agree" then 4
when s1.nonPandemicLearning ="Neutral" or s1.nonPandemicLearning="Nuetral" then 3
when s1.nonPandemicLearning ="Disagree" then 2
when s1.nonPandemicLearning ="Strongly Disagree" then 1
END AS nonPandemicLearning,
case 
when s1.nonPandemicFocus ="Strongly Agree" then 5
when s1.nonPandemicFocus ="Agree" then 4
when s1.nonPandemicFocus ="Neutral" or s1.nonPandemicFocus="Nuetral" then 3
when s1.nonPandemicFocus ="Disagree" then 2
when s1.nonPandemicFocus ="Strongly Disagree" then 1
END AS nonPandemicFocus,
case 
when s1.nonPandemicTaskManagement ="Strongly Agree" then 5
when s1.nonPandemicTaskManagement ="Agree" then 4
when s1.nonPandemicTaskManagement ="Neutral" or s1.nonPandemicTaskManagement="Nuetral" then 3
when s1.nonPandemicTaskManagement ="Disagree" then 2
when s1.nonPandemicTaskManagement ="Strongly Disagree" then 1
END AS nonPandemicTaskManagement,
case 
when s1.rateFeeWorth ="No" then 0
when s1.rateFeeWorth ="Yes" then 1
END AS rateFeeWorth
FROM stage1_feedback s1"""
stage1_feed_box_4_legend = "covidCase: 1=>Yes, 0=>No <br>" \
                           "rateThemeDesign: 5=>Strongly Agree, 1=>Strongly Disagree <br>" \
                           "timeSpendEyrc: 6=>more than 60 hours, 5=>48-60 hours, 4=>36-48 hours, 3=>24-36 hours, 2=>12-24 hours, 1=>less than 12 hours <br>" \
                           "timeSpendAcademics: 6=>more than 60 hours, 5=>48-60 hours, 4=>36-48 hours, 3=>24-36 hours, 2=>12-24 hours, 1=>less than 12 hours <br>" \
                           "timeSpendRecreation: 6=>more than 60 hours, 5=>48-60 hours, 4=>36-48 hours, 3=>24-36 hours, 2=>12-24 hours, 1=>less than 12 hours <br>" \
                           "timeSpendOther: 6=>more than 60 hours, 5=>48-60 hours, 4=>36-48 hours, 3=>24-36 hours, 2=>12-24 hours, 1=>less than 12 hours <br>" \
                           "nonPandemicSelfContribution: 5=>Strongly Agree, 1=>Strongly Disagree <br>" \
                           "nonPandemicLearning: 5=>Strongly Agree, 1=>Strongly Disagree <br>" \
                           "nonPandemicFocus: 5=>Strongly Agree, 1=>Strongly Disagree <br>" \
                           "nonPandemicTaskManagement: 5=>Strongly Agree, 1=>Strongly Disagree <br>"
