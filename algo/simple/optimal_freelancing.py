"""
<div class="html">
<p>
  </p><p>
    You recently started freelance software development and have been offered
    a variety of job opportunities. Each job has a deadline, meaning there is no
    value in completing the work after the deadline. Additionally, each job
    has an associated payment representing the profit for completing that job.
    Given this information, write a function that returns the maximum profit that
    can be obtained in a 7-day period.
  </p>

  <p>
    Each job will take 1 full day to complete, and the deadline will be given
    as the number of days left to complete the job. For example, if a job has a
    deadline of 1, then it can only be completed if it is the first job worked
    on. If a job has a deadline of 2, then it could be started on the first or
    second day.
  </p>

  <p>
    Note: There is no requirement to complete all of the jobs. Only one job can
    be worked on at a time, meaning that in some scenarios it will be impossible
    to complete them all.
  </p>
<h3>Sample Input</h3>
<pre><span class="CodeEditor-promptParameter">jobs</span> = [
  {"deadline": 1, "payment": 1},
  {"deadline": 2, "payment": 1},
  {"deadline": 2, "payment": 2}
]
</pre>
<h3>Sample Output</h3>
<pre>3 <span class="CodeEditor-promptComment">// Job 0 would be completed first, followed by job 2. Job 1 is not completed.</span>
</pre>
</div>
"""

def optimalFreelancing(jobs):
    jobs = sorted(jobs, key= lambda x: x["payment"], reverse=True)
    LENGTH_OF_WEEK = 7
    timeline = [False] * LENGTH_OF_WEEK
    total_profit = 0
    for job in jobs:
        max_time = min(job["deadline"],LENGTH_OF_WEEK)
        for time in reversed(range(max_time)):
            if not timeline[time]:
                timeline[time] = True
                total_profit += job["payment"]
                break
    return total_profit
