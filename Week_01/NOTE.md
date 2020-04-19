#学习笔记
- 脑图：
    - 解题模式：![](think.png)
    - 时间空间复杂度 ![](time.png)
    - 当前提及的知识点 ![](knowledge.png)
    - 当前数据结构内容整理 1[](mynote.png) 内容见numbers表

#本周作业
- remove-duplicates-from-sorted-array:
    - 遍历删除法，每次数组的删除操作都是 O(n)的复杂度，总体时间复杂度 (1+n)n/2 --> O(n<sup>2</sup>)
    - 双指针法(实际使用)： 快指针遍历[1:],慢指针从首个元素和快指针元素对比，相同跳过，不同： 慢指针+1，下一个元素替换成新元素。时间复杂度 O(n).
- design-circular-deque:
    - 基于双端链表 实现的 双端队列 时间复杂度 增删 O(1),查询 O(n);空间复杂度 O(1)
