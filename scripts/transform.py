import pandas as pd

def transform_data(df):
    print("Starting transformation...")
    
    
    df['last_purchase_date'] = pd.to_datetime(
        df['last_purchase_date'], 
        errors='coerce'
    )


    df = df.dropna(subset=['last_purchase_date'])

    
    aggregated_df = df.groupby('last_purchase_date').agg(
        total_customers=('customer_id', 'nunique'),
        avg_income=('annual_income', 'mean'),
        avg_spending_score=('spending_score', 'mean'),
        churned_customers=('churned', 'sum'),
        avg_purchase_value=('avg_purchase_value', 'mean')
    ).reset_index()

    print("✅ Data transformed & aggregated")
    return aggregated_df