from __future__ import annotations
from datetime import datetime, timedelta

from reimburse import ProjectDays, State, Day


def main():

    # Set 1:
    #  Project 1: Low Cost City Start Date: 9/1/15 End Date: 9/3/15

    s1_p1 = ProjectDays.from_range("2015-09-01", "2015-09-01", State.WORK_LOW)

    # Set 2:
    #   Project 1: Low Cost City Start Date: 9/1/15 End Date: 9/1/15
    #   Project 2: High Cost City Start Date: 9/2/15 End Date: 9/6/15
    #   Project 3: Low Cost City Start Date: 9/6/15 End Date: 9/8/15

    s2_p1 = ProjectDays.from_range("2015-09-01", "2015-09-01", State.WORK_LOW)
    s2_p2 = ProjectDays.from_range("2015-09-02", "2015-09-06", State.WORK_HIGH)
    s2_p3 = ProjectDays.from_range("2015-09-06", "2015-09-08", State.WORK_LOW)

    print((s2_p1 + s2_p2)._populate_travel_days())
    print((s2_p1 + s2_p2).reimbursement())

    # Set 3:
    #   Project 1: Low Cost City Start Date: 9/1/15 End Date: 9/3/15
    #   Project 2: High Cost City Start Date: 9/5/15 End Date: 9/7/15
    #   Project 3: High Cost City Start Date: 9/8/15 End Date: 9/8/15

    s3_p1 = ProjectDays.from_range("2015-09-01", "2015-09-03", State.WORK_LOW)
    s3_p2 = ProjectDays.from_range("2015-09-05", "2015-09-07", State.WORK_HIGH)
    s3_p3 = ProjectDays.from_range("2015-09-08", "2015-09-08", State.WORK_HIGH)

    # Set 4:
    #   Project 1: Low Cost City Start Date: 9/1/15 End Date: 9/1/15
    #   Project 2: Low Cost City Start Date: 9/1/15 End Date: 9/1/15
    #   Project 3: High Cost City Start Date: 9/2/15 End Date: 9/2/15
    #   Project 4: High Cost City Start Date: 9/2/15 End Date: 9/3/15

    s4_p1 = ProjectDays.from_range("2015-09-01", "2015-09-01", State.WORK_LOW)
    s4_p2 = ProjectDays.from_range("2015-09-01", "2015-09-01", State.WORK_LOW)
    s4_p3 = ProjectDays.from_range("2015-09-02", "2015-09-02", State.WORK_HIGH)
    s4_p4 = ProjectDays.from_range("2015-09-02", "2015-09-03", State.WORK_HIGH)


if __name__ == "__main__":
    main()
