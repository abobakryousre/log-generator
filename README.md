# Log Generator - Statistics tool

Generate random logs for netwokr traffic as below format

- date time source-ip des-ip port protocol username action

## Installation

install Python 3+ 


## Run Locally

Clone the project

```bash
  git clone https://github.com/abobakryousre/log-generator.git
```

Go to the project directory

```bash
  cd log-generator
```

Install dependencies

```bash
  python -m vevn .venv
  source .venv\bin\activate
  pip install -r requirments.txt
```

Start the application

- defualt logs size is: 1M
```bash
  python log_generator.py
```

- running with cusotm log size = 10K
```bash
  python log_generator.py "10000"
```

## Statistics tool

get below insights from the generated log by running the stat-tool.py

1) top 10 allow source ip
2) to 10 deny username
3) top 5 des ip for deny username
4) tcp baypass traffic count
5) tcp baypass top 5 services
6) top 5 hours for unique users


```bash
  python stat-tool.py
```
