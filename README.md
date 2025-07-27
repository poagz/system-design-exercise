# system-design-exercise
Blocking and Non-Blocking I/O with Python/Flask + k6 tests


### How it works?
1. add virtual env `python3 -m venv venv`
2. activate virtual env `source venv/bin/activate`
3. install requirements `pip install -r requirements.txt`
4. init db `python3 init.py`
5. run blocking i/o app `python3 blocking.py` and non-blocking i/o app `python3 nonblocking.py`
6. run blocking i/o test `docker compose run k6 run /tests/blocking.js` and non-blocking i/o test `docker compose run k6 run /tests/nonblocking.js`

### What you shall see
poagz@laptop$ docker compose run k6 run /tests/nonblocking.js

         /\      Grafana   /‾‾/  
    /\  /  \     |\  __   /  /   
   /  \/    \    | |/ /  /   ‾‾\ 
  /          \   |   (  |  (‾)  |
 / __________ \  |_|\_\  \_____/ 

     execution: local
        script: /tests/nonblocking.js
        output: -

     scenarios: (100.00%) 1 scenario, 10 max VUs, 35s max duration (incl. graceful stop):
              * default: 10 looping VUs for 5s (gracefulStop: 30s)



  █ TOTAL RESULTS 

    checks_total.......................: 620     108.440935/s
    checks_succeeded...................: 100.00% 620 out of 620
    checks_failed......................: 0.00%   0 out of 620

    ✓ status is 200

    HTTP
    http_req_duration.......................................................: avg=87.57ms  min=7.72ms  med=17.57ms max=1.84s p(90)=210.87ms p(95)=352.31ms
      { expected_response:true }............................................: avg=87.57ms  min=7.72ms  med=17.57ms max=1.84s p(90)=210.87ms p(95)=352.31ms
    http_req_failed.........................................................: 0.00%  0 out of 620
    http_reqs...............................................................: 620    108.440935/s

    EXECUTION
    iteration_duration......................................................: avg=876.86ms min=85.39ms med=706.1ms max=3.27s p(90)=1.96s    p(95)=2.25s   
    iterations..............................................................: 62     10.844094/s
    vus.....................................................................: 10     min=10       max=10
    vus_max.................................................................: 10     min=10       max=10

    NETWORK
    data_received...........................................................: 100 kB 18 kB/s
    data_sent...............................................................: 89 kB  16 kB/s


poagz@laptop$ docker compose run k6 run /tests/blocking.js

         /\      Grafana   /‾‾/  
    /\  /  \     |\  __   /  /   
   /  \/    \    | |/ /  /   ‾‾\ 
  /          \   |   (  |  (‾)  |
 / __________ \  |_|\_\  \_____/ 

     execution: local
        script: /tests/blocking.js
        output: -

     scenarios: (100.00%) 1 scenario, 10 max VUs, 35s max duration (incl. graceful stop):
              * default: 10 looping VUs for 5s (gracefulStop: 30s)



  █ TOTAL RESULTS 

    checks_total.......................: 660     116.73337/s
    checks_succeeded...................: 100.00% 660 out of 660
    checks_failed......................: 0.00%   0 out of 660

    ✓ status is 200

    HTTP
    http_req_duration.......................................................: avg=80.28ms  min=6.67ms  med=7.9ms    max=3.16s p(90)=86.89ms p(95)=637.28ms
      { expected_response:true }............................................: avg=80.28ms  min=6.67ms  med=7.9ms    max=3.16s p(90)=86.89ms p(95)=637.28ms
    http_req_failed.........................................................: 0.00%  0 out of 660
    http_reqs...............................................................: 660    116.73337/s

    EXECUTION
    iteration_duration......................................................: avg=805.25ms min=79.48ms med=522.49ms max=3.24s p(90)=2.08s   p(95)=2.56s   
    iterations..............................................................: 66     11.673337/s
    vus.....................................................................: 10     min=10       max=10
    vus_max.................................................................: 10     min=10       max=10

    NETWORK
    data_received...........................................................: 131 kB 23 kB/s
    data_sent...............................................................: 94 kB  17 kB/s
