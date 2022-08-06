# O(n) time | O(d) space
# n: number of people
# d: depth of the org chart
def getLowestCommonManager(topManager, reportOne, reportTwo):
    return getOrgInfo(topManager, reportOne, reportTwo).lower_common_manager


def getOrgInfo(manager, report_one, report_two):
    num_important_reports = 0
    for directReport in manager.directReports:
        org_info = getOrgInfo(directReport, report_one, report_two)
        if org_info.num_important_reports == 2:
            return org_info
        num_important_reports += org_info.num_important_reports
    if manager == report_one or manager == report_two:
        num_important_reports += 1
    lowest_common_manager = manager if num_important_reports == 2 else None
    return OrgInfo(lowest_common_manager, num_important_reports)


class OrgInfo:
    def __init__(self, lower_common_manager, num_important_reports):
        self.lower_common_manager = lower_common_manager
        self.num_important_reports = num_important_reports


# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
