FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt  
    # && pip install pandas

COPY . .

CMD [ "python3", "app.py" ]


# FROM ubuntu:22.04

# RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
#     && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
# ENV LANG=en_US.utf8

# WORKDIR /usr/src/app

# RUN apt-get update && apt-get install -y \
#     python3-pip \
#     python3-venv 

# COPY . .
# # COPY requirements.txt .

# # Create a virtual environment and install dependencies
# RUN python3 -m venv myenv \
#     && ./myenv/bin/pip install --upgrade pip \
#     && ./myenv/bin/pip install -r requirements.txt


# # Set the entry point (optional depending on your app)
# ENTRYPOINT ["python3", "basic.py"]