<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>KRYX PRO - क्रांतिकारी मॉल</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root { --amz-blue: #232f3e; --amz-orange: #febd69; --bg: #eaeded; --card-bg: #ffffff; }

        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Arial, sans-serif; }
        body { background: var(--bg); color: #0f1111; overflow-x: hidden; padding-bottom: 70px; }

        /* टॉप हेडर अमेज़न स्टाइल */
        .header { background: var(--amz-blue); padding: 10px 15px; color: white; display: flex; flex-direction: column; gap: 8px; }
        .header-top { display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 20px; font-weight: bold; color: white; }
        .logo span { color: var(--amz-orange); }
        .search-box { background: white; border-radius: 4px; display: flex; overflow: hidden; }
        .search-box input { flex: 1; border: none; padding: 10px; outline: none; }
        .search-btn { background: var(--amz-orange); padding: 10px 15px; border: none; }

        /* हीरो बैनर */
        .hero-banner { width: 100%; height: 160px; background: linear-gradient(to bottom, transparent, var(--bg)), url('https://via.placeholder.com/800x400/febd69/000000?text=KRYX+Revolutionary+Deals'); background-size: cover; }

        /* अमेज़न स्टाइल कार्ड्स */
        .container { padding: 0 10px; margin-top: -40px; }
        .amz-card { background: var(--card-bg); padding: 15px; border-radius: 4px; margin-bottom: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
        .amz-card h3 { font-size: 16px; margin-bottom: 12px; font-weight: bold; }
        
        /* 4-प्रोडक्ट ग्रिड (अमेज़न स्टाइल) */
        .grid-4 { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
        .grid-item { text-align: left; cursor: pointer; }
        .grid-item img { width: 100%; height: 100px; object-fit: cover; border-radius: 2px; }
        .grid-item p { font-size: 12px; margin-top: 4px; color: #565959; }

        /* डील सेक्शन */
        .deal-item { display: flex; flex-direction: column; }
        .deal-img { width: 100%; height: 200px; object-fit: contain; background: #f7f7f7; }
        .tag { background: #cc0c39; color: white; padding: 4px 8px; font-size: 11px; width: fit-content; border-radius: 2px; margin: 8px 0; }

        /* बॉटम नेविगेशन */
        .nav-bar { position: fixed; bottom: 0; width: 100%; background: white; display: flex; padding: 12px 0; border-top: 1px solid #ddd; z-index: 1000; }
        .nav-item { flex: 1; text-align: center; color: #0f1111; font-size: 11px; text-decoration: none; }
        .nav-item i { font-size: 20px; margin-bottom: 4px; }
        .nav-item.active { color: #007185; }
    </style>
</head>
<body>

    <div class="header">
        <div class="header-top">
            <div class="logo">KRYX<span>.in</span></div>
            <div>मुकेश <i class="fas fa-chevron-right" style="font-size: 10px;"></i></div>
        </div>
        <div class="search-box">
            <input type="text" placeholder="KRYX पर सर्च करें...">
            <button class="search-btn"><i class="fas fa-search"></i></button>
        </div>
    </div>

    <div class="hero-banner"></div>

    <div class="container">
        <div class="amz-card">
            <h3>जहाँ आपने छोड़ा था, वहीं से शुरू करें</h3>
            <div class="grid-4">
                <div class="grid-item">
                    <img src="https://via.placeholder.com/150/000/fff?text=Tech">
                    <p>टेक एक्सेसरीज</p>
                </div>
                <div class="grid-item">
                    <img src="https://via.placeholder.com/150/333/fff?text=Fashion">
                    <p>फैशन</p>
                </div>
                <div class="grid-item">
                    <img src="https://via.placeholder.com/150/666/fff?text=Tools">
                    <p>टूल्स</p>
                </div>
                <div class="grid-item">
                    <img src="https://via.placeholder.com/150/999/fff?text=Decor">
                    <p>होम डेकोर</p>
                </div>
            </div>
        </div>

        <div class="amz-card">
            <h3>आज की क्रांतिकारी डील</h3>
            <div class="deal-item">
                <img src="https://via.placeholder.com/300/f1f3f6/000?text=KRYA+PRO+Logo" class="deal-img">
                <span class="tag">50% तक की छूट</span>
                <p style="font-size: 14px;">KRYA प्रो डिजाइन सर्विसेज - सिर्फ़ आज के लिए</p>
                <p style="color: #565959; font-size: 12px; margin-top: 4px;">और देखें</p>
            </div>
        </div>
    </div>

    <nav class="nav-bar">
        <a href="#" class="nav-item active"><i class="fas fa-home"></i><br>होम</a>
        <a href="#" class="nav-item"><i class="fas fa-user"></i><br>प्रोफाइल</a>
        <a href="#" class="nav-item"><i class="fas fa-shopping-cart"></i><br>कार्ट</a>
        <a href="#" class="nav-item"><i class="fas fa-bars"></i><br>मेनू</a>
    </nav>

</body>
</html>
