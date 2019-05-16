# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/9 16:58
# 文件名称：btc_close_2017_6.py
# 开发软件：PyCharm
with open('收盘价Dashboard.html','w',encoding = 'utf8') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title><metacharset="utf-8"></head><body>\n')
    for svg in [
        '收盘价折线图（￥）.svg','收盘价对数变换折线图（￥）.svg','收盘价月日均值（￥）.svg','收盘价周日均值（￥）.svg',
        '收盘价星期均值（￥）.svg'
    ]:
        html_file.write('   <object type="image/svg+xml" data="{0}"height=500></object>\n'.format(svg))
    html_file.write('</body></html>')