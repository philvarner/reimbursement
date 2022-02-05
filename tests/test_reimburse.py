import pytest
from reimburse import *


def test_state():
    assert DayType.OPEN + DayType.OPEN == DayType.OPEN
    assert DayType.OPEN + DayType.FULL_LOW == DayType.FULL_LOW
    assert DayType.OPEN + DayType.FULL_HIGH == DayType.FULL_HIGH
    assert DayType.FULL_HIGH + DayType.OPEN == DayType.FULL_HIGH
    assert DayType.FULL_HIGH + DayType.FULL_LOW == DayType.FULL_HIGH
    assert DayType.FULL_LOW + DayType.FULL_HIGH == DayType.FULL_HIGH


def test_project_days():
    assert (
        len(Project.from_range("2015-09-01", "2015-09-01", DayType.FULL_LOW).days) == 3
    )
    assert (
        len(Project.from_range("2015-09-02", "2015-09-06", DayType.FULL_HIGH).days) == 7
    )

    s2_p1 = Project.from_range("2015-09-01", "2015-09-01", DayType.FULL_LOW)
    s2_p2 = Project.from_range("2015-09-02", "2015-09-06", DayType.FULL_HIGH)

    pds = (s2_p1 + s2_p2).populate_travel_days()
    assert pds.days[0].state == DayType.OPEN
    assert pds.days[1].state == DayType.FULL_LOW
    assert pds.days[2].state == DayType.FULL_HIGH


def test_day():
    day = Day(date=datetime.fromisoformat("2015-09-03"), state=DayType.OPEN) + Day(
        date=datetime.fromisoformat("2015-09-03"), state=DayType.FULL_HIGH
    )
    assert day.date == datetime.fromisoformat("2015-09-03")
    assert day.state == DayType.FULL_HIGH

    with pytest.raises(Exception):  # dates don't match
        Day(date=datetime.fromisoformat("2015-09-03"), state=DayType.OPEN) + Day(
            date=datetime.fromisoformat("2015-09-04"), state=DayType.FULL_HIGH
        )

    assert Day(date=datetime.fromisoformat("2015-09-03"), state=DayType.OPEN) != Day(
        date=datetime.fromisoformat("2015-09-04"), state=DayType.FULL_HIGH
    )

    assert Day(date=datetime.fromisoformat("2015-09-03"), state=DayType.OPEN) < Day(
        date=datetime.fromisoformat("2015-09-04"), state=DayType.FULL_HIGH
    )

    assert Day(date=datetime.fromisoformat("2015-09-04"), state=DayType.OPEN) == Day(
        date=datetime.fromisoformat("2015-09-04"), state=DayType.FULL_HIGH
    )

    assert Day(date=datetime.fromisoformat("2015-09-03"), state=DayType.OPEN) + Day(
        date=datetime.fromisoformat("2015-09-03"), state=DayType.FULL_HIGH
    ) == Day(date=datetime.fromisoformat("2015-09-03"), state=DayType.FULL_HIGH)
