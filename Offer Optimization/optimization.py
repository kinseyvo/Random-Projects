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
