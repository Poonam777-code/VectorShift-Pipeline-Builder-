from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Pipeline(BaseModel):
    nodes: List[Dict]
    edges: List[Dict]

@app.post("/pipelines/parse")
def parse_pipeline(pipeline: Pipeline):
    node_ids = {node["id"] for node in pipeline.nodes}
    graph = {node_id: [] for node_id in node_ids}

    for edge in pipeline.edges:
        if edge["source"] in node_ids and edge["target"] in node_ids:
            graph[edge["source"]].append(edge["target"])

    visited = set()
    stack = set()

    def dfs(node):
        if node in stack:
            return False
        if node in visited:
            return True

        visited.add(node)
        stack.add(node)

        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False

        stack.remove(node)
        return True

    is_dag = all(dfs(n) for n in node_ids if n not in visited)

    return {
        "num_nodes": len(pipeline.nodes),
        "num_edges": len(pipeline.edges),
        "is_dag": is_dag,
    }