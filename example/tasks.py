from celery import shared_task
from time import sleep

@shared_task(bind=True)
def go_to_sleep(self,duration):
    print('running go_to_sleep for '+str(duration)+' seconds ...')
    sleep(duration)
    return 'Done'