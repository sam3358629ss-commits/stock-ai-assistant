
import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI選股助手", layout="wide")

st.title("📈 AI 選股助手 V2")
st.title("測試更新成功")

st.markdown("### 今日當沖候選股")

daytrade_df = pd.DataFrame({
    "股票": ["波若威", "聯亞", "創意", "弘塑", "辛耘"],
    "題材": ["CPO", "CPO", "ASIC", "CoWoS", "CoWoS"],
    "強度": [92, 88, 90, 85, 83],
    "策略": [
        "爆量突破",
        "5分K強勢",
        "AI主流",
        "量縮整理",
        "法人連買"
    ]
})

st.dataframe(daytrade_df, use_container_width=True)

st.markdown("---")

st.markdown("### 波段推薦（15~20%目標）")

swing_df = pd.DataFrame({
    "股票": ["世芯", "上詮", "均華"],
    "策略": ["子母K整理", "突破月線", "量縮後放量"],
    "預估空間": ["15%", "18%", "20%"]
})

st.dataframe(swing_df, use_container_width=True)

st.markdown("---")

st.markdown("### 市場情緒")

st.success("AI / ASIC / CPO 討論熱度持續升溫")
st.warning("短線漲多族群需留意震盪")

st.markdown("---")

st.markdown("### AI供應鏈樹狀圖")

tree = '''
AI
├── ASIC
│   ├── 創意
│   ├── 世芯
│   └── 聯發科
├── CoWoS
│   ├── 辛耘
│   ├── 弘塑
│   └── 均華
└── CPO
    ├── 聯亞
    ├── 波若威
    └── 上詮
'''

st.code(tree)

st.markdown("---")

st.markdown("### 新聞摘要")

news = [
    "NVIDIA 持續擴大 AI 資本支出。",
    "CoWoS 需求維持高檔。",
    "CPO 題材近期熱度回升。"
]

for n in news:
    st.write("•", n)
