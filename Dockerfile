# 
FROM python:3.10-slim
 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["python", "main.py", "80"]
