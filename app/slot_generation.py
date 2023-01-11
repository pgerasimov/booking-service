from app import db
from app.models import Slots


def slot_generation(form):
    date = form.work_date.data
    start_work_time = form.start_time.data
    end_work_time = form.end_time.data
    work_duration = int(form.duration.data)
    slot_end_time = 0

    for slot_start_time in range(start_work_time, end_work_time, work_duration):
        slot_end_time = slot_start_time + work_duration
        print(f'string number {slot_start_time}')
        print(f'end {slot_end_time}')

        # new_slot = Slots(
        #     user='uniq book 2',
        #     date=date,
        #     time_start=i,
        #     time_end=slotEnd,
        #     status='free'
        # )
        #
        # db.session.add(new_slot)
        # db.session.commit()

        # db.session.commit()
    # TODO: Write module for generate slots.
    # Дата - статик в бд; Берем начало - старт тайм, окончание в старт+продолжительность - это слот.
    # Дальше берем окончаение + продолжительность, если сумма == Времени конца - стопаем.
    # Каждую итерацию пишем в БД отдельной записью
    return 'ok'
