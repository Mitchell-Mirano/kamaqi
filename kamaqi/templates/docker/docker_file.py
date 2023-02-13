DOCKER_FILE=\
"""
FROM ubuntu

RUN apt update -y
RUN apt install pip -y

WORKDIR /{{project_name}}

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app","--reload", "--host", "0.0.0.0", "--port", "80"]

"""
