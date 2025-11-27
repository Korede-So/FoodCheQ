import os
import re

# Directory
folder = r"c:\Users\Admin1\Desktop\New Project\FoodCheQ\product-category"

# Already updated files
updated = ['peppermint.html', 'aloe-vera.html', 'ashwagandha.html', 'bacopa-monneri.html', 
           'bamboo-leaf.html', 'baobab.html', 'black-pepper.html']

# Remaining files to process
remaining = ['blackthorn.html', 'butterbur.html', 'calendula.html', 'cinnamon.html', 
             'clove.html', 'dandelion.html', 'ginger.html', 'ginkgo.html', 'ginseng.html',
             'green-tea.html', 'guduchi.html', 'guggula.html', 'holy-basil.html', 
             'kava-kava.html', 'lavender.html', 'lemon-balm.html', 'milk-thistle.html', 
             'mint-tea.html', 'mullein.html', 'oregano.html', 'parsley.html', 
             'passion.html', 'skullcap.html', 'tumeric.html']

count = 0
for filename in remaining:
    filepath = os.path.join(folder, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filename}")
        continue
    
    # Read file
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract product info from current product section
    # Pattern: from <div class="container product-section"> to <h3 id="related-title">
    pattern = r'<div class="container product-section">.*?<h3 id="related-title">'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        # Try alternate pattern for section tag
        pattern = r'<section class="container[^>]*product-section"[^>]*>.*?<h3 id="related-title">'
        match = re.search(pattern, content, re.DOTALL)
    
    if match:
        old_section = match.group(0)[:-len('<h3 id="related-title">')]  # Remove trailing h3 tag
        
        # Extract key data
        title_match = re.search(r'<h2[^>]*>([^<]+)</h2>', old_section)
        title = title_match.group(1).strip() if title_match else "Product"
        
        img_match = re.search(r'<img[^>]*src="([^"]*)"[^>]*alt="([^"]*)"', old_section)
        img_src = img_match.group(1) if img_match else "/image/placeholder.png"
        img_alt = img_match.group(2) if img_match else "Product"
        
        price_match = re.search(r'<p class="price">([^<]+)</p>', old_section)
        price = price_match.group(1).strip() if price_match else "$0.00"
        
        desc_match = re.search(r'<h4>Product Description</h4>\s*<p>(.*?)</p>', old_section, re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else "Product description."
        
        benefits_match = re.search(r'<h4>Health Benefits</h4>\s*<ul>(.*?)</ul>', old_section, re.DOTALL)
        if benefits_match:
            benefits_html = benefits_match.group(1).strip()
            # Convert <li> to <li class="list-group-item">
            benefits_html = benefits_html.replace('<li>', '<li class="list-group-item">')
        else:
            benefits_html = "<li class=\"list-group-item\">Supports overall wellness</li>"
        
        # Build new section
        new_section = f'''  <!-- Product Section -->
  <section class="container py-5 product-section">
    <div class="row align-items-center g-4">
      <!-- Product Image -->
      <div class="col-md-6 text-center">
        <img src="{img_src}" class="img-fluid rounded shadow-sm product-img" alt="{img_alt}">
      </div>
      <!-- Product Content -->
      <div class="col-md-6 product-content">
        <h2 class="fw-bold mb-3" style="color: var(--main-green);">{title}</h2>
        <p class="price h4 text-success fw-bold">{price}</p>
        <div class="d-flex gap-2 flex-wrap mt-3">
          <button class="btn btn-green flex-fill"><i class="fa-solid fa-cart-shopping me-1"></i> Add to Cart</button>
          <button class="btn btn-outline-success flex-fill"><i class="fa-regular fa-heart me-1"></i> Wishlist</button>
          <button class="btn btn-outline-success flex-fill"><i class="fa-solid fa-mug-hot me-1"></i> Free Sample</button>
        </div>
      </div>
    </div>

    <!-- Product Details -->
    <div class="details mt-5">
      <h4 class="fw-bold mb-3">Product Description</h4>
      <p>{description}</p>
      
      <h4 class="fw-bold mt-4 mb-3">Health Benefits</h4>
      <ul class="list-group list-group-flush">
{benefits_html}
      </ul>
    </div>
  </section>

  <h3 id="related-title">Related Items</h3>'''
        
        # Replace in content
        new_content = content.replace(match.group(0), new_section + '<h3 id="related-title">')
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        count += 1
        print(f"✓ Updated: {filename}")
    else:
        print(f"⚠ Could not find product section in: {filename}")

print(f"\nTotal updated: {count}/{len(remaining)}")
