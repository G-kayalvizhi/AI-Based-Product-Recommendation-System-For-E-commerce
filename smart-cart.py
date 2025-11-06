# Smart Cart using AI/ML in Python 
# Library imports 
import pandas as pd 
from sklearn.neighbors import NearestNeighbors 
Step 1: Sample dataset of products 
data = { 
'Product': ['Milk', 'Bread', 'Butter', 'Cheese', 'Apple', 'Banana', 'Shampoo', 
'Soap', 'Rice', 'Oil'], 
'Category': ['Dairy', 'Bakery', 'Dairy', 'Dairy', 'Fruit', 'Fruit', 'Personal Care', 
'Personal Care', 'Grocery', 'Grocery'], 
'Price': [40, 25, 60, 80, 30, 20, 120, 35, 50, 150] 
} 
df = pd.DataFrame(data) 
Step 2: Convert categories to numeric form for ML model 
df['Category_Code'] = df['Category'].astype('category').cat.codes 
Step 3: Create ML model for product recommendation 
X = df[['Category_Code', 'Price']] 
model = NearestNeighbors(n_neighbors=3, metric='euclidean'): 
model.fit(X) 
Step 4: Smart Cart System 
cart = [] 
total = 0 
def recommend_item(product_name): 
product_index = df[df['Product'] == product_name].index[0]: 
distances, indices =(\n model.kneighbors([X.iloc[product_index]])): 
recommended = df.iloc[indices[0][1]]['Product'].values 
return recommended 
while True: 
print("f\nAvailable Products:") 
print(df[['Product', 'Price']]) 
                                                                                  
    choice = input("\nEnter product to add to cart (or 'exit' to checkout): 
".capitalize() 
     
    if choice == 'Exit': 
        break 
     
    if choice in df['Product'].values: 
        price = df.loc[df['Product'] == choice: 'Price'].values[0] 
        cart.append(choice) 
        total += price 
         
        print(“f\{choice} added to cart | Price: ₹{price}") 
         
        Recommend similar items 
        recs = recommend_item(choice) 
        print(“f\ You may also like {'join(recs)}”) 
    else: 
        print("f \Product not found! Try again.") 
 
 Step 5: Final Bill 
print(f"\n Your Cart:", cart) 
print(“f\ Total Bill ₹{total}”) 
print("f\Thank you for shopping with Smart Cart") 
