# extract null value and plotta 将含有null的行提取并画图表
def nulldata_plot (dataframe):
    
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    nulldata = dataframe.isnull().sum().reset_index()
    nulldata.columns = ["Column","Count"]
    nulldata = nulldata[nulldata["Count"] > 0]
    sns.barplot (data=nulldata, x="Column",y="Count",hue="Column")
    plt.title("Null values")
    return plt.show()


# extract null value 将含有null的行提取并做出新的表格
def extr_null (dataframe):
    # 統計缺值欄位
    nulldata = dataframe.isnull().sum()
    print("缺值欄位與數量：\n", nulldata[nulldata > 0])

    # 提取含缺值的行
    missing_rows = dataframe[dataframe.isnull().any(axis=1)]
    print("共有", missing_rows.shape[0], "行含缺值")

    
    return missing_rows.to_excel("missing_rows.xlsx", index=False)