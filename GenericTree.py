class TreeNode:
    def __init__(self,data):
        self.data=data
        self.childrens=[]
        self.parent=None

    def get_level(self):
        level=0
        parent = self.parent
        while parent:
            level+=1
            parent = parent.parent

        return level

    def add_children(self,child):
        child.parent=self
        self.childrens.append(child)

    def print_tree(self):
        level = self.get_level()
        spaces = ' ' * level * 2

        print(spaces+"|-->"+self.data)
        if self.childrens:
            for child in self.childrens:
                child.print_tree()


def build_tree():
    root = TreeNode("Electronics")

    mobiles = TreeNode("Mobiles")
    mobiles.add_children(TreeNode("Samsung"))
    mobiles.add_children(TreeNode("Vivo"))

    laptops = TreeNode("Laptops")
    laptops.add_children(TreeNode("Mac"))
    laptops.add_children(TreeNode("Windows"))

    tvs = TreeNode("TV")
    tvs.add_children(TreeNode("Sony"))
    tvs.add_children(TreeNode("LG"))

    root.add_children(mobiles)
    root.add_children(laptops)
    root.add_children(tvs)

    root.print_tree()

build_tree()