# -*- coding: utf-8 -*-
import os
import xlwt
import datetime
from hashlib import md5

SAVE_PATH = os.path.dirname(os.path.abspath(__file__))+'../static/tmp/'

def export_xls(orders):
    b = xlwt.Workbook(u'订单详情')
    sh = b.add_sheet(u'订单列表')
    sh.write(0, 0, u'订单编号')
    sh.write(0, 1, u'买家姓名')
    sh.write(0, 2, u'买家电话')
    sh.write(0, 3, u'买家地址')
    sh.write(0, 4, u'订单状态')
    sh.write(0, 5, u'订单时间')
    sh.write(0, 6, u'商品所在学校')
    sh.write(0, 7, u'商品所在楼栋')
    sh.write(0, 8, u'订单详情')
    sh.write(0, 9, u'总价')
    sh.write(0, 10, u'送货人姓名')
    sh.write(0, 11, u'送货人联系信息')
    for i in range(len(orders)):
        o = orders[i]
        sh.write(i+1, 0, o.ticketid)    
        sh.write(i+1, 1, o.receiver)
        sh.write(i+1, 2, o.phone)
        sh.write(i+1, 3, o.contact_info)
        sh.write(i+1, 4, o.status)
        sh.write(i+1, 5, o.released_time)
        sh.write(i+1, 6, o.school_name_rd)
        sh.write(i+1, 7, o.building_name_rd)
        sh.write(i+1, 9, o.tot_price_rd)
        sh.write(i+1, 10, o.sender_name_rd)
        sh.write(i+1, 11, o.sender_contact_info_rd)
        
        od_sns = o.order_snapshots.all()
        od_sns_info = []
        for j in range(len(od_sns)):
            sn = od_sns[j].snapshot
            sn_info = [sn.name, str(sn.price), str(od_sns[j].quantity)]
            od_sns_info.append(u' '.join(sn_info))
        sh.write(i+1, 8, u'\n'.join(od_sns_info))
    fn = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S_%f')+'.xls'
    b.save(SAVE_PATH+fn)
    return fn

def export_product_xls(items, pd_name):
    b = xlwt.Workbook()
    sh = b.add_sheet(pd.name)
    sh.write(0, 0, u'订单编号')
    sh.write(0, 1, u'买家姓名')
    sh.write(0, 2, u'买家电话')
    sh.write(0, 3, u'买家地址')
    sh.write(0, 4, u'订单状态')
    sh.write(0, 5, u'订单时间')
    sh.write(0, 6, u'送货人姓名')
    sh.write(0, 7, u'送货人联系信息')
    sh.write(0, 8, u'商品所在学校')
    sh.write(0, 9, u'商品所在楼栋')
    sh.write(0, 10, u'商品名')
    sh.write(0, 11, u'商品描述')
    sh.write(0, 12, u'商品单价')
    sh.write(0, 13, u'购买数量')
    for i in range(len(items)):
        order = items[0]
        od_sn = items[1]
        sn = items[2]
        sh.write(i+1, 0, order.ticketid)
        sh.write(i+1, 1, order.receiver)
        sh.write(i+1, 2, order.phone)
        sh.write(i+1, 3, order.addr)
        sh.write(i+1, 4, order.status)
        sh.write(i+1, 5, order.released_time)
        sh.write(i+1, 6, order.sender_name_rd)
        sh.write(i+1, 7, order.sender_contact_info_rd)
        sh.write(i+1, 8, order.school_name_rd)
        sh.write(i+1, 9, order.building_name_rd)
        sh.write(i+1, 10, sn.name)
        sh.write(i+1, 11, sn.description)
        sh.write(i+1, 12, sn.price)
        sh.write(i+1, 13, od_sn.quantity)
    fn = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S_%f')+'.xls'
    b.save(SAVE_PATH+fn)
    return fn

