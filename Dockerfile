# Our base image
FROM alpine:3.5

# Install python and pip
RUN apk add --update py2-pip
RUN pip install --upgrade pip
RUN pip install Flask

# Install Python modules needed by the Python app
RUN mkdir -p /usr/src/app/
RUN pip freeze > /usr/src/app/requirements.txt
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# Copy files required for the app to run
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/

# Tell the port number the container should expose
EXPOSE 5000

# Run the application
CMD ["python", "/usr/src/app/app.py"]
