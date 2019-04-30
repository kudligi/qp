FROM ubuntu:16.04

RUN apt-get update

RUN apt-get install -y python  && \
    apt-get install -y python-pip  && \
    pip install Flask  && \
    pip install pandas  && \
    pip install requests && \
    pip install elasticsearch && \
    apt-get install -y curl  

WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
#RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable
ENV FLASK_APP /app/source/app.py

EXPOSE 5000

CMD flask run --host=0.0.0.0