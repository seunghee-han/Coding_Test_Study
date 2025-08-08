class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        # 원소를 맨 끝에 추가
        self.items.append(value)
        # 현재 노드의 index
        cur_index = len(self.items) - 1

        while cur_index !=1: #1인 경우에는 root node. 올라갈일 x
        # 부모노드랑 비교ㅕ해서 내가 더 크면 위치 바꿈
            parent_index = cur_index // 2

            if self.items[cur_index] > self.items[parent_index] :
                self.items[cur_index], self.items[parent_index] =self.items[parent_index], self.items[cur_index]

                cur_index = parent_index
            else:
                break
        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!