task0_feedbackSelect = """SELECT theme,
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
                END AS forumUsefulness,
                case 
                when task0Difficulty ="Strongly Agree" then 5
                when task0Difficulty ="Agree" then 4
                when task0Difficulty ="Neutral" or task0Difficulty="Nuetral" then 3
                when task0Difficulty ="Disagree" then 2
                when task0Difficulty ="Strongly Disagree" then 1
                END AS task0Difficultyness

                from task0_feedback"""
task0_feedbackSelect_legend = {
    'themeEnjoy': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'task0Simplicity': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'task0ResourceHelpful': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'task0Resource': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateSelfKnowledgeBefore_1': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeAfter_1': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'forumUseful': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'task0Difficulty': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    }
}

task1_feedbackSelect = """SELECT tf1.theme,
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
task1_feedbackSelect_legend = {
    'taskEasiness': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'taskEasiness_b': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'taskEasiness_c': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateTaskDifficulty': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'sessionHelpfulness': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateSelfContribution': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateResources': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateForumUsefulness': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateSelfContributionSatisfaction': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateTeamContributionSatisfaction': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateSelfKnowledgeBefore_1': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeAfter_1': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeBefore_2': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeAfter_2': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeBefore_3': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeAfter_3': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'taskDifficulty': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateMember1': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateMember2': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateMember3': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    }
}

task2_feedbackSelect = """SELECT tf2.theme,
                case 
                when tf2.taskEasiness ="Strongly Agree" then 5
                when tf2.taskEasiness ="Agree" then 4
                when tf2.taskEasiness ="Neutral" or tf2.taskEasiness="Nuetral" then 3
                when tf2.taskEasiness ="Disagree" then 2
                when tf2.taskEasiness ="Strongly Disagree" then 1
                END AS taskEasiness,
                
                case 
                when tf2.taskEasiness_b ="Strongly Agree" then 5
                when tf2.taskEasiness_b ="Agree" then 4
                when tf2.taskEasiness_b ="Neutral" or tf2.taskEasiness_b="Nuetral" then 3
                when tf2.taskEasiness_b ="Disagree" then 2
                when tf2.taskEasiness_b ="Strongly Disagree" then 1
                END AS taskEasiness_b,
                
                case 
                when tf2.taskEasiness_c ="Strongly Agree" then 5
                when tf2.taskEasiness_c ="Agree" then 4
                when tf2.taskEasiness_c ="Neutral" or tf2.taskEasiness_c="Nuetral" then 3
                when tf2.taskEasiness_c ="Disagree" then 2
                when tf2.taskEasiness_c ="Strongly Disagree" then 1
                END AS taskEasiness_c,
                
                case 
                when tf2.rateTaskDifficulty ="Very High" then 5
                when tf2.rateTaskDifficulty ="High" then 4
                when tf2.rateTaskDifficulty ="Neutral" or tf2.rateTaskDifficulty="Nuetral" then 3
                when tf2.rateTaskDifficulty ="Low" then 2
                when tf2.rateTaskDifficulty ="Very Low" then 1
                when tf2.rateTaskDifficulty ="N/A" then 0
                END AS rateTaskDifficulty,
                
                case 
                when tf2.sessionHelpfulness ="Strongly Agree" then 5
                when tf2.sessionHelpfulness ="Agree" then 4
                when tf2.sessionHelpfulness ="Neutral" or tf2.sessionHelpfulness="Nuetral" then 3
                when tf2.sessionHelpfulness ="Disagree" then 2
                when tf2.sessionHelpfulness ="Strongly Disagree" then 1
                END AS sessionHelpfulness,
                
                case 
                when tf2.rateSelfContribution ="Very High" then 5
                when tf2.rateSelfContribution ="High" then 4
                when tf2.rateSelfContribution ="Neutral" or tf2.rateSelfContribution="Nuetral" then 3
                when tf2.rateSelfContribution ="Low" then 2
                when tf2.rateSelfContribution ="Very Low" then 1
                when tf2.rateSelfContribution ="N/A" then 0
                END AS rateSelfContribution,
                
                case 
                when tf2.rateResources ="Strongly Agree" then 5
                when tf2.rateResources ="Agree" then 4
                when tf2.rateResources ="Neutral" or tf2.rateResources="Nuetral" then 3
                when tf2.rateResources ="Disagree" then 2
                when tf2.rateResources ="Strongly Disagree" then 1
                END AS rateResources,
                
                case 
                when tf2.rateForumUsefulness ="Strongly Agree" then 5
                when tf2.rateForumUsefulness ="Agree" then 4
                when tf2.rateForumUsefulness ="Neutral" or tf2.rateForumUsefulness="Nuetral" then 3
                when tf2.rateForumUsefulness ="Disagree" then 2
                when tf2.rateForumUsefulness ="Strongly Disagree" then 1
                END AS rateForumUsefulness,
                
                case 
                when tf2.rateSelfContributionSatisfaction ="Strongly Agree" then 5
                when tf2.rateSelfContributionSatisfaction ="Agree" then 4
                when tf2.rateSelfContributionSatisfaction ="Neutral" or tf2.rateSelfContributionSatisfaction="Nuetral" then 3
                when tf2.rateSelfContributionSatisfaction ="Disagree" then 2
                when tf2.rateSelfContributionSatisfaction ="Strongly Disagree" then 1
                END AS rateSelfContributionSatisfaction,
                
                case 
                when tf2.rateTeamContributionSatisfaction ="Strongly Agree" then 5
                when tf2.rateTeamContributionSatisfaction ="Agree" then 4
                when tf2.rateTeamContributionSatisfaction ="Neutral" or tf2.rateTeamContributionSatisfaction="Nuetral" then 3
                when tf2.rateTeamContributionSatisfaction ="Disagree" then 2
                when tf2.rateTeamContributionSatisfaction ="Strongly Disagree" then 1
                END AS rateTeamContributionSatisfaction,
                
                case 
                when tf2.rateSelfKnowledgeBefore_1 ="Very High" then 5
                when tf2.rateSelfKnowledgeBefore_1 ="High" then 4
                when tf2.rateSelfKnowledgeBefore_1 ="Neutral" or tf2.rateSelfKnowledgeBefore_1="Nuetral" then 3
                when tf2.rateSelfKnowledgeBefore_1 ="Low" then 2
                when tf2.rateSelfKnowledgeBefore_1 ="Very Low" then 1
                when tf2.rateSelfKnowledgeBefore_1 ="N/A" then 0
                END AS rateSelfKnowledgeBefore_1,
                
                case 
                when tf2.rateSelfKnowledgeAfter_1 ="Very High" then 5
                when tf2.rateSelfKnowledgeAfter_1 ="High" then 4
                when tf2.rateSelfKnowledgeAfter_1 ="Neutral" or tf2.rateSelfKnowledgeAfter_1="Nuetral" then 3
                when tf2.rateSelfKnowledgeAfter_1 ="Low" then 2
                when tf2.rateSelfKnowledgeAfter_1 ="Very Low" then 1
                when tf2.rateSelfKnowledgeAfter_1 ="N/A" then 0
                END AS rateSelfKnowledgeAfter_1,
                
                case 
                when tf2.rateSelfKnowledgeBefore_2 ="Very High" then 5
                when tf2.rateSelfKnowledgeBefore_2 ="High" then 4
                when tf2.rateSelfKnowledgeBefore_2 ="Neutral" or tf2.rateSelfKnowledgeBefore_2="Nuetral" then 3
                when tf2.rateSelfKnowledgeBefore_2 ="Low" then 2
                when tf2.rateSelfKnowledgeBefore_2 ="Very Low" then 1
                when tf2.rateSelfKnowledgeBefore_2 ="N/A" then 0
                END AS rateSelfKnowledgeBefore_2,
                
                case 
                when tf2.rateSelfKnowledgeAfter_2 ="Very High" then 5
                when tf2.rateSelfKnowledgeAfter_2 ="High" then 4
                when tf2.rateSelfKnowledgeAfter_2 ="Neutral" or tf2.rateSelfKnowledgeAfter_2="Nuetral" then 3
                when tf2.rateSelfKnowledgeAfter_2 ="Low" then 2
                when tf2.rateSelfKnowledgeAfter_2 ="Very Low" then 1
                when tf2.rateSelfKnowledgeAfter_2 ="N/A" then 0
                END AS rateSelfKnowledgeAfter_2,
                
                case 
                when tf2.rateSelfKnowledgeBefore_3 ="Very High" then 5
                when tf2.rateSelfKnowledgeBefore_3 ="High" then 4
                when tf2.rateSelfKnowledgeBefore_3 ="Neutral" or tf2.rateSelfKnowledgeBefore_3="Nuetral" then 3
                when tf2.rateSelfKnowledgeBefore_3 ="Low" then 2
                when tf2.rateSelfKnowledgeBefore_3 ="Very Low" then 1
                when tf2.rateSelfKnowledgeBefore_3 ="N/A" then 0
                END AS rateSelfKnowledgeBefore_3,
                
                case 
                when tf2.rateSelfKnowledgeAfter_3 ="Very High" then 5
                when tf2.rateSelfKnowledgeAfter_3 ="High" then 4
                when tf2.rateSelfKnowledgeAfter_3 ="Neutral" or tf2.rateSelfKnowledgeAfter_3="Nuetral" then 3
                when tf2.rateSelfKnowledgeAfter_3 ="Low" then 2
                when tf2.rateSelfKnowledgeAfter_3 ="Very Low" then 1
                when tf2.rateSelfKnowledgeAfter_3 ="N/A" then 0
                END AS rateSelfKnowledgeAfter_3,
         
                case 
                when tf2.taskDifficulty ="Strongly Agree" then 5
                when tf2.taskDifficulty ="Agree" then 4
                when tf2.taskDifficulty ="Neutral" or tf2.taskDifficulty="Nuetral" then 3
                when tf2.taskDifficulty ="Disagree" then 2
                when tf2.taskDifficulty ="Strongly Disagree" then 1
                END AS taskDifficulty,
                
                case 
                when tf2.rateMember1 ="Strongly Agree" then 5
                when tf2.rateMember1 ="Agree" then 4
                when tf2.rateMember1 ="Neutral" or tf2.rateMember1="Nuetral" then 3
                when tf2.rateMember1 ="Disagree" then 2
                when tf2.rateMember1 ="Strongly Disagree" then 1
                END AS rateMember1,
                
                case 
                when tf2.rateMember2 ="Strongly Agree" then 5
                when tf2.rateMember2 ="Agree" then 4
                when tf2.rateMember2 ="Neutral" or tf2.rateMember2="Nuetral" then 3
                when tf2.rateMember2 ="Disagree" then 2
                when tf2.rateMember2 ="Strongly Disagree" then 1
                END AS rateMember2,
                
                case 
                when tf2.rateMember3 ="Strongly Agree" then 5
                when tf2.rateMember3 ="Agree" then 4
                when tf2.rateMember3 ="Neutral" or tf2.rateMember3="Nuetral" then 3
                when tf2.rateMember3 ="Disagree" then 2
                when tf2.rateMember3 ="Strongly Disagree" then 1
                END AS rateMember3
                FROM task2_feedback tf2"""
task2_feedbackSelect_legend = {
    'taskEasiness': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'taskEasiness_b': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'taskEasiness_c': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateTaskDifficulty': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'sessionHelpfulness': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateSelfContribution': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateResources': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateForumUsefulness': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateSelfContributionSatisfaction': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateTeamContributionSatisfaction': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateSelfKnowledgeBefore_1': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeAfter_1': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeBefore_2': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeAfter_2': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeBefore_3': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeAfter_3': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'taskDifficulty': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateMember1': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateMember2': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateMember3': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    }
}

task3_feedbackSelect = """SELECT tf3.theme,
                case 
                when tf3.taskEasiness ="Strongly Agree" then 5
                when tf3.taskEasiness ="Agree" then 4
                when tf3.taskEasiness ="Neutral" or tf3.taskEasiness="Nuetral" then 3
                when tf3.taskEasiness ="Disagree" then 2
                when tf3.taskEasiness ="Strongly Disagree" then 1
                END AS taskEasiness,
                
                case 
                when tf3.taskEasiness_b ="Strongly Agree" then 5
                when tf3.taskEasiness_b ="Agree" then 4
                when tf3.taskEasiness_b ="Neutral" or tf3.taskEasiness_b="Nuetral" then 3
                when tf3.taskEasiness_b ="Disagree" then 2
                when tf3.taskEasiness_b ="Strongly Disagree" then 1
                END AS taskEasiness_b,
                
                case 
                when tf3.taskEasiness_c ="Strongly Agree" then 5
                when tf3.taskEasiness_c ="Agree" then 4
                when tf3.taskEasiness_c ="Neutral" or tf3.taskEasiness_c="Nuetral" then 3
                when tf3.taskEasiness_c ="Disagree" then 2
                when tf3.taskEasiness_c ="Strongly Disagree" then 1
                END AS taskEasiness_c,
                
                case 
                when tf3.rateTaskDifficulty ="Very High" then 5
                when tf3.rateTaskDifficulty ="High" then 4
                when tf3.rateTaskDifficulty ="Neutral" or tf3.rateTaskDifficulty="Nuetral" then 3
                when tf3.rateTaskDifficulty ="Low" then 2
                when tf3.rateTaskDifficulty ="Very Low" then 1
                when tf3.rateTaskDifficulty ="N/A" then 0
                END AS rateTaskDifficulty,
                
                case 
                when tf3.sessionHelpfulness ="Strongly Agree" then 5
                when tf3.sessionHelpfulness ="Agree" then 4
                when tf3.sessionHelpfulness ="Neutral" or tf3.sessionHelpfulness="Nuetral" then 3
                when tf3.sessionHelpfulness ="Disagree" then 2
                when tf3.sessionHelpfulness ="Strongly Disagree" then 1
                END AS sessionHelpfulness,
                
                case 
                when tf3.rateSelfContribution ="Very High" then 5
                when tf3.rateSelfContribution ="High" then 4
                when tf3.rateSelfContribution ="Neutral" or tf3.rateSelfContribution="Nuetral" then 3
                when tf3.rateSelfContribution ="Low" then 2
                when tf3.rateSelfContribution ="Very Low" then 1
                when tf3.rateSelfContribution ="N/A" then 0
                END AS rateSelfContribution,
                
                case 
                when tf3.rateResources ="Strongly Agree" then 5
                when tf3.rateResources ="Agree" then 4
                when tf3.rateResources ="Neutral" or tf3.rateResources="Nuetral" then 3
                when tf3.rateResources ="Disagree" then 2
                when tf3.rateResources ="Strongly Disagree" then 1
                END AS rateResources,
                
                case 
                when tf3.rateForumUsefulness ="Strongly Agree" then 5
                when tf3.rateForumUsefulness ="Agree" then 4
                when tf3.rateForumUsefulness ="Neutral" or tf3.rateForumUsefulness="Nuetral" then 3
                when tf3.rateForumUsefulness ="Disagree" then 2
                when tf3.rateForumUsefulness ="Strongly Disagree" then 1
                END AS rateForumUsefulness,
                
                case 
                when tf3.rateSelfContributionSatisfaction ="Strongly Agree" then 5
                when tf3.rateSelfContributionSatisfaction ="Agree" then 4
                when tf3.rateSelfContributionSatisfaction ="Neutral" or tf3.rateSelfContributionSatisfaction="Nuetral" then 3
                when tf3.rateSelfContributionSatisfaction ="Disagree" then 2
                when tf3.rateSelfContributionSatisfaction ="Strongly Disagree" then 1
                END AS rateSelfContributionSatisfaction,
                
                case 
                when tf3.rateTeamContributionSatisfaction ="Strongly Agree" then 5
                when tf3.rateTeamContributionSatisfaction ="Agree" then 4
                when tf3.rateTeamContributionSatisfaction ="Neutral" or tf3.rateTeamContributionSatisfaction="Nuetral" then 3
                when tf3.rateTeamContributionSatisfaction ="Disagree" then 2
                when tf3.rateTeamContributionSatisfaction ="Strongly Disagree" then 1
                END AS rateTeamContributionSatisfaction,
                
                case 
                when tf3.rateSelfKnowledgeBefore_1 ="Very High" then 5
                when tf3.rateSelfKnowledgeBefore_1 ="High" then 4
                when tf3.rateSelfKnowledgeBefore_1 ="Neutral" or tf3.rateSelfKnowledgeBefore_1="Nuetral" then 3
                when tf3.rateSelfKnowledgeBefore_1 ="Low" then 2
                when tf3.rateSelfKnowledgeBefore_1 ="Very Low" then 1
                when tf3.rateSelfKnowledgeBefore_1 ="N/A" then 0
                END AS rateSelfKnowledgeBefore_1,
                
                case 
                when tf3.rateSelfKnowledgeAfter_1 ="Very High" then 5
                when tf3.rateSelfKnowledgeAfter_1 ="High" then 4
                when tf3.rateSelfKnowledgeAfter_1 ="Neutral" or tf3.rateSelfKnowledgeAfter_1="Nuetral" then 3
                when tf3.rateSelfKnowledgeAfter_1 ="Low" then 2
                when tf3.rateSelfKnowledgeAfter_1 ="Very Low" then 1
                when tf3.rateSelfKnowledgeAfter_1 ="N/A" then 0
                END AS rateSelfKnowledgeAfter_1,
                
                case 
                when tf3.rateSelfKnowledgeBefore_2 ="Very High" then 5
                when tf3.rateSelfKnowledgeBefore_2 ="High" then 4
                when tf3.rateSelfKnowledgeBefore_2 ="Neutral" or tf3.rateSelfKnowledgeBefore_2="Nuetral" then 3
                when tf3.rateSelfKnowledgeBefore_2 ="Low" then 2
                when tf3.rateSelfKnowledgeBefore_2 ="Very Low" then 1
                when tf3.rateSelfKnowledgeBefore_2 ="N/A" then 0
                END AS rateSelfKnowledgeBefore_2,
                
                case 
                when tf3.rateSelfKnowledgeAfter_2 ="Very High" then 5
                when tf3.rateSelfKnowledgeAfter_2 ="High" then 4
                when tf3.rateSelfKnowledgeAfter_2 ="Neutral" or tf3.rateSelfKnowledgeAfter_2="Nuetral" then 3
                when tf3.rateSelfKnowledgeAfter_2 ="Low" then 2
                when tf3.rateSelfKnowledgeAfter_2 ="Very Low" then 1
                when tf3.rateSelfKnowledgeAfter_2 ="N/A" then 0
                END AS rateSelfKnowledgeAfter_2,
                
                case 
                when tf3.rateSelfKnowledgeBefore_3 ="Very High" then 5
                when tf3.rateSelfKnowledgeBefore_3 ="High" then 4
                when tf3.rateSelfKnowledgeBefore_3 ="Neutral" or tf3.rateSelfKnowledgeBefore_3="Nuetral" then 3
                when tf3.rateSelfKnowledgeBefore_3 ="Low" then 2
                when tf3.rateSelfKnowledgeBefore_3 ="Very Low" then 1
                when tf3.rateSelfKnowledgeBefore_3 ="N/A" then 0
                END AS rateSelfKnowledgeBefore_3,
                
                case 
                when tf3.rateSelfKnowledgeAfter_3 ="Very High" then 5
                when tf3.rateSelfKnowledgeAfter_3 ="High" then 4
                when tf3.rateSelfKnowledgeAfter_3 ="Neutral" or tf3.rateSelfKnowledgeAfter_3="Nuetral" then 3
                when tf3.rateSelfKnowledgeAfter_3 ="Low" then 2
                when tf3.rateSelfKnowledgeAfter_3 ="Very Low" then 1
                when tf3.rateSelfKnowledgeAfter_3 ="N/A" then 0
                END AS rateSelfKnowledgeAfter_3,
         
                case 
                when tf3.taskDifficulty ="Strongly Agree" then 5
                when tf3.taskDifficulty ="Agree" then 4
                when tf3.taskDifficulty ="Neutral" or tf3.taskDifficulty="Nuetral" then 3
                when tf3.taskDifficulty ="Disagree" then 2
                when tf3.taskDifficulty ="Strongly Disagree" then 1
                END AS taskDifficulty,
                
                case 
                when tf3.rateMember1 ="Strongly Agree" then 5
                when tf3.rateMember1 ="Agree" then 4
                when tf3.rateMember1 ="Neutral" or tf3.rateMember1="Nuetral" then 3
                when tf3.rateMember1 ="Disagree" then 2
                when tf3.rateMember1 ="Strongly Disagree" then 1
                END AS rateMember1,
                
                case 
                when tf3.rateMember2 ="Strongly Agree" then 5
                when tf3.rateMember2 ="Agree" then 4
                when tf3.rateMember2 ="Neutral" or tf3.rateMember2="Nuetral" then 3
                when tf3.rateMember2 ="Disagree" then 2
                when tf3.rateMember2 ="Strongly Disagree" then 1
                END AS rateMember2,
                
                case 
                when tf3.rateMember3 ="Strongly Agree" then 5
                when tf3.rateMember3 ="Agree" then 4
                when tf3.rateMember3 ="Neutral" or tf3.rateMember3="Nuetral" then 3
                when tf3.rateMember3 ="Disagree" then 2
                when tf3.rateMember3 ="Strongly Disagree" then 1
                END AS rateMember3

                FROM task3_feedback tf3"""
task3_feedbackSelect_legend = {
    'taskEasiness': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'taskEasiness_b': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'taskEasiness_c': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateTaskDifficulty': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'sessionHelpfulness': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateSelfContribution': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateResources': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateForumUsefulness': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateSelfContributionSatisfaction': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateTeamContributionSatisfaction': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateSelfKnowledgeBefore_1': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeAfter_1': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeBefore_2': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeAfter_2': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeBefore_3': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeAfter_3': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'taskDifficulty': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateMember1': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateMember2': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateMember3': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    }
}

task4_feedbackSelect = """SELECT tf4.theme,
                case 
                when tf4.taskEasiness ="Strongly Agree" then 5
                when tf4.taskEasiness ="Agree" then 4
                when tf4.taskEasiness ="Neutral" or tf4.taskEasiness="Nuetral" then 3
                when tf4.taskEasiness ="Disagree" then 2
                when tf4.taskEasiness ="Strongly Disagree" then 1
                END AS taskEasiness,
                
                case 
                when tf4.taskEasiness_b ="Strongly Agree" then 5
                when tf4.taskEasiness_b ="Agree" then 4
                when tf4.taskEasiness_b ="Neutral" or tf4.taskEasiness_b="Nuetral" then 3
                when tf4.taskEasiness_b ="Disagree" then 2
                when tf4.taskEasiness_b ="Strongly Disagree" then 1
                END AS taskEasiness_b,
                
                case 
                when tf4.taskEasiness_c ="Strongly Agree" then 5
                when tf4.taskEasiness_c ="Agree" then 4
                when tf4.taskEasiness_c ="Neutral" or tf4.taskEasiness_c="Nuetral" then 3
                when tf4.taskEasiness_c ="Disagree" then 2
                when tf4.taskEasiness_c ="Strongly Disagree" then 1
                END AS taskEasiness_c,
                
                case 
                when tf4.rateTaskDifficulty ="Very High" then 5
                when tf4.rateTaskDifficulty ="High" then 4
                when tf4.rateTaskDifficulty ="Neutral" or tf4.rateTaskDifficulty="Nuetral" then 3
                when tf4.rateTaskDifficulty ="Low" then 2
                when tf4.rateTaskDifficulty ="Very Low" then 1
                when tf4.rateTaskDifficulty ="N/A" then 0
                END AS rateTaskDifficulty,
                
                case 
                when tf4.sessionHelpfulness ="Strongly Agree" then 5
                when tf4.sessionHelpfulness ="Agree" then 4
                when tf4.sessionHelpfulness ="Neutral" or tf4.sessionHelpfulness="Nuetral" then 3
                when tf4.sessionHelpfulness ="Disagree" then 2
                when tf4.sessionHelpfulness ="Strongly Disagree" then 1
                END AS sessionHelpfulness,
                
                case 
                when tf4.rateSelfContribution ="Very High" then 5
                when tf4.rateSelfContribution ="High" then 4
                when tf4.rateSelfContribution ="Neutral" or tf4.rateSelfContribution="Nuetral" then 3
                when tf4.rateSelfContribution ="Low" then 2
                when tf4.rateSelfContribution ="Very Low" then 1
                when tf4.rateSelfContribution ="N/A" then 0
                END AS rateSelfContribution,
                
                case 
                when tf4.rateResources ="Strongly Agree" then 5
                when tf4.rateResources ="Agree" then 4
                when tf4.rateResources ="Neutral" or tf4.rateResources="Nuetral" then 3
                when tf4.rateResources ="Disagree" then 2
                when tf4.rateResources ="Strongly Disagree" then 1
                END AS rateResources,
                
                case 
                when tf4.rateForumUsefulness ="Strongly Agree" then 5
                when tf4.rateForumUsefulness ="Agree" then 4
                when tf4.rateForumUsefulness ="Neutral" or tf4.rateForumUsefulness="Nuetral" then 3
                when tf4.rateForumUsefulness ="Disagree" then 2
                when tf4.rateForumUsefulness ="Strongly Disagree" then 1
                END AS rateForumUsefulness,
                
                case 
                when tf4.rateSelfContributionSatisfaction ="Strongly Agree" then 5
                when tf4.rateSelfContributionSatisfaction ="Agree" then 4
                when tf4.rateSelfContributionSatisfaction ="Neutral" or tf4.rateSelfContributionSatisfaction="Nuetral" then 3
                when tf4.rateSelfContributionSatisfaction ="Disagree" then 2
                when tf4.rateSelfContributionSatisfaction ="Strongly Disagree" then 1
                END AS rateSelfContributionSatisfaction,
                
                case 
                when tf4.rateTeamContributionSatisfaction ="Strongly Agree" then 5
                when tf4.rateTeamContributionSatisfaction ="Agree" then 4
                when tf4.rateTeamContributionSatisfaction ="Neutral" or tf4.rateTeamContributionSatisfaction="Nuetral" then 3
                when tf4.rateTeamContributionSatisfaction ="Disagree" then 2
                when tf4.rateTeamContributionSatisfaction ="Strongly Disagree" then 1
                END AS rateTeamContributionSatisfaction,

                case 
                when tf4.ratePreviousTaskFeedback ="Strongly Agree" then 5
                when tf4.ratePreviousTaskFeedback ="Agree" then 4
                when tf4.ratePreviousTaskFeedback ="Neutral" or tf4.ratePreviousTaskFeedback="Nuetral" then 3
                when tf4.ratePreviousTaskFeedback ="Disagree" then 2
                when tf4.ratePreviousTaskFeedback ="Strongly Disagree" then 1
                END AS ratePreviousTaskFeedback,
                
                case 
                when tf4.rateSelfKnowledgeBefore_1 ="Very High" then 5
                when tf4.rateSelfKnowledgeBefore_1 ="High" then 4
                when tf4.rateSelfKnowledgeBefore_1 ="Neutral" or tf4.rateSelfKnowledgeBefore_1="Nuetral" then 3
                when tf4.rateSelfKnowledgeBefore_1 ="Low" then 2
                when tf4.rateSelfKnowledgeBefore_1 ="Very Low" then 1
                when tf4.rateSelfKnowledgeBefore_1 ="N/A" then 0
                END AS rateSelfKnowledgeBefore_1,
                
                case 
                when tf4.rateSelfKnowledgeAfter_1 ="Very High" then 5
                when tf4.rateSelfKnowledgeAfter_1 ="High" then 4
                when tf4.rateSelfKnowledgeAfter_1 ="Neutral" or tf4.rateSelfKnowledgeAfter_1="Nuetral" then 3
                when tf4.rateSelfKnowledgeAfter_1 ="Low" then 2
                when tf4.rateSelfKnowledgeAfter_1 ="Very Low" then 1
                when tf4.rateSelfKnowledgeAfter_1 ="N/A" then 0
                END AS rateSelfKnowledgeAfter_1,
                
                case 
                when tf4.rateSelfKnowledgeBefore_2 ="Very High" then 5
                when tf4.rateSelfKnowledgeBefore_2 ="High" then 4
                when tf4.rateSelfKnowledgeBefore_2 ="Neutral" or tf4.rateSelfKnowledgeBefore_2="Nuetral" then 3
                when tf4.rateSelfKnowledgeBefore_2 ="Low" then 2
                when tf4.rateSelfKnowledgeBefore_2 ="Very Low" then 1
                when tf4.rateSelfKnowledgeBefore_2 ="N/A" then 0
                END AS rateSelfKnowledgeBefore_2,
                
                case 
                when tf4.rateSelfKnowledgeAfter_2 ="Very High" then 5
                when tf4.rateSelfKnowledgeAfter_2 ="High" then 4
                when tf4.rateSelfKnowledgeAfter_2 ="Neutral" or tf4.rateSelfKnowledgeAfter_2="Nuetral" then 3
                when tf4.rateSelfKnowledgeAfter_2 ="Low" then 2
                when tf4.rateSelfKnowledgeAfter_2 ="Very Low" then 1
                when tf4.rateSelfKnowledgeAfter_2 ="N/A" then 0
                END AS rateSelfKnowledgeAfter_2,
                
                case 
                when tf4.rateSelfKnowledgeBefore_3 ="Very High" then 5
                when tf4.rateSelfKnowledgeBefore_3 ="High" then 4
                when tf4.rateSelfKnowledgeBefore_3 ="Neutral" or tf4.rateSelfKnowledgeBefore_3="Nuetral" then 3
                when tf4.rateSelfKnowledgeBefore_3 ="Low" then 2
                when tf4.rateSelfKnowledgeBefore_3 ="Very Low" then 1
                when tf4.rateSelfKnowledgeBefore_3 ="N/A" then 0
                END AS rateSelfKnowledgeBefore_3,
                
                case 
                when tf4.rateSelfKnowledgeAfter_3 ="Very High" then 5
                when tf4.rateSelfKnowledgeAfter_3 ="High" then 4
                when tf4.rateSelfKnowledgeAfter_3 ="Neutral" or tf4.rateSelfKnowledgeAfter_3="Nuetral" then 3
                when tf4.rateSelfKnowledgeAfter_3 ="Low" then 2
                when tf4.rateSelfKnowledgeAfter_3 ="Very Low" then 1
                when tf4.rateSelfKnowledgeAfter_3 ="N/A" then 0
                END AS rateSelfKnowledgeAfter_3,



                case 
                when tf4.rateSelfKnowledgeBefore_4 ="Very High" then 5
                when tf4.rateSelfKnowledgeBefore_4 ="High" then 4
                when tf4.rateSelfKnowledgeBefore_4 ="Neutral" or tf4.rateSelfKnowledgeBefore_4="Nuetral" then 3
                when tf4.rateSelfKnowledgeBefore_4 ="Low" then 2
                when tf4.rateSelfKnowledgeBefore_4 ="Very Low" then 1
                when tf4.rateSelfKnowledgeBefore_4 ="N/A" then 0
                END AS rateSelfKnowledgeBefore_4,

                case 
                when tf4.rateSelfKnowledgeAfter_4 ="Very High" then 5
                when tf4.rateSelfKnowledgeAfter_4 ="High" then 4
                when tf4.rateSelfKnowledgeAfter_4 ="Neutral" or tf4.rateSelfKnowledgeAfter_4="Nuetral" then 3
                when tf4.rateSelfKnowledgeAfter_4 ="Low" then 2
                when tf4.rateSelfKnowledgeAfter_4 ="Very Low" then 1
                when tf4.rateSelfKnowledgeAfter_4 ="N/A" then 0
                END AS rateSelfKnowledgeAfter_4,

                case 
                when tf4.rateSelfKnowledgeBefore_5 ="Very High" then 5
                when tf4.rateSelfKnowledgeBefore_5 ="High" then 4
                when tf4.rateSelfKnowledgeBefore_5 ="Neutral" or tf4.rateSelfKnowledgeBefore_5="Nuetral" then 3
                when tf4.rateSelfKnowledgeBefore_5 ="Low" then 2
                when tf4.rateSelfKnowledgeBefore_5 ="Very Low" then 1
                when tf4.rateSelfKnowledgeBefore_5 ="N/A" then 0
                END AS rateSelfKnowledgeBefore_5,

                case 
                when tf4.rateSelfKnowledgeAfter_5 ="Very High" then 5
                when tf4.rateSelfKnowledgeAfter_5 ="High" then 4
                when tf4.rateSelfKnowledgeAfter_5 ="Neutral" or tf4.rateSelfKnowledgeAfter_5="Nuetral" then 3
                when tf4.rateSelfKnowledgeAfter_5 ="Low" then 2
                when tf4.rateSelfKnowledgeAfter_5 ="Very Low" then 1
                when tf4.rateSelfKnowledgeAfter_5 ="N/A" then 0
                END AS rateSelfKnowledgeAfter_5,
         
                case 
                when tf4.taskDifficulty ="Strongly Agree" then 5
                when tf4.taskDifficulty ="Agree" then 4
                when tf4.taskDifficulty ="Neutral" or tf4.taskDifficulty="Nuetral" then 3
                when tf4.taskDifficulty ="Disagree" then 2
                when tf4.taskDifficulty ="Strongly Disagree" then 1
                END AS taskDifficulty,
                
                case 
                when tf4.rateMember1 ="Strongly Agree" then 5
                when tf4.rateMember1 ="Agree" then 4
                when tf4.rateMember1 ="Neutral" or tf4.rateMember1="Nuetral" then 3
                when tf4.rateMember1 ="Disagree" then 2
                when tf4.rateMember1 ="Strongly Disagree" then 1
                END AS rateMember1,
                
                case 
                when tf4.rateMember2 ="Strongly Agree" then 5
                when tf4.rateMember2 ="Agree" then 4
                when tf4.rateMember2 ="Neutral" or tf4.rateMember2="Nuetral" then 3
                when tf4.rateMember2 ="Disagree" then 2
                when tf4.rateMember2 ="Strongly Disagree" then 1
                END AS rateMember2,
                
                case 
                when tf4.rateMember3 ="Strongly Agree" then 5
                when tf4.rateMember3 ="Agree" then 4
                when tf4.rateMember3 ="Neutral" or tf4.rateMember3="Nuetral" then 3
                when tf4.rateMember3 ="Disagree" then 2
                when tf4.rateMember3 ="Strongly Disagree" then 1
                END AS rateMember3,

                case 
                when tf4.confidentToFinish ="Strongly Agree" then 5
                when tf4.confidentToFinish ="Agree" then 4
                when tf4.confidentToFinish ="Neutral" or tf4.confidentToFinish="Nuetral" then 3
                when tf4.confidentToFinish ="Disagree" then 2
                when tf4.confidentToFinish ="Strongly Disagree" then 1
                END AS confidentToFinish

                FROM task4_feedback tf4"""

task4_feedbackSelect_legend = {
    'taskEasiness': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'taskEasiness_b': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'taskEasiness_c': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateTaskDifficulty': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'sessionHelpfulness': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateSelfContribution': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateResources': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateForumUsefulness': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateSelfContributionSatisfaction': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateTeamContributionSatisfaction': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'ratePreviousTaskFeedback': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateSelfKnowledgeBefore_1': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeAfter_1': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeBefore_2': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeAfter_2': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeBefore_3': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeAfter_3': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeBefore_4': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeAfter_4': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeBefore_5': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeAfter_5': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'taskDifficulty': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateMember1': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateMember2': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateMember3': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'confidentToFinish': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    }
}

task5_feedbackSelect = """SELECT tf5.theme,
                case 
                when tf5.rateTask5 ="Strongly Agree" then 5
                when tf5.rateTask5 ="Agree" then 4
                when tf5.rateTask5 ="Neutral" or tf5.rateTask5="Nuetral" then 3
                when tf5.rateTask5 ="Disagree" then 2
                when tf5.rateTask5 ="Strongly Disagree" then 1
                END AS rateTask5,
                
                case 
                when tf5.rateTask5Design ="Strongly Agree" then 5
                when tf5.rateTask5Design ="Agree" then 4
                when tf5.rateTask5Design ="Neutral" or tf5.rateTask5Design="Nuetral" then 3
                when tf5.rateTask5Design ="Disagree" then 2
                when tf5.rateTask5Design ="Strongly Disagree" then 1
                END AS rateTask5Design,
                
                case 
                when tf5.rateCollaboration ="Strongly Agree" then 5
                when tf5.rateCollaboration ="Agree" then 4
                when tf5.rateCollaboration ="Neutral" or tf5.rateCollaboration="Nuetral" then 3
                when tf5.rateCollaboration ="Disagree" then 2
                when tf5.rateCollaboration ="Strongly Disagree" then 1
                END AS rateCollaboration,
                
                case 
                when tf5.rateSelfContribution ="Very High" then 5
                when tf5.rateSelfContribution ="High" then 4
                when tf5.rateSelfContribution ="Neutral" or tf5.rateSelfContribution="Nuetral" then 3
                when tf5.rateSelfContribution ="Low" then 2
                when tf5.rateSelfContribution ="Very Low" then 1
                when tf5.rateSelfContribution ="N/A" then 0
                END AS rateSelfContribution,
                
                case 
                when tf5.rateGrader ="Strongly Agree" then 5
                when tf5.rateGrader ="Agree" then 4
                when tf5.rateGrader ="Neutral" or tf5.rateGrader="Nuetral" then 3
                when tf5.rateGrader ="Disagree" then 2
                when tf5.rateGrader ="Strongly Disagree" then 1
                END AS rateGrader,
                
                case 
                when tf5.rateResource ="Very High" then 5
                when tf5.rateResource ="High" then 4
                when tf5.rateResource ="Neutral" or tf5.rateResource="Nuetral" then 3
                when tf5.rateResource ="Low" then 2
                when tf5.rateResource ="Very Low" then 1
                when tf5.rateResource ="N/A" then 0
                END AS rateResource,
                
                case 
                when tf5.rateEffectiveness ="Strongly Agree" then 5
                when tf5.rateEffectiveness ="Agree" then 4
                when tf5.rateEffectiveness ="Neutral" or tf5.rateEffectiveness="Nuetral" then 3
                when tf5.rateEffectiveness ="Disagree" then 2
                when tf5.rateEffectiveness ="Strongly Disagree" then 1
                END AS rateEffectiveness,
                
                case 
                when tf5.referredResources ="Strongly Agree" then 5
                when tf5.referredResources ="Agree" then 4
                when tf5.referredResources ="Neutral" or tf5.referredResources="Nuetral" then 3
                when tf5.referredResources ="Disagree" then 2
                when tf5.referredResources ="Strongly Disagree" then 1
                END AS referredResources,
                
                case 
                when tf5.rateDifficulty_1 ="Strongly Agree" then 5
                when tf5.rateDifficulty_1 ="Agree" then 4
                when tf5.rateDifficulty_1 ="Neutral" or tf5.rateDifficulty_1="Nuetral" then 3
                when tf5.rateDifficulty_1 ="Disagree" then 2
                when tf5.rateDifficulty_1 ="Strongly Disagree" then 1
                END AS rateDifficulty_1,
                
                case 
                when tf5.rateDifficulty_2 ="Strongly Agree" then 5
                when tf5.rateDifficulty_2 ="Agree" then 4
                when tf5.rateDifficulty_2 ="Neutral" or tf5.rateDifficulty_2="Nuetral" then 3
                when tf5.rateDifficulty_2 ="Disagree" then 2
                when tf5.rateDifficulty_2 ="Strongly Disagree" then 1
                END AS rateDifficulty_2,
                
                case 
                when tf5.rateSelfKnowledgeBefore_1 ="Very High" then 5
                when tf5.rateSelfKnowledgeBefore_1 ="High" then 4
                when tf5.rateSelfKnowledgeBefore_1 ="Neutral" or tf5.rateSelfKnowledgeBefore_1="Nuetral" then 3
                when tf5.rateSelfKnowledgeBefore_1 ="Low" then 2
                when tf5.rateSelfKnowledgeBefore_1 ="Very Low" then 1
                when tf5.rateSelfKnowledgeBefore_1 ="N/A" then 0
                END AS rateSelfKnowledgeBefore_1,
                
                case 
                when tf5.rateSelfKnowledgeAfter_1 ="Very High" then 5
                when tf5.rateSelfKnowledgeAfter_1 ="High" then 4
                when tf5.rateSelfKnowledgeAfter_1 ="Neutral" or tf5.rateSelfKnowledgeAfter_1="Nuetral" then 3
                when tf5.rateSelfKnowledgeAfter_1 ="Low" then 2
                when tf5.rateSelfKnowledgeAfter_1 ="Very Low" then 1
                when tf5.rateSelfKnowledgeAfter_1 ="N/A" then 0
                END AS rateSelfKnowledgeAfter_1,
                
                case 
                when tf5.rateSelfKnowledgeBefore_2 ="Very High" then 5
                when tf5.rateSelfKnowledgeBefore_2 ="High" then 4
                when tf5.rateSelfKnowledgeBefore_2 ="Neutral" or tf5.rateSelfKnowledgeBefore_2="Nuetral" then 3
                when tf5.rateSelfKnowledgeBefore_2 ="Low" then 2
                when tf5.rateSelfKnowledgeBefore_2 ="Very Low" then 1
                when tf5.rateSelfKnowledgeBefore_2 ="N/A" then 0
                END AS rateSelfKnowledgeBefore_2,
                
                case 
                when tf5.rateSelfKnowledgeAfter_2 ="Very High" then 5
                when tf5.rateSelfKnowledgeAfter_2 ="High" then 4
                when tf5.rateSelfKnowledgeAfter_2 ="Neutral" or tf5.rateSelfKnowledgeAfter_2="Nuetral" then 3
                when tf5.rateSelfKnowledgeAfter_2 ="Low" then 2
                when tf5.rateSelfKnowledgeAfter_2 ="Very Low" then 1
                when tf5.rateSelfKnowledgeAfter_2 ="N/A" then 0
                END AS rateSelfKnowledgeAfter_2,
                
                case 
                when tf5.rateSelfKnowledgeBefore_3 ="Very High" then 5
                when tf5.rateSelfKnowledgeBefore_3 ="High" then 4
                when tf5.rateSelfKnowledgeBefore_3 ="Neutral" or tf5.rateSelfKnowledgeBefore_3="Nuetral" then 3
                when tf5.rateSelfKnowledgeBefore_3 ="Low" then 2
                when tf5.rateSelfKnowledgeBefore_3 ="Very Low" then 1
                when tf5.rateSelfKnowledgeBefore_3 ="N/A" then 0
                END AS rateSelfKnowledgeBefore_3,
                
                case 
                when tf5.rateSelfKnowledgeAfter_3 ="Very High" then 5
                when tf5.rateSelfKnowledgeAfter_3 ="High" then 4
                when tf5.rateSelfKnowledgeAfter_3 ="Neutral" or tf5.rateSelfKnowledgeAfter_3="Nuetral" then 3
                when tf5.rateSelfKnowledgeAfter_3 ="Low" then 2
                when tf5.rateSelfKnowledgeAfter_3 ="Very Low" then 1
                when tf5.rateSelfKnowledgeAfter_3 ="N/A" then 0
                END AS rateSelfKnowledgeAfter_3,
         
                case 
                when tf5.rateDifficulty_3 ="Strongly Agree" then 5
                when tf5.rateDifficulty_3 ="Agree" then 4
                when tf5.rateDifficulty_3 ="Neutral" or tf5.rateDifficulty_3="Nuetral" then 3
                when tf5.rateDifficulty_3 ="Disagree" then 2
                when tf5.rateDifficulty_3 ="Strongly Disagree" then 1
                END AS rateDifficulty_3,
                
                case 
                when tf5.rateTaskRemarks ="Strongly Agree" then 5
                when tf5.rateTaskRemarks ="Agree" then 4
                when tf5.rateTaskRemarks ="Neutral" or tf5.rateTaskRemarks="Nuetral" then 3
                when tf5.rateTaskRemarks ="Disagree" then 2
                when tf5.rateTaskRemarks ="Strongly Disagree" then 1
                END AS rateTaskRemarks,
                
                case 
                when tf5.rateForumUsefulness ="Strongly Agree" then 5
                when tf5.rateForumUsefulness ="Agree" then 4
                when tf5.rateForumUsefulness ="Neutral" or tf5.rateForumUsefulness="Nuetral" then 3
                when tf5.rateForumUsefulness ="Disagree" then 2
                when tf5.rateForumUsefulness ="Strongly Disagree" then 1
                END AS rateForumUsefulness,
                
                case 
                when tf5.rateLiveSessionUsefulness ="Strongly Agree" then 5
                when tf5.rateLiveSessionUsefulness ="Agree" then 4
                when tf5.rateLiveSessionUsefulness ="Neutral" or tf5.rateLiveSessionUsefulness="Nuetral" then 3
                when tf5.rateLiveSessionUsefulness ="Disagree" then 2
                when tf5.rateLiveSessionUsefulness ="Strongly Disagree" then 1
                END AS rateLiveSessionUsefulness,

                case 
                when tf5.rateMantraSession ="Strongly Agree" then 5
                when tf5.rateMantraSession ="Agree" then 4
                when tf5.rateMantraSession ="Neutral" or tf5.rateMantraSession="Nuetral" then 3
                when tf5.rateMantraSession ="Disagree" then 2
                when tf5.rateMantraSession ="Strongly Disagree" then 1
                END AS rateMantraSession,

                case 
                when tf5.rateTask4ProgressUsefulness ="Strongly Agree" then 5
                when tf5.rateTask4ProgressUsefulness ="Agree" then 4
                when tf5.rateTask4ProgressUsefulness ="Neutral" or tf5.rateTask4ProgressUsefulness="Nuetral" then 3
                when tf5.rateTask4ProgressUsefulness ="Disagree" then 2
                when tf5.rateTask4ProgressUsefulness ="Strongly Disagree" then 1
                END AS rateTask4ProgressUsefulness

                FROM task5_feedback tf5"""

task5_feedbackSelect_legend = {
    'rateTask5': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateTask5Design': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateCollaboration': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateSelfContribution': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateGrader': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateResource': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateEffectiveness': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'referredResources': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateDifficulty_1': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateDifficulty_2': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateSelfKnowledgeBefore_1': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeAfter_1': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeBefore_2': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeAfter_2': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeBefore_3': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateSelfKnowledgeAfter_3': {
        5:'Very High',
        4:'High',
        3:'Neutral',
        2:'Low',
        1:'Very Low',
    },
    'rateDifficulty_3': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateTaskRemarks': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateForumUsefulness': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateLiveSessionUsefulness': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateMantraSession': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateTask4ProgressUsefulness': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    }
}

stage1_feedbackSelect_1 = """SELECT s1.theme,
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

stage1_feedbackSelect_1_legend = {
    'rateThemeEasiness': {
            5:'Very Easy',
            4:'Easy',
            3:'Neutral',
            2:'Difficult',
            1:'Very Difficult',
        },
    'rateTaskProblemStatement': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateTaskDifficulty': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateTasksHelpfulness': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateTaskResources': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateTaskHosting': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'externalResourses': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    }   
}

stage1_feedbackSelect_2 = """SELECT s1.theme,
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

stage1_feedbackSelect_2_legend = {
    'discourseHelpfulness': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'discourseInstructorResponse': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'discourseStudentResponse': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'discoursePosts': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'discoursePolls': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    }
}

stage1_feedbackSelect_3 = """SELECT s1.theme,
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

stage1_feedbackSelect_3_legend = {
    'teamOrindividual': {
        4:'4-member Team',
        3:'3-member Team',
        2:'2-member Team',
        1:'Individual',
        0:'NAN'
    },
    'rateCollaborativeSkillsBefore': {
        5:'5-Points',
        4:'4-Points',
        3:'3-Points',
        2:'2-Points',
        1:'1-Point',
        0:'NAN'
    },
    'rateCollaborativeSkillsAfter': {
        5:'5-Points',
        4:'4-Points',
        3:'3-Points',
        2:'2-Points',
        1:'1-Point',
        0:'NAN'
    },
    'rateSelfLearningSkillsBefore': {
        5:'5-Points',
        4:'4-Points',
        3:'3-Points',
        2:'2-Points',
        1:'1-Point',
        0:'NAN'
    },
    'rateSelfLearningSkillsAfter': {
        5:'5-Points',
        4:'4-Points',
        3:'3-Points',
        2:'2-Points',
        1:'1-Point',
        0:'NAN'
    },
    'ratePeerLearningBefore': {
        5:'5-Points',
        4:'4-Points',
        3:'3-Points',
        2:'2-Points',
        1:'1-Point',
        0:'NAN'
    },
    'ratePeerLearningAfter': {
        5:'5-Points',
        4:'4-Points',
        3:'3-Points',
        2:'2-Points',
        1:'1-Point',
        0:'NAN'
    },
    'rateHandsOnSkillsBefore': {
        5:'5-Points',
        4:'4-Points',
        3:'3-Points',
        2:'2-Points',
        1:'1-Point',
        0:'NAN'
    },
    'rateHandsOnSkillsAfter': {
        5:'5-Points',
        4:'4-Points',
        3:'3-Points',
        2:'2-Points',
        1:'1-Point',
        0:'NAN'
    }
}

stage1_feedbackSelect_4 = """SELECT s1.theme,
case 
when s1.covidCase ="No" then 1
when s1.covidCase ="Yes" then 2
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
when s1.rateFeeWorth ="No" then 1
when s1.rateFeeWorth ="Yes" then 2
END AS rateFeeWorth
FROM stage1_feedback s1"""

stage1_feedbackSelect_4_legend = {
    'covidCase': {
        2:'Yes',
        1:'No',
        0:'NAN'
    },
    'rateThemeDesign': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'timeSpendEyrc': {
        6:'> 60 hours',
        5:'48-60 hours',
        4:'36-48 hours', 
        3:'24-36 hours', 
        2:'12-24 hours', 
        1:'< 12 hours',
        0:'NAN'
    },
    'timeSpendAcademics': {
        6:'> 60 hours',
        5:'48-60 hours',
        4:'36-48 hours', 
        3:'24-36 hours', 
        2:'12-24 hours', 
        1:'< 12 hours',
        0:'NAN'
    },
    'timeSpendRecreation': {
        6:'> 60 hours',
        5:'48-60 hours',
        4:'36-48 hours', 
        3:'24-36 hours', 
        2:'12-24 hours', 
        1:'< 12 hours',
        0:'NAN'
    },
    'timeSpendOther': {
        6:'> 60 hours',
        5:'48-60 hours',
        4:'36-48 hours', 
        3:'24-36 hours', 
        2:'12-24 hours', 
        1:'< 12 hours'
    },
    'nonPandemicSelfContribution': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'nonPandemicLearning': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'nonPandemicFocus': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'nonPandemicTaskManagement': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateFeeWorth': {
        2:'Yes',
        1:'No',
        0:'NAN'
    }
}

stage2_feedbackSelect_1 = """SELECT s2.theme,
case 
when s2.rateThemeEasiness ="Very Easy" then 5
when s2.rateThemeEasiness ="Easy" then 4
when s2.rateThemeEasiness ="Neutral" or s2.rateThemeEasiness="Nuetral" then 3
when s2.rateThemeEasiness ="Difficult" then 2
when s2.rateThemeEasiness ="Very Difficult" then 1
END AS rateThemeEasiness,
case 
when s2.rateTaskProblemStatement ="Strongly Agree" then 5
when s2.rateTaskProblemStatement ="Agree" then 4
when s2.rateTaskProblemStatement ="Neutral" or s2.rateTaskProblemStatement="Nuetral" then 3
when s2.rateTaskProblemStatement ="Disagree" then 2
when s2.rateTaskProblemStatement ="Strongly Disagree" then 1
END AS rateTaskProblemStatement,
case 
when s2.rateTaskDifficulty ="Strongly Agree" then 5
when s2.rateTaskDifficulty ="Agree" then 4
when s2.rateTaskDifficulty ="Neutral" or s2.rateTaskDifficulty="Nuetral" then 3
when s2.rateTaskDifficulty ="Disagree" then 2
when s2.rateTaskDifficulty ="Strongly Disagree" then 1
END AS rateTaskDifficulty,
case 
when s2.rateTasksHelpfulness ="Strongly Agree" then 5
when s2.rateTasksHelpfulness ="Agree" then 4
when s2.rateTasksHelpfulness ="Neutral" or s2.rateTasksHelpfulness="Nuetral" then 3
when s2.rateTasksHelpfulness ="Disagree" then 2
when s2.rateTasksHelpfulness ="Strongly Disagree" then 1
END AS rateTasksHelpfulness,
case 
when s2.rateTaskResources ="Strongly Agree" then 5
when s2.rateTaskResources ="Agree" then 4
when s2.rateTaskResources ="Neutral" or s2.rateTaskResources="Nuetral" then 3
when s2.rateTaskResources ="Disagree" then 2
when s2.rateTaskResources ="Strongly Disagree" then 1
END AS rateTaskResources,
case 
when s2.rateTaskHosting ="Strongly Agree" then 5
when s2.rateTaskHosting ="Agree" then 4
when s2.rateTaskHosting ="Neutral" or s2.rateTaskHosting="Nuetral" then 3
when s2.rateTaskHosting ="Disagree" then 2
when s2.rateTaskHosting ="Strongly Disagree" then 1
END AS rateTaskHosting,
case 
when s2.externalResourses ="Strongly Agree" then 5
when s2.externalResourses ="Agree" then 4
when s2.externalResourses ="Neutral" or s2.externalResourses="Nuetral" then 3
when s2.externalResourses ="Disagree" then 2
when s2.externalResourses ="Strongly Disagree" then 1
END AS externalResourses
FROM stage2_feedback s2"""

stage2_feedbackSelect_1_legend = {
    'rateThemeEasiness': {
            5:'Very Easy',
            4:'Easy',
            3:'Neutral',
            2:'Difficult',
            1:'Very Difficult',
        },
    'rateTaskProblemStatement': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateTaskDifficulty': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateTasksHelpfulness': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateTaskResources': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateTaskHosting': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'externalResourses': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    }   
}

stage2_feedbackSelect_2 = """SELECT s2.theme,
case 
when s2.discourseHelpfulness ="Strongly Agree" then 5
when s2.discourseHelpfulness ="Agree" then 4
when s2.discourseHelpfulness ="Neutral" or s2.discourseHelpfulness="Nuetral" then 3
when s2.discourseHelpfulness ="Disagree" then 2
when s2.discourseHelpfulness ="Strongly Disagree" then 1
END AS discourseHelpfulness,
case 
when s2.discourseInstructorResponse ="Strongly Agree" then 5
when s2.discourseInstructorResponse ="Agree" then 4
when s2.discourseInstructorResponse ="Neutral" or s2.discourseInstructorResponse="Nuetral" then 3
when s2.discourseInstructorResponse ="Disagree" then 2
when s2.discourseInstructorResponse ="Strongly Disagree" then 1
END AS discourseInstructorResponse,
case 
when s2.discourseStudentResponse ="Strongly Agree" then 5
when s2.discourseStudentResponse ="Agree" then 4
when s2.discourseStudentResponse ="Neutral" or s2.discourseStudentResponse="Nuetral" then 3
when s2.discourseStudentResponse ="Disagree" then 2
when s2.discourseStudentResponse ="Strongly Disagree" then 1
END AS discourseStudentResponse,
case 
when s2.discoursePosts ="Strongly Agree" then 5
when s2.discoursePosts ="Agree" then 4
when s2.discoursePosts ="Neutral" or s2.discoursePosts="Nuetral" then 3
when s2.discoursePosts ="Disagree" then 2
when s2.discoursePosts ="Strongly Disagree" then 1
END AS discoursePosts
FROM stage2_feedback s2"""

stage2_feedbackSelect_2_legend = {
    'discourseHelpfulness': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'discourseInstructorResponse': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'discourseStudentResponse': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'discoursePosts': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    }
}

stage2_feedbackSelect_3 = """SELECT s2.theme,
case 
when s2.teamOrindividual ="4-member Team" then 4
when s2.teamOrindividual ="3-member Team" then 3
when s2.teamOrindividual ="2-member Team" then 2
when s2.teamOrindividual ="Individual" then 1
END AS teamOrindividual,
case 
when s2.rateCollaborativeSkillsBefore ="5" then 5
when s2.rateCollaborativeSkillsBefore ="4" then 4
when s2.rateCollaborativeSkillsBefore ="3" then 3
when s2.rateCollaborativeSkillsBefore ="2" then 2
when s2.rateCollaborativeSkillsBefore ="1" then 1
END AS rateCollaborativeSkillsBefore,
case 
when s2.rateCollaborativeSkillsAfter ="5" then 5
when s2.rateCollaborativeSkillsAfter ="4" then 4
when s2.rateCollaborativeSkillsAfter ="3" then 3
when s2.rateCollaborativeSkillsAfter ="2" then 2
when s2.rateCollaborativeSkillsAfter ="1" then 1
END AS rateCollaborativeSkillsAfter,
case 
when s2.rateSelfLearningSkillsBefore ="5" then 5
when s2.rateSelfLearningSkillsBefore ="4" then 4
when s2.rateSelfLearningSkillsBefore ="3" then 3
when s2.rateSelfLearningSkillsBefore ="2" then 2
when s2.rateSelfLearningSkillsBefore ="1" then 1
END AS rateSelfLearningSkillsBefore,
case 
when s2.rateSelfLearningSkillsAfter ="5" then 5
when s2.rateSelfLearningSkillsAfter ="4" then 4
when s2.rateSelfLearningSkillsAfter ="3" then 3
when s2.rateSelfLearningSkillsAfter ="2" then 2
when s2.rateSelfLearningSkillsAfter ="1" then 1
END AS rateSelfLearningSkillsAfter,
case 
when s2.ratePeerLearningBefore ="5" then 5
when s2.ratePeerLearningBefore ="4" then 4
when s2.ratePeerLearningBefore ="3" then 3
when s2.ratePeerLearningBefore ="2" then 2
when s2.ratePeerLearningBefore ="1" then 1
END AS ratePeerLearningBefore,
case 
when s2.ratePeerLearningAfter ="5" then 5
when s2.ratePeerLearningAfter ="4" then 4
when s2.ratePeerLearningAfter ="3" then 3
when s2.ratePeerLearningAfter ="2" then 2
when s2.ratePeerLearningAfter ="1" then 1
END AS ratePeerLearningAfter,
case 
when s2.rateHandsOnSkillsBefore ="5" then 5
when s2.rateHandsOnSkillsBefore ="4" then 4
when s2.rateHandsOnSkillsBefore ="3" then 3
when s2.rateHandsOnSkillsBefore ="2" then 2
when s2.rateHandsOnSkillsBefore ="1" then 1
END AS rateHandsOnSkillsBefore,
case 
when s2.rateHandsOnSkillsAfter ="5" then 5
when s2.rateHandsOnSkillsAfter ="4" then 4
when s2.rateHandsOnSkillsAfter ="3" then 3
when s2.rateHandsOnSkillsAfter ="2" then 2
when s2.rateHandsOnSkillsAfter ="1" then 1
END AS rateHandsOnSkillsAfter
FROM stage2_feedback s2"""
stage2_feedbackSelect_3_legend = {
    'teamOrindividual': {
        4:'4-member Team',
        3:'3-member Team',
        2:'2-member Team',
        1:'Individual',
        0:'NAN'
    },
    'rateCollaborativeSkillsBefore': {
        5:'5-Points',
        4:'4-Points',
        3:'3-Points',
        2:'2-Points',
        1:'1-Point',
        0:'NAN'
    },
    'rateCollaborativeSkillsAfter': {
        5:'5-Points',
        4:'4-Points',
        3:'3-Points',
        2:'2-Points',
        1:'1-Point',
        0:'NAN'
    },
    'rateSelfLearningSkillsBefore': {
        5:'5-Points',
        4:'4-Points',
        3:'3-Points',
        2:'2-Points',
        1:'1-Point',
        0:'NAN'
    },
    'rateSelfLearningSkillsAfter': {
        5:'5-Points',
        4:'4-Points',
        3:'3-Points',
        2:'2-Points',
        1:'1-Point',
        0:'NAN'
    },
    'ratePeerLearningBefore': {
        5:'5-Points',
        4:'4-Points',
        3:'3-Points',
        2:'2-Points',
        1:'1-Point',
        0:'NAN'
    },
    'ratePeerLearningAfter': {
        5:'5-Points',
        4:'4-Points',
        3:'3-Points',
        2:'2-Points',
        1:'1-Point',
        0:'NAN'
    },
    'rateHandsOnSkillsBefore': {
        5:'5-Points',
        4:'4-Points',
        3:'3-Points',
        2:'2-Points',
        1:'1-Point',
        0:'NAN'
    },
    'rateHandsOnSkillsAfter': {
        5:'5-Points',
        4:'4-Points',
        3:'3-Points',
        2:'2-Points',
        1:'1-Point',
        0:'NAN'
    }
}

stage2_feedbackSelect_4 = """SELECT s2.theme,
case 
when s2.covidCase ="No" then 1
when s2.covidCase ="Yes" then 2
END AS covidCase,
case 
when s2.rateThemeDesign ="Strongly Agree" then 5
when s2.rateThemeDesign ="Agree" then 4
when s2.rateThemeDesign ="Neutral" or s2.rateThemeDesign="Nuetral" then 3
when s2.rateThemeDesign ="Disagree" then 2
when s2.rateThemeDesign ="Strongly Disagree" then 1
END AS rateThemeDesign,
case 
when s2.timeSpendEyrc ="less than 12 hours" then 1
when s2.timeSpendEyrc ="12-24 hours" then 2
when s2.timeSpendEyrc ="24-36 hours" then 3
when s2.timeSpendEyrc ="36-48 hours" then 4
when s2.timeSpendEyrc ="48-60 hours" then 5
when s2.timeSpendEyrc ="more than 60 hours" then 6
END AS timeSpendEyrc,
case 
when s2.timeSpendAcademics ="less than 12 hours" then 1
when s2.timeSpendAcademics ="12-24 hours" then 2
when s2.timeSpendAcademics ="24-36 hours" then 3
when s2.timeSpendAcademics ="36-48 hours" then 4
when s2.timeSpendAcademics ="48-60 hours" then 5
when s2.timeSpendAcademics ="more than 60 hours" then 6
END AS timeSpendAcademics,
case 
when s2.timeSpendRecreation ="less than 12 hours" then 1
when s2.timeSpendRecreation ="12-24 hours" then 2
when s2.timeSpendRecreation ="24-36 hours" then 3
when s2.timeSpendRecreation ="36-48 hours" then 4
when s2.timeSpendRecreation ="48-60 hours" then 5
when s2.timeSpendRecreation ="more than 60 hours" then 6
END AS timeSpendRecreation,
case 
when s2.timeSpendOther ="less than 12 hours" then 1
when s2.timeSpendOther ="12-24 hours" then 2
when s2.timeSpendOther ="24-36 hours" then 3
when s2.timeSpendOther ="36-48 hours" then 4
when s2.timeSpendOther ="48-60 hours" then 5
when s2.timeSpendOther ="more than 60 hours" then 6
END AS timeSpendOther,
case 
when s2.nonPandemicSelfContribution ="Strongly Agree" then 5
when s2.nonPandemicSelfContribution ="Agree" then 4
when s2.nonPandemicSelfContribution ="Neutral" or s2.nonPandemicSelfContribution="Nuetral" then 3
when s2.nonPandemicSelfContribution ="Disagree" then 2
when s2.nonPandemicSelfContribution ="Strongly Disagree" then 1
END AS nonPandemicSelfContribution,
case 
when s2.nonPandemicLearning ="Strongly Agree" then 5
when s2.nonPandemicLearning ="Agree" then 4
when s2.nonPandemicLearning ="Neutral" or s2.nonPandemicLearning="Nuetral" then 3
when s2.nonPandemicLearning ="Disagree" then 2
when s2.nonPandemicLearning ="Strongly Disagree" then 1
END AS nonPandemicLearning,
case 
when s2.nonPandemicFocus ="Strongly Agree" then 5
when s2.nonPandemicFocus ="Agree" then 4
when s2.nonPandemicFocus ="Neutral" or s2.nonPandemicFocus="Nuetral" then 3
when s2.nonPandemicFocus ="Disagree" then 2
when s2.nonPandemicFocus ="Strongly Disagree" then 1
END AS nonPandemicFocus,
case 
when s2.nonPandemicTaskManagement ="Strongly Agree" then 5
when s2.nonPandemicTaskManagement ="Agree" then 4
when s2.nonPandemicTaskManagement ="Neutral" or s2.nonPandemicTaskManagement="Nuetral" then 3
when s2.nonPandemicTaskManagement ="Disagree" then 2
when s2.nonPandemicTaskManagement ="Strongly Disagree" then 1
END AS nonPandemicTaskManagement,
case 
when s2.rateFeeWorth ="No" then 1
when s2.rateFeeWorth ="Yes" then 2
END AS rateFeeWorth
FROM stage2_feedback s2"""
stage2_feedbackSelect_4_legend = {
    'covidCase': {
        2:'Yes',
        1:'No',
        0:'NAN'
    },
    'rateThemeDesign': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'timeSpendEyrc': {
        6:'> 60 hours',
        5:'48-60 hours',
        4:'36-48 hours', 
        3:'24-36 hours', 
        2:'12-24 hours', 
        1:'< 12 hours',
        0:'NAN'
    },
    'timeSpendAcademics': {
        6:'> 60 hours',
        5:'48-60 hours',
        4:'36-48 hours', 
        3:'24-36 hours', 
        2:'12-24 hours', 
        1:'< 12 hours',
        0:'NAN'
    },
    'timeSpendRecreation': {
        6:'> 60 hours',
        5:'48-60 hours',
        4:'36-48 hours', 
        3:'24-36 hours', 
        2:'12-24 hours', 
        1:'< 12 hours',
        0:'NAN'
    },
    'timeSpendOther': {
        6:'> 60 hours',
        5:'48-60 hours',
        4:'36-48 hours', 
        3:'24-36 hours', 
        2:'12-24 hours', 
        1:'< 12 hours'
    },
    'nonPandemicSelfContribution': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'nonPandemicLearning': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'nonPandemicFocus': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'nonPandemicTaskManagement': {
        5:'Strongly Agree',
        4:'Agree',
        3:'Neutral',
        2:'Disagree',
        1:'Strongly Disagree',
        0:'NAN'
    },
    'rateFeeWorth': {
        2:'Yes',
        1:'No',
        0:'NAN'
    }
}