# j: jobs, d: dependencies
# time: O(j+d)
# space: O(j+d)
def topologicalSort(jobs, deps):
    # 建立一個誰先誰後的 graph
    job_graph = create_job_graph(jobs, deps)
    return get_order_jobs(job_graph)


def create_job_graph(jobs, deps):
    graph = JobGraph(jobs)
    for pre_req, job in deps:
        # adding edges
        graph.add_pre_req(job, pre_req)
    return graph


# 找到可行的 order
def get_order_jobs(graph):
    ordered_jobs = []
    nodes = graph.nodes
    while len(nodes):
        # 隨便找一個node
        node = nodes.pop()
        # 用dfs方式去搜尋
        contains_cycle = depth_first_search(node, ordered_jobs)
        if contains_cycle:
            return []
    return ordered_jobs


def depth_first_search(node, ordered_jobs):
    # 假如搜尋過，那就不理他
    if node.visited:
        return False
    # 假如看到的node也標示為visiting，代表cycle
    if node.visiting:
        return True

    node.visiting = True
    # 繼續往下做pre_req的dfs
    for pre_req_node in node.pre_reqs:
        contains_cycle = depth_first_search(pre_req_node, ordered_jobs)
        if contains_cycle:
            return True
    node.visited = True
    node.visiting = False
    # no pre_reqs
    ordered_jobs.append(node.job)
    return False


class JobGraph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.add_node(job)

    def add_pre_req(self, job, pre_req):
        job_node = self.get_node(job)
        pre_req_node = self.get_node(pre_req)
        job_node.pre_reqs.append(pre_req_node)

    def add_node(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])

    def get_node(self, job):
        if job not in self.graph:
            self.add_node(job)
        return self.graph[job]


class JobNode:
    def __init__(self, job):
        self.job = job
        self.pre_reqs = []
        self.visited = False
        self.visiting = False
