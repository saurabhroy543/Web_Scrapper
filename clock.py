from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from scrpper import check_price


sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(check_price, 'interval', seconds=10)

sched.start()