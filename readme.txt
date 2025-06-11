# User Funnel Drop-Off Analysis

This project analyzes how users move through a five-stage product funnel, from homepage visit to purchase. The goal is to identify where users drop off and suggest ways to improve the user experience and increase conversions.

## What the Data Includes

The dataset has 17,175 records with these columns:
- user_id: unique user identifier
- stage: funnel step (homepage, product_page, cart, checkout, purchase)
- conversion: whether the user reached that step (True/False)

## Key Findings

The funnel sees major drop-off between stages. For example:
- 25% of users reached the product page
- Less than 0.5% reached the checkout
- Only 0.14% completed a purchase

This suggests usability issues or unclear value messaging.

## Recommendations

- Make homepage navigation more intuitive
- Highlight product benefits earlier in the funnel
- Simplify checkout steps to reduce friction
- Test small changes through A/B testing

## Tools Used

- Python
- Pandas
- Matplotlib

## Output

A CSV summary and a chart showing drop-off at each funnel stage were created to support the analysis.
