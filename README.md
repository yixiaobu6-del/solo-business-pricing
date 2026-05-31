# 一人公司定价决策器

> 独立开发者/小团队科学定价决策支持工具，多维度定价分析

---

## Features / 功能特点

| 功能 | 说明 |
|------|------|
| 输入参数 | 产品成本、期望利润率、竞品价格区间、用户付费意愿、产品类型 |
| 建议价格区间 | 综合成本导向+竞争导向+价值导向三大维度计算 |
| 定价策略推荐 | 撇脂定价/渗透定价/价值定价/分层定价等策略详解 |
| 心理学依据 | 锚定效应/左位数效应/对比原理/损失厌恶等原理 |
| 对比图表 | 各定价维度柱状图可视化对比 |
| 方案保存 | 保存和对比不同定价方案的历史记录 |

## Installation / 安装

无需安装，直接在浏览器中打开 `index.html` 即可使用。

```bash
# 克隆仓库
git clone https://github.com/yourusername/pricing-decision-maker.git

cd pricing-decision-maker
open index.html
```

## Usage / 使用方法

### 基础用法

1. 打开 `index.html`
2. 调整输入参数（成本、利润率、竞品价格等）
3. 右侧自动更新建议价格区间和定价策略
4. 查看心理学依据优化定价方案
5. 点击「保存当前方案」留存记录

### 定价计算示例

```javascript
// 三大定价维度计算
function calculatePricing(params) {
  const { cost, expectedMargin, minPrice, maxPrice, willingnessToPay } = params;
  
  // 成本导向定价
  const costBasedPrice = cost * (1 + expectedMargin / 100);
  
  // 竞争导向定价
  const competitorAvg = (minPrice + maxPrice) / 2;
  const competitionBasedPrice = competitorAvg;
  
  // 价值导向定价
  const valueBasedPrice = willingnessToPay;
  
  return {
    suggestedMin: Math.min(costBasedPrice, competitionBasedPrice),
    suggestedMax: Math.max(valueBasedPrice, competitionBasedPrice),
    costBased: costBasedPrice,
    competitionBased: competitionBasedPrice,
    valueBased: valueBasedPrice
  };
}
```

### 定价策略对比

| 策略 | 适用场景 | 优点 | 风险 |
|------|----------|------|------|
| 撇脂定价 | 创新产品、蓝海市场 | 利润高、品牌形象好 | 可能抑制市场普及 |
| 渗透定价 | 竞争激烈市场 | 快速获客、抢占份额 | 利润低、品牌感知弱 |
| 价值定价 | 品牌成熟、品质公认 | 品牌溢价、利润稳定 | 需持续品质证明 |
| 分层定价 | 用户需求差异化 | 覆盖面广、灵活度高 | 管理复杂度增加 |

### 定价心理学原理

| 原理 | 说明 | 应用示例 |
|------|------|----------|
| 锚定效应 | 先展示高价，让后续价格显便宜 | 先展示 1999，再展示 999 |
| 左位数效应 | 299 比 300 感知便宜很多 | 定价用 9/7/5 结尾 |
| 对比原理 | 三个选项中间通常被选 | 基础版/标准版/高级版 |
| 损失厌恶 | 失去痛苦 > 获得快乐 | 限时优惠制造紧迫感 |

## Contributing / 贡献

参见 [CONTRIBUTING.md](CONTRIBUTING.md)

## License / 许可证

MIT License - 参见 [LICENSE](LICENSE)

---

> 版本：1.0.0 | 更新日期：2026-05-30