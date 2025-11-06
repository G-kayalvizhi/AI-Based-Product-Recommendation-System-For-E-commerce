# 🛒 Smart Cart using AI/ML in Python

## 📍 Introduction
**Smart Cart** is an intelligent and scalable e-commerce prototype that enhances the online shopping experience using **Machine Learning**. The system analyzes product categories and pricing to recommend similar products to users in real-time. It aims to make online shopping faster, smarter, and more personalized.

---

## 📍 Project Overview
The **Smart Cart** system leverages AI/ML techniques, particularly **K-Nearest Neighbors (KNN)**, to suggest related items based on user selections.  
It works by:
1. Taking a sample dataset of products.
2. Encoding categories into numerical form.
3. Training a recommendation model.
4. Suggesting similar items when a product is added to the cart.
5. Generating a final bill summary upon checkout.

---

## 📍 Key Responsibilities and Tasks
- Designed and implemented a **Python-based AI/ML recommendation system**.
- Used **Pandas** for data manipulation and preprocessing.
- Implemented the **KNN (Nearest Neighbors)** algorithm for product similarity detection.
- Created an **interactive shopping simulation** using input/output commands.
- Generated product recommendations dynamically during cart updates.

---

## 📍 Skills and Knowledge Gained
- Machine Learning Model Building (using **Scikit-learn**)
- Data Preprocessing and Feature Encoding
- Python Libraries: **Pandas**, **NumPy**, **Scikit-learn**
- Logical Problem Solving and Interactive System Design
- Basic E-commerce Recommendation System Logic

---

## 📍 Challenges and Solutions
| Challenge | Solution |
|------------|-----------|
| Encoding categorical data for ML model | Used `.astype('category').cat.codes` to convert product categories into numeric values |
| Selecting the right similarity metric | Implemented **Euclidean distance** in KNN for better product similarity |
| Displaying real-time recommendations | Integrated dynamic recommendation calls within user input loop |
| Managing user-friendly console interface | Used formatted print statements for better interaction and clarity |

---

## 📍 Achievements and Outcomes
- Successfully built a **mini AI-powered recommendation system**.
- Enhanced understanding of **KNN-based recommendation logic**.
- Designed a **user-friendly console shopping experience**.
- Strengthened Python coding and debugging skills.
- Developed a foundation for **future e-commerce AI models**.

---

## 📍 Conclusion and Future Plan
The **Smart Cart** project demonstrates how AI/ML can enhance user experience in online shopping.  
In the future, the system can be expanded by:
- Integrating **real-time product databases**.
- Using **content-based filtering with NLP** for text-based recommendations.
- Creating a **web-based interface** with frameworks like Flask or Django.
- Implementing **user purchase history-based hybrid models**.

---

## 🧠 Tech Stack
- **Language:** Python  
- **Libraries:** Pandas, Scikit-learn  
- **Algorithm:** K-Nearest Neighbors (KNN)  
- **Dataset:** Sample Product Dataset  

---

## 🚀 How to Run the Project
```bash
# Clone the repository
git clone https://github.com/<your-username>/SmartCart-AI.git

# Navigate to the project folder
cd SmartCart-AI

# Run the script
python smart_cart.py

## Project Structure

SmartCart-AI/
│
├── smart_cart.py           # Main Python code
├── README.md               # Project documentation
└── dataset.csv (optional)  # Sample dataset if extended

## Sample output

Available Products:
   Product   Price
0  Milk       40
1  Bread      25
...

Enter product to add to cart (or 'exit' to checkout): Milk
Milk added to cart | Price: ₹40
You may also like: Butter, Cheese, Bread

Your Cart: ['Milk']
Total Bill: ₹40
Thank you for shopping with Smart Cart!

