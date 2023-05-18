{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNn1LJj1Qwi5RPoV3nx4+BY",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/hyeontae04/202310968/blob/main/hw9.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "qjt0psmtNtpv"
      },
      "outputs": [],
      "source": [
        "\n",
        "#포인트 클래스\n",
        "class Point :\n",
        "  def __init__(self, x=0, y=0):\n",
        "    self.__x = x\n",
        "    self.__y = y\n",
        "\n",
        "  def show(self):\n",
        "    print(f'({self.__x}, {self.__y})')\n",
        "\n",
        "  def set(self, x, y):\n",
        "    self.__x = x\n",
        "    self.__y = y\n",
        "\n",
        "  def get(self):\n",
        "    return(self.__x, self.__y)\n",
        "\n",
        "\n",
        "#사용자 정의 함수부\n",
        "def test() :\n",
        "  p1 = Point()\n",
        "  p2 = Point(2, 3)\n",
        "  p1.show(); print() # (0,0)\n",
        "\n",
        "  p1.set(10, 20); p1.show(); print() #(10,20)\n",
        "  \n",
        "  p2.show(); print()# (2,3)\n",
        "  x, y = p2.get()\n",
        "  print(f'x={x}, y={y}') #x=2, y=3\n",
        "\n",
        "if __name__ == '__main__' :\n",
        "  test()\n"
      ]
    }
  ]
}