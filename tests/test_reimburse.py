import pytest
from reimburse import *


def test_state():
  assert State.OPEN.combine(State.OPEN) == State.OPEN
  assert State.OPEN.combine(State.WORK_LOW) == State.WORK_LOW
  assert State.WORK_HIGH.combine(State.WORK_LOW) == State.WORK_HIGH
  assert State.WORK_LOW.combine(State.WORK_HIGH) == State.WORK_HIGH

def test_project_days():
  assert len(ProjectDays('2015-09-01', '2015-09-01', State.WORK_LOW).days) == 3
  assert len(ProjectDays('2015-09-02', '2015-09-06', State.WORK_HIGH).days) == 7

def test_day():
  day = Day(date=datetime.fromisoformat("2015-09-03"), state=State.OPEN).combine(
  Day(date=datetime.fromisoformat("2015-09-03"), state=State.WORK_HIGH)
  )
  assert day.date == datetime.fromisoformat("2015-09-03")
  assert day.state == State.WORK_HIGH

  with pytest.raises(Exception): # dates don't match
    Day(date=datetime.fromisoformat("2015-09-03"), state=State.OPEN).combine(
    Day(date=datetime.fromisoformat("2015-09-04"), state=State.WORK_HIGH)
    )

  assert Day(date=datetime.fromisoformat("2015-09-03"), state=State.OPEN) != \
    Day(date=datetime.fromisoformat("2015-09-04"), state=State.WORK_HIGH)

  assert Day(date=datetime.fromisoformat("2015-09-03"), state=State.OPEN) < \
Day(date=datetime.fromisoformat("2015-09-04"), state=State.WORK_HIGH)
  
  assert Day(date=datetime.fromisoformat("2015-09-04"), state=State.OPEN) == \
Day(date=datetime.fromisoformat("2015-09-04"), state=State.WORK_HIGH)
