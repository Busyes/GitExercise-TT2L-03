# alarm.py
def get_alarm_data():
    alarm_time = get_alarm_time_from_database()
    alarm_sound = get_alarm_sound_from_database()
    return {
        'alarm_time': alarm_time,
        'alarm_sound': alarm_sound,
    }