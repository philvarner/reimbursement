from __future__ import annotations
from enum import Enum
from datetime import datetime, timedelta
from typing import List
from dataclasses import dataclass
from functools import reduce
import copy


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

    def __add__(self, state2: State) -> State:
        return max(self, state2)

    def reimbursement(self) -> int:
        if self == self.TRAVEL_LOW:
            return 45
        elif self == self.TRAVEL_HIGH:
            return 55
        elif self == self.WORK_LOW:
            return 75
        elif self == self.WORK_HIGH:
            return 85
        else:
            return 0


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

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.date > other.date
        return NotImplemented

    def __add__(self, other: Day) -> Day:
        if self.date != other.date:
            raise Exception(
                f"tried to combine Days that had different dates: {self.date} {other.date}"
            )
        return Day(self.date, self.state + other.state)


class ProjectDays:
    def __init__(self, days: List[Day]) -> ProjectDays:
        self.days = days

    @classmethod
    def from_range(cls, start: str, end: str, state: State) -> None:

        start_date = datetime.fromisoformat(start)
        end_date = datetime.fromisoformat(end)

        if start_date > end_date:
            raise Exception("start date not before end date")

        pre_date = start_date - timedelta(days=1)
        day_count = (
            end_date - start_date
        ).days + 3  # 3 = before + after + end inclusive
        pd = ProjectDays(
            [Day(pre_date + timedelta(days=x), state) for x in range(day_count)]
        )
        pd.days[0].state = State.OPEN
        pd.days[-1].state = State.OPEN

        return pd

    def __str__(self):
        return str(self.days)

    def __add__(self, other: ProjectDays) -> ProjectDays:
        all_days = sorted(self.days + other.days)

        def f(xs, y):
            if xs[-1] == y:
                xs[-1] == xs[-1] + y
            else:
                xs.append(y)
            return xs

        return ProjectDays(reduce(f, all_days, all_days[0:1]))

    def _populate_travel_days(self) -> ProjectDays:
        new_days = copy.deepcopy(self.days)
        for i, day in enumerate(new_days[1:-1], start=1):
            if (
                new_days[i - 1].state == State.OPEN
                or new_days[i + 1].state == State.OPEN
            ):
                if day.state == State.WORK_HIGH:
                    day.state = State.TRAVEL_HIGH
                elif day.state == State.WORK_LOW:
                    day.state = State.TRAVEL_LOW
        return new_days

    def reimbursement(self):
        return sum([d.state.reimbursement() for d in self._populate_travel_days()])
