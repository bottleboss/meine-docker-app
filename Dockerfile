# 1. Start-Image festlegen
FROM python:3.9-slim

# 2. Arbeitsverzeichnis im Container erstellen
WORKDIR /app

# 3. Abhängigkeiten installieren (ein schlauer Trick für schnelleres Bauen)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Den restlichen Code kopieren
COPY . .

# 5. Den Port freigeben, auf dem die App läuft
EXPOSE 8080

# 6. Befehl zum Starten der App definieren
CMD ["python", "app.py"]
