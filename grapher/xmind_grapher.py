import xmind
from grapher.grapher import Grapher
from tqdm import tqdm


class XMindGrapher(Grapher):
    def __init__(self, filename, tree) -> None:
        super().__init__(filename, tree)
        self.xmind_graph = xmind.load(filename)
    
    def generate_graph(self):
        # iterate over self.tree and create a topic per line
        node_list = self.tree
        xmind_primary_sheet = self.xmind_graph.getPrimarySheet()
        xmind_root_node = xmind_primary_sheet.getRootTopic()
        xmind_root_node.setTitle("main")
        XMindGrapher.graph_recursively(xmind_root_node, self.tree)

    @staticmethod
    def graph_recursively(xmind_node, subtree):
        if len(subtree) == 0:
            return
        for dir in tqdm(subtree, desc=f"Parsing {xmind_node.getTitle()}..."):
            sub_topic = xmind_node.addSubTopic()
            sub_topic.setTitle(dir)
            XMindGrapher.graph_recursively(sub_topic, subtree[dir])

    def save_graph(self):
        xmind.save(self.xmind_graph)
        return self.xmind_graph._path