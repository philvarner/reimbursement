
from enum import Enum
from datetime import datetime
from typing import List
from __future__ import annotations
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

@dataclass
class ProjectDays:

  days: List[Day]

  def combine(self, project_days2: ProjectDays) -> ProjectDays:
    pass