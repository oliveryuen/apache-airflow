FROM puckel/docker-airflow

# install Java
USER root
RUN mkdir -p /usr/share/man/man1 && apt-get update -y && apt-get install -y openjdk-8-jdk

# configure Airflow
USER airflow
COPY dags/helloworld.py /usr/local/airflow/dags/helloworld.py
COPY scripts /usr/local/airflow/scripts

EXPOSE 8080
