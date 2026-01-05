from sqlalchemy import create_engine

def load_data(df):
    db_url = "postgresql+psycopg2://postgres:Password@host.docker.internal:5432/customer_db"
    
    engine = create_engine(db_url)
    
    print("Connecting to database...")
    df.to_sql("customer_analytics", engine, if_exists="replace", index=False)
    print("✅ Data loaded into PostgreSQL successfully.")
