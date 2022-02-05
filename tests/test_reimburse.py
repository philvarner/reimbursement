import pytest
from reimburse import *


def test_state():
  assert State.OPEN + State.OPEN == State.OPEN
  assert State.OPEN + State.WORK_LOW == State.WORK_LOW
  assert State.OPEN + State.WORK_HIGH == State.WORK_HIGH
  assert State.WORK_HIGH + State.OPEN == State.WORK_HIGH
  assert State.WORK_HIGH + State.WORK_LOW == State.WORK_HIGH
  assert State.WORK_LOW + State.WORK_HIGH == State.WORK_HIGH

def test_project_days():
  assert len(ProjectDays.from_range('2015-09-01', '2015-09-01', State.WORK_LOW).days) == 3
  assert len(ProjectDays.from_range('2015-09-02', '2015-09-06', State.WORK_HIGH).days) == 7

  s2_p1 = ProjectDays.from_range("2015-09-01", "2015-09-01", State.WORK_LOW)
  s2_p2 = ProjectDays.from_range("2015-09-02", "2015-09-06", State.WORK_HIGH)

  pds = (s2_p1 + s2_p2)._populate_travel_days()
  assert pds.days[0].state == State.OPEN 
  assert pds.days[1].state == State.WORK_LOW 
  assert pds.days[2].state == State.WORK_HIGH 

def test_day():
  day = Day(date=datetime.fromisoformat("2015-09-03"), state=State.OPEN) + \
  Day(date=datetime.fromisoformat("2015-09-03"), state=State.WORK_HIGH)
  assert day.date == datetime.fromisoformat("2015-09-03")
  assert day.state == State.WORK_HIGH

  with pytest.raises(Exception): # dates don't match
    Day(date=datetime.fromisoformat("2015-09-03"), state=State.OPEN) + \
    Day(date=datetime.fromisoformat("2015-09-04"), state=State.WORK_HIGH)

  assert Day(date=datetime.fromisoformat("2015-09-03"), state=State.OPEN) != \
    Day(date=datetime.fromisoformat("2015-09-04"), state=State.WORK_HIGH)

  assert Day(date=datetime.fromisoformat("2015-09-03"), state=State.OPEN) < \
Day(date=datetime.fromisoformat("2015-09-04"), state=State.WORK_HIGH)
  
  assert Day(date=datetime.fromisoformat("2015-09-04"), state=State.OPEN) == \
Day(date=datetime.fromisoformat("2015-09-04"), state=State.WORK_HIGH)

  assert    Day(date=datetime.fromisoformat("2015-09-03"), state=State.OPEN) + \
    Day(date=datetime.fromisoformat("2015-09-03"), state=State.WORK_HIGH) == \
      Day(date=datetime.fromisoformat("2015-09-03"), state=State.WORK_HIGH)
