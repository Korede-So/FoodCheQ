function updateCartCount() {
  const cart = JSON.parse(localStorage.getItem("cart")) || [];
  document.getElementById("cartCount").textContent = cart.reduce((sum, item) => sum + item.qty, 0);
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

// Run on every page load
document.addEventListener("DOMContentLoaded", updateCartCount);



function updateCartCount() {
  const cart = JSON.parse(localStorage.getItem("cart")) || [];
  const count = cart.reduce((sum, item) => sum + item.qty, 0);
  const badge = document.getElementById("cartCount");
  if (badge) badge.textContent = count;
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

// Attach event listeners to all Add to Cart buttons
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

// Initialize cart badge on page load
updateCartCount();

