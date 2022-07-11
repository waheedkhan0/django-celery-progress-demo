from celery import shared_task
from time import sleep
from celery_progress.backend import ProgressRecorder

@shared_task(bind=True)
def go_to_sleep(self,duration):
    print('running go_to_sleep for '+str(duration)+' seconds ...')
    progress_recorder = ProgressRecorder(self)
    number_of_times = 60
    for i in range(number_of_times):
        sleep(duration)
        progress_recorder.set_progress(i+1,number_of_times,f' On iteration {i}')
    return 'Done'