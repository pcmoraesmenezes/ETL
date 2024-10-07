# %%
import pandas as pd
import psycopg
from load_dotenv import load_dotenv
import os
from pathlib import Path

# %%
load_dotenv()

HOST = os.getenv("HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DB = os.getenv("DB")
PORT = os.getenv("PORT")

# %%
try:
    connectDB = psycopg.connect(
        host=HOST,
        port=PORT,
        dbname=DB,
        user=USER,
        password=PASSWORD
    )

    cursor = connectDB.cursor()

    print("Conexão estabelecida com sucesso!")

except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")


# %%
cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS categoria (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL
        );
    """
)

connectDB.commit()


# %%
cursor.execute(
    """
    TRUNCATE TABLE categoria;
    """
)

connectDB.commit()

# %%
df = pd.read_excel(Path.cwd() / "data" / "Categoria.xlsx")

# %%
for index, row in df.iterrows():
    cursor.execute(
        f"""
            INSERT INTO categoria (name)
            VALUES ('{row['name']}');
        """
    )

connectDB.commit()

#%%

cursor.execute(
    """
        SELECT * FROM categoria;
    """
)

result = cursor.fetchall()

print(result)

# %%
cursor.close()
connectDB.close()


