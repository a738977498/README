class Node(object):
    def __init__(self, item):
        # item 用來存放資料
        self.item = item
        # next 是下一個節點的標識
        self.next = None

class SingleLinkList(object):
    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        return self._head == None

    def length(self):
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):  # 遍歷鍊錶
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next

    def add(self, item):  # 頭部添加
        # 先建立一個保存 item 的節點
        node = Node(item)
        # 將新節點的鏈接域 next 指向頭節點，即 _head 所指向的位置
        node.next = self._head
        # 將鏈表的頭 _head 指向新的節點
        self._head = node

    def append(self, item):  # 尾部添加
        node = Node(item)
        # 先判斷鏈表是否為空，若是空鏈表，則將 _head 指向新的節點
        if self.is_empty():
            self._head = node
        # 若不為空，則找到尾部，將尾部節點的 next 指向新的節點
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):  # 任意位置添加
        # 若指定位置 pos 為第一個元素，則執行頭部文件插入
        if pos <= 0:
            self.add(item)
        # 若指定位置超過鏈表尾部，則執行插入尾部
        elif pos > (self.length() - 1):
            self.append(item)
        # 找到指定位置
        else:
            node = Node(item)
            count = 0
            # pre 用來指向指定位置 pos 的前一個位置 pos-1，初始節點開始移動到指定位置
            pre = self._head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 先將新節點 node 的 next 指向插入位置的節點
            node.next = pre.next
            # 將插入位置的前一個節點的 next 指向新節點
            pre.next = node

    def remove(self, item):
        cur = self._head
        pre = None
        while cur != None:
            # 找到指定元素
            if cur.item == item:
                # 如果第一個就是要刪除的節點
                if not pre:
                    # 將頭指針指向頭節點的下一個節點
                    self._head = cur.next
                else:
                    # 將刪除位置的前一個節點的 next 指向刪除位置的後一個節點
                    pre.next = cur.next
                break
            else:
                # 繼續按鏈表後移節點
                pre = cur
                cur = cur.next

    def search(self, item):
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

if __name__ == "__main__":
    ll = SingleLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2,4)
    print("length:",ll.length())
    ll.travel()
    print(ll.search(3))
    print(ll.search(5))
    ll.remove(1)
    print("length:",ll.length())
    ll.travel()
