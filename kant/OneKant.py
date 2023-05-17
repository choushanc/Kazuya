import time

from xtask.XTask import XTask


class OneKant:
    def __init__(self):
        self.xtask = XTask()

    def run(self, get_god):
        def func(job_id: str, keep, end):
            js = 0
            while keep(job_id):
                self.register_func(job_id, js)
                time.sleep(1)
                js += 1
            end(job_id)

        self.xtask.add_jobs([func], get_god)

    def register_func(self,*args,**kwargs):
        pass
