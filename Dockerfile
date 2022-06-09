FROM python:3.9-slim as base
#COPY .db /home/app/db
COPY csvql /home/app/csvql
COPY Pipfile /home/app/Pipfile
COPY requirements.txt /home/app/requirements.txt
COPY run.py /home/app/run.py

#RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pipenv

WORKDIR /home/app

#RUN pipenv install --skip-lock
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

#CMD ["streamlit" ,"run", "csvql/Home.py"]
CMD ["python","run.py"]