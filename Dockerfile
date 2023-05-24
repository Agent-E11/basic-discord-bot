# Start with base image
FROM python:3.10.8

# Add the requirements for the script
ADD requirements.txt /app/requirements.txt

# Add the default `library` module
ADD library.py /app/library.py

# Install requirements
RUN pip install -r /app/requirements.txt

# Add the actual script
ADD botScript.py /app/botScript.py

# Run the script when the container starts
ENTRYPOINT ["python"]

CMD ["/app/botScript.py"]