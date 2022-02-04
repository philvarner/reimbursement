
from __future__ import annotations
from enum import Enum
from datetime import datetime, timedelta
from re import I
from typing import List
from dataclasses import dataclass

class State(Enum):
  OPEN = 1
  WORK_HIGH = 2
  WORK_LOW = 3
  TRAVEL_HIGH = 4
  TRAVEL_LOW = 5

  def combine(self, state2: State) -> State:
    pass

@dataclass
class Day:

  date: datetime.date
  state: State

  def combine(self, day2: Day) -> Day:
    pass

class ProjectDays:

  def __init__(self, start: str, end: str, state: State) -> None:

    start_date = datetime.fromisoformat(start)
    end_date = datetime.fromisoformat(end)

    if start_date > end_date:
      raise Exception("start date not before end date")

    pre_date = start_date - timedelta(days=1)
    day_count = (end_date - start_date).days + 3 # 3 = before + after + end inclusive
    self.days: List[Day] = \
      [Day(pre_date + timedelta(days=x), state) for x in range(day_count)]
    self.days[0].state = State.OPEN
    self.days[-1].state = State.OPEN

  def __str__(self):
     return str(self.days)

  def combine(self, project_days2: ProjectDays) -> ProjectDays:
    pass


# Set 1:
#  Project 1: Low Cost City Start Date: 9/1/15 End Date: 9/3/15

s1_p1 = ProjectDays('2015-09-01', '2015-09-01', State.WORK_LOW)

print(s1_p1)

# Set 2:
#   Project 1: Low Cost City Start Date: 9/1/15 End Date: 9/1/15
#   Project 2: High Cost City Start Date: 9/2/15 End Date: 9/6/15
#   Project 3: Low Cost City Start Date: 9/6/15 End Date: 9/8/15

s2_p1 = ProjectDays('2015-09-01', '2015-09-01', State.WORK_LOW)
s2_p2 = ProjectDays('2015-09-02', '2015-09-06', State.WORK_HIGH)
s2_p3 = ProjectDays('2015-09-06', '2015-09-08', State.WORK_LOW)

print(s2_p1)
print(s2_p2)
print(s2_p3)

# Set 3:
#   Project 1: Low Cost City Start Date: 9/1/15 End Date: 9/3/15
#   Project 2: High Cost City Start Date: 9/5/15 End Date: 9/7/15
#   Project 3: High Cost City Start Date: 9/8/15 End Date: 9/8/15

s3_p1 = ProjectDays('2015-09-01', '2015-09-03', State.WORK_LOW)
s3_p2 = ProjectDays('2015-09-05', '2015-09-07', State.WORK_HIGH)
s3_p3 = ProjectDays('2015-09-08', '2015-09-08', State.WORK_HIGH)

print(s3_p1)
print(s3_p2)
print(s3_p3)
print(s3_p3)

# Set 4:
#   Project 1: Low Cost City Start Date: 9/1/15 End Date: 9/1/15
#   Project 2: Low Cost City Start Date: 9/1/15 End Date: 9/1/15
#   Project 3: High Cost City Start Date: 9/2/15 End Date: 9/2/15
#   Project 4: High Cost City Start Date: 9/2/15 End Date: 9/3/15

s4_p1 = ProjectDays('2015-09-01', '2015-09-01', State.WORK_LOW)
s4_p2 = ProjectDays('2015-09-01', '2015-09-01', State.WORK_LOW)
s4_p3 = ProjectDays('2015-09-02', '2015-09-02', State.WORK_HIGH)
s4_p4 = ProjectDays('2015-09-02', '2015-09-03', State.WORK_HIGH)

print(s4_p1)
print(s4_p2)
print(s4_p3)
print(s4_p4)