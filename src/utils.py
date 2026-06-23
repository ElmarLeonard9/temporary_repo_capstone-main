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