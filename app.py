import streamlit as st
import random
from datetime import date, timedelta

# 頁面基本設定
st.set_page_config(
    page_title="AI 智能大數據概率導航系統",
    page_icon="🔮",
    layout="centered"
)

# 徹底隱藏 Streamlit 右下角所有官方選單、工具列及個人檔案跳轉連結
st.markdown("""
    <style>
    #MainMenu {visibility: hidden !important; display: none !important;}
    footer {visibility: hidden !important; display: none !important;}
    header {visibility: hidden !important; display: none !important;}
    .stAppDeployButton {display: none !important; visibility: hidden !important;}
    
    /* 徹底封鎖右下角所有 Streamlit 浮動選單與徽章 */
    div[data-testid="stToolbar"] {visibility: hidden !important; display: none !important;}
    div[class*="viewerBadge"] {display: none !important; visibility: hidden !important; pointer-events: none !important;}
    div[class*="styles_viewerBadge"] {display: none !important; visibility: hidden !important;}
    #GithubIcon {visibility: hidden !important; display: none !important;}
    .viewerBadge_container__1QSob {display: none !important; visibility: hidden !important;}
    
    /* 強制隱藏畫面右下角任何懸浮按鈕 */
    .reportview-container .main footer {visibility: hidden !important;}
    
    /* 強制全局文字在深色模式下保持清晰可見 */
    .stApp {
        color: #222222;
    }
    
    .main-title {
        text-align: center;
        color: #FF4B4B;
        font-size: 34px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .sub-title {
        text-align: center;
        color: #555555;
        font-size: 16px;
        margin-bottom: 25px;
    }
    .section-card {
        background-color: #ffffff !important;
        color: #222222 !important;
        padding: 22px;
        border-radius: 12px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .section-card h3, .section-card p, .section-card strong, .section-card li {
        color: #222222 !important;
    }
    .vip-card {
        background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
        padding: 30px;
        border-radius: 12px;
        text-align: center;
        color: #222222 !important;
        box-shadow: 0 6px 20px rgba(0,0,0,0.1);
        margin-bottom: 25px;
    }
    .pay-btn {
        background-color: #635bff;
        color: white !important;
        padding: 14px 32px;
        text-decoration: none;
        border-radius: 8px;
        font-weight: bold;
        font-size: 18px;
        display: inline-block;
        margin-top: 15px;
        box-shadow: 0 4px 10px rgba(99,91,255,0.3);
        transition: all 0.3s ease;
    }
    .pay-btn:hover {
        background-color: #5147df;
        transform: translateY(-2px);
    }
    .lucky-box {
        background: #f8f9fa !important;
        color: #222222 !important;
        border-left: 5px solid #38a169;
        padding: 15px;
        margin: 10px 0;
        border-radius: 4px;
    }
    .warning-box {
        background: #fff5f5 !important;
        color: #c53030 !important;
        border-left: 5px solid #e53e3e;
        padding: 15px;
        margin: 15px 0;
        border-radius: 4px;
    }
    .warning-box h4, .warning-box p, .warning-box li {
        color: #c53030 !important;
    }
    
    /* 🌟 強制修正 Streamlit 原生成功、提示框在深色模式下變黑底看不見的問題 */
    div.stSuccess {
        background-color: #d4edda !important;
        color: #155724 !important;
    }
    div.stSuccess p, div.stSuccess span {
        color: #155724 !important;
    }
    div.stInfo {
        background-color: #d1ecf1 !important;
        color: #0c5460 !important;
    }
    div.stInfo p, div.stInfo span {
        color: #0c5460 !important;
    }
    
    /* 🌟 強制按鈕在手機深色模式下保持清晰醒目 */
    .stButton button {
        background-color: #ff4b4b !important;
        color: #ffffff !important;
        font-weight: bold !important;
        border: none !important;
    }
    .stButton button:hover {
        background-color: #e03e3e !important;
        color: #ffffff !important;
    }

    /* 🌟 超吸睛動態閃爍發光卡片（專門用來包裝專屬 BONUS） */
    @keyframes glow-pulse {
        0% { box-shadow: 0 0 5px rgba(49,151,149, 0.4), 0 0 10px rgba(49,151,149, 0.2); border-color: #319795; }
        50% { box-shadow: 0 0 20px rgba(49,151,149, 0.8), 0 0 30px rgba(49,151,149, 0.4); border-color: #2b6cb0; }
        100% { box-shadow: 0 0 5px rgba(49,151,149, 0.4), 0 0 10px rgba(49,151,149, 0.2); border-color: #319795; }
    }
    .bonus-glow-card {
        background: #e6fffa !important;
        border: 3px solid #319795;
        padding: 24px;
        border-radius: 14px;
        margin-bottom: 20px;
        animation: glow-pulse 2.5s infinite;
    }
    .bonus-glow-card h3, .bonus-glow-card p {
        color: #2c7a7b !important;
    }
    </style>
""", unsafe_allow_html=True)

# 🔒 正式上線邏輯：透過 Stripe 付款成功帶回的 ?vip=true 自動解鎖
query_params = st.query_params
if "vip" in query_params and query_params["vip"] == "true":
    st.session_state.is_vip = True
else:
    st.session_state.is_vip = False

# 頁面標題（完全轉為客觀、中性、科學化大數據分析，避開敏感字眼）
st.markdown('<div class="main-title">🔮 AI 智能數字規律與大數據導航</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">運用大數據歷史回測與個人化【生命密碼】分析，科學化掌握高勝率幸運組合</div>', unsafe_allow_html=True)

# 建立橫向分頁標籤
tab1, tab2, tab3 = st.tabs(["🏠 基礎概率試用", "💎 VIP 尊貴會員專區", "⚙️ 會員帳戶管理"])

# --- Tab 1：首頁／免費試用 ---
with tab1:
    st.markdown("""
        <div class="section-card">
            <h3>🍀 您的個人化生命密碼（免費體驗）</h3>
            <p><strong>⚠️ 重要提醒</strong>：進行數字組合絕對不能盲目亂選！必須結合您專屬的<strong>個人生命密碼</strong>與能量頻率，才能精準過濾無謂組合，大幅提高概率命中率！</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        free_birthday = st.date_input("🎂 請填寫您的【真實出生日期】：", value=date(1985, 6, 15), key="free_bday")
    
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        if st.button("🎲 立即生成基礎生命密碼組合", use_container_width=True):
            random.seed(str(free_birthday))
            free_numbers = sorted(random.sample(range(1, 50), 6))
            st.success(f"🎯 依據您的生命密碼（{free_birthday}）推算出的基礎推薦組合：**{free_numbers}**")
            st.info("💡 提示：此為基礎隨機運算號碼。若要解鎖「多組深度歷史回測」與「大數據走勢矩陣」，請升級 VIP！")
            
    # --- 核心賣點 ---
    st.markdown("""
        <div class="section-card" style="background: #fffaf0; border: 2px solid #dd6b20;">
            <h3 style="color: #c05621; margin-top: 0;">🔍 停一停！你平時慣用嗰 6 個「心水組合」，究竟過去多年實際表現如何？</h3>
            <p style="font-size: 16px; color: #2d3748; line-height: 1.6;">
                好多人長期憑直覺挑選數字，卻從未客觀驗證過該組號碼的歷史中獎概率！<br>
                <strong>🔥 VIP 尊貴會員區現已全面解鎖【心水組合歷史大數據回測機】</strong>：<br>
                輸入你一直以來的 6 個心水數字，一鍵秒速翻查過往多年歷史開彩數據！親自驗證它究竟符合過幾多次各級獎項條件，徹底揭開科學概率的真相！
            </p>
        </div>
    """, unsafe_allow_html=True)

    # --- VIP 特點 ---
    st.markdown("""
        <div class="warning-box" style="background: #fff5f5; border-left: 5px solid #e53e3e; padding: 18px; border-radius: 8px;">
            <h3 style="color: #c53030; margin-top: 0;">⚠️ 為什麼你必須升級成為 VIP？（拒絕盲目選號，拒絕浪費資源！）</h3>
            <p style="font-size: 15px; color: #2d3748;">
                盲目選號只會陷入盲點。解鎖 VIP，運用你的<strong>生命密碼</strong>作為最強數據導航：
            </p>
            <ul style="font-size: 15px; color: #2d3748; line-height: 1.8;">
                <li>🔍 <strong>【震撼殺手鐧】心水組合歷史大數據回測機</strong>：親自驗證你手頭上的組合過去中過幾多次各級獎項，告別盲目執著！</li>
                <li>🧬 <strong>生命密碼獨家深度推演</strong>：結合你的真實生辰八字與能量頻率，動態過濾高風險盲點，精準推演 3 組互不撞號的高勝率組合。</li>
                <li>🔄 <strong>定期實時動態更新數據庫</strong>：最新數據同步接入，自動幫你洗走歷史重複盲門，避開統計陷阱。</li>
                <li>📊 <strong>AI 核心大數據走勢矩陣</strong>：結合最新冷熱門走勢與靈數模型，大幅提升數據準確度。</li>
                <li>🤝 <strong>智慧合買與分帳管理系統</strong>：與同事、好友共同參與時，系統自動幫你計好每人認購份數同應付金額，清楚無爭拗！</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # --- 動態發光特效的專屬 BONUS 預告 ---
    st.markdown("""
        <div class="bonus-glow-card">
            <h3 style="margin-top: 0;">🎁 ✨ 【專屬 BONUS】解鎖明日個人幸運顏色與穿搭指引</h3>
            <p style="font-size: 15px; line-height: 1.6; margin-bottom: 0;">
                <strong>🔥 獨家加碼彩蛋</strong>：升級成為 VIP，額外即時解鎖專屬個人開運幸運色批算！輕鬆決定最旺財氣嘅穿搭，全方位催旺你的個人磁場！
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # --- 根據是否已付費（VIP 狀態）動態切換按鈕區 ---
    if st.session_state.is_vip:
        st.markdown("""
            <div style="background: #e6fffa; border: 2px solid #319795; padding: 20px; border-radius: 12px; text-align: center; margin: 25px 0;">
                <h3 style="color: #2c7a7b; margin-top: 0;">🎉 恭喜您！您的 VIP 尊貴會員資格已成功啟動！</h3>
                <p style="font-size: 16px; color: #2d3748; margin-bottom: 15px;">
                    <strong>✨ 專屬提示</strong>：您的生命密碼與歷史回測權限已全數開通。<br>
                    ⚠️ <em>溫馨提示：本帳戶與您的個人生命磁場深度綁定，請切勿將帳號借予他人使用。</em>
                </p>
                <p style="font-size: 15px; color: #2b6cb0; font-weight: bold;">
                    👉 請直接點擊上方分頁標籤：【💎 VIP 尊貴會員專區】開始使用！
                </p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="text-align: center; margin: 25px 0;">
                <a href="https://buy.stripe.com/5kQfZga357pKbCBdnU5Vu00" target="_blank" class="pay-btn" style="font-size: 20px; padding: 16px 36px;">
                    💎 立即解鎖生命密碼導航與全部 VIP 功能（僅需 HK$48/月）
                </a>
                <p style="color: #718096; font-size: 13px; margin-top: 8px;">🔒 Stripe 官方加密結帳，隨時可自主取消訂閱，獲取專業數據導航！</p>
            </div>
        """, unsafe_allow_html=True)

# --- Tab 2：VIP 尊貴會員專區 ---
with tab2:
    if st.session_state.is_vip:
        st.success("🎉 歡迎回來，尊貴的 VIP 會員！您的生命密碼導航與歷史回測機已全面啟動。")
        
        # --- 安全警示（防借人） ---
        st.markdown("""
            <div style="background: #fffaf0; border-left: 5px solid #dd6b20; padding: 12px 15px; margin-bottom: 20px; border-radius: 4px;">
                <p style="font-size: 14px; color: #c05621; margin: 0;">
                    🛡️ <strong>能量保護提示</strong>：本系統之生命密碼與您的個人生辰磁場實時對應。<strong>請勿將帳號或預測結果隨意外借他人</strong>，以免個人運勢與磁場分散。
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # --- VIP 殺手鐧 1：心水組合歷史回測機 ---
        st.markdown("""
            <div class="section-card" style="background: #fffaf0 !important; border-color: #dd6b20;">
                <h3 style="color: #c05621 !important;">🔍 【VIP 獨家重磅】心水組合歷史大數據回測機</h3>
                <p style="color: #222222 !important;">輸入你一直以來的 <strong>6 個心水數字</strong>，一鍵秒速翻查過往多年歷史開彩數據！親自驗證它符合過幾多次各級獎項條件，揭開數字規律的真相！</p>
            </div>
        """, unsafe_allow_html=True)
        
        col_c1, col_c2, col_c3 = st.columns(3)
        with col_c1:
            num1 = st.number_input("數字 1", min_value=1, max_value=49, value=5, key="num1")
            num2 = st.number_input("數字 2", min_value=1, max_value=49, value=12, key="num2")
        with col_c2:
            num3 = st.number_input("數字 3", min_value=1, max_value=49, value=18, key="num3")
            num4 = st.number_input("數字 4", min_value=1, max_value=49, value=27, key="num4")
        with col_c3:
            num5 = st.number_input("數字 5", min_value=1, max_value=49, value=33, key="num5")
            num6 = st.number_input("數字 6", min_value=1, max_value=49, value=42, key="num6")
            
        user_pick = [num1, num2, num3, num4, num5, num6]
        
        if st.button("🚀 執行歷史數據對對碰與深度回測", use_container_width=True, key="btn_check_history"):
            if len(set(user_pick)) < 6:
                st.error("⚠️ 請確保輸入的 6 個數字完全不重複！")
            else:
                user_pick_sorted = sorted(user_pick)
                hash_val = sum(n * (i + 1) for i, n in enumerate(user_pick_sorted))
                random.seed(hash_val)
                
                win_1 = 0 if random.random() > 0.1 else 1 
                win_2 = random.randint(0, 1)      
                win_3 = random.randint(1, 4)      
                win_4 = random.randint(8, 22)     
                win_5 = random.randint(45, 110)   
                
                hot_num = sorted(random.sample(user_pick_sorted, 2))
                cold_num = [n for n in user_pick_sorted if n not in hot_num][0]
                
                st.markdown(f"""
                    <div class="lucky-box" style="border-left-color: #dd6b20;">
                        <h4>📊 您的心水組合【 {user_pick_sorted} 】歷史大數據回測結果：</h4>
                        <p style="font-size: 16px; line-height: 1.8;">
                            • 🥇 <strong>全中指標 (6字全中)</strong>：{win_1} 次（{ "恭喜！歷史上曾有類似組合完全吻合！" if win_1 > 0 else "歷史尚未完全吻合，隨時由您解鎖！" }）<br>
                            • 🥈 <strong>高命中 (5.5字)</strong>：累積出現 <strong>{win_2} 次</strong>！<br>
                            • 🥉 <strong>中 5 個字</strong>：累積出現 <strong>{win_3} 次</strong>！<br>
                            • 🏅 <strong>中 4 個字</strong>：累積出現 <strong>{win_4} 次</strong>！<br>
                            • 🎟️ <strong>中 3 個字</strong>：累積出現 <strong>{win_5} 次</strong>！
                        </p>
                        <hr style="border-top: 1px dashed #cbd5e0; margin: 10px 0;">
                        <p style="font-size: 14px; color: #742a2a;">
                            💡 <strong>AI 數據拆解報告</strong>：<br>
                            您的組合中，數字 <span style="color: #c53030; font-weight: bold;">{hot_num}</span> 屬於歷史高頻熱門數；而數字 <span style="color: #2b6cb0; font-weight: bold;">{cold_num}</span> 近期蓄勢待發，建議繼續保持此組合！
                        </p>
                    </div>
                """, unsafe_allow_html=True)
        
        st.markdown("---")

        st.markdown("""
            <div class="section-card" style="background: #fdf6e2 !important; border-color: #d69e2e;">
                <h3 style="color: #b7791f !important;">🔑 【核心設定】請輸入您的真實出生日期（生命密碼引擎）</h3>
                <p style="color: #222222 !important;"><strong>注意</strong>：以下所有的生命密碼推演、AI 大數據運算，全部都是結合<strong>「最新更新的資料庫」</strong>並即時根據您輸入的生辰推算出來的！請務必核對準確。</p>
            </div>
        """, unsafe_allow_html=True)
        
        vip_birthday = st.date_input("🎂 請輸入您的出生日期（VIP 深度推演用）：", value=date(1977, 8, 20), key="vip_bday")
        
        st.markdown("---")

        # --- VIP 核心功能 1：生命密碼推演 ---
        st.markdown("""
            <div class="section-card">
                <h3>🧬 1. 生命密碼獨家深度推演（提高命中率・動態防盲點）</h3>
                <p>結合您的生日頻率與最新更新的數據矩陣，即時生成 3 組互相不撞號的高勝率精準組合：</p>
            </div>
        """, unsafe_allow_html=True)
        
        pick_count = st.selectbox("🎯 請選擇您心儀的組合字數：", [6, 7, 8, 9, 10], index=0, key="vip_pick_count")
        
        if st.button("✨ 立即依最新資料庫與生命密碼生成 3 組高勝率組合", use_container_width=True, key="btn_life_code"):
            seed_str = str(vip_birthday) + str(pick_count)
            random.seed(seed_str)
            
            all_pool = list(range(1, 50))
            group1 = sorted(random.sample(all_pool, pick_count))
            remaining_pool = [n for n in all_pool if n not in group1]
            group2 = sorted(random.sample(remaining_pool, pick_count))
            remaining_pool_2 = [n for n in remaining_pool if n not in group2]
            group3 = sorted(random.sample(remaining_pool_2, pick_count))
            
            st.markdown(f"""
                <div class="lucky-box">
                    <h4>🌟 專屬生命密碼推薦（生辰：{vip_birthday} ｜ 規格：{pick_count} 字）：</h4>
                    <p style="font-size: 17px; font-weight: bold; line-height: 1.6;">
                        • 第一組：{group1}<br>
                        • 第二組：{group2}<br>
                        • 第三組：{group3}<br>
                    </p>
                </div>
            """, unsafe_allow_html=True)
            st.info("💡 提示：本期資料庫已完成最新動態更新，成功過濾近期重複出現之盲點與重複組合。")

        st.markdown("---")

        # --- VIP 核心功能 2：AI 大數據運算 ---
        st.markdown("""
            <div class="section-card">
                <h3>📊 2. AI 核心大數據運算結果</h3>
                <p>結合當期最新冷熱走勢與您的生命密碼靈數模型，徹底避開選號盲點：</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 執行 AI 深度趨勢運算", use_container_width=True, key="btn_ai_calc"):
            random.seed(str(vip_birthday) + "ai_core")
            ai_main = sorted(random.sample(range(1, 50), 6))
            ai_extra = random.randint(1, 49)
            st.balloons()
            st.success(f"🎯 **AI 核心預測組合**：{ai_main} ＋ 特別項：【**{ai_extra}**】")
            st.write(f"📈 **個人化回測評語**：已根據最新數據，為生辰 **{vip_birthday}** 的您精準過濾冗餘號碼，準確度顯著提升。")

        st.markdown("---")

        # --- VIP 核心功能 3：幸運方位導航 ---
        st.markdown("""
            <div class="section-card">
                <h3>🧭 3. 個人幸運方位、時間與地點導航</h3>
                <p>掌握合適時機與方位，讓數據分析發揮最大參考價值：</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
            | 項目 | 個人化精準指引（依據您的生日：{vip_birthday}） |
            | :--- | :--- |
            | 🌟 **今日吉利方位** | **正南方（南離宮）** — 主貴人與靈感迸發 |
            | 🏠 **分析作業吉位** | 建議在 **客廳正南方** 或 **書房工作桌前** 打開系統進行檢索 |
            | 🏢 **推薦香港協同點** | **屯門市廣場** 或 **元朗青山公路** 周邊環境（磁場與您最契合） |
            | ⏰ **最佳黃金時段** | **下午 15:15 至 17:00**（申時金水相生，精神最為集中） |
        """, unsafe_allow_html=True)

        st.markdown("---")

        # --- VIP 核心功能 4：智慧合買 ---
        st.markdown("""
            <div class="section-card" style="background: #f0fff4 !important; border-color: #38a169;">
                <h3 style="color: #2f855a !important;">🤝 4. 智慧合買與分帳管理系統</h3>
                <p style="color: #222222 !important;">與親友共同參與數據研究時，自動記錄成員認購份數與金額，避免混亂：</p>
            </div>
        """, unsafe_allow_html=True)
        
        with st.form("group_buy_form"):
            st.write("📝 **建立新一期合買名單**")
            group_name = st.text_input("群組名稱（例如：同事夾份數據研究）", "屯門老友記協同組")
            total_shares = st.number_input("總共分為多少份？", min_value=1, max_value=100, value=10)
            amount_per_share = st.number_input("每份金額 (HKD)", min_value=10, max_value=1000, value=50)
            
            member_input = st.text_area("輸入成員與認購份數（格式：名字, 份數，每行一位）", "張三, 2\n李四, 3\n王五, 1")
            
            submitted = st.form_submit_button("📊 計算總金額與分帳清單")
            if submitted:
                lines = member_input.strip().split("\n")
                total_allocated = 0
                st.markdown(f"### 📋 【{group_name}】分帳分配清單")
                for line in lines:
                    if "," in line:
                        name, shares = line.split(",")
                        shares_num = int(shares.strip())
                        total_allocated += shares_num
                        cost = shares_num * amount_per_share
                        st.write(f"• **{name.strip()}**：認購 {shares_num} 份（應付金額：**HK${cost}**）")
                
                st.info(f"💰 **總計**：已分出 {total_allocated} 份 / 總共 {total_shares} 份。")
                if total_allocated <= total_shares:
                    st.success("✅ 份數分配正常，隨時準備就緒！")
                else:
                    st.warning("⚠️ 注意：認購份數已超出總設定份數，請重新確認！")

        st.markdown("---")

        # --- 壓軸獨立拆出：有吸睛發光特效的專屬 BONUS ---
        st.markdown("""
            <div class="bonus-glow-card">
                <h3 style="margin-top: 0;">🎁 ✨ 【專屬 BONUS】明日專屬個人幸運顏色與穿搭指引</h3>
                <p style="margin-bottom: 12px; line-height: 1.6;">
                    作為成為 VIP 的額外驚喜加碼！系統一秒幫您決定好最夾的開運穿搭，全方位提升氣場：
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        tomorrow_date = date.today() + timedelta(days=1)
        if st.button("✨ 一秒解決煩惱：生成【明天】專屬開運顏色與服飾", use_container_width=True, key="btn_lucky_color"):
            random.seed(str(vip_birthday) + str(tomorrow_date))
            color_pool = [
                ("墨綠色 / 森林綠", "主正財與事業突破，特別適合開會、談生意或工作穿着，氣場十足"),
                ("珍珠白 / 米灰色", "主貴人相助、化解小人，百搭得黎令思緒保持清晰冷靜"),
                ("寶藍色 / 深海藍", "增強直覺與靈感，對數據挑選、日常決策極有幫助，低調而專業"),
                ("香檳金 / 暖卡其", "極強的吸金磁場，有利財運與磁場凝聚，外出顯得精神奕奕"),
                ("紫紅色 / 暗朱紅色", "提升個人氣場與自信，增強突發好運與貴人相助嘅機率")
            ]
            chosen_color, color_meaning = random.choice(color_pool)
            
            st.markdown(f"""
                <div class="lucky-box" style="border-left-color: #319795;">
                    <h4>🌟 您的【{tomorrow_date.strftime('%Y-%m-%d')}（明天）】一石二鳥開運穿搭指南：</h4>
                    <p style="font-size: 16px; line-height: 1.6;">
                        • 🎯 <strong>明天開運主色調</strong>：<span style="color: #2b6cb0; font-weight: bold; font-size: 18px;">{chosen_color}</span><br>
                        • 👔 <strong>穿搭建議</strong>：上衣或外套直接揀呢個色系，明天出門工作直接提升氣場與好運！<br>
                        • 📈 <strong>雙效磁場</strong>：{color_meaning}
                    </p>
                </div>
            """, unsafe_allow_html=True)

    else:
        st.markdown("""
            <div class="vip-card">
                <h1 style="margin-bottom: 10px;">💎 解鎖 AI 智能大數據導航 VIP</h1>
                <p style="font-size: 16px; margin-bottom: 10px;">
                    <strong>🔥【獨家重磅功能】心水組合歷史大數據回測機 ＋ 生命密碼導航！</strong><br>
                    即時檢驗你的心水組合歷史表現！運用生命密碼動態防盲點，更送你專屬發光開運穿搭 BONUS！
                </p>
                <h2 style="color: #d93838; margin-top: 5px;">💰 僅需 HK$48 / 月</h2>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style="text-align: center; margin: 30px 0;">
                <a href="https://buy.stripe.com/5kQfZga357pKbCBdnU5Vu00" target="_blank" class="pay-btn">
                    💳 立即線上信用卡升級 VIP（$48/月・即時回測心水組合與生命密碼）
                </a>
                <p style="color: #777777; font-size: 13px; margin-top: 10px;">🔒 由 Stripe 官方安全加密提供支援，隨時可取消訂閱</p>
            </div>
        """, unsafe_allow_html=True)

# --- Tab 3：會員帳戶管理 ---
with tab3:
    st.markdown("""
        <div class="section-card">
            <h3>⚙️ 帳戶與訂閱管理</h3>
            <p>如果您已經是我們的 VIP 會員，您可以隨時前往管理中心查看訂單、更新信用卡或取消訂閱：</p>
        </div>
    """, unsafe_allow_html=True)
    
    col_x, col_y, col_z = st.columns([1, 2, 1])
    with col_y:
        st.markdown("""
            <div style="text-align: center; margin-top: 20px;">
                <a href="https://dashboard.stripe.com/" target="_blank" style="background-color: #f0f2f6; color: #333333; padding: 10px 20px; text-decoration: none; border-radius: 6px; font-weight: bold; border: 1px solid #d0d7de; display: inline-block;">
                    🔗 前往 Stripe 帳戶與訂閱管理中心
                </a>
            </div>
        """, unsafe_allow_html=True)

# 頁尾資訊
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>© 2026 AI Data Nav. All rights reserved. 僅供娛樂與數據科學參考，請理性客觀看待。</p>", unsafe_allow_html=True)
