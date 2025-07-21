"""
Problem statement:
We’ve noticed that as items sell, their popularity increases due to social proof.
If the probability of selling changes to p = 0.3 + 0.02k,
where k is the number of users who previously sold an item.

How would you compute the expected number of successful sales
for the first 10 sellers of a particular product?

E[Si] = 0.3+0.02*E[Si-1] where E[Si] is the expected number of successful sales for the i-th seller.

This script calculates the expected number of successful sales for a given number of sellers.
"""
#%%
def calculate_expected_sales(num_sellers):
    """
    Computes the expected number of successful sales for a given number of sellers
    based on the probability p = 0.3 + 0.02 * k, where k is the number of previous successful sales.

    Args:
        num_sellers (int): The total number of sellers to consider.

    Returns:
        tuple: A tuple containing:
               - list: A list of the expected probability of success for each seller.
               - float: The total expected number of successful sales.
    """

    if num_sellers <= 0:
        return [], 0.0

    # Initialize a list to store the expected probability of success for each seller.
    # dp[i] will store the expected probability of success for the (i+1)-th seller.
    # We will also keep track of the cumulative expected successful sales.
    expected_prob_per_seller = [0.0] * num_sellers
    cumulative_expected_successful_sales = 0.0

    # Base case for the first seller (k=0, as there are no previous sellers)
    # The probability for the first seller is p = 0.3 + 0.02 * 0 = 0.3
    expected_prob_per_seller[0] = 0.3
    cumulative_expected_successful_sales += expected_prob_per_seller[0]

    # Iterate through the remaining sellers
    for i in range(1, num_sellers):
        # For the i-th seller (index i), 'k' is the cumulative expected successful sales
        # from the previous 'i' sellers (up to index i-1).
        # The formula is p = 0.3 + 0.02 * k_expected
        current_expected_prob = 0.3 + 0.02 * cumulative_expected_successful_sales
        expected_prob_per_seller[i] = current_expected_prob

        # Update the cumulative expected successful sales
        cumulative_expected_successful_sales += current_expected_prob

    return expected_prob_per_seller, cumulative_expected_successful_sales
#%%
# --- Main execution ---
if __name__ == "__main__":
    num_sellers_to_consider = 10
    expected_probs, total_expected_sales = calculate_expected_sales(num_sellers_to_consider)

    print(f"Expected probability of success for each of the first {num_sellers_to_consider} sellers:")
    for i, prob in enumerate(expected_probs):
        print(f"  Seller {i + 1}: {prob:.4f}")

    print(f"\nTotal expected number of successful sales for the first {num_sellers_to_consider} sellers: {total_expected_sales:.4f}")
