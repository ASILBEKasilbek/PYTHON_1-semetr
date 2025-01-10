import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import random

# Kubik ranglari
colors = {
    "U": "white",  # Yuqori
    "D": "yellow", # Past
    "F": "green",  # Old
    "B": "blue",   # Orqa
    "L": "orange", # Chap
    "R": "red"     # O'ng
}

# Kubikning boshlang'ich holati
def initialize_cube():
    return {
        face: np.array([[colors[face]] * 3 for _ in range(3)])
        for face in colors
    }

# Yuzalarni chizish
def draw_face(ax, origin, dx, dy, dz, color):
    vertices = [
        [origin[0], origin[1], origin[2]],
        [origin[0] + dx, origin[1], origin[2]],
        [origin[0] + dx, origin[1] + dy, origin[2] + dz],
        [origin[0], origin[1] + dy, origin[2] + dz],
    ]
    poly = Poly3DCollection([vertices])
    poly.set_facecolor(color)
    ax.add_collection3d(poly)

# 3D kubikni chizish
def draw_cube(ax, state):
    ax.clear()
    coords = {
        "U": [(-1 + i, -1 + j, 1) for i in range(3) for j in range(3)],
        "D": [(-1 + i, -1 + j, -1) for i in range(3) for j in range(3)],
        "F": [(-1 + i, -1, 1 - j) for i in range(3) for j in range(3)],
        "B": [(-1 + i, 1, -1 + j) for i in range(3) for j in range(3)],
        "L": [(-1, -1 + i, 1 - j) for i in range(3) for j in range(3)],
        "R": [(1, -1 + i, 1 - j) for i in range(3) for j in range(3)],
    }
    for face, positions in coords.items():
        for idx, pos in enumerate(positions):
            draw_face(ax, pos, 0.66, 0.66, 0.66, state[face][idx // 3, idx % 3])
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    ax.set_axis_off()

# Yuzalarni burish
def rotate_face(face):
    return np.rot90(face, -1)

def rotate_face_reverse(face):
    return np.rot90(face, 1)

# Harakatlar
def move_F(state):
    state["F"] = rotate_face(state["F"])
    state["U"][2, :], state["R"][:, 0], state["D"][0, :], state["L"][:, 2] = (
        state["L"][:, 2][::-1],
        state["U"][2, :],
        state["R"][:, 0][::-1],
        state["D"][0, :]
    )

def move_F_reverse(state):
    state["F"] = rotate_face_reverse(state["F"])
    state["L"][:, 2], state["U"][2, :], state["R"][:, 0], state["D"][0, :] = (
        state["U"][2, :][::-1],
        state["R"][:, 0],
        state["D"][0, :][::-1],
        state["L"][:, 2]
    )

# Orqa yuzani burish
def move_B(state):
    state["B"] = rotate_face(state["B"])
    state["U"][0, :], state["L"][:, 0], state["D"][2, :], state["R"][:, 2] = (
        state["R"][:, 2][::-1],
        state["U"][0, :],
        state["L"][:, 0][::-1],
        state["D"][2, :]
    )

def move_B_reverse(state):
    state["B"] = rotate_face_reverse(state["B"])
    state["R"][:, 2], state["U"][0, :], state["L"][:, 0], state["D"][2, :] = (
        state["U"][0, :][::-1],
        state["L"][:, 0],
        state["D"][2, :][::-1],
        state["R"][:, 2]
    )

# Boshqa harakatlarni burish: move_R, move_L, move_U, move_D

# Kubikni aralashtirish
def shuffle_cube(state, steps=20):
    moves = [move_F, move_B]  # boshqa harakatlar ham qo'shiladi
    for _ in range(steps):
        random.choice(moves)(state)

def shuffle_and_solve(state, steps=20):
    moves = [move_F, move_B]
    reverse_moves = [move_F_reverse, move_B_reverse]
    applied_moves = []

    # Aralashtirish
    for _ in range(steps):
        idx = random.randint(0, len(moves) - 1)

        moves[idx](state)
        applied_moves.append(idx)

    # Yechish
    for idx in reversed(applied_moves):
        reverse_moves[idx](state)

# Asosiy funksiyani yaratish
def main():
    state = initialize_cube()
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection="3d")

    def on_key(event):
        if event.key == "f":
            move_F(state)
        elif event.key == "b":
            move_B(state)
        elif event.key == "s":  # Aralashtirish
            shuffle_cube(state, steps=20)
        elif event.key == "x":  # Yechish
            shuffle_and_solve(state, steps=20)
        draw_cube(ax, state)
        plt.draw()

    fig.canvas.mpl_connect("key_press_event", on_key)
    draw_cube(ax, state)
    plt.show()

if __name__ == "__main__":
    main()
