def add_time(start, duration, day=False):
  ## Start
  all_part = start.split()
  time_part = all_part[0].split(":")
  start_time_m = int(time_part[1])
  if all_part[1] == "PM":
    start_time_h = int(time_part[0]) + 12
  elif all_part[1] == "AM":
    start_time_h = int(time_part[0])
  ## Duration
  time_dur = duration.split(":")
  time_dur_h = int(time_dur[0])
  time_dur_m = int(time_dur[1])
  ## Time update
  update_h = start_time_h + time_dur_h
  update_m = start_time_m + time_dur_m
  if update_m // 60 != 0:
    update_h += update_m // 60
    update_m = update_m % 60
  ## Update days
  update_days = 0
  new_update_h = update_h
  if update_h > 24:
    update_days = update_h // 24
    new_update_h = update_h % 24
    if new_update_h == 0:
      new_update_h = 24
  ## Check time period
  time_period = ["AM", "PM"]
  if (new_update_h * 60 + update_m) < 720 or (new_update_h * 60 +
                                              update_m) >= 1440:
    new_time_p = time_period[0]
  elif (new_update_h * 60 + update_m) >= 720 and (new_update_h * 60 +
                                                  update_m) < 1440:
    new_time_p = time_period[1]
  ## Reformat
  ###### hours
  reform_h = str(new_update_h)
  if int(reform_h) // 12 == 1 and int(reform_h) % 12 != 0:
    reform_h = int(reform_h) % 12
    reform_h = str(reform_h)
  elif int(reform_h) // 12 == 2:
    reform_h = 12
    reform_h = str(reform_h)
  ###### min
  new_update_m = str(update_m)
  if int(update_m) // 10 == 0:
    new_update_m = '0' + str(update_m)
  ## Result
  ### If day is added
  weekly = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
  ]
  if day:
    day = day.strip().lower()
    location_update_days = (weekly.index(day) + update_days) % 7
    location_update_days = weekly[location_update_days]
    new_time = reform_h + ':' + new_update_m + " " + new_time_p + ", " + location_update_days.title(
    )
  else:
    new_time = reform_h + ':' + new_update_m + " " + new_time_p
  #### Condition Check
  if update_days == 0:
    new_time = new_time
  elif update_days == 1:
    new_time = new_time + " (next day)"
  elif update_days > 1:
    new_time = new_time + " (" + str(update_days) + " days later)"
  return new_time
