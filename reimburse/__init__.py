from __future__ import annotations
from enum import Enum
from datetime import datetime, timedelta
from typing import List
from dataclasses import dataclass
from functools import reduce
import copy


class DayType(Enum):
    OPEN = 1
    FULL_LOW = 2
    FULL_HIGH = 3

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

    def __add__(self, other: DayType) -> DayType:
        return max(self, other)


REIMBURSEMENTS = {DayType.OPEN: 0, DayType.FULL_LOW: 75, DayType.FULL_HIGH: 85}
TRAVEL_ADJUSTMENT = -30


@dataclass
class Day:

    date: datetime.date
    state: DayType
    travel: bool = False

    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.date == other.date
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.date < other.date
        return NotImplemented

    def __add__(self, other: Day) -> Day:
        if self.date != other.date:
            raise Exception(
                f"tried to combine Days that had different dates: {self.date} {other.date}"
            )
        return Day(self.date, self.state + other.state)

    def reimbursement(self) -> int:
        amt = REIMBURSEMENTS.get(self.state, 0)
        if self.travel:
            amt = max(0, amt + TRAVEL_ADJUSTMENT)
        return amt


class Project:
    def __init__(self, days: List[Day]) -> Project:
        self.days = days

    @classmethod
    def from_range(cls, start: str, end: str, state: DayType) -> None:
        """create a set of project days from an inclusive start and end date"""

        start_date = datetime.fromisoformat(start)
        end_date = datetime.fromisoformat(end)

        if start_date > end_date:
            raise Exception("start date not before end date")

        pre_date = start_date - timedelta(days=1)
        day_count = (
            end_date - start_date
        ).days + 3  # 3 = before + after + end inclusive
        pd = Project(
            [Day(pre_date + timedelta(days=x), state) for x in range(day_count)]
        )
        pd.days[0].state = DayType.OPEN
        pd.days[-1].state = DayType.OPEN

        return pd

    def __str__(self):
        return str(self.days)

    def __add__(self, other: Project) -> Project:
        all_days = sorted(self.days + other.days)

        def f(xs, y):
            if xs[-1] == y:
                xs[-1] = xs[-1] + y
            else:
                xs.append(y)
            return xs

        return Project(reduce(f, all_days[1:], all_days[0:1]))

    def populate_travel_days(self) -> Project:
        new_days = copy.deepcopy(self.days)
        for i, day in enumerate(new_days[1:-1], start=1):
            if (
                new_days[i - 1].state == DayType.OPEN
                or new_days[i + 1].state == DayType.OPEN
            ):
                day.travel = True
        return Project(new_days)

    def reimbursement(self):
        return sum((d.reimbursement() for d in self.populate_travel_days().days))
