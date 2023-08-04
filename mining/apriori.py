import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

def perform_association_rule_mining():
    # Sample dataset (transaction data)
    data = {'TransactionID': [1, 1, 1, 2, 2, 3, 3, 3, 4, 4],
            'Item': ['A', 'B', 'C', 'A', 'B', 'A', 'C', 'D', 'B', 'C']}
    df = pd.DataFrame(data)

    # Perform one-hot encoding (convert the data into a binary matrix)
    one_hot_encoded = df.pivot_table(index='TransactionID', columns='Item', aggfunc=lambda x: 1, fill_value=0)

    # Apply Apriori algorithm to find frequent itemsets
    frequent_itemsets = apriori(one_hot_encoded, min_support=0.2, use_colnames=True)

    # Generate association rules
    association_rules_df = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.5)

    print("Frequent Itemsets:")
    print(frequent_itemsets)

    print("\nAssociation Rules:")
    print(association_rules_df)

if __name__ == "__main__":
    perform_association_rule_mining()

