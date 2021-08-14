from background_task import background
from main.models import Diary, Note
from datetime import datetime

@background()
def delete_old_diaries():

    cnt = 0
    now = datetime.now()
    current_datetime = str('{}-{}-{} {}:{}:{}'.format(now.year, now.month, now.day, now.hour, now.minute, now.second))

    diaries = Diary.objects.filter().order_by('-expiration')
    for diary in diaries:
        if str(diary.expiration)[:-6] <= current_datetime:
            diary.delete()
            cnt += 1
        print(str(diary.expiration)[:-6] ,':',current_datetime)
    print('Удалено {} записей'.format(cnt))
            
delete_old_diaries(repeat=10)   

