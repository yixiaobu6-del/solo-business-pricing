"""一人公司定价决策器"""

def analyze_pricing(cost: float, market_min: float, market_max: float,
                    value_factor: float = 1.0, is_subscription: bool = False):
    """
    分析定价策略

    参数:
        cost: 成本（元）
        market_min: 市场最低价
        market_max: 市场最高价
        value_factor: 价值感知系数 (0.5-2.0)
        is_subscription: 是否订阅制
    """
    # 成本加成定价
    cost_plus = cost * (1 + 0.3) if cost > 0 else 0

    # 竞争定价
    competitive = (market_min + market_max) / 2

    # 价值定价
    value_based = cost * value_factor * 3

    # 综合建议
    recommended = max(cost_plus, min(value_based, competitive * 1.5))

    if is_subscription:
        monthly = recommended
        yearly = recommended * 10
        result = {
            "月付": f"¥{monthly:.0f}/月",
            "年付": f"¥{yearly:.0f}/年（省{((12-monthly)/12*100):.0f}%）",
            "recommended": "年付",
        }
    else:
        one_time = recommended
        tier_basic = recommended * 0.7
        tier_pro = recommended * 1.5
        tier_enterprise = recommended * 3
        result = {
            "基础版": f"¥{tier_basic:.0f}",
            "标准版": f"¥{one_time:.0f}",
            "专业版": f"¥{tier_pro:.0f}",
            "企业版": f"¥{tier_enterprise:.0f}",
            "recommended": "标准版",
        }

    return {
        "成本价": f"¥{cost:.0f}",
        "成本加成": f"¥{cost_plus:.0f}",
        "竞争定价": f"¥{competitive:.0f}",
        "价值定价": f"¥{value_based:.0f}",
        "推荐价格": result,
    }


if __name__ == "__main__":
    result = analyze_pricing(cost=50, market_min=99, market_max=499, value_factor=1.2)
    for k, v in result.items():
        print(f"{k}: {v}")
