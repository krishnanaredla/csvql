FROM python:3.9-slim as base
#COPY .db /home/app/db
COPY csvql /home/app/csvql
COPY Pipfile /home/app/Pipfile

RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pipenv

WORKDIR /home/app

RUN pipenv install --skip-lock

CMD ["pipenv", "run" ,"streamlit" ,"run", "csvql/Home.py"]