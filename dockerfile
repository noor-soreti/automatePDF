FROM python:3.9-bookworm

# Set the working directory
WORKDIR /usr/src/app

# Install Python dependencies
# RUN pip install Flask pandas "camelot-py[base]"

# Copy project files into the container
COPY . .

RUN pip install -r requirements.txt

# Set the default command
CMD [ "python3", "app.py" ]
