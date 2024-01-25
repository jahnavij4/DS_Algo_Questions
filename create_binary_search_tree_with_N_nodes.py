class Node:
  def __init__(self,val=0,left=None,right=None):
    self.val=val
    self.left=left
    self.right=right
class BinarySearchTree:
  def preorder(self,root):
    if root is not None:
      print(root.val)
      self.preorder(self,root.left)
      self.preorder(self,root.right)
  def construct(self,start,end):
    list_=[]
    if start>end:
      list_.append(None)
      return list_
    for i in range(start,end+1):
      leftBST=self.construct(self,start,i-1)
      rightBST=self.construct(self,i+1,end)
      for j in range(len(leftBST)):
        left=leftBST[j]
        for k in range(len(rightBST)):
          right=rightBST[k]
          newNode=Node(i)
          newNode.left=left
          newNode.right=right
          list_.append(newNode)
    return list_
c=BinarySearchTree
out=c.construct(c,1,3)
for i in range(len(out)):
  print("-------",i,"th BST--------")
  c.preorder(c,out[i])
