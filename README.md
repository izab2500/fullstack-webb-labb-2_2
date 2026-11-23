# Laboration 2.2 - Skapa REST-webbtjänst med backend-ramverk

API:et är utvecklat med FastAPI och används för att hantera böcker genom CRUD-operationer (Create, Read, Update, Delete).


## API Endpoints

| Metod  | Endpoint         | Handling            | Konsekvens                  | 
|--------|------------------|---------------------|-----------------------------|
| GET    | /books           | Läsa                | Hämtar alla böcker          | 
| GET    | /books/{book_id} | Läsa                | Hämtar en befintlig bok     |
| POST   | /books           | Skapa               | Skapar en ny bok            |
| PUT    | /books/{book_id} | Updatera            | Uppdaterar en befintlig bok |
| DELETE | /books/{book_id} | Radera              | Raderar en befintlig bok    |

## Krav för att köra projektet

- Python (för att köra FastAPI)

- XAMPP ( för att köra Apache (behövs endast för phpmyadmin) och MySQL lokalt)

- Git (för att klona repot)

- En kodredigerare (Visual Studio Code är att föredra)

## Klona repot

1. Öppna ett terminalfönster

2. Klona repot:

```bash
git clone https://github.com/izab2500/fullstack-webb-labb-2_2.git

```

3. Gå till backend-mappen: cd backend

## Installera beroenden

1. Skapa en virtuell miljö:

```bash
python -m venv .venv

```

2. Aktivera den virtuella miljön (powershell):

```bash
.venv\Scripts\Activate.ps1

```

3. Installera projektets beroenden:

```bash
pip install -r requirements.txt

```

## Konfigurera miljövariabler

1. Skapa en fil med namnet .env i backend-mappen

2. Lägg till anslutningssträng:

```env
 DATABASE_URL=mysql+pymysql://root:@localhost:3306/book_api

 ```

**OBS!** Ovanståend är för lokal anslutning med användarnamnet root utan lösenord.

## Starta databasen

1. Öppna XAMPP control Panel

2. Starta **Apache** och **MySQL**

3. Öppna phpmyadmin via http://localhost/phpmyadmin

4. Skapa en ny databas med namnet **book_api**


## Starta FastAPI

1. Kontrollera att du befinner dig i backend-mappen och att den virtuella miljön är aktiverad

2. Starta API:et:

```bash 
python -m uvicorn app.main:app --reload

```

## Testa API:et

1. När server är startad gå till: http://127.0.0.1:8000 

2. Öppna sedan: http://127.0.0.1:8000/docs (för att testa API:et)

## Videodemostration

[videodemonstration](https://www.youtube.com/watch?v=kdushJMMcQo)