# This file functions to store all functions that have been created for analysis purposes.
def rename_cat(category):
    if category == "Lemari": return "Wardrobe"
    elif category == "lmri": return "Wardrobe"
    elif category == "Sofa": return "Sofa & Sofabed"
    elif category == "sofabed": return "Sofa & Sofabed"
    elif category == "Dekorasi": return "Decoration"
    elif category == "Kursi Kerja": return "Office Chair"
    elif category == "Meja Makan": return "Dining Table"
    else: return category

def fill_ret_cost(category):
    if category == "Decoration": return 170000
    elif category == "Office Chair": return 480000
    elif category == "Dining Table": return 1150000
    elif category == "Bed": return 1480000
    elif category == "Sofa & Sofabed": return 1850000
    else: return 2400000

def extract_city(store_name):
    if 'Mobile App' in store_name or 'Website' in store_name:
        return 'Online'
    if store_name.startswith('DEC '):
        parts = store_name.split()
        if len(parts) >= 3:
            return ' '.join(parts[1:-1])
    return 'Unknown'

def print_test(name, stat, p, sig_msg, insig_msg, stat_label='Stat'):
    sig = sig_msg if p < 0.05 else insig_msg
    print(f"\n── {name} ──\n   {stat_label} = {stat:.4f}, p = {p:.4f}\n   → {sig}")