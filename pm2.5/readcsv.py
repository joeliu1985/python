import pandas as pd
import matplotlib.pyplot as plt

def read_csv():
    data = pd.read_csv("深圳-air-quality - 副本.csv")
    times = data['date'].tolist()
    # 分时间区间,保证最后一位纳入标签
    ticks = list(range(0, len(times), 2))
    if ticks[-1] != len(times) - 1:
        ticks.append(len(times) - 1)
    labels = [times[i] for i in ticks]
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    plt.rcParams['font.sans-serif'] = [u'SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    fig = plt.figure(figsize=(8, 4), dpi=100)
    # 设置图形的显示风格
    plt.style.use('ggplot')
    ax1 = fig.add_subplot(111)
    data = data.sort_values(by='date', ascending=True)
    ax1.plot(data['pm25'], '-v', linewidth=1.5)
    ax1.legend(loc='upper right', frameon=False, fontsize=10)
    ax1.set_xlabel('时间', fontsize=10)
    ax1.set_ylabel('pm25', fontsize=10)
    ax1.set_xticks(ticks)
    ax1.set_xticklabels(labels, rotation=45, horizontalalignment='right')
    #df = data.iloc[:,[0,1]]
    #df1 = df.groupby(["date"], as_index=True)["pm25"]
    #print(df1)
    #plt.rc('font', family='SimHei', size=10)
    #plt.ylabel('pm25')
    #plt.xlabel('日期1')
    plt.savefig("pm25.png", dpi=200)
    #b = df1.cumsum()
    #b.plot()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    read_csv()