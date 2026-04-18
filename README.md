<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KRYA Shopping Mall - Official</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js"></script>
    <style>
        :root { --primary: #fbbf24; --bg: #0b1120; --card: #1e293b; --text: #f8fafc; --accent: #10b981; }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Roboto, sans-serif; }
        body { background: var(--bg); color: var(--text); min-height: 100vh; overflow-x: hidden; }

        /* Navigation */
        .navbar { background: var(--card); padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 1000; border-bottom: 1px solid #334155; }
        .logo { color: var(--primary); font-size: 24px; font-weight: 800; letter-spacing: 2px; }

        /* Auth Screen */
        .auth-container { height: 90vh; display: flex; justify-content: center; align-items: center; }
        .auth-card { background: var(--card); padding: 30px; border-radius: 20px; width: 90%; max-width: 400px; border: 1px solid rgba(251, 191, 36, 0.3); text-align: center; }
        
        input, select { width: 100%; padding: 12px; margin: 10px 0; border-radius: 10px; border: 1px solid #334155; background: #0f172a; color: white; }
        .btn { width: 100%; padding: 12px; border-radius: 10px; border: none; font-weight: bold; cursor: pointer; transition: 0.3s; }
        .btn-primary { background: var(--primary); color: #000; }
        .btn-success { background: var(--accent); color: #fff; }

        /* Product Grid */
        .main-container { padding: 20px; max-width: 1200px; margin: auto; }
        .product-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 20px; margin-top: 20px; }
        .product-card { background: var(--card); border-radius: 15px; padding: 15px; border: 1px solid #334155; transition: 0.3s; }
        .product-card:hover { transform: translateY(-5px); border-color: var(--primary); }
        .product-img { width: 100%; height: 140px; object-fit: cover; border-radius: 10px; margin-bottom: 10px; }
        .price { color: var(--primary); font-weight: bold; font-size: 1.2rem; }

        /* Cart & Admin Sections */
        .section-title { border-left: 4px solid var(--primary); padding-left: 10px; margin: 20px 0; font-size: 22px; }
        .hidden { display: none !important; }

        /* Floating Cart Icon */
        .cart-float { position: fixed; bottom: 20px; right: 20px; background: var(--primary); color: #000; width: 60px; height: 60px; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-size: 24px; cursor: pointer; box-shadow: 0 5px 15px rgba(0,0,0,0.4); }
        
        /* Admin User Table */
        table { width: 100%; border-collapse: collapse; margin-top: 15px; background: var(--card); }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #334155; }
        
        @media (max-width: 600px) {
            .product-grid { grid-template-columns: repeat(2, 1fr); gap: 10px; }
        }
    </style>
</head>
<body>

<div class="navbar" id="main-nav" class="hidden">
    <div class="logo">KRYA</div>
    <div class="nav-icons">
        <i class="fas fa-home" onclick="showSection('home-view')" style="margin-right:20px; cursor:pointer;"></i>
        <i class="fas fa-user-shield" id="admin-icon" onclick="showSection('admin-view')" style="margin-right:20px; cursor:pointer; display:none;"></i>
        <i class="fas fa-sign-out-alt" onclick="location.reload()" style="color:#ef4444; cursor:pointer;"></i>
    </div>
</div>

<div id="auth-view" class="auth-container">
    <div class="auth-card">
        <h2 style="color:var(--primary); margin-bottom:15px;">MALL LOGIN</h2>
        <div id="email-step">
            <input type="email" id="user-email" placeholder="Email Address">
            <button class="btn btn-primary" onclick="sendOTP()">Get OTP</button>
        </div>
        <div id="otp-step" class="hidden">
            <input type="number" id="otp-input" placeholder="Enter 6-digit OTP">
            <button class="btn btn-primary" onclick="verifyOTP()">Verify & Enter</button>
        </div>
        <p id="status-msg" style="margin-top:10px; font-size:12px;"></p>
    </div>
</div>

<div id="home-view" class="main-container hidden">
    <h2 class="section-title">New Arrivals</h2>
    <div class="product-grid" id="product-list">
        </div>
</div>

<div id="cart-view" class="main-container hidden">
    <h2 class="section-title">My Cart</h2>
    <div id="cart-items"></div>
    <div style="margin-top:20px; background:var(--card); padding:20px; border-radius:15px;">
        <h3>Total: ₹<span id="cart-total">0</span></h3>
        <button class="btn btn-success" style="margin-top:15px;" onclick="checkout()">Pay via UPI</button>
    </div>
</div>

<div id="admin-view" class="main-container hidden">
    <h2 class="section-title">Admin Control Room</h2>
    
    <div class="auth-card" style="max-width:100%; text-align:left; margin-bottom:30px;">
        <h3>Add New Product</h3>
        <input type="text" id="p-name" placeholder="Product Name">
        <input type="number" id="p-price" placeholder="Price (INR)">
        <input type="text" id="p-img" placeholder="Image URL (Unsplash link)">
        <button class="btn btn-primary" onclick="addProduct()">Publish Product</button>
    </div>

    <h3>Manage Users</h3>
    <div style="overflow-x:auto;">
        <table id="user-table">
            <thead>
                <tr><th>Email</th><th>Handle</th><th>Action</th></tr>
            </thead>
            <tbody id="user-list-body"></tbody>
        </table>
    </div>
</div>

<div class="cart-float" id="cart-btn" class="hidden" onclick="showSection('cart-view')">
    <i class="fas fa-shopping-bag"></i>
    <span id="cart-count" style="position:absolute; top:0; right:0; background:red; color:white; font-size:12px; padding:2px 6px; border-radius:50%;">0</span>
</div>

<script type="module">
    import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
    import { getFirestore, doc, setDoc, getDoc, collection, addDoc, query, orderBy, onSnapshot, getDocs, updateDoc } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

    // --- CONFIGURATION ---
    const firebaseConfig = {
      apiKey: "AIzaSyCBC5iztNy0P-4-vY6Djec5ff26mTtJk30",
      authDomain: "sample-firebase-ai-app-37d2b.firebaseapp.com",
      projectId: "sample-firebase-ai-app-37d2b",
      storageBucket: "sample-firebase-ai-app-37d2b.firebasestorage.app",
      messagingSenderId: "652996597348",
      appId: "1:652996597348:web:6bfed4775ccb1c9572b171"
    };

    const app = initializeApp(firebaseConfig);
    const db = getFirestore(app);
    emailjs.init("msEHMlMxmjBbBoqnn");

    let generatedOTP;
    let currentUser = null;
    let cart = [];
    const ADMIN_EMAIL = "your-admin-email@gmail.com"; // इसे अपने ईमेल से बदलें

    // --- NAVIGATION LOGIC ---
    window.showSection = (id) => {
        ['auth-view', 'home-view', 'cart-view', 'admin-view'].forEach(s => {
            document.getElementById(s).classList.add('hidden');
        });
        document.getElementById(id).classList.remove('hidden');
    };

    // --- AUTH SYSTEM ---
    window.sendOTP = function() {
        const email = document.getElementById('user-email').value;
        if(!email.includes('@')) return alert("Enter valid email");
        
        generatedOTP = Math.floor(100000 + Math.random() * 900000);
        emailjs.send('service_gls676h', 'template_6teuhl4', { email: email, otp: generatedOTP })
            .then(() => {
                document.getElementById('email-step').classList.add('hidden');
                document.getElementById('otp-step').classList.remove('hidden');
            });
    };

    window.verifyOTP = async function() {
        const input = document.getElementById('otp-input').value;
        if(input == generatedOTP) {
            const email = document.getElementById('user-email').value;
            const uid = btoa(email);
            const userSnap = await getDoc(doc(db, "users", uid));
            
            if(!userSnap.exists()) {
                await setDoc(doc(db, "users", uid), { email: email, handle: "@user"+Math.floor(Math.random()*1000), role: email === ADMIN_EMAIL ? 'admin' : 'user' });
            }
            
            currentUser = { uid, email, ...(userSnap.data() || {role: 'user'}) };
            loginSuccess();
        }
    };

    function loginSuccess() {
        showSection('home-view');
        document.getElementById('main-nav').classList.remove('hidden');
        document.getElementById('cart-btn').classList.remove('hidden');
        if(currentUser.email === ADMIN_EMAIL || currentUser.role === 'admin') {
            document.getElementById('admin-icon').style.display = 'block';
            loadAdminData();
        }
        loadProducts();
    }

    // --- MALL LOGIC ---
    function loadProducts() {
        onSnapshot(collection(db, "products"), (snap) => {
            const list = document.getElementById('product-list');
            list.innerHTML = "";
            snap.forEach(d => {
                const p = d.data();
                list.innerHTML += `
                    <div class="product-card">
                        <img src="${p.img}" class="product-img">
                        <h4>${p.name}</h4>
                        <p class="price">₹${p.price}</p>
                        <button class="btn btn-primary" onclick="addToCart('${p.name}', ${p.price})">Add to Cart</button>
                    </div>
                `;
            });
        });
    }

    window.addToCart = (name, price) => {
        cart.push({name, price});
        updateCartUI();
    };

    function updateCartUI() {
        document.getElementById('cart-count').innerText = cart.length;
        const cartItems = document.getElementById('cart-items');
        let total = 0;
        cartItems.innerHTML = "";
        cart.forEach((item, idx) => {
            total += item.price;
            cartItems.innerHTML += `<div style="display:flex; justify-content:space-between; padding:10px; border-bottom:1px solid #334155;">
                <span>${item.name}</span> <span>₹${item.price}</span>
            </div>`;
        });
        document.getElementById('cart-total').innerText = total;
    }

    window.checkout = () => {
        const total = document.getElementById('cart-total').innerText;
        if(total == 0) return alert("Cart is empty");
        
        // UPI Deep Link (Legal & Free)
        // मुकेश जी, यहाँ 'your-upi-id@okicici' की जगह अपनी असली UPI ID डालें।
        const upiID = "your-upi-id@okicici"; 
        const name = "KRYA Mall";
        const upiUrl = `upi://pay?pa=${upiID}&pn=${name}&am=${total}&cu=INR`;
        
        window.location.href = upiUrl;
    };

    // --- ADMIN LOGIC ---
    window.addProduct = async () => {
        const name = document.getElementById('p-name').value;
        const price = Number(document.getElementById('p-price').value);
        const img = document.getElementById('p-img').value;

        if(!name || !price) return alert("Details भरें");
        await addDoc(collection(db, "products"), { name, price, img });
        alert("Product Added!");
    };

    async function loadAdminData() {
        const usersSnap = await getDocs(collection(db, "users"));
        const tbody = document.getElementById('user-list-body');
        tbody.innerHTML = "";
        usersSnap.forEach(u => {
            const data = u.data();
            tbody.innerHTML += `
                <tr>
                    <td>${data.email}</td>
                    <td><input type="text" value="${data.handle}" id="h-${u.id}" style="width:100px; padding:5px;"></td>
                    <td><button onclick="updateUser('${u.id}')" class="btn btn-success" style="padding:5px 10px;">Save</button></td>
                </tr>
            `;
        });
    }

    window.updateUser = async (uid) => {
        const newHandle = document.getElementById(`h-${uid}`).value;
        await updateDoc(doc(db, "users", uid), { handle: newHandle });
        alert("User Profile Updated!");
    };

</script>
</body>
</html>
