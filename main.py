from __future__ import annotations
from reimburse import Project, DayType


def main():

    # Set 1:
    #  Project 1: Low Cost City Start Date: 9/1/15 End Date: 9/3/15

    s1_p1 = Project.from_range("2015-09-01", "2015-09-01", DayType.FULL_LOW)
    reimb = s1_p1.reimbursement()
    print(f"Set 1: {reimb}")
    assert reimb == 45

    # Set 2:
    #   Project 1: Low Cost City Start Date: 9/1/15 End Date: 9/1/15
    #   Project 2: High Cost City Start Date: 9/2/15 End Date: 9/6/15
    #   Project 3: Low Cost City Start Date: 9/6/15 End Date: 9/8/15

    # LT|HW|HW|HW|HW|HW|LW|LT =>  590

    s2_p1 = Project.from_range("2015-09-01", "2015-09-01", DayType.FULL_LOW)
    s2_p2 = Project.from_range("2015-09-02", "2015-09-06", DayType.FULL_HIGH)
    s2_p3 = Project.from_range("2015-09-06", "2015-09-08", DayType.FULL_LOW)

    reimb = (s2_p1 + s2_p2 + s2_p3).reimbursement()
    print(f"Set 2: {reimb}")
    assert reimb == 590

    # Set 3:
    #   Project 1: Low Cost City Start Date: 9/1/15 End Date: 9/3/15
    #   Project 2: High Cost City Start Date: 9/5/15 End Date: 9/7/15
    #   Project 3: High Cost City Start Date: 9/8/15 End Date: 9/8/15

    # LT|LW|LT|O|HT|HW|HW|HT| => 445

    s3_p1 = Project.from_range("2015-09-01", "2015-09-03", DayType.FULL_LOW)
    s3_p2 = Project.from_range("2015-09-05", "2015-09-07", DayType.FULL_HIGH)
    s3_p3 = Project.from_range("2015-09-08", "2015-09-08", DayType.FULL_HIGH)

    reimb = (s3_p1 + s3_p2 + s3_p3).reimbursement()
    print(f"Set 3: {reimb}")
    assert reimb == 445

    # Set 4:
    #   Project 1: Low Cost City Start Date: 9/1/15 End Date: 9/1/15
    #   Project 2: Low Cost City Start Date: 9/1/15 End Date: 9/1/15
    #   Project 3: High Cost City Start Date: 9/2/15 End Date: 9/2/15
    #   Project 4: High Cost City Start Date: 9/2/15 End Date: 9/3/15

    # LT | HW | HT => 185

    s4_p1 = Project.from_range("2015-09-01", "2015-09-01", DayType.FULL_LOW)
    s4_p2 = Project.from_range("2015-09-01", "2015-09-01", DayType.FULL_LOW)
    s4_p3 = Project.from_range("2015-09-02", "2015-09-02", DayType.FULL_HIGH)
    s4_p4 = Project.from_range("2015-09-02", "2015-09-03", DayType.FULL_HIGH)

    reimb = (s4_p1 + s4_p2 + s4_p3 + s4_p4).reimbursement()
    print(f"Set 4: {reimb}")
    assert reimb == 185


if __name__ == "__main__":
    main()
