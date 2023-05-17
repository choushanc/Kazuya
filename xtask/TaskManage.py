import datetime
import time
from string import ascii_uppercase
from typing import Dict,List
a0 = list(ascii_uppercase)
class TaskManage:
    __job_id_cache:Dict[str,str] = {}
    __js:int=0
    def __init__(self):
        pass

    def get_job_id(self) -> str:
        job_id = a0[self.__js]
        self.__job_id_cache[job_id] = job_id
        self.__js += 1
        return job_id

    def comp_job_id(self,job_id:str):
        del self.__job_id_cache[job_id]

    def safe_out(self,__clicked_after):
        e0 = datetime.datetime.now() + datetime.timedelta(seconds=5)

        def ashes():
            na = True
            if datetime.datetime.now() > e0:
                print('强退')
                na = False
            elif self.__job_id_cache:
                pass
            else:
                na = False
            return na
        while ashes():
            time.sleep(1)
        __clicked_after()