#!/usr/bin/env python
# coding: utf-8

# In[2]:


def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):
    # ここから記述
    left = 0
    right = len(sorted_array) - 1
    
    while left <= right:
        mid = (left+right)//2
        tmp_num = sorted_array[mid]
        # ターゲット発見
        if tmp_num == target_number:
            return mid
        # ターゲットが配列前半に存在
        elif tmp_num > target_number:
            right = mid -1
        # ターゲットが配列後半に存在
        elif tmp_num < target_number:
            left = mid +1
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()


# In[ ]:




