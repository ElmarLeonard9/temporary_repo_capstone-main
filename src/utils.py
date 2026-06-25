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