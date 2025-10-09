FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

COPY appdynamics.cfg /etc/appdynamics.cfg

COPY . .

EXPOSE 5000

# CMD ["python", "app.py"]
CMD ["pyagent", "run", "-c", "/etc/appdynamics.cfg", "--", "python", "app.py"]




