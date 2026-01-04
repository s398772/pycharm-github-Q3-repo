# ==========================
# Assignment 3: Turtle Recursive Pattern
# Author: Sharif Mohiminul Jahid
# Description:
# This program uses recursion and the turtle module
# to draw a recursive pattern on each edge of a polygon.
# ==========================

import turtle


def draw_edge(length, depth):
    """
    Recursively draws one edge of the polygon.
    At depth 0, it simply draws a straight line.
    For higher depths, the edge is divided into
    smaller segments to create a fractal-like pattern.
    """

    # Base case: when recursion depth reaches 0
    if depth == 0:
        turtle.forward(length)
        return

    # Reduce the length for recursive subdivision
    length = length / 3

    # Draw the four recursive segments
    draw_edge(length, depth - 1)
    turtle.right(60)

    draw_edge(length, depth - 1)
    turtle.left(120)

    draw_edge(length, depth - 1)
    turtle.right(60)

    draw_edge(length, depth - 1)


def draw_polygon(sides, length, depth):
    """
    Draws a polygon by repeatedly calling the
    recursive draw_edge() function for each side.
    """

    # Calculate the external turning angle
    angle = 360 / sides

    # Draw each side of the polygon
    for _ in range(sides):
        draw_edge(length, depth)
        turtle.right(angle)


def main():
    """
    Main function to take user input,
    configure turtle settings, and
    start the drawing process.
    """

    # Take user inputs
    sides = int(input("Enter the number of sides: "))
    length = int(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    # Turtle setup for fast and clean drawing
    turtle.speed(0)
    turtle.hideturtle()

    # Position turtle so the shape is centered
    turtle.penup()
    turtle.goto(-length / 2, 0)
    turtle.pendown()

    # Draw the recursive polygon
    draw_polygon(sides, length, depth)

    # Keep the window open
    turtle.done()


# Program execution starts here
main()
