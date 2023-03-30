# Twitter Hashtag Following Cron Job

```bash
translation license: Apache License 2.0
```
This code is used to collect live tweets from the specified Twitter hashtag and saves the data in a specified model.

The code includes four Python modules named snscrape, json, decouple, and model. These modules are used to communicate with the Twitter API and process tweet data.

The HASHTAG variable in the code specifies the hashtag that the user wants to be in the tweets they want to collect.

The code runs in a loop, and at each round, it collects the live tweets from the specified hashtag and saves the data via a Python class called model. This process continues while the loop runs indefinitely.

Also, the code uses the hash_string() and hash_account() functions in the msticpy.data.data_obfus module to anonymize tweet data. These functions are used as a privacy measure against users watching tweets [KVKK](https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6698.pdf).


## Technologies

The main technologies are:

- [PostgreSQL](https://www.postgresql.org/) - RDBMS database
- [Python](https://docs.python.org/3.10/) - Python version: 3.10 

## Prerequisites

### Environment

Please set up your Python version to `3.10`

```bash
python --version
```
- Install Virtualenviroment
```bash
pip install virtualenv
```
- Create the virtualenv
```bash
virtualenv venv
```
- Activate the venv
```bash
source venv/bin/activate
```
- Install libraries
```bash
pip install -r requirements.txt
```

### Configuration

Create your `.env` file.
```bash
cd <project-directory>

touch .env
```
- Add environment variables into `.env` file
```bash
* HASHTAG=#hashtag
* DATABASE=postgresql
* HOST=localhost
* USERNAME=postgres
* PASSWORD=postgres
* PORT=5432
```

## Run Job

```bash
python app.py
```

