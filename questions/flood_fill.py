from dataclasses import dataclass

Image = list[list[int]]


@dataclass(frozen=True)
class Point:
    row: int
    col: int


def flood_fill(image: Image, sr: int, sc: int, color: int) -> Image:
    rows = len(image)
    cols = len(image[0])
    clone = [row[:] for row in image]  # clone 2d list.
    visited: set[Point] = set()
    initial_color = image[sr][sc]

    def loop(sr: int, sc: int) -> None:
        point = Point(sr, sc)
        if (
            color == initial_color
            or (sr < 0 or sr > rows - 1)
            or (sc < 0 or sc > cols - 1)
            or point in visited
        ):
            return

        visited.add(point)
        current_color = image[sr][sc]
        if current_color != initial_color:
            return

        clone[sr][sc] = color

        # check top, bottom, left, right.
        loop(sr - 1, sc)
        loop(sr + 1, sc)
        loop(sr, sc - 1)
        loop(sr, sc + 1)

    loop(sr, sc)
    return clone
