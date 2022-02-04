
from __future__ import annotations
from enum import Enum
from datetime import datetime, timedelta
from re import I
from typing import List
from dataclasses import dataclass

class State(Enum):
  OPEN = 1
  TRAVEL_LOW = 2
  TRAVEL_HIGH = 3
  WORK_LOW = 4
  WORK_HIGH = 5

  def __lt__(self, other):
     if self.__class__ is other.__class__:
       return self.value < other.value
     return NotImplemented

  def combine(self, state2: State) -> State:
    return max(self, state2)

@dataclass
class Day:

  date: datetime.date
  state: State

  def __eq__(self, other):
    if self.__class__ is other.__class__:
      return self.date == other.date
    return NotImplemented

  def __lt__(self, other):
    if self.__class__ is other.__class__:
      return self.date < other.date
    return NotImplemented

  def combine(self, other: Day) -> Day:
    if self.date != other.date:
      raise Exception("tried to combine Days that had different dates")
    return Day(self.date, self.state.combine(other.state))

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

  def combine(self, other: ProjectDays) -> ProjectDays:
    pass

  def populate_travel_days(self) -> ProjectDays:
    pass
