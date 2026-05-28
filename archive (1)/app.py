import streamlit as st
import pandas as pd
import plotly.express as px
from mlxtend.frequent_patterns import apriori, association_rules

st.set_page_config(layout="wide")
st.title("🍕 Pizza Business Command Center")

@st.cache_data
def load_data():
    file_path = r'C:\Users\Ameen\Desktop\MyProjects-P\Pizza Place Sales\final_data.csv'
    df = pd.read_csv(file_path)
    return df

df = load_data()

total_revenue = df['total_price'].sum()
total_orders = df['order_id'].nunique()
avg_order_value = total_revenue / total_orders

st.subheader("Key Performance Indicators")
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"$ {total_revenue:,.2f}")
col2.metric("Total Orders", f"{total_orders:,}")
col3.metric("Avg Order Value", f"$ {avg_order_value:,.2f}")

st.markdown("---")

st.subheader("Sales Trends & Top Performers")
top_pizzas = df.groupby('name')['quantity'].sum().sort_values(ascending=False).head(10)

fig1 = px.bar(x=top_pizzas.index, y=top_pizzas.values, 
             labels={'x': 'Pizza Name', 'y': 'Quantity Sold'})
st.plotly_chart(fig1, use_container_width=True)

st.markdown("---")

st.subheader("💡 AI Combo Recommendations (Dynamic)")

basket = df.groupby(['order_id', 'name'])['quantity'].sum().unstack().reset_index().fillna(0).set_index('order_id')
basket = basket.applymap(lambda x: 1 if x > 0 else 0)

frequent_itemsets = apriori(basket, min_support=0.01, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

top_rules = rules.sort_values('lift', ascending=False).head(5)
top_rules = top_rules[['antecedents', 'consequents', 'lift']]

# Clean up the output to be professional and readable
def clean_names(x):
    return list(x)[0]

top_rules['antecedents'] = top_rules['antecedents'].apply(clean_names)
top_rules['consequents'] = top_rules['consequents'].apply(clean_names)
top_rules.columns = ['If Customer buys', 'They will likely buy', 'Strength (Lift)']

st.table(top_rules)
st.success("These recommendations are updated automatically based on real-time sales patterns!")

#cd Desktop\MyProjects-P\Pizza Place Sales\archive (1)
#streamlit run app.py