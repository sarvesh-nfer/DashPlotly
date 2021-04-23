#for extracting the data from elastic search
import os
import sys
import elasticsearch
from elasticsearch import Elasticsearch
import pandas as pd
from tqdm import tqdm
import numpy as np
from elasticsearch import helpers
from datetime import date
from datetime import timedelta
import plotly.graph_objects as go
from plotly.subplots import make_subplots

es= Elasticsearch([{'host': '10.10.6.251','port': 9200}])

es.ping()

#for Slide placement to get thickness info
res = es.search(index="slide_locking", doc_type="", body={"query": {"match_all": {}}}, size=100000)
print(type(res))
print(len((res['hits']['hits'])))
from pandas.io.json import json_normalize
df = json_normalize(res['hits']['hits'])

#for Slide placement to get thickness info
res = es.search(index="slide_placement", doc_type="", body={"query": {"match_all": {}}}, size=100000)
print(type(res))
print(len((res['hits']['hits'])))
from pandas.io.json import json_normalize
dfsp = json_normalize(res['hits']['hits'])

# for bb_validation and saving as bb dataframe
res = es.search(index="bounding_box_validation", doc_type="", body={"query": {"match_all": {}}}, size=100000)
print(type(res))
print(len((res['hits']['hits'])))
from pandas.io.json import json_normalize
bb = json_normalize(res['hits']['hits'])

# for post and saving as post dataframe
res = es.search(index="post", doc_type="", body={"query": {"match_all": {}}}, size=100000)
print(type(res))
print(len((res['hits']['hits'])))
from pandas.io.json import json_normalize
post = json_normalize(res['hits']['hits'])



'''
__________________________________________________

Adding date as an columns from time stamp
__________________________________________________
'''

df['date'] = pd.to_datetime(df['_source.data.time_stamp']).dt.date
df['date'] = pd.to_datetime(df['date'])

dfsp['date'] = pd.to_datetime(dfsp['_source.data.time_stamp']).dt.date
dfsp['date'] = pd.to_datetime(dfsp['date'])

bb['date'] = pd.to_datetime(bb['_source.data.time_stamp']).dt.date
bb['date'] = pd.to_datetime(bb['date'])

'''
__________________________________________________

Renaming the columns of the dataframes for to make it more simpler
__________________________________________________
'''

df.rename(columns={'_index':'index',
                   '_type':'type',
                   '_id':'id', 
                   '_score':'score',
                   '_source.data.first_status':'first_status',
                   '_source.data.first_read_angle':'first_read_angle', 
                   '_source.data.first_initial_current':'first_initial_current',
                   '_source.data.first_final_current':'first_final_current',
                   '_source.data.first_current_diff':'first_current_diff',
                   '_source.data.second_status':'second_status', 
                   '_source.data.second_read_angle':'second_read_angle',
                   '_source.data.second_initial_current':'second_inital_current',
                   '_source.data.second_final_current':'second_final_current',
                   '_source.data.second_current_diff':'second_current_diff',
                   '_source.data.cluster_name':'cluster_name',
                   '_source.data.scanner_name':'scanner_name',
                   '_source.data.u_id':'u_id',
                   '_source.data.load_identifier':'load_identifier',
                   '_source.data.row_index':'row_index',
                   '_source.data.col_index':'col_index',
                   '_source.data.time_stamp':'time_stamp',
                   '_source.data.first_lock_step_counter':'first_lock_step_counter',
                   '_source.data.slide_id':'slide_id',
                  }, inplace=True)

dfsp.rename(columns={'_index':'index',
                   '_type':'type',
                   '_id':'id', 
                   '_score':'score',
                   '_source.data.slide_top_edge_px':'slide_top_edge_px',
                   '_source.data.slide_bottom_edge_px':'slide_bottom_edge_px',
                   '_source.data.slide_height_um':'slide_height_um',
                   '_source.data.is_slide_found':'slide_found',
                   '_source.data.slide_top_width_um':'slide_top_width_um',
                   '_source.data.slide_bottom_width_um':'slide_bottom_width_um',
                   '_source.data.slide_left_bottom_side_px':'slide_left_bottom_side_px',
                   '_source.data.slide_left_top_side_px':'slide_left_top_side_px',
                   '_source.data.slide_right_bottom_side_px':'slide_right_bottom_side_px',
                   '_source.data.slide_right_top_side_px':'slide_right_top_side_px',
                   '_source.data.is_slide_placed':'slide_placed',
                   '_source.data.slide_bottom_width_dimension_status':'slide_bottom_width_dimension_status',
                   '_source.data.slide_top_width_dimension_status':'slide_top_width_dimension_status',
                   '_source.data.distance_change_px':'distance_change_px',
                   '_source.data.left_corner_difference_px':'left_corner_difference_px',
                   '_source.data.right_corner_difference_px':'right_corner_difference_px', 
                   '_source.data.slope_px':'slope_px',
                   '_source.data.angle_degrees':'angle_degrees',
                   '_source.data.y_offset_px':'y_offset_px',
                   '_source.data.x_offset_px':'x_offset_px',
                   '_source.data.offset_pos_x_um':'offset_pos_x_um',
                   '_source.data.offset_pos_y_um':'offset_pos_y_um',
                   '_source.data.placement_status':'placement_status',
                   '_source.data.x_dimen_status':'x_dimen_status',
                   '_source.data.y_dimen_status':'y_dimen_status',
                   '_source.data.height_status':'height_status',
                   '_source.data.slide_thickness':'slide_thickness',
                   '_source.data.raw_slide_thickness':'raw_slide_thickness',
                   '_source.data.cluster_name':'cluster_name',
                   '_source.data.scanner_name':'scanner_name',
                   '_source.data.u_id':'u_id',
                   '_source.data.load_identifier':'load_identifier',
                   '_source.data.row_index':'row_index',
                   '_source.data.col_index':'col_index',
                   '_source.data.time_stamp':'time_stamp',
                   '_source.data.loaded_date':'loaded_date',
                   '_source.data.slide_id':'slide_id',
                   '_source.data.row':'row',
                   '_source.data.column':'column',
                   '_source.data.permissible_angle':'permissible_angle',
                   '_source.data.slide_width_um':'slide_width_um',
                   '_source.data.actual_angle':'actual_angle',
                  }, inplace=True)

bb.rename(columns={'_index':'index', '_type':'type', '_id':'id', '_score':'score', '_source.data.slide_name':'slide_name',
       '_source.data.validation_info':'validation_info' , '_source.data.cluster_name':'cluster_name',
       '_source.data.scanner_name':'scanner_name', '_source.data.u_id':'u_id',
       '_source.data.time_stamp':'time_stamp', '_source.author':'author', '_source.text':'text',},inplace=True)

'''
__________________________________________________

For yesterday's date
__________________________________________________
'''
today = date.today()
yesterday = today - timedelta(days = 8)
today=str(today)
yesterday=str(yesterday)
#print(yesterday)

data=bb[bb['date']>=yesterday]
data2=dfsp[dfsp['date']>=yesterday]
data3=df[df['date']>=yesterday]

data2['slide_id']=data2['slide_id'].astype(int)
data2['slide_name']=data2['scanner_name']+'_'+data2['slide_id'].map(str)
'''
__________________________________________________

CSV for bestZ and thickness
__________________________________________________
'''
data=data.reset_index(drop=True)

slide_name=[]
blob_index=[]
x_position=[]
y_position=[]
stack_size=[]
reference_z=[]
best_z=[]
z_difference=[]
best_index=[]
focus_metric=[]
color_metric=[]
process_time=[]
capture_status=[]
date=[]
p=0
for i in data:
    for j in data['validation_info']:
        for k in j:
            slide_name.append(data['slide_name'][p])
            blob_index.append(k['blob_index'])
            x_position.append(k['x_position'])
            y_position.append(k['y_position'])
            stack_size.append(k['stack_size'])
            reference_z.append(k['reference_z'])
            best_z.append(k['best_z'])
            z_difference.append(k['z_difference'])
            best_index.append(k['best_index'])
            focus_metric.append(k['focus_metric'])
            color_metric.append(k['color_metric'])
            process_time.append(k['process_time'])
            capture_status.append(k['capture_status'])
            date.append(data['date'][p])

            parse_bb =pd.DataFrame(list(zip(date,slide_name,blob_index,x_position,y_position,stack_size,reference_z,best_z,z_difference,best_index,focus_metric,color_metric,process_time,capture_status))
                               ,columns =['date','slide_name','blob_index','x_position','y_position','stack_size','reference_z','best_z','z_difference','best_index','focus_metric','color_metric','process_time','capture_status'])
        if p!=len(data['scanner_name'])-1:
            p=p+1
        else:
            break
parse_bb['Biopsy']=np.bitwise_and(parse_bb['focus_metric']  >= 6 , parse_bb['color_metric'] >= 7)
parse_bb['Debris']=np.bitwise_and(parse_bb['focus_metric'] >= 6 , parse_bb['color_metric'] < 7)
parse_bb['Background']=np.bitwise_and(parse_bb['focus_metric'] < 6 , parse_bb['color_metric'] < 7)
#parse_bb['Biopsy']=parse_bb['Biopsy'].replace([True,False],['true','false'])
#parse_bb['Debris']=parse_bb['Debris'].replace([True,False],['true','false'])
#parse_bb['Background']=parse_bb['Background'].replace([True,False],['true','false'])
parse_bb.to_csv('/home/adminspin/Music/dash-report/apps/parse_bb.csv',index=False)
parse_bb=parse_bb[parse_bb.best_z != -1]

merge_bs=pd.merge(parse_bb,data2,on='slide_name',how='inner',indicator=True)

##Merged_bs is for best-Z V slide thickness
merge_bs.to_csv('/home/adminspin/Music/dash-report/apps/merged.csv',index=False)
#df.to_csv(os.path.join(cwd, "new"))

'''
__________________________________________________

CSV for current difference
__________________________________________________
'''
data3=data3.dropna(subset=['slide_id'])
data3 = data3.sort_values(["row_index", "col_index"], ascending = (True, True))
data3['row_col']=data3['row_index'].map(str)+','+data3['col_index'].map(str)
data3['slide_id']=data3['slide_id'].astype(int)
data3['slide_name']=data3['scanner_name']+'_'+data3['slide_id'].map(str)
#data3['date2'] = pd.to_datetime(data3['time_stamp']).dt.date
#data3['drop']=data3['date'].astype(str)+'-'+data3['load_identifier']

data3.to_csv('/home/adminspin/Music/dash-report/apps/current.csv',index=False)

'''
__________________________________________________

CSV for slide angle and offset
__________________________________________________
'''
curr_data=data2[['slide_name','permissible_angle','slide_height_um','slide_width_um','scanner_name','actual_angle','date',
         'time_stamp','slide_id','load_identifier','offset_pos_x_um','offset_pos_y_um','row_index','col_index']]

curr_data=curr_data[curr_data['slide_height_um'] != 0]
curr_data['slide_height_mm']=curr_data['slide_height_um']/1000
curr_data = curr_data.sort_values(["row_index", "col_index"], ascending = (True, True))
curr_data['row_col']=curr_data['row_index'].map(str)+','+curr_data['col_index'].map(str)

curr_data.to_csv('/home/adminspin/Music/dash-report/apps/angleoffset.csv',index=False)


'''
__________________________________________________

Centering data shit
__________________________________________________
'''

postf=post[['_source.data.load_identifier','_source.data.centering_info','_source.data.scanner_name','_source.data.time_stamp',]]
postf['date'] = pd.to_datetime(postf['_source.data.time_stamp']).dt.date
postf['date'] = pd.to_datetime(postf['date'])
postf['_source.data.centering_info']

print('yesterday-----',yesterday)

postf=postf[postf['date']>=yesterday]
postf=postf[postf['_source.data.centering_info'].map(lambda d: len(d)) > 0]
postf=postf.reset_index(drop=True)

p1_3=post[post['_source.data.scanner_name']=='S1']
p1_2=post[post['_source.data.scanner_name']=='H01CBA05P']
p2_2=post[post['_source.data.scanner_name']=='H01CBA03P']
p3_2=post[post['_source.data.scanner_name']=='H01CBA01P']
p4_2=post[post['_source.data.scanner_name']=='H01CBA06P']

#__________________________________________________________________________ after scan
new1=p1_2.groupby('_source.data.time_stamp', as_index=False).max()
new1=new1['_source.data.time_stamp'].iloc[-1]
p1=p1_2[p1_2['_source.data.time_stamp']==new1]

new2=p2_2.groupby('_source.data.time_stamp', as_index=False).max()
new2=new2['_source.data.time_stamp'].iloc[-1]
p2=p2_2[p2_2['_source.data.time_stamp']==new2]

new3=p3_2.groupby('_source.data.time_stamp', as_index=False).max()
new3=new3['_source.data.time_stamp'].iloc[-1]
p3=p3_2[p3_2['_source.data.time_stamp']==new3]

#new4=p4_2.groupby('_source.data.time_stamp', as_index=False).max()
#new4=new4['_source.data.time_stamp'].iloc[-1]


#new5=p1_3.groupby('_source.data.time_stamp', as_index=False).max()
#new5=new5['_source.data.time_stamp'].iloc[-1]

#___________________________________________________________________________ before scan

new11=p1_2.groupby('_source.data.time_stamp', as_index=False).max()
new11=new11['_source.data.time_stamp'].iloc[-2]
p11=p1_2[p1_2['_source.data.time_stamp']==new11]

new22=p2_2.groupby('_source.data.time_stamp', as_index=False).max()
new22=new22['_source.data.time_stamp'].iloc[-2]
p22=p2_2[p2_2['_source.data.time_stamp']==new22]

new33=p3_2.groupby('_source.data.time_stamp', as_index=False).max()
new33=new33['_source.data.time_stamp'].iloc[-2]
p33=p3_2[p3_2['_source.data.time_stamp']==new33]





#p4_2=p4_2[p4_2['_source.data.time_stamp']==new4]

#p1_3=p1_3[p1_3['_source.data.time_stamp']==new5]

p1=p1.reset_index(drop=True)
p2=p2.reset_index(drop=True)
p3=p3.reset_index(drop=True)
#p4_2=p4_2.reset_index(drop=True)
#p1_3=p1_3.reset_index(drop=True)

p11=p11.reset_index(drop=True)
p22=p22.reset_index(drop=True)
p33=p33.reset_index(drop=True)

d=0
for j in p1['_source.data.centering_info']:
    df2=pd.DataFrame.from_dict(j)
    df2['_source.data.scanner_name']=p1['_source.data.scanner_name'][d]
    df2['_source.data.time_stamp']=p1['_source.data.time_stamp'][d]
    df2['centring_coordinate_y'] = df2['centring_coordinate_y'].values[::-1]
    if d!=len(p1)-1:
        d=d+1
    else:
        break

d=0
for j in p11['_source.data.centering_info']:
    df22=pd.DataFrame.from_dict(j)
    df22['_source.data.scanner_name']=p11['_source.data.scanner_name'][d]
    df22['_source.data.time_stamp']=p11['_source.data.time_stamp'][d]
    df22['centring_coordinate_y'] = df22['centring_coordinate_y'].values[::-1]
    if d!=len(p11)-1:
        d=d+1
    else:
        break

df2.to_csv('/home/adminspin/Music/dash-report/apps/post2.csv',index=False)
df22.to_csv('/home/adminspin/Music/dash-report/apps/post22.csv',index=False)

d=0
for j in p2['_source.data.centering_info']:
    df3=pd.DataFrame.from_dict(j)
    df3['_source.data.scanner_name']=p2['_source.data.scanner_name'][d]
    df3['_source.data.time_stamp']=p2['_source.data.time_stamp'][d]
    df3['centring_coordinate_y'] = df3['centring_coordinate_y'].values[::-1]
    if d!=len(p2)-1:
        d=d+1
    else:
        break

d=0
for j in p22['_source.data.centering_info']:
    df33=pd.DataFrame.from_dict(j)
    df33['_source.data.scanner_name']=p22['_source.data.scanner_name'][d]
    df33['_source.data.time_stamp']=p22['_source.data.time_stamp'][d]
    df33['centring_coordinate_y'] = df33['centring_coordinate_y'].values[::-1]
    if d!=len(p22)-1:
        d=d+1
    else:
        break

df3.to_csv('/home/adminspin/Music/dash-report/apps/post3.csv',index=False)
df33.to_csv('/home/adminspin/Music/dash-report/apps/post33.csv',index=False)

d=0
for j in p3['_source.data.centering_info']:
    df4=pd.DataFrame.from_dict(j)
    df4['_source.data.scanner_name']=p3['_source.data.scanner_name'][d]
    df4['_source.data.time_stamp']=p3['_source.data.time_stamp'][d]
    df4['centring_coordinate_y'] = df4['centring_coordinate_y'].values[::-1]
    if d!=len(p3)-1:
        d=d+1
    else:
        break


d=0
for j in p33['_source.data.centering_info']:
    df44=pd.DataFrame.from_dict(j)
    df44['_source.data.scanner_name']=p33['_source.data.scanner_name'][d]
    df44['_source.data.time_stamp']=p33['_source.data.time_stamp'][d]
    df44['centring_coordinate_y'] = df44['centring_coordinate_y'].values[::-1]
    if d!=len(p33)-1:
        d=d+1
    else:
        break

df4.to_csv('/home/adminspin/Music/dash-report/apps/post4.csv',index=False)
df44.to_csv('/home/adminspin/Music/dash-report/apps/post44.csv',index=False)

print("_"*120)
print("All csv saved")
print("_"*120)
