from flask_login import current_user
from app import db
from app.models import Slots


def slot_generation(form):
    date = form.work_date.data
    start_work_time = form.start_time.data
    end_work_time = form.end_time.data
    work_duration = int(form.duration.data)
    user_id = current_user.id

    for slot_start_time in range(start_work_time, end_work_time, work_duration):
        slot_end_time = slot_start_time + work_duration
        print(f'string number {slot_start_time}')
        print(f'end {slot_end_time}')

        new_slot = Slots(
            user=user_id,
            date=date,
            time_start=slot_start_time,
            time_end=slot_end_time,
            status='free'
        )

        db.session.add(new_slot)
        db.session.commit()


# TODO: Write module for generate slots.
# Дата - статик в бд; Берем начало - старт тайм, окончание в старт+продолжительность - это слот.
# Дальше берем окончаение + продолжительность, если сумма == Времени конца - стопаем.
# Каждую итерацию пишем в БД отдельной записью
    return 'ok'
