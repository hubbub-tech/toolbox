# -*- coding: utf-8 -*-
"""
ratio query functions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rDp16Els0ZLzTQJCU2XGI6PkeoFKeMDL
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from blubber_orm import Users, Reservations

def get_num_calendared(user_id):
    calendared_reservations = Reservations.filter({
        "renter_id": user_id,
        "is_calendared": True
    })
    return len(calendared_reservations)

def get_num_queried(user_id):
    queried_reservations = Reservations.filter({
        "renter_id": user_id
    })
    return len(queried_reservations)

def get_conversion_ratio(user_id):
    num_calendared = get_num_calendared(user_id)
    num_queried = get_num_queried(user_id)
    conversion_ratio = num_calendared / num_queried
    return conversion_ratio

# NOTEBOOK WORK BELOW

# given reservations.csv, make grouped datasets
# functions to return ratio by item id and renter id
path=input("enter file path for reservations.csv: ")
df=pd.read_csv(path)
# df

def groupbyrenter(resdf):
  resbyrenter=pd.DataFrame(resdf.groupby(by=['renter_id']).sum()['is_calendared'])
  resbyrenter=resbyrenter.join(pd.DataFrame(resdf.groupby(by=['renter_id']).size()))
  resbyrenter.columns=['num_calendared','num_queried']
  resbyrenter['num_calendared/num_queried']=resbyrenter.num_calendared/resbyrenter.num_queried
  resbyrenter=resbyrenter.join(pd.DataFrame(resdf.groupby(by=['renter_id']).mean()['charge']))
  resbyrenter.rename(columns={"charge": "avg_charge"},inplace=True)
  return resbyrenter

  def group_by_renter():
      return

# groupbyrenter(df)

def groupbyrenteritem(resdf):
  resbyrenteritem=pd.DataFrame(resdf.groupby(by=['renter_id','item_id']).sum()['is_calendared'])
  resbyrenteritem=resbyrenteritem.join(pd.DataFrame(resdf.groupby(by=['renter_id','item_id']).size())) # join with num times queried per user per item
  resbyrenteritem.columns=['num_calendared','num_queried']
  resbyrenteritem['num_calendared/num_queried']=resbyrenteritem.num_calendared/resbyrenteritem.num_queried
  resbyrenteritem=resbyrenteritem.join(pd.DataFrame(resdf.groupby(by=['renter_id','item_id']).mean()['charge']))
  resbyrenteritem.rename(columns={"charge": "avg_charge"},inplace=True)
  return resbyrenteritem

  def group_by_renter_item():
      return

# groupbyrenteritem(df)

def groupbyitem(resdf):
  resbyitem=pd.DataFrame(resdf.groupby(by=['item_id']).sum()['is_calendared'])
  resbyitem=resbyitem.join(pd.DataFrame(resdf.groupby(by=['item_id']).size()))
  resbyitem.columns=['num_calendared','num_queried']
  resbyitem['num_calendared/num_queried']=resbyitem.num_calendared/resbyitem.num_queried
  resbyitem=resbyitem.join(pd.DataFrame(df.groupby(by=['item_id']).mean()['charge']))
  resbyitem.rename(columns={"charge": "avg_charge"},inplace=True)
  return resbyitem

  def group_by_item():
      return

# groupbyitem(df)
resbyrenter=groupbyrenter(df)
resbyrenteritem=groupbyrenteritem(df)
resbyitem=groupbyitem(df)

# query function for item id
def item_ratio1(item_id): # only returns ratio
  try:
    return resbyitem.loc[item_id,'num_calendared/num_queried']
  except:
    print('! the item queried does not exist, try another item id !')

# item_ratio1(1)

# item_ratio1(5)

def item_ratio2(item_id): # returns everything
  try:
    return resbyitem.loc[item_id,:]
  except:
    print('! the item queried does not exist, try another item id !')

# item_ratio2(1)

# query function for renter id
def renter_ratio1(renter_id):
  try:
    return resbyrenter.loc[renter_id,'num_calendared/num_queried']
  except:
    print('! the renter queried does not exist, try another renter id !')

# renter_ratio1(1)

def renter_ratio2(renter_id):
  try:
    return resbyrenter.loc[renter_id,:]
  except:
    print('! the renter queried does not exist, try another renter id !')

# renter_ratio2(1)

# query function for renter and item id
def renter_item_ratio1(renter_id,item_id):
  try:
    return resbyrenteritem.loc[renter_id,:].loc[item_id,'num_calendared/num_queried']
  except:
    print('! the renter-item combination queried does not exist, try another combination !')

# renter_item_ratio1(1,15)

def renter_item_ratio2(renter_id,item_id):
  try:
    return resbyrenteritem.loc[renter_id,:].loc[item_id,:]
  except:
    print('! the renter-item combination queried does not exist, try another combination !')

# renter_item_ratio2(1,24)

# ask user for query mode, and ask for query detail level
# then ask for corresponding inputs
mode_dict={'1':'item id','2':'renter id','3':'renter & item id'}
detail_dict={'1':'ratio only','2':'ratio & other info'}

while True:
	mode=input("enter query mode (type 1 for item id, 2 for renter id, 3 for renter & item id): ")
	print(mode, mode_dict[mode])
	detail=input("enter how much detail (type 1 for ratio only, 2 for ratio & more info): ")
	print(detail,detail_dict[detail])

	if mode=='1' and detail=='1':
		item_id=input("enter an item id: ")
		print(item_ratio1(int(item_id)))

	elif mode=='1' and detail=='2':
		item_id=input("enter an item id: ")
		print(item_ratio2(int(item_id)))

	elif mode=='2' and detail=='1':
		retner_id=input("enter a renter id: ")
		print(renter_ratio1(int(renter_id)))

	elif mode=='2' and detail=='2':
		renter_id=input("enter a renter id: ")
		print(renter_ratio2(int(renter_id)))

	elif mode=='3' and detail=='1':
		renter_id=input("enter a renter id: ")
		item_id=input("enter an item id: ")
		print(renter_item_ratio1(int(renter_id),int(item_id)))

	elif mode=='3' and detail=='2':
		renter_id=input("enter a renter id: ")
		item_id=input("enter an item id: ")
		print(renter_item_ratio1(int(renter_id),int(item_id)))
