import xlwt

from jira import JIRA


def search_issues_and_reassign():
    all_my_issues = jira.search_issues('project=CRB and assignee = currentUser()')
    for my_issue in all_my_issues:
        if my_issue.fields.customfield_11401 == 'REL-204 [LO.74]':
            print(my_issue.key + ': ' + my_issue.fields.summary + ' Статус: ' + my_issue.fields.status.name + ' Owner: ' + my_issue.fields.customfield_11401)
            # jira.assign_issue(my_issue, None)


def save_issues_to_file(issues):
    font0 = xlwt.Font()
    font0.name = 'Times New Roman'
    font0.colour_index = 2
    font0.bold = True

    style0 = xlwt.XFStyle()
    style0.font = font0

    wb = xlwt.Workbook()
    ws = wb.add_sheet('REL TASKS')

    ws.write(0, 0, 'TASK', style0)
    ws.write(0, 1, 'SUMMARY', style0)
    str_number = 1
    for save_issue in issues:
        ws.write(str_number, 0, save_issue.key)
        ws.write(str_number, 1, save_issue.fields.summary)
        str_number += 1

    wb.save('example.xls')


def get_inside_issues(issue_key):
    inside_issues = []
    issue = jira.issue(issue_key)
    issue_type_id = insideIssue.fields.issuetype.id
    for issue_link in issue.fields.issuelinks:
        # if issue.fields.project.key == 'REL' or issue.fields.project.key == 'BRF':

        if hasattr(issue_link, 'outwardIssue') and issue_type_id == 10003:
            inside_issue = issue_link.outwardIssue
            inside_issues.append(inside_issue)

    return inside_issues


def get_outside_issues(issue_key):
    inside_issues = []
    issue = jira.issue(issue_key)
    for issue_link in issue.fields.issuelinks:
        if hasattr(issue_link, 'outwardIssue'):
            inside_issue = issue_link.outwardIssue
        else:
            inside_issue = issue_link.inwardIssue

        inside_issues.append(inside_issue)
    return inside_issues


def check_in_our_project(check_issue):
    for project in OUR_PROJECTS:
        if check_issue.find(project) != -1:
            return True
    return False


def clear_not_our_tickets(inside_tickets):
    inside_tickets = [x for x in inside_tickets if check_in_our_project(x.key)]

    return inside_tickets

jira = JIRA(server='https://dit.rencredit.ru/jira', basic_auth=('ext_azhuravlev2', '**'), validate=True)

issues = get_outside_issues('REL-330')
issues = clear_not_our_tickets(issues)
issue_to_excel = []
for insideIssue in issues:
    _inside_issues = get_inside_issues(insideIssue.key)
    _inside_issues = clear_not_our_tickets(_inside_issues)

    # issue_to_excel.append(insideIssue)
    _issue_type_id = insideIssue.fields.issuetype.id

    if _inside_issues.__len__() == 0 and _issue_type_id == 10003:
        continue

    print(insideIssue.key + ' ' + insideIssue.fields.summary)
    for ii in _inside_issues:
        print('     ' + ii.key + ' ' + ii.fields.summary)

save_issues_to_file(issue_to_excel)


# jira.assign_issue('FPD-2538', None)
# summary = issue.fields.summary
# jira.remove_watcher(issue, 'ext_dnikishin')
# jira.add_comment(issue, 'тест коммент')
# jira.add_comment('MCO-1330', 'тест коммент')
# comment = jira.comment('MCO-1330', '175976')
# comment.delete()
# watcher = jira.watchers(issue)
# print("Issue has {} watcher(s)".format(watcher.watchCount))
# for watcher in watcher.watchers:
#     print(watcher)
#     watcher is instance of jira.resources.User:
#     print(watcher.emailAddress)
# search_issues_and_reassign()