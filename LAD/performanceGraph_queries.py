def performanceQueries(theme, task, sub_task):
    print(theme, task, sub_task)
    # if int(task) == 0:
    # if int(task)
    query = {
        0: """ SELECT theme, marks from task0_status where theme = '{}' """.format(theme, task),
        1: """ SELECT theme, marks, task1_number from task1_status where theme = '{}' and task1_number = '{}' """.format(theme, task),
        2: """ SELECT theme, marks, task2_number from task2_status where theme = '{}' and task2_number = '{}' """.format(theme, task),
        3: """ SELECT theme, marks, penalty, task3_number from task3_status where theme = '{}' and task3_number = '{}' """.format(theme, task),
        4: """ SELECT theme, marks, penalty, task4_number from task4_status where theme = '{}' and task1_number = '{}' """.format(theme, task),
        5: """ SELECT theme, marks, penalty, task5_number from task5_status where theme = '{}' and task1_number = '{}' """.format(theme, task),
        6: """ SELECT theme, marks, penalty, task6_number from task6_status where theme = '{}' and task1_number = '{}' """.format(theme, task)
    }
    return query[task]
    # task_0 = """ SELECT theme, marks from task0_status where theme = '{}' """.format(theme, task_num)
    # task_1 = """ SELECT theme, marks, task1_number from task1_status where theme = '{}' and task1_number = '{}' """.format(theme, task_num)
    # task_2 = """ SELECT theme, marks, task2_number from task2_status where theme = '{}' and task2_number = '{}' """.format(theme, task_num)
    # task_3 = """ SELECT theme, marks, penalty, task3_number from task3_status where theme = '{}' and task3_number = '{}' """.format(theme, task_num)
    # task_4 = """ SELECT theme, marks, penalty, task4_number from task4_status where theme = '{}' and task1_number = '{}' """.format(theme, task_num)
    # task_5 = """ SELECT theme, marks, penalty, task5_number from task5_status where theme = '{}' and task1_number = '{}' """.format(theme, task_num)
    # task_6 = """ SELECT theme, marks, penalty, task6_number from task6_status where theme = '{}' and task1_number = '{}' """.format(theme, task_num)
    # task_7 = """ SELECT theme, marks, penalty, task7_number from task7_status where theme = '{}' """.format(theme)

#    return (""" SELECT 
                # theme, 
                # task0_marks,
                # task0_penalty,
                # task1a_marks,
                # task1a_penalty,
                # task1b_marks,
                # task1b_penalty,
                # task1c_marks,
                # task1c_penalty,
                # task2a_marks,
                # task2a_penalty,
                # task2b_marks,
                # task2b_penalty,
                # task3_marks,
                # task3_penalty,
                # task4a_marks,
                # task4a_penalty,
                # task4b_marks,
                # task4b_penalty,
                # task4c_marks,
                # task4c_penalty,
                # task5_marks,
                # task5_penalty,
                # task6_original_marks,
                # task6_original_penalty,
                # task6_bonus_marks,
                # task6_bonus_penalty,
                # task6_code_marks,
                # task6_code_penalty
                # from team_grades 
                # where theme = '{}'""".format(theme))