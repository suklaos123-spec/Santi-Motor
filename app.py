import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import warnings

st.sidebar.image(
    "images/Logo.jpeg",
    width=180
)
warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="ລາຄາລົດຈັກມືສອງ",
    page_icon="🏍️",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Lao&display=swap');

    html, body, [class*="css"] {
        font-family: 'Noto Sans Lao', sans-serif;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    }
    section[data-testid="stSidebar"] * {
        color: #e0e0e0 !important;
    }

    /* Main background */
    .main { background-color: #f0f2f6; }

    /* Cards */
    .card {
        background: white;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }

    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
    }
    .metric-card h2 { color: white !important; margin: 0; font-size: 2rem; }
    .metric-card p  { color: rgba(255,255,255,0.85) !important; margin: 4px 0 0; font-size: 0.9rem; }

    /* Price result */
    .price-result {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        border-radius: 16px;
        padding: 32px;
        text-align: center;
        color: white;
    }
    .price-result h1 { font-size: 3rem; margin: 0; color: white !important; }
    .price-result p  { font-size: 1.1rem; color: rgba(255,255,255,0.9) !important; }

    /* Section header */
    .section-header {
        font-size: 1.4rem;
        font-weight: 700;
        color: #1a1a2e;
        border-left: 4px solid #667eea;
        padding-left: 12px;
        margin-bottom: 16px;
    }

    /* Nav pills in sidebar */
    div[data-testid="stRadio"] label {
        display: block;
        padding: 10px 16px;
        border-radius: 8px;
        cursor: pointer;
        transition: background 0.2s;
    }
    div[data-testid="stRadio"] label:hover {
        background: rgba(255,255,255,0.1);
    }

    /* Divider */
    hr { border-color: #e0e0e0; margin: 24px 0; }

    /* Badges */
    .badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 600;
    }
    .badge-blue   { background: #dbeafe; color: #1d4ed8; }
    .badge-green  { background: #dcfce7; color: #15803d; }
    .badge-purple { background: #f3e8ff; color: #7e22ce; }
    .badge-red    { background: #fee2e2; color: #b91c1c; }
</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_data():
    df = pd.read_csv("dataset.santi1.csv")
    df.columns = df.columns.str.strip()
    return df

@st.cache_resource
def load_model():
    return joblib.load("model_lr.pkl")

try:
    df = load_data()
    model = load_model()
    data_loaded = True
except Exception as e:
    st.error(f"❌ ໂຫຼດຂໍ້ມູນ/ໂມເດວບໍ່ສຳເລັດ: {e}")
    st.info("ກະລຸນາໃຫ້ `dataset_santi1.csv` ແລະ `model_lr.pkl` ຢູ່ໃນ folder ດຽວກັນກັບ `app.py`")
    data_loaded = False


BRANDS     = {
    "Honda Click": 0, "Honda PCX": 1, "Honda Scoopy": 2, "Honda Wave100": 3,
    "Honda Wave110i": 4, "Honda Wave125": 5, "Kawasaki Ninja250": 6, "Kawasaki Z250": 7,
    "Kawasaki Z300": 8, "Suzuki Bergman": 9, "Suzuki Raider": 10, "Suzuki Smash": 11,
    "Yamaha Fino": 12, "Yamaha Mio": 13, "Yamaha NMAX": 14, "Yamaha R15": 15
}
TYPES      = {"ອໍໂຕ້": 0, 
    "ເກຍມື": 1, 
    "ເດິ່ງອັດຕະໂນມັດ": 2}
CONDITIONS ={"ດີຫຼາຍ": 3, 
    "ດີ": 2, 
    "ພໍໃຊ້": 1, 
    "ເກົ່າ": 0}

CONDITION_COLOR = {
    'Excellent': 'badge-green',
    'Good':      'badge-blue',
    'Fair':      'badge-purple',
    'Old':       'badge-red',
}


with st.sidebar:
    st.markdown("## 🏍️ ລາຄາລົດຈັກມືສອງ")
    st.markdown("---")
    page = st.radio(
        "ເລືອກໜ້າ",
        ["🏠  ໜ້າຫຼັກ", "📊  ຕາຕະລາງຂໍ້ມູນ", "🔮  ພະຍາກອນລາຄາ", "📈  ວິເຄາະຂໍ້ມູນ", "ℹ️  ກ່ຽວກັບ"],
        label_visibility="collapsed",
    )
    st.markdown("---")
    if data_loaded:
        st.markdown(f"**ຈຳນວນຂໍ້ມູນທັງໝົດ:** {len(df):,} rows")
        st.markdown(f"**ຍີ່ຫໍ້:** {df['Brand_Model'].nunique()} ຍີ່ຫໍ້")
    st.markdown("---")
    st.caption("🎓 ໂຄງການ: ປະເມີນລາຄາລົດຈັກ")
    st.caption("🛠️ Stack: Python · Streamlit · Scikit-learn")


if page == "🏠  ໜ້າຫຼັກ":
    st.markdown("<h1 style='color:#1a1a2e;'>🏍️ ແບບຈໍາລອງການປະເມີນລາຄາລົດຈັກມືສອງ</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#6b7280; font-size:1.1rem;'>ໃຊ້ Machine Learning (Linear Regression) ໃນການທຳນາຍລາຄາລົດຈັກ</p>", unsafe_allow_html=True)
    st.markdown("---")

    if data_loaded:
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(f"""
            <div class="metric-card">
                <h2>{len(df):,}</h2>
                <p>📋 ຈຳນວນຂໍ້ມູນທັງໝົດ</p>
            </div>""", unsafe_allow_html=True)
        with c2:
            st.markdown(f"""
            <div class="metric-card" style="background:linear-gradient(135deg,#4facfe,#00f2fe);">
                <h2>{df['Brand_Model'].nunique()}</h2>
                <p>🏷️ ຍີ່ຫໍ້ລົດ</p>
            </div>""", unsafe_allow_html=True)
        with c3:
            avg = int(df['Price'].mean())
            st.markdown(f"""
            <div class="metric-card" style="background:linear-gradient(135deg,#43e97b,#38f9d7);">
                <h2>{avg:,}</h2>
                <p>💰 ລາຄາສະເລ່ຍ (USD)</p>
            </div>""", unsafe_allow_html=True)
        with c4:
            st.markdown(f"""
            <div class="metric-card" style="background:linear-gradient(135deg,#fa709a,#fee140);">
                <h2>{df['Year'].max()}</h2>
                <p>📅 ລຸ້ນໃໝ່ສຸດ</p>
            </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="section-header">📌 ກ່ຽວກັບໂຄງການ</div>', unsafe_allow_html=True)
            st.markdown("""
            ລະບົບນີ້ຊ່ວຍໃຫ້ທ່ານ:
            - 🔍 ກວດສອບຂໍ້ມູນລົດຈັກມືສອງໃນຕາຕະລາງ
            - 🔮 ທຳນາຍລາຄາດ້ວຍ (Linear Regression)
            - 📈 ເບິ່ງ Dashboard ວິເຄາະລາຄາຕາມຍີ່ຫໍ້, ປີ, ສະພາບ
            - 📊 ເຂົ້າໃຈປັດໃຈທີ່ກຳນົດລາຄາ
            """)
            st.markdown('</div>', unsafe_allow_html=True)

        with col_b:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="section-header">⚡ ການນຳໃຊ້ງ່າຍໆ</div>', unsafe_allow_html=True)
            st.markdown("""
            1. ໄປທີ່ **🔮 ພະຍາກອນລາຄາ**
            2. ເລືອກຍີ່ຫໍ້, ປີ, ປະເພດ, cc, ໄລຍະທາງ, ສະພາບ
            3. ກົດ **"ພະຍາກອນລາຄາ"**
            4. ລະບົບຈະສະແດງລາຄາທີ່ຄາດຄະເນ
            """)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">🔍 ຕົວຢ່າງຂໍ້ມູນ 5 ລາຍການ</div>', unsafe_allow_html=True)
        st.dataframe(df.head(5), use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)


elif page == "📊  ຕາຕະລາງຂໍ້ມູນ":
    st.markdown("<h2 style='color:#1a1a2e;'>📊 ຕາຕະລາງຂໍ້ມູນລົດຈັກ</h2>", unsafe_allow_html=True)
    st.markdown("---")

    if data_loaded:
        # Filters
        with st.expander("🔽 ຕົວກອງຂໍ້ມູນ", expanded=True):
            f1, f2, f3 = st.columns(3)
            with f1:
                brand_filter = st.multiselect("ຍີ່ຫໍ້", options=sorted(df['Brand_Model'].unique()), default=[])
            with f2:
                cond_filter = st.multiselect("ສະພາບ", options=CONDITIONS, default=[])
            with f3:
                year_range = st.slider("ປີ", int(df['Year'].min()), int(df['Year'].max()),
                                       (int(df['Year'].min()), int(df['Year'].max())))

        filtered = df.copy()
        if brand_filter:
            filtered = filtered[filtered['Brand_Model'].isin(brand_filter)]
        if cond_filter:
            filtered = filtered[filtered['Condition'].isin(cond_filter)]
        filtered = filtered[(filtered['Year'] >= year_range[0]) & (filtered['Year'] <= year_range[1])]

        st.markdown(f"**ພົບ {len(filtered):,} ລາຍການ**")
        st.dataframe(filtered, use_container_width=True, hide_index=True, height=500)

        st.download_button(
            "⬇️ ດາວໂຫຼດ CSV",
            filtered.to_csv(index=False).encode("utf-8"),
            file_name="filtered_dataset.csv",
            mime="text/csv",
        )

        st.markdown("---")
        st.markdown('<div class="section-header">📐 ສະຖິຕິສະຫຼຸບ</div>', unsafe_allow_html=True)
        st.dataframe(filtered.describe().round(2), use_container_width=True)


elif page == "🔮  ພະຍາກອນລາຄາ":
    st.markdown("<h2 style='color:#1a1a2e;'>🔮 ພະຍາກອນລາຄາລົດຈັກ</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#6b7280;'>ໃສ່ຂໍ້ມູນລົດຈັກ ແລ້ວລະບົບຈະຄາດຄະເນລາຄາ</p>", unsafe_allow_html=True)
    st.markdown("---")

    col_form, col_result = st.columns([1, 1], gap="large")

    with col_form:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">📝 ຂໍ້ມູນລົດ</div>', unsafe_allow_html=True)

        brand   = st.selectbox("🏷️ ຍີ່ຫໍ້ / ຮຸ່ນ", BRANDS)
        year    = st.slider("📅 ປີ", 2010, 2025, 2020)
        ltype   = st.selectbox("⚙️ ປະເພດເກຍ", TYPES)
        cc      = st.slider("🔧 ຂະໜາດເຄື່ອງ (CC)", 100, 300, 155, step=5)
        mileage = st.number_input("🛣️ ໄລຍະທາງ (km)", min_value=0, max_value=200000,
                                   value=30000, step=1000)
        cond    = st.selectbox("✅ ສະພາບ", CONDITIONS)

        st.markdown("<br>", unsafe_allow_html=True)
        predict_btn = st.button("🚀 ພະຍາກອນລາຄາ", use_container_width=True, type="primary")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_result:
        st.markdown('<div class="card" style="min-height:300px;">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">💰 ຜົນການພະຍາກອນ</div>', unsafe_allow_html=True)

        if predict_btn:
            if not data_loaded:
                st.error("ໂຫຼດໂມເດວບໍ່ໄດ້")
            else:
                try:
                    brand_encoded = BRANDS[brand]
                    ltype_encoded = TYPES[ltype]
                    cond_encoded = CONDITIONS[cond]

                    
                    input_df = pd.DataFrame({
                    "Brand_Model": [brand_encoded],  
                    "Year": [year],
                    "Type": [ltype_encoded],        
                    "Engine_CC": [cc],
                    "Mileage_km": [mileage],
                    "Condition": [cond_encoded],     
                })

                    price = model.predict(input_df)[0]
                    price = max(0, price)

                    badge_cls = CONDITION_COLOR.get(cond, 'badge-blue')

                    st.markdown(f"""
                    <div class="price-result">
                        <p>💡 ລາຄາທີ່ຄາດຄະເນ</p>
                        <h1>${price:,.0f}</h1>
                        <p>USD (ໂດລາສະຫະລັດ)</p>
                    </div>
                    """, unsafe_allow_html=True)

                    st.markdown("<br>", unsafe_allow_html=True)
                    st.markdown("**🔎 ສະຫຼຸບຂໍ້ມູນທີ່ໃສ່:**")
                    summary = {
                        "ຍີ່ຫໍ້ / ຮຸ່ນ":     brand,
                        "ປີ":               year,
                        "ປະເພດເກຍ":        ltype,
                        "ຂະໜາດເຄື່ອງ":     f"{cc} CC",
                        "ໄລຍະທາງ":         f"{mileage:,} km",
                        "ສະພາບ":            cond,
                    }
                    for k, v in summary.items():
                        st.markdown(f"- **{k}:** {v}")

                    
                    similar = df[
                        (df['Brand_Model'] == brand) &
                        (df['Year'].between(year - 2, year + 2))
                    ]
                    if len(similar) > 0:
                        avg_similar = similar['Price'].mean()
                        diff = price - avg_similar
                        diff_pct = (diff / avg_similar) * 100
                        st.markdown("---")
                        icon = "📈" if diff >= 0 else "📉"
                        st.info(f"{icon} ລາຄາໃນ dataset ຄ້າຍຄືກັນ: **${avg_similar:,.0f}** "
                                f"({'สูงกว่า' if diff >= 0 else 'ຕ່ຳກວ່າ'} {abs(diff_pct):.1f}%)")

                except Exception as e:
                    st.error(f"ພະຍາກອນລົ້ມເຫຼວ: {e}")
        else:
            st.markdown("""
            <div style='text-align:center; padding: 60px 0; color:#9ca3af;'>
                <div style='font-size:3rem;'>🏍️</div>
                <p>ໃສ່ຂໍ້ມູນ ແລ້ວກົດ "ພະຍາກອນລາຄາ"</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)


elif page == "📈  ວິເຄາະຂໍ້ມູນ":
    st.markdown("<h2 style='color:#1a1a2e;'>📈 ວິເຄາະຂໍ້ມູນ Dashboard</h2>", unsafe_allow_html=True)
    st.markdown("---")

    if data_loaded:
        try:
            import plotly.express as px
            import plotly.graph_objects as go

            
            r1c1, r1c2 = st.columns(2)

            with r1c1:
                avg_brand = df.groupby('Brand_Model')['Price'].mean().sort_values(ascending=False).reset_index()
                fig1 = px.bar(avg_brand, x='Price', y='Brand_Model', orientation='h',
                              title='💰 ລາຄາສະເລ່ຍຕາມຍີ່ຫໍ້',
                              color='Price', color_continuous_scale='Viridis',
                              labels={'Price': 'USD', 'Brand_Model': ''})
                fig1.update_layout(height=450, showlegend=False, coloraxis_showscale=False)
                st.plotly_chart(fig1, use_container_width=True)

            with r1c2:
                fig2 = px.histogram(df, x='Price', nbins=30,
                                    title='📊 ການກະຈາຍຂອງລາຄາ',
                                    color_discrete_sequence=['#667eea'],
                                    labels={'Price': 'USD', 'count': 'ຈຳນວນ'})
                fig2.update_layout(height=450)
                st.plotly_chart(fig2, use_container_width=True)

            
            r2c1, r2c2 = st.columns(2)

            with r2c1:
                avg_year = df.groupby('Year')['Price'].mean().reset_index()
                fig3 = px.line(avg_year, x='Year', y='Price',
                               title='📅 ລາຄາສະເລ່ຍຕາມປີ',
                               markers=True, color_discrete_sequence=['#f5576c'],
                               labels={'Price': 'USD'})
                fig3.update_layout(height=380)
                st.plotly_chart(fig3, use_container_width=True)

            with r2c2:
                avg_cond = df.groupby('Condition')['Price'].mean().reset_index()
                fig4 = px.bar(avg_cond, x='Condition', y='Price',
                              title='✅ ລາຄາສະເລ່ຍຕາມສະພາບ',
                              color='Condition',
                              color_discrete_map={
                                  'Excellent': '#22c55e', 'Good': '#3b82f6',
                                  'Fair': '#a855f7', 'Old': '#ef4444'
                              },
                              labels={'Price': 'USD', 'Condition': 'ສະພາບ'})
                fig4.update_layout(height=380, showlegend=False)
                st.plotly_chart(fig4, use_container_width=True)

            
            r3c1, r3c2 = st.columns(2)

            with r3c1:
                fig5 = px.scatter(df, x='Mileage_km', y='Price',
                                  color='Condition', title='🛣️ ໄລຍະທາງ vs ລາຄາ',
                                  color_discrete_map={
                                      'Excellent': '#22c55e', 'Good': '#3b82f6',
                                      'Fair': '#a855f7', 'Old': '#ef4444'
                                  },
                                  opacity=0.6,
                                  labels={'Mileage_km': 'ໄລຍະທາງ (km)', 'Price': 'USD'})
                fig5.update_layout(height=380)
                st.plotly_chart(fig5, use_container_width=True)

            with r3c2:
                type_count = df['Type'].value_counts().reset_index()
                fig6 = px.pie(type_count, names='Type', values='count',
                              title='⚙️ ສັດສ່ວນປະເພດເກຍ',
                              color_discrete_sequence=px.colors.qualitative.Set3)
                fig6.update_layout(height=380)
                st.plotly_chart(fig6, use_container_width=True)

            
            fig7 = px.box(df, x='Brand_Model', y='Price',
                          title='📦 Box Plot ລາຄາຕາມຍີ່ຫໍ້',
                          color='Brand_Model',
                          labels={'Brand_Model': 'ຍີ່ຫໍ້', 'Price': 'USD'})
            fig7.update_layout(height=420, showlegend=False, xaxis_tickangle=-35)
            st.plotly_chart(fig7, use_container_width=True)

        except ImportError:
            
            st.warning("⚠️ Plotly ບໍ່ຖືກຕິດຕັ້ງ — ສະແດງ chart ພື້ນຖານ")

            avg_brand = df.groupby('Brand_Model')['Price'].mean().sort_values(ascending=False)
            st.markdown("**💰 ລາຄາສະເລ່ຍຕາມຍີ່ຫໍ້**")
            st.bar_chart(avg_brand)

            avg_year = df.groupby('Year')['Price'].mean()
            st.markdown("**📅 ລາຄາສະເລ່ຍຕາມປີ**")
            st.line_chart(avg_year)

            avg_cond = df.groupby('Condition')['Price'].mean().sort_values(ascending=False)
            st.markdown("**✅ ລາຄາສະເລ່ຍຕາມສະພາບ**")
            st.bar_chart(avg_cond)

            st.markdown("**⚙️ ຈຳນວນລົດຕາມປະເພດເກຍ**")
            st.bar_chart(df['Type'].value_counts())


elif page == "ℹ️  ກ່ຽວກັບ":
    st.markdown("<h2 style='color:#1a1a2e;'>ℹ️ ກ່ຽວກັບໂຄງການ</h2>", unsafe_allow_html=True)
    st.markdown("---")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">🎯 ຈຸດປະສົງ</div>', unsafe_allow_html=True)
        st.markdown("""
        ລະບົບນີ້ພັດທະນາຂຶ້ນເພື່ອ:

        - ຊ່ວຍ **ຜູ້ຊື້** ຮູ້ລາຄາທີ່ເໝາະສົມ ກ່ອນຕັດສິນໃຈ
        - ຊ່ວຍ **ຜູ້ຂາຍ** ຕັ້ງລາຄາໃຫ້ສົມເຫດສົມຜົນ
        - ວິເຄາະ **ປັດໃຈ** ທີ່ສົ່ງຜົນຕໍ່ລາຄາລົດຈັກ
        - ສ້າງ **ຄວາມໂປ່ງໃສ** ໃນຕະຫຼາດລົດຈັກມືສອງ
        """)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">🤖 ໂມເດວ AI</div>', unsafe_allow_html=True)
        st.markdown("""
        | ລາຍການ | ລາຍລະອຽດ |
        |--------|---------|
        | **Algorithm** | Linear Regression |
        | **Library** | Scikit-learn |
        | **Features** | 6 ຕົວແປ |
        | **Training data** | 1,000 rows |
        | **ໂມເດວໄຟລ໌** | `model_lr.pkl` |
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">📋 ຂໍ້ມູນ Dataset</div>', unsafe_allow_html=True)
        st.markdown("""
        | Column | ປະເພດ | ຄຳອະທິບາຍ |
        |--------|-------|---------|
        | `Brand_Model` | Text | ຍີ່ຫໍ້ ແລະ ຮຸ່ນລົດ |
        | `Year` | Int | ປີທີ່ຜະລິດ |
        | `Type` | Text | ປະເພດເກຍ |
        | `Engine_CC` | Int | ຂະໜາດເຄື່ອງ (cc) |
        | `Mileage_km` | Int | ໄລຍະທາງທີ່ໃຊ້ (km) |
        | `Condition` | Text | ສະພາບ |
        | `Price` | Int | ລາຄາ (USD) |
        """)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">🛠️ Technology Stack</div>', unsafe_allow_html=True)
        st.markdown("""
        <span class="badge badge-blue">🐍 Python 3.x</span>&nbsp;
        <span class="badge badge-green">🌐 Streamlit</span>&nbsp;
        <span class="badge badge-purple">🤖 Scikit-learn</span>&nbsp;
        <span class="badge badge-red">📊 Plotly</span>&nbsp;
        <span class="badge badge-blue">🐼 Pandas</span>&nbsp;
        <span class="badge badge-green">🔢 NumPy</span>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
   