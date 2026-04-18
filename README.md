<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>KRYA PRO SUPER APP</title>
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    
    <style>
        :root { --primary: #fbbf24; --bg: #0b1120; --card: #1e293b; --text: #f8fafc; --pink: #ff477e; }

        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', sans-serif; }
        
        body, html { height: 100%; width: 100%; background: var(--bg); color: var(--text); overflow: hidden; }

        #app-root { display: flex; flex-direction: column; height: 100vh; width: 100%; }

        .header { background: var(--card); padding: 12px 15px; display: flex; justify-content: space-between; border-bottom: 1px solid #334155; align-items: center; }
        
        .news-ticker { background: #1e3a8a; color: var(--primary); padding: 4px; font-size: 13px; font-weight: bold; }

        .main-content { flex: 1; overflow-y: auto; padding: 15px; padding-bottom: 80px; }

        /* ID कार्ड का नया एडजस्टेड साइज */
        .id-card { 
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); 
            border: 1.5px solid var(--primary); 
            border-radius: 12px; 
            padding: 12px; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
            max-width: 350px; /* चौड़ाई फिक्स की गई */
            margin: 0 auto;
        }
        .id-photo { width: 65px; height: 80px; border-radius: 6px; border: 1px solid var(--primary); object-fit: cover; }
        .u-info h4 { color: var(--primary); font-size: 16px; }
        .u-info p { font-size: 11px; color: #94a3b8; margin-top: 2px; }

        /* मॉल एसेट स्टाइल (Flipkart Style) */
        .mall-section { margin-top: 20px; }
        .mall-title { color: var(--primary); font-size: 14px; font-weight: bold; margin-bottom: 10px; display: flex; justify-content: space-between; }
        .mall-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
        .product-card { background: var(--card); border-radius: 8px; padding: 8px; border: 1px solid #334155; }
        .p-img { width: 100%; height: 100px; background: #0f172a; border-radius: 4px; margin-bottom: 8px; object-fit: contain; }
        .p-name { font-size: 12px; font-weight: bold; color: var(--text); height: 32px; overflow: hidden; }
        .p-price { color: var(--primary); font-size: 14px; font-weight: bold; margin-top: 4px; }

        /* नेविगेशन */
        .nav-bar { position: fixed; bottom: 0; width: 100%; background: var(--card); display: flex; padding: 10px 0; border-top: 1px solid #334155; z-index: 100; }
        .nav-item { flex: 1; text-align: center; color: #94a3b8; font-size: 11px; cursor: pointer; }
        .nav-item.active { color: var(--primary); }

        .btn-p { background: var(--primary); color: black; border: none; padding: 12px; border-radius: 8px; font-weight: bold; width: 100%; cursor: pointer; margin-top: 15px; }
    </style>
</head>
<body>

<div id="app-root">
    <div class="header">
        <b style="font-size: 18px;">KRYA <span style="color:var(--primary);">PRO</span></b>
        <span>🪙 <span id="balance">700</span></span>
    </div>

    <div class="news-ticker">
        <marquee scrollamount="5">🚀 क्रांतिकारी मॉल लाइव है! सेलर्स अपनी डायरेक्टरी जोड़ना शुरू करें | मुकेश राय...</marquee>
    </div>

    <div class="main-content">
        <div id="tab-home">
            <div class="id-card">
                <div style="display:flex; gap:12px; align-items: center;">
                    <img id="card-img" src="https://via.placeholder.com/65x80" class="id-photo">
                    <div class="u-info">
                        <h4 id="u-name">मुकेश राय</h4>
                        <p id="u-skill"><i class="fas fa-code"></i> टेक स्पेशलिस्ट</p>
                        <p id="u-addr"><i class="fas fa-map-marker-alt"></i> बांका, बिहार</p>
                    </div>
                </div>
            </div>

            <div class="mall-section">
                <div class="mall-title">
                    <span>🛍️ क्रांतिकारी मॉल (Products)</span>
                    <span style="color:var(--primary); font-size: 11px;">View All</span>
                </div>
                
                <div class="mall-grid">
                    <div class="product-card">
                        <img src="https://via.placeholder.com/100" class="p-img">
                        <div class="p-name">Premium KRYA Logo Design</div>
                        <div class="p-price">₹499</div>
                    </div>
                    <div class="product-card">
                        <img src="https://via.placeholder.com/100" class="p-img">
                        <div class="p-name">Digital Entrepreneur Course</div>
                        <div class="p-price">₹999</div>
                    </div>
                </div>
            </div>

            <button class="btn-p" onclick="go('chat')">🚀 सेलर्स से चैट करें</button>
        </div>
    </div>

    <div class="nav-bar">
        <div class="nav-item active" onclick="go('home')"><i class="fas fa-home"></i><br>होम</div>
        <div class="nav-item" onclick="alert('मॉल पेज...')"><i class="fas fa-store"></i><br>मॉल</div>
        <div class="nav-item" onclick="go('chat')"><i class="fas fa-comments"></i><br>चैट</div>
        <div class="nav-item" onclick="alert('प्रोफाइल...')"><i class="fas fa-user"></i><br>प्रोफाइल</div>
    </div>
</div>

<script>
    function go(t) {
        // नेविगेशन लॉजिक यहाँ आएगा
        if(t === 'chat') alert('चैट सिस्टम लोड हो रहा है...');
    }
</script>
</body>
</html>
