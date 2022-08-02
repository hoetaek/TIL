"""def solution(id_list, report, k):
    report_dict = {user: set() for user in id_list}

    for r in report:
        reporter, reportee = r.split()
        report_dict[reporter].add(reportee)

    reported_users = [
        user for user in report_dict if len(reported_dict[user]) >= k]
    answer = [len([i for i in report_dict[user] if i in reported_users])
              for user in id_list]
    return answer"""


def solution(id_list, report, k):
    reported_dict = {user: set() for user in id_list}
    answer = [0] * len(id_list)

    for r in report:
        reporter, reportee = r.split()
        reported_dict[reportee].add(reporter)

    reported_users = [
        user for user in id_list if len(reported_dict[user]) >= k]
    for r in set(report):
        reporter, reportee = r.split()
        if reportee in reported_users:
            answer[id_list.index(reporter)] += 1
    return answer


id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2


print(solution(id_list, report, k))
