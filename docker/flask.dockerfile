# Menggunakan image Python
FROM python:3.9

# File Direktori kerja
WORKDIR /app

# Menyalin requirements ke dalam kontainer
COPY ./app/requirements.txt .

# Instal dependencies
RUN pip install -r requirements.txt

# Menyalin kode aplikasi ke dalam kontainer
COPY ./app .

# Perintah untuk menjalankan aplikasi Flask
CMD ["python", "app.py"]
