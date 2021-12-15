import networkx as nx

data = open("day15.txt", "r").read().strip()
risk = [[int(n) for n in row] for row in data.split("\n")]

M, N = len(risk), len(risk[0])
num_tiles = 5

G = nx.DiGraph()
move_dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for i in range(M * num_tiles):
    for j in range(N * num_tiles):
        idiv, imod = divmod(i, M)
        jdiv, jmod = divmod(j, N)
        weight = (risk[imod][jmod] + idiv + jdiv) % 9
        if weight == 0:
            weight = 9

        for dx, dy in move_dirs:
            G.add_edge((j, i), (j + dy, i + dx), weight=weight)

print(
    "Part 1",
    nx.dijkstra_path_length(G, (0, 0), (N - 1, M - 1), "weight")
    - risk[0][0]
    + risk[N - 1][M - 1],
)

final = risk[N - 1][M - 1] + num_tiles + num_tiles - 2
final = final - 9 if final > 9 else final

print(
    "Part 2",
    nx.dijkstra_path_length(G, (0, 0), (num_tiles * N - 1, num_tiles * M - 1), "weight")
    - risk[0][0]
    + final,
)