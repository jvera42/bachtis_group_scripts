#pip install pygsheets

import pandas as pd
import numpy as np
import pygsheets as pyg
import asyncio

clock_df = pd.read_excel('/content/table.xlsx')

print(clock_df[['Name','Value']].head())

values_str = clock_df[['Name','Value']].to_numpy()
values_str.T[:,12:] = np.roll(values_str.T[:,12:], 1, axis=1)

#print(values_str)

values = values_str.copy()
clk_0_q1 = np.array([])
clk_0_q2 = np.array([])
clk_1_q1 = np.array([])
clk_1_q2 = np.array([])

for i in range(len(values)):
  value_0 = values[i,1]
  quad_0 = values[i,0]
  value_str = value_0.replace('[U] ','')
  quad_str_1 = quad_0.replace('framework_i/quad','')

  quad_number = int(quad_str_1[1:3])
  if quad_number >= 20 and quad_number < 24:
    quad_str_2 = quad_str_1.replace('_slr0','')
  elif quad_number >= 24 and quad_number < 28:
    quad_str_2 = quad_str_1.replace('_slr1','')
  elif quad_number >= 28 and quad_number < 32:
    quad_str_2 = quad_str_1.replace('_slr2','')
  elif quad_number >= 32 and quad_number <=35:
    quad_str_2 = quad_str_1.replace('_slr3','')
  elif quad_number == 12:
    quad_str_2 = quad_str_1.replace('1127_slr1_clk1','127_clk1')

  value = int(value_str)
  quad = quad_str_2[0:8]

  q = quad[0]

  values[i,1] = value
  values[i,0] = quad

  clk = np.array([quad,value])

  if quad[-1] == '0':
    if q == '1':
      if clk_0_q1.size == 0:
        clk_0_q1 = np.append(clk_0_q1, clk)
      else:
        clk_0_q1 = np.vstack((clk_0_q1, clk))
    else:
      if clk_0_q2.size == 0:
        clk_0_q2 = np.append(clk_0_q2, clk)
      else:
        clk_0_q2 = np.vstack((clk_0_q2, clk))
  elif quad[-1] == '1':
    if q == '1':
      if clk_1_q1.size == 0:
        clk_1_q1 = np.append(clk_1_q1, clk)
      else:
        clk_1_q1 = np.vstack((clk_1_q1, clk))
    else:
      if clk_1_q2.size == 0:
        clk_1_q2 = np.append(clk_1_q2, clk)
      else:
        clk_1_q2 = np.vstack((clk_1_q2, clk))

#print(clk_0_q1)
#print(clk_0_q2)
#print(clk_1_q1)
#print(clk_1_q2)

client = pyg.authorize(service_account_file='/content/clock-project-449821-df96f8c442fa.json')

ss = client.open('Production Database')

ws_list = ss.worksheets()
ws_active = str(ws_list[-1])
ws_index = ws_active[-3:-1]

ws = ss.worksheet(property='index',value=ws_index)

async def c_0_1():
  i1 = 0
  m = 0
  while i1 < len(clk_0_q1):
    ws.update_value('M'+str(m+3),clk_0_q1[i1,1])
    m+=1
    i1+=1
    await asyncio.sleep(0.01)

async def c_0_2():
  i2 = 0
  q = 0
  while i2 < len(clk_0_q2):
    ws.update_value('Q'+str(q+3),clk_0_q2[i2,1])
    q+=1
    i2+=1
    await asyncio.sleep(0.01)

async def c_1_1():
  j1 = 0
  n = 0
  while j1 < len(clk_1_q1):
    if ws.get_value('N'+str(n+3)) != '':
      n+=1
      await asyncio.sleep(0.01)
      continue
    else:
      ws.update_value('N'+str(n+3),clk_1_q1[j1,1])
      n+=1
      j1+=1
      await asyncio.sleep(0.01)

async def c_1_2():
  j2 = 0
  r = 0
  while j2 < len(clk_1_q2):
    if ws.get_value('R'+str(r+3)) != '':
      r+=1
      await asyncio.sleep(0.01)
      continue
    else:
      ws.update_value('R'+str(r+3),clk_1_q2[j2,1])
      r+=1
      j2+=1
      await asyncio.sleep(0.01)

async def main():
  L = await asyncio.gather(
      c_0_1(),
      c_0_2(),
      c_1_1(),
      c_1_2()
  )
  print('Complete! Yay!')

await main()