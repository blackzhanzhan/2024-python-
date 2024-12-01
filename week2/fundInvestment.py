"""
程序功能：实现基金定投
f = 0.001 * (x - 17)2 + 0.8599
"""

def main():
    net_value = []      # 基金净值列表
    fund_share = []     # 基金份额列表
    num = int(input("请输入您每月定投的金额（单位：元）:"))
    invest_month = int(input("请输入定投投资的月数："))
    # 任务1：追加完成基金净值列表和基金份额列表中的数据

    for i in range(invest_month):
        net_month_value=0.001*(i-16)*(i-16)+0.8599
        net_value.append(net_month_value)
        #份额保留两位小数
        fund_month_share=round(num/net_month_value,2)
        fund_share.append(fund_month_share)

    fund_share_sum = sum(fund_share)                    # 期末总基金份额
    ending_assets = fund_share_sum * net_value[-1]      # 期末资产
    earnings = ending_assets - num * invest_month       # 期末收益
    print("您定投月份为{:*^6}月，总投资{:^10,}元，投资的份额为：{:^10,.2f}".format(invest_month, num * invest_month, fund_share_sum))
    print("您投资基金的当前净值为每份{}元，期末资产为{:^10,.2f}元，".format(net_value[-1], ending_assets))
    print("期末收益为{:^10,.2f}元，收益率为：{:.2f}%".format(earnings, earnings/(num * invest_month)*100))

if __name__ == '__main__':
    main()
