def process_splits(scene_graphs, t_start, t_end):
    # Assume we have a list of scene graphs for the entire surgery
    scene_graphs = [SceneGraph(nodes_1, positions_1, t1), SceneGraph(nodes_2, positions_2, t2), ...]

    # Manually defining processes based on which scene graphs belong to which process
    cleaning_graphs = scene_graphs[:20]  # First 20 scene graphs
    incision_graphs = scene_graphs[20:40]  # Next 20 scene graphs
    suturing_graphs = scene_graphs[40:60]  # Next 20 scene graphs

    # Create Process objects for each action
    cleaning_process = Process('Cleaning', cleaning_graphs)
    incision_process = Process('Incision', incision_graphs)
    suturing_process = Process('Suturing', suturing_graphs)
    return result