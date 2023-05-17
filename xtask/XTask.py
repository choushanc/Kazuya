import datetime
import time

from xtask.TaskBones import TaskBones
from xtask.TaskManage import TaskManage
from typing import Dict, List
from apscheduler.schedulers.background import BackgroundScheduler
taskmanage = TaskManage()
sc = BackgroundScheduler()
sc.start()
class TaskTag:
    ASY = 'ASY'
class XTask:
    def __init__(self):
        pass

    def add_jobs(self, func_list: List, get_god, end_jobs=None):
        sta: Dict[str, TaskBones] = {}
        for func in func_list:
            job_id = taskmanage.get_job_id()
            sta[job_id] = TaskBones(job_id)

            def keep(job_id: str):
                if get_god():
                    return  sta[job_id].job_state == True
                else:
                    return False

            def end(job_id: str):
                sta[job_id].job_state = False
                taskmanage.comp_job_id(job_id)

            sc.add_job(func=func, kwargs=dict(job_id=job_id, keep=keep, end=end))
        d0 = datetime.datetime.now() + datetime.timedelta(minutes=5)
        def ashes():
            na = True
            if datetime.datetime.now() > d0:
                na = False
            else:
                e0 = [s0.job_state for s0 in sta.values()]
                if True in e0:
                    pass
                else:
                    na = False
            return na

        while ashes():
            time.sleep(1)
        if end_jobs:
            end_jobs()
