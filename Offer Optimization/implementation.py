import pandas as pd

# Bid Optimization Function
def optimize_bid(row):
    rule_1 = row['breakeven_acos'] + 0.10
    rule_2 = row['breakeven_acos'] - 0.05
    rule_3 = 1.25 * row['breakeven_acos']
    rule_4 = 2.75 * row['breakeven_acos']
    rule_5 = 2.5 * row['breakeven_acos']

    new_effective_bid = row['effective_bid']
    change_type = 'no change'
    new_state = row['state']

    if row['acos'] > rule_1:
        # Decrease by 25%
        new_effective_bid *= 0.75
        change_type = 'bid decrease'

    elif row['acos'] < rule_2 and row['units_ordered'] >= 2:
        # Increase by 15%
        new_effective_bid *= 1.15
        change_type = 'bid increase'
    
    elif row['sales'] == 0 and row['cost'] > rule_3:
        # Decrease by 25%
        new_effective_bid *= 0.75
        change_type = 'bid decrease'

    elif row['acos'] > rule_4:
        new_state = 'paused'
        change_type = 'paused since acos is greater'

    elif row['sales'] == 0 and row['cost'] > rule_5:
        new_state = 'paused'
        change_type = 'paused (no sales)'
    
    final_bid = new_effective_bid / row['top_search_multiplier']

    return final_bid, change_type



# Read Performance Data
performance_data = pd.read_excel('wa2_keyword_performance.xlsx')

# Get the most recent date and the date 30 days before
most_recent_date = performance_data['date'].max()
start_date = most_recent_date - pd.Timedelta(days = 30)

# Filter data in the date ranges
filtered_performance_data = performance_data[(performance_data['date'] >= start_date)]

# Aggregate Metrics (help from google on this part)
aggregated_metrics = filtered_performance_data.groupby('keyword_id').agg({
    'impressions': 'sum',
    'clicks': 'sum',
    'cost': 'sum',
    'sales': 'sum',
    'units_ordered': 'sum'
}).reset_index()

# Calculate ACoS (Advertising Cost of Sales)
aggregated_metrics['acos'] = aggregated_metrics['cost'] / aggregated_metrics['sales']

# Keep unaggregated values
aggregated_metrics = aggregated_metrics.merge(filtered_performance_data[['keyword_id', 'match_type', 'campaign_id', 'campaign_name', 'short_id', 'top_search_multiplier']], on = 'keyword_id', how = 'left').drop_duplicates()

# Read Bid File
bid_data = pd.read_excel('wa2_keyword_bid.xlsx')

# Map Bid onto the Aggregated Performance Table via keyword_id
aggregated_metrics = aggregated_metrics.merge(bid_data[['keyword_id', 'bid', 'state']], on = "keyword_id", how = "left")

# Calculate effective_bid, given bid and top_search_multiplier
aggregated_metrics['effective_bid'] = aggregated_metrics['bid'] * aggregated_metrics['top_search_multiplier']

# Read Product Database
product_data = pd.read_excel('wa2_product_database.xlsx')

# Apply bid optimization rules and propose a new effective_bid value
# optimize_bid()

# Output File
output = aggregated_metrics[['keyword_id', 'final_proposed_bid', 'final_proposed_state', 'change_type']]
output.to_excel('optimized_bids.xlsx', index=False)

# use short_id