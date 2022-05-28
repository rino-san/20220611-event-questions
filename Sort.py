#!/usr/bin/env python
# coding: utf-8

# In[13]:


def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]
    
def sort(array):
###################<前提>###################
# (1)いずれかがrefとの大小関係を満たさず、値の交換を行わない場合
    #(左側の値)<refの場合はleftに追加
    #(右側の値)>=refのときはrightに追加
# (2)大小関係を満たす場合
    #値の交換をした上で、(右側の値)をleftに、(左側の値)をrightに格納する
# (3)先頭の値が最小になった場合
    #無限ループを防ぐため、leftに格納する
    
    left = []
    right = []

    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array
    # 基準値
    ref = array[0]
    
    l_ind = 0
    r_ind = len(array)-1    
    
    while l_ind <= r_ind:
        # (3)の場合
        if l_ind == r_ind:
            tmp = array[l_ind]
            if tmp > ref:
                right = [tmp] + right
                break
            else:
                left.append(tmp)
                break

        tmp_l = array[l_ind]
        tmp_r = array[r_ind] 
        ##(2)の場合
        if tmp_l < ref:
            left.append(tmp_l)
            l_ind += 1
            
        elif tmp_l >= ref:
            ##(1)の場合
            if array[r_ind] < ref:
                left.append(tmp_r)
                right = [tmp_l] + right
                l_ind += 1
                r_ind -= 1
            ## (2)の場合
            else:
                # right.insert(0,tmp_r)
                right = [tmp_r]+ right
                # right.append(tmp_r)
                r_ind -= 1
    #再帰によるソート
    left = sort(left)
    right = sort(right)
    return left+right

if __name__ == '__main__':
    main()


# In[ ]:




