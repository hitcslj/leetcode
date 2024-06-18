'''
分配资源ID

给定一个管理ID的资源池，可以从资源池中分配资源ID和释放资源ID，分配方式有动态分配和指定分配，
动态分配是从资源池的开始分配一个资源ID，指定分配是指定一个资源ID进行分配，
无论哪种分配方式释放资源ID时都需要放到资源池的尾部。执行一系列操作后，请问资源池的第一个空闲资源ID应该是多少?
注意:
资源池的初始顺序是从小到大。
资源池中空闲资源ID不足时，动态分配失败，对资源池不进行任何操作.
指定分配资源ID已经被占用或者不在资源池范围内时，对资源池不进行任何操作。
释放资源ID不在资源池范围内时或者已经是空闲资源ID时，对资源池不进行任何操作。
保证每个用例最后都有空闲资源ID

输入
第一行是资源池的范围:
第二行是操作个数。
第三行开始，第一个数字代表操作类型，1表示动态分配，2表示指定分配，3表示释放；
如果第一个数字是1，第二个表示分配的个数;
如果第一个数字是2，第二个表示分配的资源ID;
如果第一个数字是3，第二个表示释放的资源ID。
输出
资源池的第一个空闲资源ID

Example 
Input:
1 3
2
1 1
3 1
Output:
2
Explain:
第一行资源池范围是[1.3]，资源池的初始顺序是1->2->3。
第二行操作个数有2个。
第三行动态分配1个资源ID，资源池中剩余的资源ID顺序是2->3.
第四行释放1个资源ID，资源ID是1，资源池中剩余的资源ID顺序是2->3->1.
执行以上操作后，资源池的第一个空闲资源ID是2。


Input:
1 3
3
2 2
3 2
1 1
Output:
3
Explain: 
第一行资源池范围是[1.3]，资源池的初始顺序是1->2->3。
第二行操作人数有3个。
第三行指定分配1个资源ID，资源ID是2，资源池中剩余的资源ID顺序是1->3->2.
第四行释放1个资源D，资源ID是2，资源池中剩余的资源ID顺序是1->3->2.
第五行动态分配1个资源ID，分配的资源ID是1，资源池中剩余的资源ID顺序是3->2。
执行以上操作后，资源池的第一个空闲资源ID是3。

提示
保证输入的操作都是合法的。
操作类型范围是[1.3]。
分配次数范围是[1.100000]
资源池范围的最小值是1，最大值取值范围是[1,100000].
如果操作类型是1，分配资源个数的取值范围是[1,200]。

'''

class ListNode:
    def __init__(self, id=0, pre=None, next=None):
        self.id = id
        self.pre = pre
        self.next = next

def main():
    l,r = map(int, input().split())
    n = int(input())
    dic = {}
    head = ListNode(0)
    tail = ListNode(0)
    head.next = tail
    tail.pre = head
    cnt = r-l+1 # 资源池的数量
    for i in range(l, r+1):
        node = ListNode(i)
        dic[i] = node
        node.pre = tail.pre
        node.next = tail
        tail.pre.next = node
        tail.pre = node
    for _ in range(n):
        op, id = map(int, input().split())
        if op == 1:
            num = id
            # 动态分配num个资源ID
            if cnt < num:
                continue
            p = head.next
            for _ in range(num):
                # 删除前num个节点
                del dic[p.id]
                p.next.pre = p.pre
                p.pre.next = p.next
                p = p.next
                
        elif op == 2:
            # 指定分配资源ID
            if id not in dic:
                continue
            p = dic[id]
            p.pre.next = p.next
            p.next.pre = p.pre
            del dic[id]
        else:
            # 释放资源ID
            if id < l or id > r or id in dic:
                continue
            node = ListNode(id)
            dic[id] = node
            node.pre = tail.pre
            node.next = tail
            tail.pre.next = node
            tail.pre = node
    print(head.next.id)

if __name__ == '__main__':
    main()