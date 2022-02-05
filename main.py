from __future__ import annotations
from datetime import datetime, timedelta

from reimburse import ProjectDays, State, Day


def main():

    # Set 1:
    #  Project 1: Low Cost City Start Date: 9/1/15 End Date: 9/3/15

    s1_p1 = ProjectDays.from_range("2015-09-01", "2015-09-01", State.WORK_LOW)
    print(f"Set 1: {s1_p1.reimbursement()}")
    assert s1_p1.reimbursement() == 45

    # Set 2:
    #   Project 1: Low Cost City Start Date: 9/1/15 End Date: 9/1/15
    #   Project 2: High Cost City Start Date: 9/2/15 End Date: 9/6/15
    #   Project 3: Low Cost City Start Date: 9/6/15 End Date: 9/8/15

    # LT|HW|HW|HW|HW|HW|LW|LT =>  590  

    s2_p1 = ProjectDays.from_range("2015-09-01", "2015-09-01", State.WORK_LOW)
    s2_p2 = ProjectDays.from_range("2015-09-02", "2015-09-06", State.WORK_HIGH)
    s2_p3 = ProjectDays.from_range("2015-09-06", "2015-09-08", State.WORK_LOW)

    print(f"Set 2: {(s2_p1 + s2_p2 + s2_p3).reimbursement()}")
    assert (s2_p1 + s2_p2 + s2_p3).reimbursement() == 590

    # Set 3:
    #   Project 1: Low Cost City Start Date: 9/1/15 End Date: 9/3/15
    #   Project 2: High Cost City Start Date: 9/5/15 End Date: 9/7/15
    #   Project 3: High Cost City Start Date: 9/8/15 End Date: 9/8/15

    s3_p1 = ProjectDays.from_range("2015-09-01", "2015-09-03", State.WORK_LOW)
    s3_p2 = ProjectDays.from_range("2015-09-05", "2015-09-07", State.WORK_HIGH)
    s3_p3 = ProjectDays.from_range("2015-09-08", "2015-09-08", State.WORK_HIGH)
    print(f"Set 3: {(s3_p1 + s3_p2 + s3_p3).reimbursement()}")

    # Set 4:
    #   Project 1: Low Cost City Start Date: 9/1/15 End Date: 9/1/15
    #   Project 2: Low Cost City Start Date: 9/1/15 End Date: 9/1/15
    #   Project 3: High Cost City Start Date: 9/2/15 End Date: 9/2/15
    #   Project 4: High Cost City Start Date: 9/2/15 End Date: 9/3/15

    s4_p1 = ProjectDays.from_range("2015-09-01", "2015-09-01", State.WORK_LOW)
    s4_p2 = ProjectDays.from_range("2015-09-01", "2015-09-01", State.WORK_LOW)
    s4_p3 = ProjectDays.from_range("2015-09-02", "2015-09-02", State.WORK_HIGH)
    s4_p4 = ProjectDays.from_range("2015-09-02", "2015-09-03", State.WORK_HIGH)
    print(f"Set 4: {(s4_p1 + s4_p2 + s4_p3 + s4_p4).reimbursement()}")


if __name__ == "__main__":
    main()
