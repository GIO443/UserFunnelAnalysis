# 🧩 User Funnel Drop-Off Analysis

This project analyzes user behavior across a five-stage product funnel, from landing on the homepage to completing a purchase. The goal is to identify where users drop off and suggest improvements to the user experience and conversion flow.

## 📁 Dataset
The dataset includes 17,175 user-stage interactions with three columns:
- `user_id`: Unique identifier for each user
- `stage`: Funnel stage (`homepage`, `product_page`, `cart`, `checkout`, `purchase`)
- `conversion`: Whether the user reached that stage (True/False)

## 📊 Funnel Results

| Stage         | Users Reached | Conversion Rate (vs Homepage) |
|---------------|----------------|-------------------------------|
| Homepage      | 10,000         | 100%                          |
| Product Page  | 2,515          | 25.15%                        |
| Cart          | 449            | 4.49%                         |
| Checkout      | 36             | 0.36%                         |
| Purchase      | 14             | 0.14%                         |

## 🔍 Insights
There is a steep drop-off at each step of the funnel. Major losses occur between the homepage and product page, and again at the cart-to-checkout step. This suggests possible UX friction, unclear value propositions, or checkout barriers.

## ✅ Recommendations
- Improve homepage clarity to better guide users to product pages
- Highlight value propositions and streamline the product page
- Simplify checkout process and reduce trust barriers
- Run A/B tests to validate improvements

## 📈 Visualization
The chart below shows how users move through each funnel stage.

![Funnel Chart](funnel_chart.png)

## 🛠 Tools Used
- Python
- Pandas
- Matplotlib
