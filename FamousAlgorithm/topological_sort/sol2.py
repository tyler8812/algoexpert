# j: jobs, d: dependencies
# time: O(j+d)
# space: O(j+d)
def topologicalSort(jobs, deps):
    # 建立一個誰先誰後的 graph
    job_graph = create_job_graph(jobs, deps)
    return get_order_jobs(job_graph)


def create_job_graph(jobs, deps):
    graph = JobGraph(jobs)
    for job, dep in deps:
        # adding edges
        graph.add_dep(job, dep)
    return graph


# 找到可行的 order
def get_order_jobs(graph):
    ordered_jobs = []
    # 找不需要比他早做的node
    nodes_with_no_pre_reqs = list(
        filter(lambda node: node.pre_reqs_count == 0, graph.nodes)
    )

    # 將它加到可行解的list中並加他連到的node的edge刪掉
    while len(nodes_with_no_pre_reqs):
        node = nodes_with_no_pre_reqs.pop()
        ordered_jobs.append(node.job)
        remove_deps(node, nodes_with_no_pre_reqs)

    # 判斷還有沒有任何edge
    graph_has_edges = any(node.pre_reqs_count for node in graph.nodes)
    return [] if graph_has_edges else ordered_jobs


# 刪除當前node連到的edge
def remove_deps(node, nodes_with_no_pre_reqs):
    # 料出所有edge
    while len(node.deps):
        dep = node.deps.pop()
        # 將底下的node的pre_req數量減一
        dep.pre_reqs_count -= 1
        # 如果減完為0則加入可行解的list中
        if dep.pre_reqs_count == 0:
            nodes_with_no_pre_reqs.append(dep)


class JobGraph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.add_node(job)

    def add_dep(self, job, dep):
        job_node = self.get_node(job)
        dep_node = self.get_node(dep)
        job_node.deps.append(dep_node)
        dep_node.pre_reqs_count += 1

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
        self.pre_reqs_count = 0
        self.deps = []
