from jira import JIRA

def save_tasks(dateTasks):
    jira = JIRA(server='https://dit.rencredit.ru/jira', basic_auth=('ext_azhuravlev2', '**'), validate=True)
    for task in dateTasks:
        jira.add_worklog(task.task)

    return None