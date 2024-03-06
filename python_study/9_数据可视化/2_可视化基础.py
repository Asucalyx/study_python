#导入相关包
#模板画廊连接 https://gallery.pyecharts.org/#/README
#官网全局配置查询 https://05x-docs.pyecharts.org/#/zh-cn/  https://blog.csdn.net/qq_57099024/article/details/122030069
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
#创建折线对象
line = Line()
#添加x轴数据
line.add_xaxis(["PRC","UK","USA"])
#添加y轴数据
line.add_yaxis("GDP",[30,20,10])
#设置全局配置项
line.set_global_opts(
    title_opts = TitleOpts(title = "GDP展示",
                           pos_left = "center",
                           pos_bottom="1%"
    ),
    legend_opts=LegendOpts(
        is_show=True,
    ),
    toolbox_opts=ToolboxOpts(
        is_show=True,
    ),
    visualmap_opts=VisualMapOpts(
        is_show=True
    ),
)
#生成图像
line.render()
