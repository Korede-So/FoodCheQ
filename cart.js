// CART FUNCTIONALITY
function updateCartCount() {
  const cart = JSON.parse(localStorage.getItem("cart")) || [];
  const count = cart.reduce((sum, item) => sum + item.qty, 0);
  const badgeDesktop = document.getElementById("cartCount");
  const badgeMobile = document.getElementById("cartCountMobile");
  if (badgeDesktop) badgeDesktop.textContent = count;
  if (badgeMobile) badgeMobile.textContent = count;
}

function addToCart(product) {
  let cart = JSON.parse(localStorage.getItem("cart")) || [];
  const existing = cart.find(item => item.name === product.name);
  if (existing) {
    existing.qty += product.qty;
  } else {
    cart.push(product);
  }
  localStorage.setItem("cart", JSON.stringify(cart));
  updateCartCount();
}

// WISHLIST FUNCTIONALITY
function updateWishlistCount() {
  const wishlist = JSON.parse(localStorage.getItem("wishlist")) || [];
  const count = wishlist.length;
  const badgeDesktop = document.getElementById("wishlistCount");
  const badgeMobile = document.getElementById("wishlistCountMobile");
  if (badgeDesktop) badgeDesktop.textContent = count;
  if (badgeMobile) badgeMobile.textContent = count;
}

function addToWishlist(product) {
  let wishlist = JSON.parse(localStorage.getItem("wishlist")) || [];
  const existing = wishlist.find(item => item.name === product.name);
  if (!existing) {
    wishlist.push(product);
    localStorage.setItem("wishlist", JSON.stringify(wishlist));
    updateWishlistCount();
    alert(product.name + " added to wishlist!");
  } else {
    alert(product.name + " is already in your wishlist!");
  }
}

// EVENT LISTENERS
document.addEventListener("DOMContentLoaded", () => {
  // Cart buttons
  document.querySelectorAll(".add-to-cart").forEach(btn => {
    btn.addEventListener("click", function() {
      const product = {
        name: this.dataset.name,
        price: parseFloat(this.dataset.price),
        image: this.dataset.image,
        qty: parseInt(this.dataset.qty)
      };
      addToCart(product);
      alert(product.name + " added to cart!");
    });
  });

  // Wishlist buttons
  document.querySelectorAll(".add-to-wishlist").forEach(btn => {
    btn.addEventListener("click", function() {
      const product = {
        name: this.dataset.name,
        price: parseFloat(this.dataset.price),
        image: this.dataset.image
      };
      addToWishlist(product);
    });
  });

  // Initialize badges
  updateCartCount();
  updateWishlistCount();
});
