# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /intelense

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt


# copy the content of the local src directory to the working directory
COPY . /intelense
RUN apt-get update -y && apt-get install -y --no-install-recommends build-essential gcc \libsndfile1

EXPOSE 5000

# command to run on container start
ENTRYPOINT [ "python"]
CMD ["app.py"]